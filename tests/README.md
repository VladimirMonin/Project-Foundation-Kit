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
from `__file__`. Temporary tests/relocations use `pfk-quality/` under stdlib's
`tempfile.gettempdir()` and are cleaned by their owners. For a bounded author run,
set TMPDIR/TEMP/TMP to that run's allocated scratch before starting the native
interpreter; the tests do not need repository scratch files. No index writes. See
[checker contract and raw exits](../pack/tools/README.md).

Полный прогон требует завершённого согласованного `pack/`. Во время параллельного
редактирования положительный и отказные контракты десяти навыков проверяются отдельно,
без чтения всего payload:

```text
.venv/Scripts/python.exe -I -B -m unittest discover -s tests -p test_check_foundation.py -k test_pack_relocation_checks_actual_resources_not_cwd -v
.venv/Scripts/python.exe -I -B -m unittest discover -s tests -p test_check_foundation.py -k test_pack_exact_ten_names_and_cli_input_failures -v
.venv/Scripts/python.exe -I -B -m unittest discover -s tests -p test_check_foundation.py -k source_not_shipped -v
.venv/Scripts/python.exe -I -B -m unittest discover -s tests -p test_check_foundation.py -k test_source04_filecite_exception_remains_path_and_raw_digest_scoped -v
```

Первый тест использует синтетический пакет с десятью именами и удаляет ресурс,
требуя exit1. Второй независимо проверяет точные имена, отсутствие каждого
каталога/`SKILL.md`, лишний одиннадцатый и подмену имени при сохранении десяти
каталогов: для каждого отказа нужен exit2. В 0.4.0 к прежним семи явно добавлены
только `pf-retrospective`, `pf-memory-inventory`, `pf-caveman`; произвольное расширение
набора не разрешается. Source-specific семейство читает только 13 закреплённых
оригиналов и собственные синтетические пакеты, не текущую работу других авторов.
Тест source04 отдельно удерживает прежнюю privacy-границу. Это не полная приёмка
интегрированного пакета; full relocation, общие routes/forms и actual-pack privacy
запускаются после завершения всех авторов на согласованном кандидате.

## What automated checks actually establish

`test_check_foundation.py` tests valid typed documents/native grammar, malformed
fields/dates/kinds, duplicate keys/IDs, unsafe YAML/anchors/merge keys, accepted
placeholders, explicit template-vs-output classification, common local links and
anchors (including code-only/mixed/duplicate headings), adjacent footnotes without
false reference links, real links in footnote bodies, code-formatted inline/image/
angle/reference labels, textual reference identity and casefold, literal spans with
complete equal-length backtick delimiters, HTML IDs/wiki exclusion, unselected-body read exclusion, translations/revision mismatch, native
SKILL/resource paths, `.base` YAML shape and declared exclusion predicates, CLI
exits 0/1/2 and relocation into a Cyrillic/space path from unrelated cwd.

Tests inspect **declared predicates** in the three shipped `.base` files; they do
not implement/evaluate Bases expressions or prove Obsidian rendering. Static
contamination sentinels are a finite check, not universal secret detection.
A passing validator test is not evidence that an agent follows the skills.

