# Проверки и ограничения

## Независимая проверка 0.2.0: применение и ограниченное сравнение · 2026-10-21

**Приняты исходная реализация, два clean-context применения и оба ограниченных
прогона AD-01–12.** Это не полная web/native UI квалификация, не release/tag и не
гарантия всех клиентов/платформ. Один прогон каждой редакции не доказывает её
статистическое или причинное превосходство. Сохранённый авторский срез ниже
описывает состояние до независимой проверки, а не текущий итог применения.

### Исходники и независимые gates

Frozen-кандидат: 41 файл PFK от базы `148495df39912a04518082ff0d9a523f9305c450`
и только README/setup связанной сборки. Все 43 хеша и exact changed scope проверены,
HEAD/index не менялись. Root AGENTS, исходные fixtures, зависимости, лицензии PFK и
architecture/quality/observability основания сохранены. Required source findings нет.
Текущая правка этого документа — отдельный фактический closeout, не изменение pack.

Независимо: 32/32 unittest, native exit 0; те же пять regression methods против
исходного checker-а — native exit 1, 11 failures по поведению, не окружению.
Финальный `--pack` — native exit 0, 61 ресурс, три Bases not_checked и 51 внешняя
ссылка без сетевой проверки. Проверены дополнительные реальные Checker.run inputs,
reference identity, literals, duplicate/code headings, missing fragment и отсутствие
чтения невыбранного тела. Full-pack relocation и заполненные minimal/UI outputs
прошли; это структура/grammar, не UI evidence. Сохранённые полные Stage1/final
поставки сверены по всем байтам; их собственные checker-ы дали 52/61 ресурс, exit 0.

Build repository-only gate независимо повторён с уже установленными Python 3.14.2
и jsonschema 4.26.0 через process-local PATH: **native exit 0, failures=0 warnings=0**.
Ничего не устанавливалось; прежний авторский dependency failure не удалён из истории.
Safety с явным build root — **exit 0, Both 426 entries**. С PFK root — **exit 1,
15 findings**: все независимо классифицированы как pinned public ECC/UIZZE source
URLs, не credentials. Это не clean-scan PASS. Gitleaks 8.30.1 с полной redaction:
43 candidate files и полный PFK tree (82 файла) — exit 0, без findings; полный build
(213 файлов) — exit 1, два неизменённых false positives: synthetic redaction-test
sentinel и C# API-results declaration. Правила не ослаблялись. Это покрытие файлов,
не новый scan Git history. Существенные ограничения сборки и исторические failures
сохранены; все 19 fenced setup-блоков неизменны, взаимные GitHub README targets
ответили HTTP 200. Ни runtime/install/restart, ни Code/Task/provider не менялись.

### Native Pi: от explicit delivery к применению

Два разных чистых контекста получили по одной owned-копии исходной fixture и весь
финальный **64-файловый pack 0.2.0**, без истории разработки и готового перечня
выходных документов. Среда: Pi **1.3.0**, Node **26.7.0**; в обеих сессиях фактически
`openai-codex / gpt-6.1-sol / high`. Это reduced CLI, не повтор exact полной сборки
с pinned Node25.8.1. Контекст/skills задавались явно: `--no-context-files`,
`--no-skills` с `--skill tools/project-foundation/skills`, `--no-prompt-templates`,
`--no-extensions`, `--no-mcp`, `--no-approve`. Домашние auth/config не читались.

Независимо просмотрены outputs и относящиеся tool events, не только APPLY_RESULT:

- **Python:** прочитаны bootstrap/plan/maintain/quality SKILL, lifecycle/metadata/
  quality/minimal-adoption, contract-evolution и выбранные формы из доставленного
  экземпляра. Выход — native AGENTS, один engineering owner с разделами инструкций,
  один proposed `--uppercase` plan, corpus и один evidence report. Нет обязательного
  YAML-профиля, дерева четырёх политик или ADR на пунктуацию.
- **JS:** прочитаны bootstrap/plan/maintain/guides/quality, те же применимые shared
  references и формы. Original native AGENTS/local instruction сохранены байт-в-байт
  с добавлением только навигации. Current contract ведёт к настоящему owner-у
  `docs/instructions/local.md`; future `upper` остаётся proposed, formatter не менялся.
