# Происхождение процедур и библиотеки знаний · PFK 0.4.0

Это каноническая карта адаптации, переносимая вместе с pack. Выбранные процедуры
переведены и содержательно переработаны, **не написаны «с нуля»**. Полные сторонние
skill-пакеты, runtime, hooks, assets и настройки не включены. Собственная лицензия
[PFK MIT](LICENSE) сохраняется; отдельная адаптация Caveman сохраняет Apache-2.0.
Относящиеся donor notices —
[THIRD_PARTY_NOTICES](THIRD_PARTY_NOTICES.md).

## ECC: фиксированная редакция

Донор: [affaan-m/ECC, commit 30b68924ae9729159f44326aa3134b1d9d67c0e2](https://github.com/affaan-m/ECC/tree/30b68924ae9729159f44326aa3134b1d9d67c0e2).
Пути получателей ниже относительно pack; AD — определения случаев разработки,
не обещание их модельного PASS. Фактическая квалификация публикуется в записи приёмки
репозитория PFK, отдельно от этого переносимого материала.

| Exact donor source | Получатель / фактическое использование | Сохранено / изменено или исключено | Случай |
|---|---|---|---|
| [skills/contract-first/SKILL.md](https://github.com/affaan-m/ECC/blob/30b68924ae9729159f44326aa3134b1d9d67c0e2/skills/contract-first/SKILL.md) | [contract-evolution](references/methods/contract-evolution.md), routes plan/quality, interface-contract form; переработка процедуры | Один канон, стороны, serialized boundary; code-first разрешён, нет обязательных schema/generator/E2E для всего | AD-02/03/05 |
| [skills/change-impact/SKILL.md](https://github.com/affaan-m/ECC/blob/30b68924ae9729159f44326aa3134b1d9d67c0e2/skills/change-impact/SKILL.md) | [change-impact](references/methods/change-impact.md); адаптация | Подтверждённые связи до и actual diff после; без полного audit и impact-report по умолчанию | AD-01/07 |
| [skills/module-regression/SKILL.md](https://github.com/affaan-m/ECC/blob/30b68924ae9729159f44326aa3134b1d9d67c0e2/skills/module-regression/SKILL.md) | change-impact и route quality; адаптация | Downstream и корректная база включая committed; без REGRESSION.md, TEST-ID квот и exit=verdict | AD-07 |
| [skills/tdd-workflow/SKILL.md](https://github.com/affaan-m/ECC/blob/30b68924ae9729159f44326aa3134b1d9d67c0e2/skills/tdd-workflow/SKILL.md) | [behavior-regression](references/methods/behavior-regression.md), testing route; адаптация | Достигнутый путь, RED/та же GREEN; нет 80%, TDD для всего, detector-а и checkpoint commits | AD-01/06 |
| [skills/ai-regression-testing/SKILL.md](https://github.com/affaan-m/ECC/blob/30b68924ae9729159f44326aa3134b1d9d67c0e2/skills/ai-regression-testing/SKILL.md) | behavior-regression/contract-evolution; критически переработанные примеры | Непустой field input и отдельный empty; обе ветки для parity. Условный assertion на пустом массиве и sandbox-only proof не перенесены | AD-03/04/05 |
| [skills/test-collaboration/SKILL.md](https://github.com/affaan-m/ECC/blob/30b68924ae9729159f44326aa3134b1d9d67c0e2/skills/test-collaboration/SKILL.md) | behavior-regression; адаптация связи requirement/test/evidence | Используется существующая verification-форма, не новый registry/runtime | AD-04/06 |
| [skills/living-docs-governance/SKILL.md](https://github.com/affaan-m/ECC/blob/30b68924ae9729159f44326aa3134b1d9d67c0e2/skills/living-docs-governance/SKILL.md) | [pf-maintain](skills/pf-maintain/SKILL.md), archive-frame; адаптация | Четыре роли, не четыре файла; rationale/replacement/revisit значимого удаления в существующей истории | AD-11/12 |
| [skills/docs-governance/SKILL.md](https://github.com/affaan-m/ECC/blob/30b68924ae9729159f44326aa3134b1d9d67c0e2/skills/docs-governance/SKILL.md) | Только сопоставление с уже существующими lifecycle/quality | Механика не смысловая приёмка; router/audit/docs-map не включены, отдельного переноса текста нет | AD-01/12 |
| [skills/frontend-design-direction/SKILL.md](https://github.com/affaan-m/ECC/blob/30b68924ae9729159f44326aa3134b1d9d67c0e2/skills/frontend-design-direction/SKILL.md) | [pf-ui-design](skills/pf-ui-design/SKILL.md), ui-design form; основной UI-донор, перевод/переработка | Задача, hierarchy, применимые states, rendered evidence; без эстетических bans, memorable-detail обязанности, JSON/Node/MCP gate | AD-08/09/10 |
| [skills/design-system/SKILL.md](https://github.com/affaan-m/ECC/blob/30b68924ae9729159f44326aa3134b1d9d67c0e2/skills/design-system/SKILL.md) | pf-ui-design, web appendix; выборочная адаптация | Reuse tokens/components; без обязательных трёх competitor sites/artifacts и score gate | AD-08 |
| [skills/frontend-a11y/SKILL.md](https://github.com/affaan-m/ECC/blob/30b68924ae9729159f44326aa3134b1d9d67c0e2/skills/frontend-a11y/SKILL.md) | [web-react](skills/pf-ui-design/references/web-react.md); выборочная адаптация вопросов | Семантика/labels/focus; учебный modal без полного trap не копируется, ARIA не переносится на Qt | AD-08/10 |
| [skills/loop-design-check/SKILL.md](https://github.com/affaan-m/ECC/blob/30b68924ae9729159f44326aa3134b1d9d67c0e2/skills/loop-design-check/SKILL.md) | Только исследовательская ссылка, ничего исполняемого/нового метода | Вопросы будущего анализа Quality Engine; его API, циклы/квоты/права не проектируются здесь | Не qualification PFK runtime |

## UI lineage и лицензии

ECC называет UI-источник community salvage: **PR #1659, linus707**. State/evidence
линия пришла через **PR #2814** из
[UIZZE anti-ui-slop, 1b74390b28c18e54a87a23e7d9171101af304ae9](https://github.com/uizze/uizze/tree/1b74390b28c18e54a87a23e7d9171101af304ae9/skills/anti-ui-slop).
PFK перерабатывает вопросы «trigger/feedback/safe next action» и разделение
rendered/untested из этой линии; поэтому сохраняются **оба MIT notices**:
ECC — Copyright (c) 2026 Affaan Mustafa; UIZZE — Copyright (c) 2026 UIZZE.

Это не адаптация canonical Anthropic frontend-design: сам ECC его не rebundle.
Платные сервисы/рекламные директивы, изображения, контакты, scripts и runtime UIZZE
не включены. Их лицензии/названия не дают прав на сторонние fonts/images/services.

ECC [check-evidence.js](https://github.com/affaan-m/ECC/blob/30b68924ae9729159f44326aa3134b1d9d67c0e2/skills/frontend-design-direction/scripts/check-evidence.js)
рассмотрен как ограниченный shape/file checker, не truth/visual evaluator. Не включён
и не требуется. [.pi adapter](https://github.com/affaan-m/ECC/blob/30b68924ae9729159f44326aa3134b1d9d67c0e2/.pi/README.md)
и [root manifest](https://github.com/affaan-m/ECC/blob/30b68924ae9729159f44326aa3134b1d9d67c0e2/package.json)
подключают не только skills: extension содержит lifecycle hooks/common-rule injection.
Ни адаптер, ни commands/extensions/config/memory не копируются и не устанавливаются.

## Полные исходные материалы · 0.4.0

Владелец предоставил эти тринадцать документов для открытой публикации в составе PFK.
Это оригинальная библиотека знаний, не сторонний skill-пак: имена, YAML, текст,
примеры и ссылки сохранены **побайтно**, без сокращения или исправления исходников.
К ним применима [лицензия комплекта](LICENSE); внешние источники и продукты имеют
свои условия, их код, бинарники и графические ресурсы не включены.

Пути и SHA-256 фиксируют исходную редакцию, не доказывают её поведение:

| Исходный документ / расположение | SHA-256 |
|---|---|
| [00_README.md](references/architecture/command-first/00_README.md) | `7b07bbd88e93915cf5ba3ca9ffa5cccb9c00c1682df2e00700630af3d450f940` |
| [01_Command_First_Introduction.md](references/architecture/command-first/01_Command_First_Introduction.md) | `ad36f5e9a2edf22e6f52eb687d901abf1b9afda8136e16d7deb6c2650d04f80e` |
| [02_Command_First_Architecture_and_Contracts.md](references/architecture/command-first/02_Command_First_Architecture_and_Contracts.md) | `cc052f1190a06f7305e73fd68d5ce9a1ea84e43aa7cf9d20746019f43bf168a9` |
| [03_Command_First_Architecture_Variants.md](references/architecture/command-first/03_Command_First_Architecture_Variants.md) | `a31c2bdb7cfaa82f09ad756a5da9f5504225dce2d3702634e8487760d491542c` |
| [04_Command_First_Image_Converter_Architecture.md](references/architecture/command-first/04_Command_First_Image_Converter_Architecture.md) | `5e192de874844862046c9d737ceda63fc7cb61bc024118c63d8553dcc5ebf0b8` |
| [05_Command_First_Live_GUI_Backend.md](references/architecture/command-first/05_Command_First_Live_GUI_Backend.md) | `b7d66ff505fd8ab20ac9c129c809f51d3a69196126fb2e5b5d06eaa494d1ea98` |
| [06_Command_First_Contracts_Compatibility_and_Effects.md](references/architecture/command-first/06_Command_First_Contracts_Compatibility_and_Effects.md) | `641950c0a6f488c91cc0aaed56c80f8d340542b6a97e7e791fed5bf3f05f3704` |
| [07_Command_First_Verification_and_Delivery.md](references/architecture/command-first/07_Command_First_Verification_and_Delivery.md) | `f75e0eb3c8506d5484838997c23c631263e9001aa28c1248c48606846e557e31` |
| [FigCraft_AI_GUI_Design_Guide_RU.md](references/ui/figcraft/FigCraft_AI_GUI_Design_Guide_RU.md) | `008d346da4df289f84799661bf2dee74258a02cf691484541ace819511b071cd` |
| [FigCraft_Practice_Part_2_RU.md](references/ui/figcraft/FigCraft_Practice_Part_2_RU.md) | `6dbaeb053c1f8c12da40805b37b7dbba8611db0b00e9d59ade7ace4e7c590f86` |
| [FigCraft_Practice_Part_3_RU.md](references/ui/figcraft/FigCraft_Practice_Part_3_RU.md) | `ab4f9c4a780b3b33ea2dc6dd48415b25cb82caa10637a9cefeacce06f49dcf32` |
| [FigCraft_Practical_Workbook_RU.md](references/ui/figcraft/FigCraft_Practical_Workbook_RU.md) | `ebca260d114d17aa920bf9aa01f375c47eaf4bc1b7a9ecc022d822de53591e60` |
| [FigCraft README](references/ui/figcraft/README.md) | `07ca136afd5ca9fb88a92edcafd9c2536b7bcb81d3a8673f58f8eb920d8623fd` |

В сравнении с 0.3.0 добавлены семь оригиналов; 00/01 получили новые предоставленные
редакции, а CF02–04 и FigCraft I не изменены. Прежние SHA-256 и байты двух заменённых
редакций остаются в опубликованной истории, а не в параллельных `old`/`final-v2`.
Сохранение снимка подтверждает его редакцию, не истинность всех описанных опытов.

[pf-command-first](skills/pf-command-first/SKILL.md) и короткий [вход в серию](references/architecture/command-first/README.md)
выбирают нужные разделы, не загружают все статьи для каждого изменения.
[FigCraft-маршрут](skills/pf-ui-design/references/figcraft-handoff.md) расширяет существующий
UI-навык только при выборе этого редактора. Схемы операций, контракты и критерии
качества остаются у действующих владельцев, второго реестра нет.

Собственные шапки статей — описание источника, не accepted-статус документов проекта.
ImageConverter — архитектурный пример, не готовая реализация. Первая часть FigCraft
отражает редакцию **0.10.0**, а описанный в ней эксперимент не новый runtime-тест PFK.
Свежие возможности выбранной версии проверяются при применении. Оригинальные
Obsidian-ссылки оставлены вместе с обычной Markdown-навигацией; воспроизведение
их отображения и практическое применение новой методики — отдельные проверки.

В исходной статье 04 сохранены четыре HTML-комментария со служебными метками цитат
первоначального разбора. Это неприменимые вне источника указатели, не действующие
ссылки на поставляемые ресурсы; для использования методики они не нужны. Исключение
из прежнего запрета таких меток связано только с путём и точным SHA-256 этого снимка,
не отменяет проверку секретов, личных данных и остальных файлов.

Продолжение CF05–07 сохраняет ссылки на пять непоставленных первичных исследований.
Их перечень и рамка чтения — в [коротком входе](references/architecture/command-first/README.md);
точные условия диагностики принадлежат [tools README](tools/README.md).
Сырые исследовательские отчёты не включены, ссылки не объявлены проверенными,
другие отсутствующие цели и нарушения границ не разрешены этим исключением.

## Дополнительные навыки · 0.4.0

- [pf-retrospective](skills/pf-retrospective/SKILL.md) — новая ограниченная процедура
  на основе существующих lifecycle/quality: разбор результата, причин и уроков.
  Не копия личного недельного дневника, не автоматическое возобновление работы
  или новая процедура приёмки.
- [pf-memory-inventory](skills/pf-memory-inventory/SKILL.md) — выборочная
  содержательная переработка процедуры `memory-ops` для Pi в инвентаризацию
  без изменений. Сохранены полнота учёта, проверка происхождения, различие
  хранения и подстановки, отдельное согласование записи. Не включены частные
  записи, журналы, скрипты очистки, локальные patches или плагин.
  [Pi-приложение](skills/pf-memory-inventory/references/pi-memory.md) сверяется с
  [официальным README 1.6.1, commit 6eaf0cb68f055af4619c635d76effa108a35bb30](https://github.com/samfoy/pi-memory/blob/6eaf0cb68f055af4619c635d76effa108a35bb30/README.md).
  Это справочный контракт, не проверка живого хранилища и не рекомендация
  автоматически установить или перенастроить эту версию.
- [pf-caveman](skills/pf-caveman/SKILL.md) — изменённая адаптация русскоязычной
  процедуры понятного объяснения и
  [JuliusBrussee/caveman, skills/caveman/SKILL.md, commit 2e08b9177c07bb7249a8a2d1a6758e5db281d002](https://github.com/JuliusBrussee/caveman/blob/2e08b9177c07bb7249a8a2d1a6758e5db281d002/skills/caveman/SKILL.md).
  Сохранены ответ сначала, ясность и точность; добавлены три уровня подробности.
  Не перенесены обязательный телеграфный стиль, slash-команды, hooks, режимы
  других навыков, runtime и обещание устойчивого переключателя. Сохраняются
  [полный Apache-2.0 LICENSE](skills/pf-caveman/LICENSE), относящаяся атрибуция
  upstream NOTICE и retained MIT notice в [уведомлениях](THIRD_PARTY_NOTICES.md).
  Лицензия не означает спонсорство или передачу прав на товарные знаки.

## Первичные технические ссылки, не заимствованный payload

[Django 6.0 templates](https://docs.djangoproject.com/en/6.0/topics/templates/),
[forms](https://docs.djangoproject.com/en/6.0/topics/forms/),
[CSRF](https://docs.djangoproject.com/en/6.0/howto/csrf/) и
[static files](https://docs.djangoproject.com/en/6.0/howto/static-files/) — технические
основания собственного [Django-приложения UI-навыка](skills/pf-ui-design/references/web-django.md),
не обязательное обновление сайта и не включённые тексты документации/код Django.

[React useEffect](https://react.dev/reference/react/useEffect) — cleanup/out-of-order и
предпочтение принятой fetching-архитектуры; [W3C modal dialog](https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/)
— реальная модальность/Tab trap/initial-return focus. [Qt High DPI](https://doc.qt.io/qt-6/highdpi.html)
— coordinates/DPR; [Qt for Python threads](https://doc.qt.io/qtforpython-6/overviews/qtdoc-threads-qobject.html)
— GUI thread/affinity/queued delivery. Web и [desktop appendix](skills/pf-ui-design/references/desktop-pyside6.md)
излагают вопросы своими словами; большие тексты, код и assets этих docs не включены.
Qt for Python documentation имеет GFDL 1.3 notice, не перелицензируется MIT ECC.

[GFM §§6.3/6.5](https://github.github.com/gfm/) и
[GitHub section links](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#section-links)
— основания bounded checker fix; это собственная реализация, не полный GFM parser.

## Обновления

Нет runtime-загрузки donor main. Новая редакция требует source/license diff только
затронутых материалов, осознанного отбора и повторения относящихся случаев. Она не
перезаписывает локальные правила/адаптации и не создаёт обязательство принять весь ECC.
