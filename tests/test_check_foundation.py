"""Focused validator tests; these are NOT agent-guided bootstrap acceptance."""
import hashlib
import json
from pathlib import Path
import re
import runpy
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

KIT = Path(__file__).resolve().parents[1]
CHECKER = KIT / "pack/tools/check_foundation.py"
API = runpy.run_path(str(CHECKER), run_name="foundation_checker_tests")
SCRATCH = KIT / "artifacts/quality"
# Original source-byte digests, recorded before import on 2026-10-23.
# These portable witnesses do not read the source machine or prove runtime claims.
SOURCE_SHA256 = {
    "references/architecture/command-first/00_README.md": "78eaccb46f521037842850e1926a222d1f3a53032dcb4384d444b1114b59be59",
    "references/architecture/command-first/01_Command_First_Introduction.md": "ebd34e1749bbc4bc47fd250bf10363bd9e97223bae762781315ed8f733f709dd",
    "references/architecture/command-first/02_Command_First_Architecture_and_Contracts.md": "cc052f1190a06f7305e73fd68d5ce9a1ea84e43aa7cf9d20746019f43bf168a9",
    "references/architecture/command-first/03_Command_First_Architecture_Variants.md": "a31c2bdb7cfaa82f09ad756a5da9f5504225dce2d3702634e8487760d491542c",
    "references/architecture/command-first/04_Command_First_Image_Converter_Architecture.md": "5e192de874844862046c9d737ceda63fc7cb61bc024118c63d8553dcc5ebf0b8",
    "references/ui/figcraft/FigCraft_AI_GUI_Design_Guide_RU.md": "008d346da4df289f84799661bf2dee74258a02cf691484541ace819511b071cd",
}
# Four nonsecret opaque citation comments belong to this exact source snapshot.
FILECITE_SNAPSHOT = "references/architecture/command-first/04_Command_First_Image_Converter_Architecture.md"
PORTABLE_PRIVATE_MARKERS = ("Whisper-Voice-Machine", "C:/PY/", "C:\\\\Users\\\\", "WVM_DEV")


def document(identity="EXAMPLE-NOTE", kind="reference", status="draft", extra="", body="# Note\nSynthetic fixture.\n"):
    return (f'---\nid: "{identity}"\ntitle: "Synthetic note"\nkind: {kind}\nstatus: {status}\n'
            'created: "2026-10-19"\nupdated: "2026-10-19"\nareas: [example]\n'
            f'summary: "Synthetic validator input, not a product fact."\n{extra}---\n\n{body}')