- В обеих сессиях перед вторым решением заново прочитаны bootstrap/lifecycle/metadata,
  текущие правила и адаптация. Обоснован **foundation no-op**: после этого изменялся
  только уже объявленный report/raw evidence, не документы основы, даты или правила.
  Восстановление последовательности write/edit из tool events совпало с released
  файлами. Это процедура и решение, не одно сравнение хешей.

Во всех двух копиях полный pack совпадает с финальной поставкой по paths/байтам;
PROJECT и исходный Python/JS код неизменны. Отдельный loader probe этих исполнителей
не выполнялся. Подтверждено native model application выбранных local skills/resources,
не автоматическое обнаружение, запуск с settings fragment или применение всех шести
навыков. UI skill не требовался. Исходные checkout fixtures не редактировались.

### Все 12 исходных обязательств: принятый ограниченный результат

| # | Независимо проверенный результат | Граница |
|---|---|---|
| 1 | Python получил достаточную компактную основу, реальные команды и явные неизвестные | Один synthetic проект, не универсальная надёжность bootstrap |
| 2 | JS сохранил обе MANUAL rules, native grammar, имя/named export, two-space style и запреты dependency/silent case change | Исходный formatter не менялся |
| 3 | Оба исполнителя действительно повторили bootstrap и обосновали no-op; документы/даты не переписаны | Тот же executor внутри каждой сессии, не второй независимый запуск |
| 4 | Future `--uppercase`: пользователь, сценарий, отказ, old/new, совместимость, срезы и критерии | Proposed; реализация и её будущие проверки NOT_RUN |
| 5 | Python punctuation fix — ровно одна добавленная точка в engineering owner | Без изменения source, дат, ADR или нового плана |
| 6 | JS proposal → current reference → native local owner; названы точные updates после разрешённой реализации | Нельзя считать `upper` реализованным или отменять manual ban |
| 7 | RU/EN r1/r1 созданы и проверены; RU получил смысл empty/null и r2, EN остался r1/outdated с warning и owner handoff | Даты равны; обязательный EN sync до release-ready claim остаётся задачей проекта |
| 8 | Все новые durable Markdown выбраны как authoring, исходные native — native; ID/kind/status/quoted dates и конечные пути валидны | Obsidian selection/rendering не выполнялись |
| 9 | Исполнители реально читали файлы и относительные routes без Obsidian | Нет rendered/GUI claim |
| 10 | В каждой application-копии сохранены все 64 файла, включая notices, методы и platform refs; выбранные ресурсы реально прочитаны | Не все ресурсы требовались задаче; global collision/discovery не доказаны |
| 11 | Source facts, assumptions/draft и proposed поведение разделены; не выдуманы npm test, pytest или shipped flags | Структурный checker сам истинность текста не доказывает |
| 12 | Pack не получил fixture outputs, машинных путей, logs/auth/runtime baggage; исходные задачи/код сохранены | Synthetic отчёты остаются вне публичного pack; ZIP отдельно не собирался |

### Выполненные проверки и наблюдённое использование

Python выполнил **четыре** current-CLI subprocess cases без mocks: greeting/help —
child exit 0, missing name/unsupported uppercase — child exit 2; assertion harness —
exit 0. Повтор тех же четырёх не считается восемью уникальными тестами. JS выполнил
**14 source-boundary assertions** через data-URL из настоящих bytes: точные строки,
conversion-error identity и следующий успешный вызов, native exit 0. Это не installed
consumer, future upper или parity двух режимов; четыре CLI cases и 14 assertions
не складываются в ложный общий suite.

Scoped checker из каждого project root:

```sh
python -I -B tools/project-foundation/tools/check_foundation.py --project . --corpus docs/check-scope.json
```

`python` здесь — разрешённый tooling interpreter с PyYAML. Python corpus: **5**, exit 0,
findings пусты. JS r1 corpus: **10**, exit 0, translation current; final corpus: **10**,
exit 0, ровно ожидаемый `translation.outdated`, revision_match false. Reviewer повторил
оба final checker-а: те же native exits/counts/findings. Предметная проверка перевода
отдельно подтвердила реальный content delta; warning не отфильтрован ради PASS.
Первичный Git status в обоих scratch roots дал exit 128 (не Git-репозитории), не
ошибку продукта. Финальный JS placeholder-search exit 1 означал отсутствие совпадений.

| Контекст | Assistant response/model-call records | Input | Output | Cache-read |
|---|---:|---:|---:|---:|
| Python | 23 | 78 354 | 14 128 | 910 080 |
| JS | 32 | 73 580 | 17 240 | 1 219 456 |