Десять имён независимо заданы литералами; названия не берутся из реализации.
Переносится весь фактический пакет в каталог с кириллицей и пробелами; совпадают
полный инвентарь файлов и их байты. Сохраняются Django, React и PySide6, условный
GUI-runtime, методы контрактов/impact/регрессии/поставки, все десять native-входов,
LICENSE/provenance/notices и Apache-2.0 LICENSE Caveman, Pi-memory reference,
CLI-first и FigCraft-маршруты, все 13 оригиналов. Отдельно удерживаются ссылки
новых входов к нужной справке. После переноса удаление обычной статьи 05–07,
Django/GUI-runtime/web-ресурса, справки поставки, `00_README.md` или оригинала FigCraft
требует exit1 с конкретным `link.missing`.
Допустимые `not_checked` перечислены точно, с частотой: три Bases, пять документов
с wiki-ссылками и 184 употребления 13 исторических пар из
[ограниченной политики](../pack/tools/README.md#непоставленные-исторические-исследования).
Совпадение лишь exit0 не считается достаточным.

13 литеральных SHA-256 из независимой карты выбранных редакций **2026-10-26**
проверяют сохранность исходных байтов, включая YAML, код и ссылки. Значения не
получаются из checker-а, текущего файла или скачивания при тесте. Для этих
Markdown-справок используется `native`, не паспорт PFK-заметки; импорт не превращает
их содержание в принятую архитектуру. Тесты не требуют исходного хранилища на
машине получателя.

Исторические пары и частоты также заданы независимыми литералами. Положительный
CLI-контроль использует полные реальные оригиналы внутри синтетического ten-skill
пакета в пути с пробелами/кириллицей, из другого cwd. Отрицательные случаи:
один добавленный байт, BOM, EOL, изменённая цель, те же байты по другому пути,
неверная цель при квалифицированном снимке, существующая цель/её anchor и настоящий
сломанный ресурс. `--project` сохраняет все обычные `link.missing`; JSON и native
exits 0/1/2 проверяются отдельно от результата unittest.

Post-load synthetic body в двух адресных тестах изолирует буквальный destination
и порядок boundary-проверок от digest-guard; это не новая исходная статья или
end-to-end доказательство подменённого документа. Отдельный настоящий CLI-тест
проверяет неизменённые байты без таких подмен. Детерминированный symlink-marking
проверяет порядок отказа. Реальный dangling-target/input-symlink проверяется
отдельным filesystem-тестом; при отсутствии права создать symlink он честно skip,
а не native PASS. Boundary-правила и privacy не ослабляются ради источников.

Sentinel `filecite` допускает только неизменённый
`pack/references/architecture/command-first/04_Command_First_Image_Converter_Architecture.md`
с SHA-256 `5e192de874844862046c9d737ceda63fc7cb61bc024118c63d8553dcc5ebf0b8`.
Четыре исходных HTML-комментария содержат непрозрачные библиографические метки,
не секреты, доступные ресурсы или runtime-доказательства; они сохраняются побайтно.
В `test_source04_filecite_exception_remains_path_and_raw_digest_scoped` отказные контроли
проверяют копию тех же байтов по другому пути, изменённый снимок и добавленную метку.
Все остальные project/path sentinels действуют для каждого файла, включая оригинал;
их отдельные отказы также исполняются. Диагностика содержит маркер и путь, не тело
документа. Это узкое исключение, не отключение privacy-проверок каталога.

Конечный wiki-тест читает все восемь оригиналов Command-first, исключает code spans/fences
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
hidden under templates. Contract, verification and handoff forms are populated as
draft authoring outputs too. This is grammar evidence, not application or GUI acceptance.
Additional finite exercises:
[AD-01–AD-33](ADAPTATION_CASES.md); AD-13–AD-19 cover result depth, Django, effects
and delivery; AD-20–AD-22 cover retrospective, read-only memory inventory and exact
Caveman explanations. These are definitions, not executed model trials. Author observations, independently reviewed
clean applications/comparison and remaining qualification: [ACCEPTANCE](../docs/ACCEPTANCE.md).

Version 0.5.0 appends AD-23–AD-30 for justified boundaries, test usefulness and
mechanism reduction, and AD-31–AD-33 for selection intent, late verification and
existing whole-screen/shared-component checks. The original cases and history are
preserved. These remain NOT_RUN model/GUI definitions, not new executable tests or
a release requirement to run product code. Existing full-pack relocation includes
the two new method files because it compares the actual complete payload.

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
| 10 | Relocation keeps resources | Synthetic ten-skill and full actual pack copied to Cyrillic/space path, including 13 source-byte snapshots and new routes; CLI resolves `__file__` | Final complete-pack relocation check after integration; client use is separate |
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
scratch `перенос пакета/` folder, run its own `tools/check_foundation.py --pack`
from a different cwd with the tooling interpreter, inspect output, then remove only
the owned copy. This checks resource paths, not skill discovery/loading by every client.
