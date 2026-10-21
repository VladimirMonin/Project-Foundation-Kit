# Quality checks and two clean-agent application inputs

These are **synthetic fixtures and validator tests**, not copies of an application.
No app, model, network service, GUI or package-manager install is required. Tests
use stdlib unittest plus the checker's separate pinned PyYAML dependency.

From the Kit root, using its existing isolated tooling environment:

```text
.venv/Scripts/python.exe -I -B -m unittest discover -s tests -p test_*.py -v
.venv/Scripts/python.exe -I -B pack/tools/check_foundation.py --pack
```

On another platform use that environment's actual interpreter path. The same
commands work with absolute paths from an unrelated cwd; tests resolve resources
from `__file__`. Temporary tests/relocations live only under `artifacts/quality/`
and are cleaned by their owners. No index writes. See
[checker contract and raw exits](../pack/tools/README.md).

## What automated checks actually establish

`test_check_foundation.py` tests valid typed documents/native grammar, malformed
fields/dates/kinds, duplicate keys/IDs, unsafe YAML/anchors/merge keys, accepted
placeholders, explicit template-vs-output classification, common local links and
anchors (including code-only/mixed/duplicate headings), code-formatted inline/image/
angle/reference labels, textual reference identity and casefold, literal spans with
complete equal-length backtick delimiters, HTML IDs/wiki exclusion, unselected-body read exclusion, translations/revision mismatch, native
SKILL/resource paths, `.base` YAML shape and declared exclusion predicates, CLI
exits 0/1/2 and relocation into a Cyrillic/space path from unrelated cwd.

Tests inspect **declared predicates** in the three shipped `.base` files; they do
not implement/evaluate Bases expressions or prove Obsidian rendering. Static
contamination sentinels are a finite check, not universal secret detection.
A passing validator test is not evidence that an agent follows the skills.

The exact six names are independently asserted. Missing `pf-ui-design`, an extra
seventh directory, and a directory without SKILL each require native CLI exit 2.
Full-pack relocation includes both UI platform references, all three methods,
LICENSE/provenance/notices. Populated minimal and UI examples are checked as
native/authoring outputs, not hidden under templates. This is grammar evidence,
not application or GUI acceptance. Additional finite exercises:
[AD-01–AD-12](ADAPTATION_CASES.md); author observations, independently reviewed
clean applications/comparison and remaining qualification: [ACCEPTANCE](../docs/ACCEPTANCE.md).

## Twelve original application obligations — evidence boundary

| # | Obligation | Available automated/input witness | Required real application witness |
|---|---|---|---|
| 1 | New project receives honest sufficient foundation | `fixtures/python-cli/PROJECT.md`, valid/type/token tests | Clean executor uses finished pack; actual docs/commands vs unknowns reviewed |
| 2 | Existing rules/manual additions survive | `fixtures/existing-js/AGENTS.md`, native instruction, two MANUAL keep tokens | Executor preserves their meaning/ownership during adaptation |
| 3 | Repeat is no-op without duplicates | Both PROJECT tasks specify second pass | Actual second skill invocation and justified path/diff result; hashes alone insufficient |
| 4 | Significant feature has scenario/plan/delta | Python fixture's proposed `--uppercase` task | Agent chooses minimal forms and criteria without calling proposal implemented |
| 5 | Small fix stays small | Python fixture's punctuation task | No new architectural programme or unrelated docs |
| 6 | Contract change reaches owner instruction/reference | Existing-JS educational future-contract task | Agent names/updates true owner and knowledge, current/proposed kept separate |
| 7 | Primary guide change affects translation | Revision tests: equal dates, mismatch warning, false-current error | Agent performs content review; real pair marked outdated or synchronized honestly |
| 8 | New document fits selection conditions | Metadata/kind tests and static shipped Bases predicates | Adapted document has required properties/path; actual renderer remains separate |
| 9 | Markdown works without Obsidian | Relative links/ordinary Markdown; no GUI dependency in tests | Clean executor navigates docs as files; no GUI acceptance claim |
| 10 | Relocation keeps resources | Synthetic six-skill and full actual pack copied to Cyrillic/space path; CLI resolves `__file__` | Final complete-pack relocation check after integration; client use is separate |
| 11 | Assumptions do not become accepted facts | Placeholder/status/type rejection; fixture tasks require draft/proposed | Human reviews semantic claims; checker cannot know truth of prose |
| 12 | Portable pack has no source-project/private baggage | Finite static path/project/citation sentinel test | Integrated package/ZIP content review, no source env/logs/history copied |

The right column requires actual independently scoped application evidence; the
observed edition's outcomes and limits are recorded in [ACCEPTANCE](../docs/ACCEPTANCE.md).
Do not replace application with a templater, automatic merge harness, hash equality
or an LLM evaluator embedded in unit tests. The author does not launch another agent.

## Clean executor handoff after integration

Give one new executor only:
1. The complete finished `pack/`, not an isolated SKILL and not development chats.
2. One owned disposable copy of [Python/CLI input](fixtures/python-cli/PROJECT.md)
   or [existing JS input](fixtures/existing-js/PROJECT.md), with its tiny files.
3. Its finite write boundary, allowed checks, expected paths/results, and no
   permission for global settings, real secrets, network, app calls or publication.

Have it find the appropriate skills/resources, bootstrap, apply the named change
exercises, and reapply. Capture actual changed paths, preserved local rules,
no-op/conflict decisions, assumption statuses, guide revisions/lag, raw checks and
limits in the existing integrated acceptance record. No per-file reports or new
checkpoint/manifest chain. No implementation of the hypothetical features is needed.

For portability after peer release, copy **only finished pack contents** to an owned
`artifacts/quality/перенос пакета/` folder, run its own `tools/check_foundation.py --pack`
from a different cwd with the tooling interpreter, inspect output, then remove only
the owned copy. This checks resource paths, not skill discovery/loading by every client.