Это суммы полей usage записанных ответов, не число tools или независимых тестов,
не уникальные токены контекста и не доказательство отсутствия скрытых transport retries.
Cache-write в обоих — 0. Клиентские estimated cost fields не billing receipt;
фактическая денежная стоимость неизвестна, не 0. Расходы не выводятся из размера Markdown.

### Исправленная Stage1 ↔ финальная редакция: все AD-01–12

Два дополнительных независимых clean-context исполнителя получили одинаковые
задания и права, по одной полной поставке и исходным synthetic inputs. **Stage1 —
исправленная пятинавыковая база**, не original buggy 0.1.0; её heading ещё 0.1.0,
часть skill metadata уже 0.2.0. Поставки различались по проверенным bytes: 55 файлов
baseline против 64 final. Оригинальные inputs и package в обоих runs сохранены.
Общий boundary.py совпадает по всем raw bytes с CRLF; его hash не следует сравнивать
с hash нормализованного LF source text как будто это изменение stimulus.

В обоих runs фактически Pi1.3.0/Node26.7 и `openai-codex/gpt-6.1-sol/high`, без
объявленного token-budget cap. Baseline прочитал maintain/quality/plan/bootstrap и
относящиеся shared references/forms. Candidate прочитал maintain/quality/bootstrap/
ui-design, **все три methods**, web-react и desktop-pyside6; tool events подтверждают
полные чтения до соответствующих действий, а не только упоминания путей в отчёте.
Native application здесь — применение выбранных инструкций моделью в текущем CLI,
не отдельная аттестация loader/settings, полного build или Qt/browser runtime.

| Случай | Независимо принятый исход обоих runs | Существенная граница |
|---|---|---|
| AD-01 | Точная пунктуационная правка одной фразы в owned copy, код сохранён; без ADR/feature/полного audit | Ошибки encoding capture отделены от продукта и сохранены |
| AD-02 | Code-first serialize → реальные JSON bytes → настоящий display, owners названы | Нет второй ручной схемы или внешнего provider proof |
| AD-03 | Absent/null/numeric 0 различаются на wire и в consumer; or-zero control действительно отвергнут | Это принятая учебная семантика, не универсальная схема стоимости |
| AD-04 | Показаны vacuous empty и пропущенный второй элемент; достаточный populated field check и отдельный empty | Ожидаемые inner assertion failures проверены, не выданы за падающий native suite |
| AD-05 | Исполнены две названные локальные ветки против одного контракта; production-parity claim ограничен | Ветки различаются между runs; external production NOT_RUN |
| AD-06 | Сохранены collection/import ERROR exit 1, достигнутый null→0 assertion RED exit 1 и тот же test GREEN exit 0 после разрешённой fixture/subject коррекции | Test bytes неизменны, dependency error не RED продукта |
| AD-07 | Реальный scratch Git base/committed/staged/unstaged/untracked scope; connected consumer обнаружил несовместимый serialized field при clean tree | Baseline cost→amount оставлен как отрицательный контроль; candidate id→item_id затем адаптировал consumer. Не одинаковая миграция/benchmark |
| AD-08 | Сохранены surface=dark и ResultPanel, ограниченное решение hierarchy/wrapping/long label | Реальный UI source/rendered improvement не утверждается |
| AD-09 | Реальный OperationOwner: A→B, B, late A сохраняет B; accept-all wrong-owner отвергнут | Нет второго manager, React/Qt scheduling не проверены |
| AD-10 | Полезный desktop design/review и точные native/visual/interaction NOT_RUN | Нет GUI, HTML/import/mock не стали PASS или N/A |
| AD-11 | Cause/replacement/revisit сохранены в существующей истории; удалённый duplicate handler не воскрешён | Историческая cancellation responsibility не выдана за cancel API учебного owner-а |
| AD-12 | Компактное adoption с native manual rules, затем повторное полное чтение bootstrap/адаптации и обоснованный no-op | Шесть project paths и все bytes совпадают до/после; нет report ради повтора |

