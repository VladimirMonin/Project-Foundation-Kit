"""Focused validator tests; these are NOT agent-guided bootstrap acceptance."""
import json
from pathlib import Path
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
        pack = self.root / "перенос пакета"
        (pack / "references").mkdir(parents=True)
        (pack / "references/quality.md").write_text("# Synthetic resource\n", encoding="utf-8")
        (pack / "tools").mkdir()
        shutil.copyfile(CHECKER, pack / "tools/check_foundation.py")
        for name in ("pf-bootstrap", "pf-plan", "pf-maintain", "pf-quality", "pf-guides", "pf-ui-design"):
            folder = pack / "skills" / name
            folder.mkdir(parents=True)
            (folder / "SKILL.md").write_text(f'---\nname: {name}\ndescription: "Synthetic relocation skill"\n---\n[resource](../../references/quality.md)\n', encoding="utf-8")
        result = subprocess.run([sys.executable, "-I", "-B", str(pack / "tools/check_foundation.py"), "--pack"], cwd=KIT, capture_output=True, text=True, timeout=30)
        self.assertEqual(result.returncode, 0, result.stderr + result.stdout)
        (pack / "references/quality.md").unlink()
        result = subprocess.run([sys.executable, "-I", "-B", str(pack / "tools/check_foundation.py"), "--pack"], cwd=KIT, capture_output=True, text=True, timeout=30)
        self.assertEqual(result.returncode, 1)

    def test_pack_exact_six_names_and_cli_input_failures(self):
        # Independent literal expectation: never import the implementation's set.
        expected = {'pf-bootstrap', 'pf-plan', 'pf-maintain', 'pf-quality', 'pf-guides', 'pf-ui-design'}
        self.assertEqual({p.name for p in (KIT / 'pack/skills').iterdir() if p.is_dir()}, expected)
        pack = self.root / 'полный pack'
        shutil.copytree(KIT / 'pack', pack)
        self.assertEqual(self.cli('--pack', pack).returncode, 0)
        ui = pack / 'skills/pf-ui-design'
        ui.rename(self.root / 'held-ui')
        result = self.cli('--pack', pack)
        self.assertEqual(result.returncode, 2, result.stdout)
        self.assertEqual(json.loads(result.stdout)['exit_code'], 2)
        (self.root / 'held-ui').rename(ui)
        (pack / 'skills/unexpected-seventh').mkdir()
        self.assertEqual(self.cli('--pack', pack).returncode, 2)
        (pack / 'skills/unexpected-seventh').rmdir()
        (ui / 'SKILL.md').unlink()
        self.assertEqual(self.cli('--pack', pack).returncode, 2)

    def test_full_actual_pack_relocation_includes_methods_platforms_and_notices(self):
        pack = self.root / 'перенос всего pack'
        shutil.copytree(KIT / 'pack', pack)
        required = ('references/methods/contract-evolution.md', 'references/methods/change-impact.md',
                    'references/methods/behavior-regression.md', 'skills/pf-ui-design/SKILL.md',
                    'skills/pf-ui-design/references/web-react.md',
                    'skills/pf-ui-design/references/desktop-pyside6.md',
                    'templates/documents/ui-design.md.tmpl', 'LICENSE', 'UPSTREAM.md', 'THIRD_PARTY_NOTICES.md')
        for path in required:
            self.assertEqual((pack / path).read_bytes(), (KIT / 'pack' / path).read_bytes())
        command = [sys.executable, '-I', '-B', str(pack / 'tools/check_foundation.py'), '--pack']
        result = subprocess.run(command, cwd=self.root.parent, capture_output=True, text=True, timeout=30)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        report = json.loads(result.stdout)
        self.assertEqual(len(report['findings']), 3, report)
        self.assertTrue(all(f['code'] == 'base.not_rendered' and f['severity'] == 'not_checked' for f in report['findings']))
        (pack / 'skills/pf-ui-design/references/web-react.md').unlink()
        result = subprocess.run(command, cwd=self.root.parent, capture_output=True, text=True, timeout=30)
        self.assertEqual(result.returncode, 1)
        self.assertIn('link.missing', self.codes(json.loads(result.stdout)))

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

    def test_portable_text_has_no_source_project_or_machine_identity(self):
        for file in (KIT / "pack").rglob("*"):
            if file.is_file() and file.suffix in {".md", ".tmpl", ".base", ".txt", ".py"}:
                text = file.read_text(encoding="utf-8")
                with self.subTest(path=file.relative_to(KIT)):
                    self.assertNotIn("Whisper-Voice-Machine", text)
                    self.assertNotIn("C:/PY/", text)
                    self.assertNotIn("C:\\\\Users\\\\", text)
                    self.assertNotIn("WVM_DEV", text)
                    self.assertNotIn("filecite", text)
        # Selected static sentinels only; not a proof that all private data is absent.

    def test_two_input_fixtures_preserve_local_manual_rules(self):
        fixtures = KIT / "tests/fixtures"
        self.assertTrue((fixtures / "python-cli/main.py").is_file())
        self.assertIn("MANUAL-RULE-KEEP", (fixtures / "existing-js/AGENTS.md").read_text(encoding="utf-8"))
        self.assertIn("MANUAL-NOTE-KEEP", (fixtures / "existing-js/docs/instructions/local.md").read_text(encoding="utf-8"))
        # Input witnesses only, deliberately no pretend bootstrap/merge implementation.


if __name__ == "__main__":
    unittest.main()
