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

Полный прогон требует завершённого согласованного `pack/`. Во время параллельного
редактирования положительный и отказные контракты семи навыков проверяются отдельно,
без чтения всего payload:

```text
.venv/Scripts/python.exe -I -B -m unittest discover -s tests -p test_check_foundation.py -k test_pack_relocation_checks_actual_resources_not_cwd -v
.venv/Scripts/python.exe -I -B -m unittest discover -s tests -p test_check_foundation.py -k test_pack_exact_seven_names_and_cli_input_failures -v
```

Первый тест использует синтетический пакет с семью именами, включая
`pf-command-first`, затем удаляет настоящий ресурс и требует exit1. Он пригоден
для RED на прежней реализации с шестью навыками и GREEN на новой. Второй независимо
проверяет точные имена, отсутствие каждого каталога/`SKILL.md`, лишний восьмой и
подменённое имя при сохранении семи каталогов: для каждого отказа нужен exit2.
Это не полная приёмка интегрированного пакета.

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

Семь имён независимо заданы литералами; названия не берутся из реализации.
Переносится весь фактический пакет в каталог с кириллицей и пробелами; совпадают
полный инвентарь файлов и их байты. Сохраняются обе UI-платформы, три метода,
LICENSE/provenance/notices, новый архитектурный навык и справка по CLI-first-поставке, маршрут
FigCraft и все шесть оригиналов. Отдельно удерживаются ссылки новых входов к
нужной справке. После переноса удаление web-ресурса, CLI-first-справки, исходной
карты `00_README.md` или оригинала FigCraft требует exit1 с конкретным `link.missing`.
Допустимые `not_checked` в полном пакете перечислены точно: три Bases и пять
исходных документов с wiki-ссылками, без ослабления проверки до одного exit0.

Шесть литеральных SHA-256, снятых с оригиналов **2026-10-23** до импорта,
проверяют сохранность исходных байтов, включая YAML, код и ссылки. Для этих
Markdown-справок используется `native`, не паспорт PFK-заметки; импорт не превращает
их содержание в принятую архитектуру. Тесты не требуют исходного хранилища на
машине получателя.

Sentinel `filecite` допускает только неизменённый
`pack/references/architecture/command-first/04_Command_First_Image_Converter_Architecture.md`
с SHA-256 `5e192de874844862046c9d737ceda63fc7cb61bc024118c63d8553dcc5ebf0b8`.
Четыре исходных HTML-комментария содержат непрозрачные библиографические метки,
не секреты, доступные ресурсы или runtime-доказательства; они сохраняются побайтно.
В `test_portable_text_has_no_source_project_or_machine_identity` отказные контроли
проверяют копию тех же байтов по другому пути, изменённый снимок и добавленную метку.
Все остальные project/path sentinels действуют для каждого файла, включая оригинал;
их отдельные отказы также исполняются. Диагностика содержит маркер и путь, не тело
документа. Это узкое исключение, не отключение privacy-проверок каталога.

Конечный wiki-тест читает все пять оригиналов серии, исключает code spans/fences
и проверяет каждую наблюдаемую цель и точный текст обычного ATX-заголовка.
Поддерживаются только имеющиеся формы `[[stem#heading|label]]` и `[[#heading]]`
с необязательной подписью; пропавшая цель/заголовок дают отказ. Незнакомый синтаксис
явно останавливает свидетельство с `NOT VERIFIED`, а не считается проверенным.
Отрицательные контроли охватывают отсутствующие цели, заголовок только в code fence,
незавершённый/неподдерживаемый wiki-синтаксис и embed. Общий checker сохраняет
`link.wiki: not_checked`; Obsidian, block IDs, alias resolution и произвольный
Markdown-renderer не реализуются. Это проверка сохранности и ссылок, не исполнение
примеров, FigCraft или моделей и не доказательство практического применения.

Populated minimal and UI examples are checked as native/authoring outputs, not
hidden under templates. This is grammar evidence, not application or GUI acceptance.
Additional finite exercises:
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
| 10 | Relocation keeps resources | Synthetic seven-skill and full actual pack copied to Cyrillic/space path, including six source-byte snapshots and new routes; CLI resolves `__file__` | Final complete-pack relocation check after integration; client use is separate |
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