Reviewer повторил source-reviewed исполняемые проверки AD-02/03/04/05/09 обоих
runs: native exit 0, включая проверенные отрицательные исходы. AD06/07 оценены по
исходникам, сохранённым native runner observations и actual Git scope; исходные
failures не переписаны. AD12 checker-ы обоих исполнителей первоначально дали **exit 2,
dependency.missing (PyYAML)**. Повтор теми же delivered checker/corpus с уже имеющимся
tooling interpreter без installs: **exit 0, по 4 ресурса, findings пусты**. Это решает
observer dependency limitation, не меняет старый runner result и не доказывает JS
runtime. Полные pre-repeat byte snapshots сверены с released деревьями; actual reads
и no-op решения наблюдались отдельно от hashes.

| Comparison context | Уникальные model-response IDs | Input | Output | Cache-read |
|---|---:|---:|---:|---:|
| Corrected Stage1 baseline | 59 | 82 337 | 23 734 | 2 341 120 |
| Final candidate | 52 | 136 065 | 19 547 | 1 844 864 |

Это суммы полей usage записанных ответов; cache-write — 0 в обоих. Они не равны
уникальным context tokens или всем скрытым transport attempts. Reasoning tokens не
вычисляются из текста и не прибавляются второй раз; фактическая денежная стоимость
неизвестна. Меньшее число ответов или output tokens не доказывает дешевизну либо
лучшее качество. Оба runs достигли bounded задач, но сами создали различающиеся
fixtures, checks и design notes; это не perfectly matched benchmark и не causal
ablation. Подтверждены пригодность в этих условиях и фактическое применение новых
методов, **не измеренное превосходство** над уже исправленной базой.

### Точный остаток и граница сохранения

Настоящие web form/modal/focus и PySide6 long-operation/cancel/close/stale/resize/
scale проверки остаются **NOT_RUN**: в исходных fixtures нет GUI-приложений.
Source/design упражнения не заменяют native/rendered/interaction evidence;
отсутствие доступа не N/A. External production parity, автоматическое discovery/
settings-подключение, exact полной сборки Pi, Obsidian rendering и будущие upper/
uppercase implementations не квалифицированы этими runs. Не создавались demo apps,
новые frameworks, индексы, installs или дополнительный review-контур. Локальная
фиксация принятой source/docs дельты отделена от push, tag, release и рабочей
установки. Публичная готовность ограничена явно выполненным scope, не полным UI PASS.

## Сохранённый авторский срез 0.2.0 · 2026-10-21

**Статус: авторская реализация и ограниченная проверка; независимая приёмка и
clean-model/native/visual qualification pending.** Это не выпуск/tag и не объявление
«оба плана практически приняты». Исторические результаты 0.1.0 ниже не переносятся
на новый артефакт.

База PFK: `148495df39912a04518082ff0d9a523f9305c450`; версия исходников — 0.2.0.
Изменены bounded checker/tests, lifecycle и противоречащие consumers, минимальный
пример, три условных methods, шесть SKILL с UI web/desktop приложениями/формой,
portable provenance/notices, каталоги/версия и это свидетельство. Root AGENTS,
fixtures, лицензии PFK, dependencies и полезные architecture/observability основания
не менялись. У verification/feature-plan нет конкретного пробела: no-impact, новый
registry не нужен. Build scope — только README/setup, отдельно от методического pack.

### RED → GREEN и структурный охват

Среда: Windows, существующий изолированный Python **3.14.7**, PyYAML **6.0.3**;
установки зависимостей не выполнялись. Команды из корня PFK:

```sh
python -I -B -m unittest discover -s tests -p 'test_*.py' -v
python -I -B pack/tools/check_foundation.py --pack
```

| Проверка | Фактическое авторское наблюдение | Граница |
|---|---|---|
| Новые регрессии на исходном Checker.run | RED: общий прогон 29 методов, exit 1, 11 failures/subtests; не dependency/collection failure | Пропадали inline/image/full/collapsed code-label targets, reference identity, headings и anchor_scope; дополнительно нарушалась literal-definition граница |
| Те же регрессии после role-aware fix, Stage1 | 29/29, exit 0; полный pack — 52 ресурса, exit 0 | Исправленные пять навыков, не buggy 0.1.0; inline/image/angle/reference, code-only/кириллический/duplicate slug и настоящий missing control |
| Финальный six-skill suite | 32/32, exit 0 | Сохранены YAML/boundary/classes/CLI 0/1/2; полные delimiter runs и exclusion literals/IDs/wiki; unselected body реально не читался |
| Финальный `--pack` | 61 ресурс, exit 0; три `base.not_rendered` / not_checked | Нет error/warning; external URLs не запрашивались, Obsidian/filters не выполнялись |
| Exact set, независимо от implementation constant | Ровно bootstrap/plan/maintain/quality/guides/ui-design; missing UI, extra directory, missing SKILL → native exit 2 | Не произвольный plugin registry |
| Полный перенос | Actual full pack в путь с кириллицей и пробелами, запуск своего checker из другого cwd; обе platform refs, методы, LICENSE/UPSTREAM/notices сохранены | Проверка ресурсов, не GUI или application |
| Заполненные minimal/UI outputs | Native AGENTS + authoring engineering_policy/plan, exit 0, findings пусты | Учебные даты/NOT_RUN не стали результатами запуска UI; grammar не semantic acceptance |