class FoundationChecks(unittest.TestCase):
    def setUp(self):
        SCRATCH.mkdir(parents=True, exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(prefix="проверка path ", dir=SCRATCH)
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()

    def put(self, path, text):
        target = self.root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text, encoding="utf-8")
        return target

    def check(self, corpus):
        return API["Checker"](self.root, corpus, "project").run()

    def codes(self, report, severity=None):
        return {f["code"] for f in report["findings"] if severity is None or f["severity"] == severity}

    def cli(self, *args):
        return subprocess.run([sys.executable, "-I", "-B", str(CHECKER), *map(str, args)], cwd=self.root, capture_output=True, text=True, encoding="utf-8", timeout=30)

    def synthetic_pack(self):
        pack = self.root / "перенос пакета"
        self.put("перенос пакета/references/quality.md", "# Synthetic resource\n")
        (pack / "tools").mkdir()
        shutil.copyfile(CHECKER, pack / "tools/check_foundation.py")
        for name in ("pf-bootstrap", "pf-plan", "pf-maintain", "pf-quality", "pf-guides", "pf-ui-design", "pf-command-first"):
            self.put(f"перенос пакета/skills/{name}/SKILL.md", f'---\nname: {name}\ndescription: "Synthetic relocation skill"\n---\n[resource](../../references/quality.md)\n')
        return pack

    def assert_series_wiki_targets(self, bodies):
        # Finite original-series witness: [[stem#plain ATX heading|optional label]]
        # or [[#heading]]. No renderer, aliases, block IDs, embeds or path inference.
        headings, visible = {}, {}
        for stem, body in bodies.items():
            visible[stem] = API["visible"](body)
            headings[stem] = set(re.findall(r"(?m)^#{1,6}\s+(.+?)\s*#*\s*$", visible[stem]))
        counts = {}
        for stem, text in visible.items():
            pattern = r"\[\[([^\[\]\n]+)\]\]"
            remaining = re.sub(pattern, "", text)
            self.assertNotIn("[[", remaining, f"NOT VERIFIED: unsupported series wiki syntax in {stem}")
            self.assertNotIn("]]", remaining, f"NOT VERIFIED: unsupported series wiki syntax in {stem}")
            links = list(re.finditer(pattern, text))
            counts[stem] = len(links)
            for link in links:
                value = re.fullmatch(r"([A-Za-z0-9_]+)?#([^#|^\[\]\n]+)(?:\|[^|\[\]\n]+)?", link[1])
                self.assertIsNotNone(value, f"NOT VERIFIED: unsupported series wiki syntax: {link[0]}")
                self.assertFalse(link.start() and text[link.start() - 1] == "!", f"NOT VERIFIED: wiki embed: {link[0]}")
                target, heading = value[1] or stem, value[2]
                self.assertIn(target, bodies, f"Missing series target: {target}")
                self.assertIn(heading, headings[target], f"Missing series heading: {target}#{heading}")
        return counts

    def test_valid_document_and_native_grammar(self):
        self.put("docs/note.md", document())
        self.put("AGENTS.md", "# Native rules\nKeep local rule.\n")
        report = self.check({"docs/note.md": "authoring", "AGENTS.md": "native"})
        self.assertEqual(report["exit_code"], 0)
        self.assertEqual(report["checked"], 2)

    def test_types_dates_and_status_are_exact(self):
        for original, wrong in [('areas: [example]', 'areas: example'), ('status: draft', 'status: [draft]'), ('created: "2026-10-19"', 'created: 2026-10-19'), ('id: "EXAMPLE-NOTE"', 'id: true')]:
            with self.subTest(wrong=wrong):
                self.put("note.md", document().replace(original, wrong))
                self.assertEqual(self.check({"note.md": "authoring"})["exit_code"], 1)

    def test_safe_yaml_rejects_duplicate_keys_and_executable_tags(self):
        for extra in ['title: "duplicate"\n', 'extension: !!python/object/apply:builtins.print [unsafe]\n', 'extension: &name value\ncopy: *name\n', '<<: {extension: value}\n']:
            with self.subTest(extra=extra):
                self.put("note.md", document(extra=extra))
                self.assertIn("yaml.invalid", self.codes(self.check({"note.md": "authoring"})))

    def test_duplicate_ids_and_accepted_placeholders_are_errors(self):
        self.put("a.md", document(status="accepted", body="Unfilled {{decision}}"))
        self.put("b.md", document())
        report = self.check({"a.md": "authoring", "b.md": "authoring"})
        self.assertTrue({"id.duplicate", "placeholder.output"}.issubset(self.codes(report, "error")))
        self.put("b.md", document(identity="{{required_id}}"))
        self.assertIn("metadata.type", self.codes(self.check({"b.md": "authoring"})))

    def test_required_areas_reject_list_item_placeholders_in_every_status(self):
        cases = (
            (["testing", "documentation"], 0),
            (["{{subject_area}}"], 1),
            (["testing", "{{subject_area}}"], 1),
            (["{{subject_area}}", "documentation"], 1),
        )
        for status in sorted(API["STATUSES"]):
            for areas, expected_exit in cases:
                with self.subTest(status=status, areas=areas):
                    self.put("note.md", document(status=status).replace("areas: [example]", "areas: " + json.dumps(areas)))
                    report = self.check({"note.md": "authoring"})
                    self.assertEqual(report["exit_code"], expected_exit, report["findings"])
                    if expected_exit:
                        self.assertTrue(any(f["code"] == "metadata.type" and f["severity"] == "error" and f["message"].startswith("Required areas:") for f in report["findings"]), report["findings"])
                    else:
                        self.assertEqual(report["findings"], [])

    def test_draft_placeholder_warns_without_claiming_acceptance(self):
        self.put("a.md", document(body="Draft {{open_question}}"))
        report = self.check({"a.md": "authoring"})
        self.assertEqual(report["exit_code"], 0)
        self.assertIn("placeholder.output", self.codes(report, "warning"))

    def test_templates_are_explicit_not_a_way_to_hide_output(self):
        self.put("note.md.tmpl", "{{native template syntax}}")
        self.assertEqual(self.check({"note.md.tmpl": "templates"})["exit_code"], 0)
        with self.assertRaises(API["InputError"]):
            self.check({"note.md.tmpl": "authoring"})
        self.put("note.md", document(status="accepted", body="{{required}}"))
        with self.assertRaises(API["InputError"]):
            self.check({"note.md": "templates"})

    def test_inline_reference_links_anchors_and_footnotes(self):
        self.put("docs/a.md", document(body='[B](b.md#result)\n[B again][target]\n[target]: b.md#result\n[^note]: Python logging documentation\n'))
        self.put("docs/b.md", document(identity="EXAMPLE-B", body="# Result\n"))
        report = self.check({"docs/a.md": "authoring", "docs/b.md": "authoring"})
        self.assertEqual(report["exit_code"], 0)
        self.put("docs/b.md", document(identity="EXAMPLE-B", body="# Renamed\n"))
        self.assertIn("link.anchor", self.codes(self.check({"docs/a.md": "authoring", "docs/b.md": "authoring"})))
        self.put("docs/a.md", document(body="[missing](absent.md) [ref][undefined]"))
        self.assertTrue({"link.missing", "link.reference"}.issubset(self.codes(self.check({"docs/a.md": "authoring"}))))

    def test_code_labels_inline_images_and_angle_destinations(self):
        for label in ('`README`', 'Файл `README`', '``a ` b``'):
            for syntax in ('[{label}](target.md)', '![{label}](<target.md>)'):
                with self.subTest(label=label, syntax=syntax):
                    target = self.root / 'target.md'
                    target.unlink(missing_ok=True)
                    self.put('a.md', document(body=syntax.format(label=label)))
                    report = self.check({'a.md': 'authoring'})
                    self.assertEqual(report['exit_code'], 1, report)
                    self.assertIn('link.missing', self.codes(report, 'error'))
                    self.put('target.md', '# Existing, unselected\n')
                    self.assertEqual(self.check({'a.md': 'authoring'})['exit_code'], 0)

    def test_code_reference_labels_resolve_and_keep_text_identity(self):
        cases = (
            ('[`README`][doc]', '[doc]'),
            ('[`README`][]', '[`README`]'),
            ('[plain][`DOC`]', '[`doc`]'),
            ('[Mixed `KEY`][]', '[mixed `key`]'),
        )
        for link, definition in cases:
            with self.subTest(link=link):
                (self.root / 'target.md').unlink(missing_ok=True)
                self.put('a.md', document(body=f'{link}\n{definition}: target.md\n'))
                report = self.check({'a.md': 'authoring'})
                self.assertEqual(report['exit_code'], 1, report)
                self.assertIn('link.missing', self.codes(report))
                self.assertNotIn('link.reference', self.codes(report))
                self.put('target.md', '# Existing\n')
                self.assertEqual(self.check({'a.md': 'authoring'})['exit_code'], 0)
                self.put('a.md', document(body=link))
                self.assertIn('link.reference', self.codes(self.check({'a.md': 'authoring'})))
        # Colliding rendered labels must not alias: reference keys are source text.
        self.put('a.md', document(body='[`a`][] [`b`][] [x][] [`x`][] [Text `A`][] [Text `B`][]\n'
                 '[`a`]: a.md\n[`b`]: missing-b.md\n[x]: a.md\n[`x`]: missing-x.md\n'
                 '[text `a`]: a.md\n[text `b`]: missing-text-b.md\n'))
        report = self.check({'a.md': 'authoring'})
        missing = [f['message'] for f in report['findings'] if f['code'] == 'link.missing']
        self.assertEqual(len(missing), 3, report)
        for name in ('missing-b.md', 'missing-x.md', 'missing-text-b.md'):
            self.assertTrue(any(name in message for message in missing), report)

    def test_literal_code_full_delimiter_runs_do_not_create_syntax(self):
        literals = ('`[x](missing.md) [x][bad] [[wiki]] <i id="fake">`',
                    '``single ` [x](missing.md) [x][bad] [[wiki]] <i id="fake">``',
                    '``literal ``` [x](missing.md) [x][bad] [[wiki]] <i id="fake">``',
                    '`literal `` [x](missing.md) [x][bad] [[wiki]] <i id="fake">`',
                    '```md\n[x](missing.md) [x][bad] [[wiki]] <i id="fake">\n```',
                    '~~~md\n[x](missing.md) [x][bad] [[wiki]] <i id="fake">\n~~~')
        for literal in literals:
            with self.subTest(literal=literal):
                self.put('a.md', document(body=literal))
                report = self.check({'a.md': 'authoring'})
                self.assertEqual(report['findings'], [], report)
                self.put('a.md', document(body=literal + '\n[anchor](#fake)'))
                self.assertIn('link.anchor', self.codes(self.check({'a.md': 'authoring'})))
        # Definition opener inside a multiline code span is not a definition.
        self.put('a.md', document(body='``literal `\n[key]: a.md\n``\n[real][key]'))
        self.assertIn('link.reference', self.codes(self.check({'a.md': 'authoring'})))
        for fence in ('```', '~~~'):
            self.put('a.md', document(body=f'{fence}md\n[key]: a.md\n{fence}\n[real][key]'))
            self.assertIn('link.reference', self.codes(self.check({'a.md': 'authoring'})))
        self.put('a.md', document(body='[[outside]] `[[inside]]`'))
        report = self.check({'a.md': 'authoring'})
        self.assertEqual(sum(f['code'] == 'link.wiki' for f in report['findings']), 1)

    def test_code_headings_keep_words_duplicates_and_real_negative_control(self):
        self.put('a.md', document(body='[one](b.md#export) [two](b.md#export-1) '
                 '[mixed](b.md#запуск-pytest) [double](b.md#a--b) [id](b.md#real)'))
        self.put('b.md', document(identity='B', body='## `export`\n## `export`\n'
                 '## Запуск `pytest`\n## ``a ` b``\n<i id="real">\n'))
        corpus = {'a.md': 'authoring', 'b.md': 'authoring'}
        self.assertEqual(self.check(corpus)['exit_code'], 0)
        self.put('a.md', document(body='[bad](b.md#genuinely-missing)'))
        self.assertIn('link.anchor', self.codes(self.check(corpus), 'error'))

    def test_code_fragment_unselected_body_is_not_read(self):
        self.put('a.md', document(body='[`B`](b.md#export)'))
        self.put('b.md', '## `export`\n')
        loaded = []
        original = API['read_text']
        def observed(path):
            loaded.append(path.name)
            return original(path)
        with patch.dict(API['Checker'].load.__globals__, read_text=observed):
            report = self.check({'a.md': 'authoring'})
        self.assertEqual(loaded, ['a.md'])
        self.assertEqual(report['exit_code'], 0)
        self.assertIn('link.anchor_scope', self.codes(report, 'not_checked'))

    def test_native_outputs_and_required_instruction_trigger_cannot_keep_tokens(self):
        self.put("AGENTS.md", "# {{project_name}}")
        self.put("profile.yaml", 'name: "{{project_name}}"\n')
        report = self.check({"AGENTS.md": "native", "profile.yaml": "native"})
        self.assertEqual(sum(f["code"] == "placeholder.native" for f in report["findings"]), 2)
        self.put("instruction.md", document(kind="instruction", status="accepted", extra='read_when: "{{trigger}}"\n'))
        self.assertIn("placeholder.metadata", self.codes(self.check({"instruction.md": "authoring"})))

    def test_fenced_inline_examples_are_not_links(self):
        self.put("a.md", document(body='```md\n[bad](absent.md)\n```\n`[bad](absent.md)`\n'))
        self.assertEqual(self.check({"a.md": "authoring"})["exit_code"], 0)

    def test_local_parent_link_is_bounded_and_unselected_body_not_read(self):
        self.put("docs/a.md", document(body="[native](../AGENTS.md#rules)"))
        self.put("AGENTS.md", "# Rules\nSynthetic unselected body\n")
        loaded = []
        original = API["read_text"]
        def observed(path):
            loaded.append(path.name)
            return original(path)
        with patch.dict(API["Checker"].load.__globals__, read_text=observed):
            report = self.check({"docs/a.md": "authoring"})
        self.assertEqual(loaded, ["a.md"])
        self.assertIn("link.anchor_scope", self.codes(report, "not_checked"))
        self.put("docs/a.md", document(body="[escape](../../outside.md)"))
        self.assertIn("link.boundary", self.codes(self.check({"docs/a.md": "authoring"})))

    def guides(self, translated_revision="r1"):
        self.put("docs/ru.md", document(identity="GUIDE-RU", kind="guide", extra='language: ru\nsource_revision: "r1"\n'))
        self.put("docs/en.md", document(identity="GUIDE-EN", kind="guide", extra=f'language: en\ntranslation_source: GUIDE-RU\ntranslation_source_revision: "{translated_revision}"\ntranslation_state: current\n'))
        return {"docs/ru.md": "authoring", "docs/en.md": "authoring"}

    def test_translation_freshness_uses_revision_not_date(self):
        corpus = self.guides()
        report = self.check(corpus)
        self.assertEqual(report["translations"][0]["state"], "current")
        source = self.root / "docs/ru.md"
        source.write_text(source.read_text(encoding="utf-8").replace('source_revision: "r1"', 'source_revision: "r2"'), encoding="utf-8")
        report = self.check(corpus)
        self.assertEqual(report["exit_code"], 1)
        self.assertIn("translation.contradiction", self.codes(report, "error"))
        translated = self.root / "docs/en.md"
        translated.write_text(translated.read_text(encoding="utf-8").replace("translation_state: current", "translation_state: outdated"), encoding="utf-8")
        report = self.check(corpus)
        self.assertEqual(report["exit_code"], 0)
        self.assertEqual(report["translations"][0]["state"], "outdated")
        self.assertIn("translation.outdated", self.codes(report, "warning"))

    def test_translation_missing_source_and_bad_revision_are_not_green(self):
        corpus = self.guides()
        self.assertIn("translation.source", self.codes(self.check({"docs/en.md": "authoring"})))
        self.put("docs/en.md", document(identity="GUIDE-EN", kind="guide", extra='language: ru\ntranslation_source: GUIDE-RU\ntranslation_source_revision: 1\n'))
        report = self.check(corpus)
        self.assertTrue({"metadata.type", "translation.language", "translation.revision"}.issubset(self.codes(report)))

    def test_native_skill_structure_and_resource_link(self):
        self.put("skills/pf-example/SKILL.md", '---\nname: pf-example\ndescription: "Describe when to use this synthetic skill"\nmetadata:\n  version: "0.1.0"\n---\n[ref](../../references/quality.md)\n')
        self.put("references/quality.md", "# Resource\n")
        corpus = {"skills/pf-example/SKILL.md": "native"}
        self.assertEqual(self.check(corpus)["exit_code"], 0)
        file = self.root / "skills/pf-example/SKILL.md"
        file.write_text(file.read_text(encoding="utf-8").replace("name: pf-example", "name: Different"), encoding="utf-8")
        self.assertIn("skill.name", self.codes(self.check(corpus)))
        (self.root / "references/quality.md").unlink()
        self.assertIn("link.missing", self.codes(self.check(corpus)))

    def test_base_yaml_shape_is_not_filter_evaluation(self):
        self.put("Documents.base", 'filters:\n  and:\n    - file.inFolder("docs")\n    - \'!file.inFolder("docs/archive")\'\n    - \'!file.inFolder("docs/_templates")\'\nviews:\n  - type: table\n    name: Current documents\n')
        report = self.check({"Documents.base": "native"})
        self.assertEqual(report["exit_code"], 0)
        self.assertIn("base.not_rendered", self.codes(report, "not_checked"))
        self.put("Documents.base", "views: wrong\n")
        self.assertIn("base.structure", self.codes(self.check({"Documents.base": "native"})))

    def test_shipped_bases_declare_scope_without_running_predicates(self):
        folder = KIT / "pack/templates/obsidian"
        corpus = {}
        for filename, area in (("Documents.base", "architecture"), ("Scenarios.base", "scenarios"), ("Guides.base", "guides")):
            file = folder / filename
            data = API["safe_yaml"](file.read_text(encoding="utf-8"))
            filters = data["filters"]["and"]
            exclusions = next(value["not"] for value in filters if isinstance(value, dict) and "not" in value)
            for path in ("_templates", "archive", "_work"):
                self.assertIn(f'file.inFolder("{path}")', exclusions)
            rendered = str(data)
            self.assertIn(f'file.inFolder("{area}")', rendered)
            self.assertIn("note.status", rendered)
            self.assertNotIn("WVM", rendered)
            corpus[file.relative_to(KIT).as_posix()] = "native"
        report = API["Checker"](KIT, corpus, "project").run()
        self.assertEqual(report["exit_code"], 0)
        self.assertEqual(sum(f["code"] == "base.not_rendered" for f in report["findings"]), 3)

    def test_unknown_kind_and_optional_type_drift_are_errors(self):
        self.put("note.md", document(kind="technical_note", extra="evidence_refs: wrong\n"))
        report = self.check({"note.md": "authoring"})
        self.assertTrue({"metadata.kind", "metadata.type"}.issubset(self.codes(report)))

    def test_corpus_boundary_and_no_empty_success(self):
        for value in ({}, {"authoring": []}, {"authoring": ["../escape.md"]}, {"native": ["/absolute.md"]}, {"native": ["AGENTS.md"], "authoring": ["AGENTS.md"]}):
            with self.subTest(value=value):
                self.put("scope.json", json.dumps(value))
                with self.assertRaises(API["InputError"]):
                    API["project_corpus"](self.root, "scope.json")
        self.put("scope.json", '{"authoring": ["note.md"]}')
        result = self.cli("--project", self.root, "--corpus", "scope.json")
        self.assertEqual(result.returncode, 2)
        self.assertEqual(json.loads(result.stdout)["exit_code"], 2)

    def test_cli_raw_exits_from_unrelated_cyrillic_space_cwd(self):
        self.put("note.md", document())
        self.put("scope.json", json.dumps({"authoring": ["note.md"]}))
        result = self.cli("--project", self.root, "--corpus", "scope.json")
        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
        self.put("note.md", document(body="[bad](missing.md)"))
        result = self.cli("--project", self.root, "--corpus", "scope.json")
        self.assertEqual(result.returncode, 1)
        self.assertEqual(json.loads(result.stdout)["exit_code"], 1)
        result = self.cli("--project", self.root)
        self.assertEqual(result.returncode, 2)

    def test_pack_relocation_checks_actual_resources_not_cwd(self):
        pack = self.synthetic_pack()
        result = subprocess.run([sys.executable, "-I", "-B", str(pack / "tools/check_foundation.py"), "--pack"], cwd=KIT, capture_output=True, text=True, timeout=30)
        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
        (pack / "references/quality.md").unlink()
        result = subprocess.run([sys.executable, "-I", "-B", str(pack / "tools/check_foundation.py"), "--pack"], cwd=KIT, capture_output=True, text=True, timeout=30)
        self.assertEqual(result.returncode, 1)

    def test_pack_exact_seven_names_and_cli_input_failures(self):
        # Independent literal expectation: never import the implementation's set.
        expected = {'pf-bootstrap', 'pf-plan', 'pf-maintain', 'pf-quality', 'pf-guides', 'pf-ui-design', 'pf-command-first'}
        pack = self.synthetic_pack()
        self.assertEqual({p.name for p in (pack / 'skills').iterdir() if p.is_dir()}, expected)
        self.assertEqual(self.cli('--pack', pack).returncode, 0)

        def invalid_pack():
            result = self.cli('--pack', pack)
            self.assertEqual(result.returncode, 2, result.stdout + result.stderr)
            report = json.loads(result.stdout)
            self.assertEqual(report['exit_code'], 2)
            self.assertIn('input.invalid', self.codes(report, 'error'))

        for name in sorted(expected):
            with self.subTest(missing_directory=name):
                folder = pack / 'skills' / name
                folder.rename(self.root / 'held-skill')
                try:
                    invalid_pack()
                finally:
                    (self.root / 'held-skill').rename(folder)
            with self.subTest(missing_skill_file=name):
                skill = folder / 'SKILL.md'
                skill.rename(self.root / 'held-SKILL.md')
                try:
                    invalid_pack()
                finally:
                    (self.root / 'held-SKILL.md').rename(skill)
        extra = pack / 'skills/unexpected-eighth'
        extra.mkdir()
        invalid_pack()
        # Seven directories with a substituted name are not the seven named skills.
        command_first = pack / 'skills/pf-command-first'
        command_first.rename(self.root / 'held-command-first')
        invalid_pack()
        (self.root / 'held-command-first').rename(command_first)
        extra.rmdir()
        self.assertEqual(self.cli('--pack', pack).returncode, 0)

    def test_original_snapshots_keep_source_bytes_and_native_grammar(self):
        pack = KIT / 'pack'
        corpus = {}
        for path, digest in SOURCE_SHA256.items():
            with self.subTest(path=path):
                self.assertEqual(hashlib.sha256((pack / path).read_bytes()).hexdigest(), digest)
            corpus[path] = 'native'
        checker = API['Checker'](pack, corpus, 'pack')
        report = checker.run()
        self.assertEqual(report['checked'], 6)
        self.assertEqual(report['exit_code'], 0, report)
        self.assertEqual(checker.docs, {})  # Original YAML is not the PFK note passport.
        self.assertEqual(set(checker.bodies), set(SOURCE_SHA256))
        self.assertTrue(all(f['code'] == 'link.wiki' and f['severity'] == 'not_checked' for f in report['findings']), report)

    def test_finite_series_wiki_witness_has_real_negative_and_literal_controls(self):
        bodies = {'00_README': '## Map\n[[#Map]] [[01_Command_First_Introduction#Result|open]]\n'
                  '`[[missing#Absent]]`\n``literal ` [[missing#Absent]]``\n'
                  '```md\n[[missing#Absent]]\n## Fake\n```\n'
                  '~~~md\n[[missing#Absent]]\n~~~\n',
                  '01_Command_First_Introduction': '## Result\n[[#Result|self]]\n'}
        self.assertEqual(self.assert_series_wiki_targets(bodies), {'00_README': 2, '01_Command_First_Introduction': 1})
        for link, message in (('[[missing#Result]]', 'Missing series target'),
                              ('[[01_Command_First_Introduction#Absent]]', 'Missing series heading'),
                              ('[[#Fake]]', 'Missing series heading')):
            with self.subTest(link=link), self.assertRaisesRegex(AssertionError, message):
                self.assert_series_wiki_targets({**bodies, '00_README': bodies['00_README'] + link})
        for link in ('[[unterminated', '[[01_Command_First_Introduction]]', '[[#^block]]',
                     '[[#Map#nested]]', '[[#Map|one|two]]', '![[#Map]]'):
            with self.subTest(link=link), self.assertRaisesRegex(AssertionError, 'NOT VERIFIED'):
                self.assert_series_wiki_targets({**bodies, '00_README': bodies['00_README'] + link})

    def test_all_original_series_wiki_targets_and_headings(self):
        bodies = {Path(path).stem: (KIT / 'pack' / path).read_text(encoding='utf-8')
                  for path in SOURCE_SHA256 if path.startswith('references/architecture/')}
        self.assertEqual(self.assert_series_wiki_targets(bodies), {
            '00_README': 7, '01_Command_First_Introduction': 12,
            '02_Command_First_Architecture_and_Contracts': 18,
            '03_Command_First_Architecture_Variants': 16,
            '04_Command_First_Image_Converter_Architecture': 17,
        })

    def test_new_routes_reach_original_snapshots_and_delivery_references(self):
        routes = {
            'skills/pf-bootstrap/SKILL.md': ('../pf-command-first/SKILL.md',),
            'skills/pf-plan/SKILL.md': ('../pf-command-first/SKILL.md',),
            'skills/pf-command-first/SKILL.md': ('../../references/architecture/command-first/README.md', 'references/cli-first-delivery.md'),
            'references/architecture/command-first/README.md': tuple(Path(path).name for path in SOURCE_SHA256 if path.startswith('references/architecture/')),
            'skills/pf-ui-design/SKILL.md': ('references/figcraft-handoff.md',),
            'skills/pf-ui-design/references/figcraft-handoff.md': ('../../../references/ui/figcraft/FigCraft_AI_GUI_Design_Guide_RU.md', '../../pf-command-first/SKILL.md'),
        }
        for path, expected in routes.items():
            with self.subTest(path=path):
                links, _ = API['local_links']((KIT / 'pack' / path).read_text(encoding='utf-8'))
                self.assertTrue(set(expected).issubset({link.split('#', 1)[0] for link in links}), (path, expected, links))

    def test_full_actual_pack_relocation_includes_methods_platforms_and_notices(self):
        pack = self.root / 'перенос всего pack'
        shutil.copytree(KIT / 'pack', pack)
        expected = {'pf-bootstrap', 'pf-plan', 'pf-maintain', 'pf-quality', 'pf-guides', 'pf-ui-design', 'pf-command-first'}
        self.assertEqual({p.name for p in (pack / 'skills').iterdir() if p.is_dir()}, expected)
        for name in expected:
            self.assertTrue((pack / 'skills' / name / 'SKILL.md').is_file(), name)
        original_files = {p.relative_to(KIT / 'pack').as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
                          for p in (KIT / 'pack').rglob('*') if p.is_file()}
        relocated_files = {p.relative_to(pack).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
                           for p in pack.rglob('*') if p.is_file()}
        self.assertEqual(relocated_files, original_files)
        required = ('references/methods/contract-evolution.md', 'references/methods/change-impact.md',
                    'references/methods/behavior-regression.md', 'skills/pf-ui-design/SKILL.md',
                    'skills/pf-ui-design/references/web-react.md',
                    'skills/pf-ui-design/references/desktop-pyside6.md',
                    'skills/pf-command-first/SKILL.md', 'skills/pf-command-first/references/cli-first-delivery.md',
                    'references/architecture/command-first/README.md',
                    'skills/pf-ui-design/references/figcraft-handoff.md', *SOURCE_SHA256,
                    'templates/documents/ui-design.md.tmpl', 'LICENSE', 'UPSTREAM.md', 'THIRD_PARTY_NOTICES.md')
        for path in required:
            self.assertEqual((pack / path).read_bytes(), (KIT / 'pack' / path).read_bytes())
        classified = API['pack_corpus'](pack)
        for path, digest in SOURCE_SHA256.items():
            self.assertEqual(hashlib.sha256((pack / path).read_bytes()).hexdigest(), digest)
            self.assertEqual(classified[path], 'native')
        command = [sys.executable, '-I', '-B', str(pack / 'tools/check_foundation.py'), '--pack']
        result = subprocess.run(command, cwd=self.root.parent, capture_output=True, text=True, timeout=30)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        report = json.loads(result.stdout)
        expected_findings = {(f'templates/obsidian/{name}.base', 'base.not_rendered', 'not_checked')
                             for name in ('Documents', 'Scenarios', 'Guides')}
        expected_findings.update((path, 'link.wiki', 'not_checked') for path in SOURCE_SHA256 if path.startswith('references/architecture/'))
        self.assertEqual(sorted((f['path'], f['code'], f['severity']) for f in report['findings']), sorted(expected_findings), report)
        for path in ('skills/pf-ui-design/references/web-react.md',
                     'skills/pf-command-first/references/cli-first-delivery.md',
                     'references/architecture/command-first/00_README.md',
                     'references/ui/figcraft/FigCraft_AI_GUI_Design_Guide_RU.md'):
            with self.subTest(missing_relocated_resource=path):
                file = pack / path
                saved = file.read_bytes()
                file.unlink()
                try:
                    result = subprocess.run(command, cwd=self.root.parent, capture_output=True, text=True, timeout=30)
                    self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
                    findings = json.loads(result.stdout)['findings']
                    self.assertTrue(any(f['code'] == 'link.missing' and f['message'] == f'Missing local target: {path}' for f in findings), findings)
                finally:
                    file.write_bytes(saved)

    def test_minimal_example_and_populated_ui_form_use_output_grammar(self):
        import re
        minimal = (KIT / 'pack/references/minimal-adoption.md').read_text(encoding='utf-8')
        blocks = re.findall(r'```markdown\n(.*?)\n```', minimal, re.S)
        self.assertEqual(len(blocks), 2)
        self.put('AGENTS.md', blocks[0])
        self.put('docs/engineering.md', blocks[1])
        text = (KIT / 'pack/templates/documents/ui-design.md.tmpl').read_text(encoding='utf-8')
        values = {
            'document_id': 'EXAMPLE-UI', 'surface_name': 'Выбор результата', 'date': '2026-10-21',
            'user_result_and_bounded_design_scope': 'Учебное design-решение текущего результата без GUI claim.',
            'user_job_primary_action_and_link_to_source_requirement': 'Задача: показать текущий выбранный результат; главное действие — выбор.',
            'current_vs_proposed_behavior_and_design_implementation_or_review_mode': 'Режим design: предложено сохранять B при позднем A, не реализовано.',
            'platform_surface_owner_constraints_and_non_goals': 'Desktop-панель; существующий operation owner; без API/зависимостей.',
            'existing_components_tokens_and_ui_rules': 'Сохраняются существующие theme и ResultPanel.',
            'operation_or_data_contract_reference_without_schema_duplication': '[Локальный owner решений](engineering.md#архитектура). Это учебный маршрут, не схема API.',
            'target_window_or_viewport_conditions_and_reason': 'Предложены resize/scale условия проекта; фактические значения ещё не установлены.',
            'information_hierarchy_layout_and_reason': 'Текущий выбор и результат перед вторичными деталями для быстрого чтения.',
            'content_density_long_labels_focus_keyboard_and_applicable_accessibility': 'Длинная подпись переносится; tab order и return focus требуют native проверки.',
            'relevant_state': 'B после A', 'trigger': 'B завершился, затем поздний A',
            'visible_result': 'Остаётся B', 'next_action': 'Следующий выбор по существующему owner-у',
            'cancellation_retry_stale_result_and_existing_owner_only_when_applicable': 'Stale решает существующая identity; не добавлять второй manager. Cancel не обещан.',
            'inapplicable_states_reason_distinct_from_unavailable_test_access': 'Permission неприменим только в учебном входе без авторизации; native доступ отсутствует, это NOT_RUN.',
            'bounded_behavior_rendered_interaction_source_and_native_or_browser_checks': 'Design/source review отдельно от behavioral и rendered/interaction.',
            'existing_check_commands_or_explicitly_unknown_not_invented': 'Команда GUI пока неизвестна; не выдумывать запуск.',
            'actual_artifact_revision_conditions_observations_or_not_run_limits': 'Учебный draft; native/visual NOT_RUN, нет GUI входа. Проверяется только паспорт формы.',
            'authorized_ui_change_scope_and_contract_dependencies': 'Разрешён только этот учебный текст, реализация не выполнена.',
            'affected_guides_or_no_guide_impact_reason': 'Реальный интерфейс не изменён, guide-impact отсутствует.',
            'remaining_decision_owner_local_acceptance_policy_or_finished_scope': 'Owner учебного проекта определит native проверку и приёмку.',
        }
        text = '\n'.join(line for line in text.splitlines() if not line.startswith('>'))
        text = API['TOKEN'].sub(lambda match: values[match[0][2:-2]], text)
        self.put('docs/ui.md', text)
        report = self.check({'AGENTS.md': 'native', 'docs/engineering.md': 'authoring', 'docs/ui.md': 'authoring'})
        self.assertEqual(report['exit_code'], 0, report)
        self.assertEqual(report['findings'], [], report)

    def test_quality_templates_adapt_to_valid_draft_outputs(self):
        corpus = {}
        for index, relative in enumerate(("foundation/testing-strategy.md.tmpl", "foundation/observability-policy.md.tmpl", "instructions/testing.md.tmpl", "instructions/logging.md.tmpl")):
            text = (KIT / "pack/templates" / relative).read_text(encoding="utf-8")
            text = API["TOKEN"].sub(lambda match: "2026-10-19" if match[0] == "{{date}}" else f"EXAMPLE-{index}", text)
            # A mechanical form/type witness only; not an agent-guided adaptation.
            text = "\n".join(line for line in text.splitlines() if not line.startswith(">"))
            output = "docs/" + relative.removesuffix(".tmpl")
            self.put(output, text)
            corpus[output] = "authoring"
        checker = API["Checker"](self.root, corpus, "project")
        report = checker.run()
        self.assertEqual(report["exit_code"], 0, report["findings"])
        self.assertEqual(len(checker.docs), 4)
        self.assertTrue(all(data["status"] == "draft" for data in checker.docs.values()))

    def test_python_fixture_declared_cli_behavior(self):
        result = subprocess.run([sys.executable, "-I", "-B", str(KIT / "tests/fixtures/python-cli/main.py"), "Example"], cwd=self.root, capture_output=True, text=True, timeout=10)
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout.strip(), "Hello, Example!")

    def assert_portable_text(self, path, raw):
        text = raw.decode("utf-8")
        for marker in PORTABLE_PRIVATE_MARKERS:
            self.assertFalse(marker in text, f"Forbidden portable marker {marker!r}: {path}")
        exact_snapshot = (path == FILECITE_SNAPSHOT
                          and hashlib.sha256(raw).hexdigest() == SOURCE_SHA256[FILECITE_SNAPSHOT])
        self.assertTrue("filecite" not in text or exact_snapshot,
                        f"Unexpected filecite outside exact original snapshot: {path}")

    def test_portable_text_has_no_source_project_or_machine_identity(self):
        pack = KIT / "pack"
        for file in pack.rglob("*"):
            if file.is_file() and file.suffix in {".md", ".tmpl", ".base", ".txt", ".py"}:
                path = file.relative_to(pack).as_posix()
                with self.subTest(control="actual-pack", path=path):
                    self.assert_portable_text(path, file.read_bytes())

        snapshot = (pack / FILECITE_SNAPSHOT).read_bytes()
        self.assertTrue(b"filecite" in snapshot, "Original snapshot must exercise the citation exception")
        self.assert_portable_text(FILECITE_SNAPSHOT, snapshot)
        # Same digest outside the one path must not inherit the exception.
        other_paths = ("README.md", "references/architecture/command-first/README.md",
                       "skills/pf-command-first/SKILL.md",
                       "references/ui/" + Path(FILECITE_SNAPSHOT).name,
                       *(path for path in SOURCE_SHA256 if path != FILECITE_SNAPSHOT))
        for path in other_paths:
            with self.subTest(control="filecite-other-path", path=path):
                with self.assertRaisesRegex(AssertionError, "Unexpected filecite"):
                    self.assert_portable_text(path, snapshot)
        # Correct path alone cannot admit any changed bytes or added citation.
        for change, raw in (("changed-byte", snapshot + b"\n"),
                            ("extra-citation", snapshot + b"\n<!-- filecite -->\n"),
                            ("replacement", b"<!-- filecite -->\n")):
            with self.subTest(control="filecite-mutated-snapshot", change=change):
                with self.assertRaisesRegex(AssertionError, "Unexpected filecite"):
                    self.assert_portable_text(FILECITE_SNAPSHOT, raw)
        # Every other sentinel remains active, including at the original path.
        for marker in PORTABLE_PRIVATE_MARKERS:
            for path, raw in (("README.md", b"# Synthetic control\n"), (FILECITE_SNAPSHOT, snapshot)):
                with self.subTest(control="private-marker", path=path, marker=marker):
                    with self.assertRaisesRegex(AssertionError, "Forbidden portable marker"):
                        self.assert_portable_text(path, raw + b"\n" + marker.encode("utf-8"))
        # Selected static sentinels only; not a proof that all private data is absent.

    def test_two_input_fixtures_preserve_local_manual_rules(self):
        fixtures = KIT / "tests/fixtures"
        self.assertTrue((fixtures / "python-cli/main.py").is_file())
        self.assertIn("MANUAL-RULE-KEEP", (fixtures / "existing-js/AGENTS.md").read_text(encoding="utf-8"))
        self.assertIn("MANUAL-NOTE-KEEP", (fixtures / "existing-js/docs/instructions/local.md").read_text(encoding="utf-8"))
        # Input witnesses only, deliberately no pretend bootstrap/merge implementation.


if __name__ == "__main__":
    unittest.main()