Исправленная пятинавыковая **полная** Stage1 поставка сохранена вне Git с per-file
SHA-256 manifest для независимого сравнения. Она содержит checker fix, согласованный
lifecycle/minimal adoption, но не ECC methods/UI. Её metadata может предвосхищать
feature version; идентичность определяется сохранёнными байтами, не названием 0.1.0.
Для сравнения нельзя брать исходный buggy pack или запускать six-skill checker на
пятинавыковой поставке. Финальная полная owned-копия и отдельный identity manifest
доступны в handoff проверяющему; machine paths/raw logs в публичный комплект не входят.

### Клиент: доставка / обнаружение / чтение / применение

`pi --version` → **1.3.0**, exit 0. Установленный Pi1.3 `loadSkills` с явной полной
owned-копией и `includeDefaults:false` обнаружил **все шесть** нужных имён,
actual filePath/baseDir совпали, diagnostics пусты. Общий lifecycle прочитан от каждого
baseDir; все три methods, web/React и desktop/PySide6 references, LICENSE и оба
provenance/notices файла прочитаны, SHA-256 зафиксированы вне Git. Node probe —
**26.7.0**, не pinned Node25.8.1 сборки; это не повтор приёмки exact build.
Исторический Pi1.0.4 witness сохранён отдельно в [интеграции](../pack/integrations/pi.md).

Новых model-child/GUI/product/paid-service запусков автор не делал. Авторский текущий
контекст не независимый clean executor. У будущего application run согласованный
выбор — `openai-codex / gpt-6.1-sol / high`, но **фактический клиент/model/thinking
этих будущих прогонов пока отсутствует**. Стоимость не известна, не 0. Родитель
запускает разрешённые чистые контексты без изменения live profiles/home settings/auth.

### Все 12 исходных обязательств: без потери remainder

| # | Авторский доступный факт | Что остаётся clean executor-у / verifier-у |
|---|---|---|
| 1 | Наполненный минимальный пример валиден, Python smoke даёт Hello, Example! | Новая достаточная основа на owned Python input, навыки/ресурсы и changed paths |
| 2 | Обе исходные MANUAL rules/native owner неизменны; авторский owned repeat сохранил смысл | Реальная адаптация existing JS без потери правил, named export/indent/dependency/case-folding запретов |
| 3 | Авторское повторное чтение достаточных owners выбрало no-op; bytes/даты сохранены | Настоящий второй clean bootstrap, решение и отсутствие дублей, не одни hashes |
| 4 | Формы позволяют ограниченный future plan, fixture/main.py не менялся | Предложение --uppercase с user/scenario/failure/criteria, не implementation claim |
| 5 | Авторская punctuation exercise изменила один README без ADR/registry | Clean executor сохраняет малый размер задачи |
| 6 | Входной настоящий owner — docs/instructions/local.md; formatter trim-only неизменён | Future optional upper отдельно от current и права реализации; показать контракт→owner route |
| 7 | Unit revision mismatch при равных датах даёт outdated warning / false-current error | Создать RU/EN r1/r1 и один glossary, изменить смысл primary до r2; EN честно outdated либо review+sync |
| 8 | Authoring grammar заполненных outputs, исходные Bases predicates проверены статически | Практический placement/selection адаптации; renderer predicates не объявлять выполненными |
| 9 | Обычные relative Markdown links, checker не требует Obsidian | Исполнитель реально читает/навигацирует файлы без GUI; не renderer PASS |
| 10 | Полный pack перенесён и проверен, оба платформенных appendix/notices сохранены | Clean клиент применяет именно доставленный экземпляр, не глобальный collision |
| 11 | Примеры draft/proposed, placeholders/type/status/translation controls проходят | Смысловая проверка: assumptions≠accepted facts, планы≠реализация |
| 12 | Finite sentinel tests и ручной source/diff review; нет private env/log/runtime payload | Независимая проверка окончательной поставки и publication scope |

Обе pristine fixtures и исправленная Stage1/финальная поставки доступны родителю в
owned workspace. **Оба полных clean-model применения и их repeat пока NOT_RUN.**
Таблица определяет остаток, не заменяет его авторским templater-ом или smoke.

### AD-01–AD-12: авторские упражнения отдельно от модельной квалификации

Конечные inputs/scope/failure signals — [ADAPTATION_CASES](../tests/ADAPTATION_CASES.md).
Выполнены ограниченные авторские source/design/local-behavior exercises; это не
исполнение навыков независимой моделью и не реальный web/Qt продукт:

| Случай | Фактическое наблюдение автора |
|---|---|
| AD-01 | Одна пунктуационная правка одного owned README, без новых архитектурных форм |
| AD-02 | Документированный code-first serializer реально выдаёт JSON, display реально читает его; два owner-файла, без второй схемы |
| AD-03 | Отсутствующее cost / null / 0 имеют разные wire shapes и consumer исходы; or-zero control отвергнут |
| AD-04 | Условный field assertion на empty исполнил 0 assertions; строгий непустой случай отверг empty/missing id, populated и отдельный empty прошли |
| AD-05 | Sandbox-only вывод ограничен; исполнены обе доступные **локальные учебные** ветки одного контракта. Live/production parity этим не доказана |
| AD-06 | Native unittest: fixture import failure exit 1 без достигнутого subject; после helper repair — предметный RED exit 1 (0 вместо unknown), тот же test GREEN exit 0 после минимальной коррекции |
| AD-07 | Read-only root/empty-tree comparison обнаружил committed checker JSON provider и реального downstream — CLI tests с json.loads/exit_code assertion, несмотря на исходно clean tree; текущие staged/unstaged/untracked разделены. Все 32 final tests, включая CLI consumer, выполнены |
| AD-08 | Design/source exercise сохранило dark token и ResultPanel; иерархия/длинная подпись связаны с задачей, без новой theme/library |
| AD-09 | Настоящий учебный OperationOwner: A→B, ответ B, поздний A оставил B; тот же replay assertion отверг wrong-owner control, принимающий все ответы (late-A). Второй product manager не создавался |
| AD-10 | Design output явно записал native/visual/interaction NOT_RUN: нет executable web/Qt input; mock/import не назывались GUI PASS |
| AD-11 | Причина удаления duplicate cancel handler, replacement OperationOwner и revisit condition сохранены в одной существующей учебной истории |
| AD-12 | Автор вторично прочитал bootstrap/lifecycle и owned native owners, установил отсутствие новой нужды и выбрал no-op; ручные правила/код/даты/байты сохранены, in-project отчёт ради повтора не добавлен |

**Stage1↔Stage2 clean-model comparison: NOT_RUN по всем AD-01–12**: автор не
уполномочен запускать model children. Родитель использует эквивалентные права,
клиент/model/thinking/бюджет и независимые контексты. Авторские 12 наблюдений не
показывают улучшение модели от новой методики. Real web form/modal/focus и native
PySide6 long-operation/cancel/resize/late callback qualification — **NOT_RUN**:
в разрешённых fixtures нет этих приложений/GUI. Ничего не установлено и частный
продукт не читался/не запускался. Это конкретный остаток, не N/A и не отмена UI scope.

### Лицензии, build и окончательная граница

[UPSTREAM](../pack/UPSTREAM.md) — единственный source/commit/path→recipient owner;
[notices](../pack/THIRD_PARTY_NOTICES.md) содержат полные MIT ECC (Affaan Mustafa)
и UIZZE, pinned UI lineage #1659/linus707 и #2814. React/W3C/Qt — первичные ссылки и
собственное изложение, не bulk payload. ECC runtime/adapter/hooks/evidence.js и
Quality Engine не включены. Корневые MIT/AGENTS и fixtures сохранены.

В build только README/setup: текущая принятая Pi1.3.0 build.1 и reciprocal PFK link,
без установки навыков от ссылки. Исторические failures и ограничения не превращены
в PASS; установок/restart/profile/provider/manifests изменений нет. Выполнено:

- `powershell.exe -NoProfile -NonInteractive -ExecutionPolicy Bypass -File scripts/verify.ps1 -RepositoryOnly`
  → **exit 1, failures=3 warnings=0**: у выбранного этим script Python нет `jsonschema`
  для трёх manifest schemas. Не устанавливали и не обходили dependency gate.
- `powershell.exe -NoProfile -NonInteractive -ExecutionPolicy Bypass -File scripts/safety-check.ps1`
  → **exit 1** до scan: существующий default Root использовал пустой PSScriptRoot.
  Повтор с явным `-Root <BUILD_REPO>` → **exit 0, Both 426 files, no findings**.
  Это адресный вызов существующего интерфейса, не repair script/global среды.

Дополнительно: API checker по 26 изменённым Markdown-файлам PFK → exit_code 0,
findings пусты; build README/setup → exit_code 0, одно `link.anchor_scope` / not_checked
для невыбранного тела state-migration, без чтения этого тела. Native build grammar
сохранена, все fenced install-команды сравнены с базой и не менялись. `git diff --check`
в обоих checkout → exit 0; индексы пусты.

Тот же build safety script с явным `-Root <PFK_REPO>` → **exit 1, 15 findings**
`long-random-string`: ручной просмотр всех locations показал только обязательные
публичные immutable GitHub source URLs (SHA + путь) в UPSTREAM/THIRD_PARTY_NOTICES.
Это false positives данного detector-а, не «чистый scan PASS». Скрипт/правила не
ослаблялись, лицензированные ссылки не удалялись; независимая publication-проверка
остаётся у reviewer-а. Finite portable contamination sentinels в 32 unit tests прошли.

Независимый reviewer оценивает frozen diff и относящиеся evidence, возвращает
required findings тому же автору и владеет selective staging/commits после принятия;
родитель — публикацией. Автор не stage/commit/push и не изменяет root review policy.

## Историческая проверка 0.1.0

## Автоматические проверки

Для публичной версии используются существующие команды из [tests README](../tests/README.md) и [tools README](../pack/tools/README.md):

```sh
python -I -B -m unittest discover -s tests -p 'test_*.py' -v
python -I -B pack/tools/check_foundation.py --pack
```

Тестовый набор содержит 24 метода. Проверяются грамматика метаданных и нативных документов, безопасный YAML, placeholders, ссылки и anchors в поддерживаемом подмножестве Markdown, редакции переводов, границы выбранных файлов, CLI-коды возврата и перенос ресурсов в путь с пробелами и кириллицей.

В публичной копии на Windows выполнены все 24 теста — OK. Проверка `--pack` завершилась с exit 0: 51 ресурс, без ошибок; три представления Obsidian отмечены как не отрисованные, 21 внешняя ссылка не запрашивалась. Использовалась существующая изолированная среда инструментов, без установки новых зависимостей. Это авторская автоматическая проверка, не свидетельство поведения всех клиентов.

Gitleaks 8.30.1 проверил файлы публичной копии: совпадений с правилами поиска секретов не найдено. Дополнительно проверяются личные контакты, машинные пути и метаданные публичного коммита. Автоматический поиск ограничен своими правилами и не гарантирует отсутствия любых чувствительных данных.

## Практические и клиентские границы

В `tests/fixtures/` находятся два маленьких синтетических проекта. Они задают задачи для нового Python CLI и существующего JS-проекта, включая сохранение локальных правил, повторное применение, соразмерность планов, изменение контракта и отставание перевода.

Fixtures и unit tests не доказывают, что произвольный агент выполнит эти процедуры. Частные рабочие отчёты не поставляются; эта публичная запись не выдаёт их за воспроизводимый автоматический тест.

Общие ограничения:

- `.base` проверяется как YAML-структура; фильтры и интерфейс Obsidian не выполняются.
- Не заявлена совместимость со всеми версиями клиентов и всеми операционными системами.
- Явное чтение навыка отличается от его автоматического обнаружения клиентом.
- Внешние ссылки не запрашиваются checker-ом.
- Шаблон не является заполненным принятым документом, а план не является реализованной функцией.

## Публичная поставка

Публичный репозиторий содержит комплект, документацию и синтетические тесты под MIT. Журналы, настройки редактора, рабочие окружения, внутренние отчёты и исходная история разработки исключены. Для нового публичного коммита используется GitHub noreply вместо личного email. Это мера ограничения раскрытия данных, не гарантия отсутствия любых возможных чувствительных сведений.
