# Ограниченный read-only checker

`check_foundation.py` проверяет выбранные текстовые документы и ресурсы пакета.
Не импортирует приложение, не читает `.env`/БД/журналы, не меняет файлы или index,
не запускает сеть и не исправляет политики. Нужен Python **3.10+** и отдельно
закреплённый **PyYAML 6.0.3** из [requirements.txt](requirements.txt). Не ставьте
зависимость в защищённое окружение приложения. [PyPI](https://pypi.org/project/PyYAML/6.0.3/)
и [safe YAML API](https://pyyaml.org/wiki/PyYAMLDocumentation) — первичные основания.

## Установка и реальные интерфейсы

Создайте своё tooling venv штатным Python, затем его же интерпретатором установите
`-m pip install -r <pack>/tools/requirements.txt`. Пути в угловых скобках заменяет
человек/агент; это не готовая команда неизвестного проекта. Среда не переносится.

Из любой текущей папки, с реальными абсолютными путями:

```text
<tool-python> -I -B <pack>/tools/check_foundation.py --pack
<tool-python> -I -B <pack>/tools/check_foundation.py --pack <other-pack>
<tool-python> -I -B <pack>/tools/check_foundation.py --project <project> --corpus docs/check-scope.json
```

`--pack` без ROOT использует каталог относительно `__file__`, **не cwd**.
`--project` требует явный root и root-relative YAML/JSON corpus. Пример input:

```json
{
  "authoring": ["docs/README.md", "docs/guides/ru/start.md", "docs/guides/en/start.md"],
  "native": ["AGENTS.md", "docs/views/Documents.base"],
  "templates": ["docs/_templates/note.md.tmpl"]
}
```

Сначала выберите существующие разрешённые файлы и их грамматику. Списки не glob,
не каталоги; пустая выборка, дубли/пересечения, absolute/traversal corpus paths,
symlinks, missing/unreadable/не-UTF-8 или >1 MiB text input дают **exit2**.
Не включайте рабочие/private данные. Проверка требует только документационные
форматы `.md`, `.md.tmpl`, `.yaml`, `.yml`, `.yaml.tmpl`, `.base`.

- `authoring`: долговечный Markdown по [общей схеме](../references/metadata.md).
  Начальная safe YAML-шапка; duplicate keys, обязательные строки/areas, quoted ISO
  dates, пять статусов, словарь `kind`, типы известных optional полей и duplicate IDs
  проверяются. YAML anchors/aliases/merge keys запрещены общей схемой. Смена словаря
  требует согласованного обновления metadata.md и checker-а, не локальной поблажки.
- `native`: AGENTS и обычные package references не получают authoring-паспорт.
  Это относится и ко всем 13 сохранённым оригиналам command-first/FigCraft: их исходная
  YAML-шапка остаётся нативной частью справки, а не принятой PFK-архитектурой.
  `SKILL.md` независимо проверяет native name/description/optional metadata и
  совпадение каталога. `.yaml/.yml` — safe parse, `.base` — только YAML shape views/
  filters, **не выполнение predicates или GUI**.
- `templates`: только явно названные `.tmpl`, существование/UTF-8. Их placeholders
  и будущие output-relative links не валидируются как принятый экземпляр. После
  адаптации результат проверяется как authoring/native, не как template.

В authoring обязательное поле с `{{field}}` — error в любом статусе. В body accepted
документа незаполненный `{{field}}` — error; в draft/proposed — warning. Это поиск
согласованного синтаксиса, не способность найти любое нерешённое продуктовое решение.
Нельзя переклассифицировать accepted output как native/template ради exit0.
Незавершённые поля native AGENTS и проектного YAML также дают error, без навязывания
им паспорта заметки.

## Связи, переводы и Markdown-границы

Локальные ссылки проверяют existence в root; bodies targets **не читаются** вне
явной выборки. Fragment проверяется только в parsed Markdown corpus, иначе
`not_checked`. Поддерживаются обычные inline/image links с простым destination,
angle-bracket destination и полные/collapsed reference links, ATX headings и explicit
HTML `id`. Литералы внутри fenced blocks и code spans не создают ссылок,
definitions, HTML IDs или wikilink diagnostics. Inline code в подписи настоящей
ссылки не отменяет цель. Reference-ключи сохраняют исходный текст (включая backticks)
и casefold, а не rendered label. Содержимое inline code сохраняется в ATX slug.
Code spans сопоставляют полные backtick runs равной длины, в том числе multiline;
это ограниченное подмножество, не вся GFM-нормализация. Footnotes не считаются ссылками. Нет полного
CommonMark parser: nested destinations/brackets, shortcut references, Setext,
autolinks и renderer-specific anchors остаются вне гарантии; wikilinks отмечаются
`not_checked`. External URLs считаются, но сеть не запускается. Для переносимого
пакета используйте простые относительные Markdown-ссылки.

### Непоставленные исторические исследования

`link.source_not_shipped` имеет уровень **not_checked**, не успешной проверки ссылки.
Это фиксированная политика **только `--pack`**: совпадают точный root-relative путь
оригинала, SHA-256 **сырых байтов** выбранной редакции и буквальная относительная цель.
Префикса `pack/` в ключе нет. Таблица ниже задаёт 13 пар, а не исключение по basename:

| Точный путь от root пакета | Буквальные цели |
|---|---|
| `references/architecture/command-first/05_Command_First_Live_GUI_Backend.md` | `COMMAND_FIRST_PRACTICE.md`; `01-core-cli-and-command-first.md`; `02-design-to-code.md`; `01-command-first-and-scope.md` |
| `references/architecture/command-first/06_Command_First_Contracts_Compatibility_and_Effects.md` | `COMMAND_FIRST_PRACTICE.md`; `01-core-cli-and-command-first.md`; `01-command-first-and-architecture.md`; `01-command-first-and-scope.md` |
| `references/architecture/command-first/07_Command_First_Verification_and_Delivery.md` | Все пять буквальных целей из первых двух строк |

Ожидаемые digest закреплены в коде и независимых тестах по
[карте происхождения](../UPSTREAM.md); это не настраиваемый язык ignore-правил.
Смена даже одного байта, BOM/концов строк, пути или destination лишает ссылку
исключения. `./`, percent-encoding, query/fragment или другое написание не получают
разрешение через нормализованную цель. В `--project` те же отсутствующие исследования
остаются `link.missing: error`.

Сначала действуют прежние absolute/root/traversal/symlink-проверки. Исключение
рассматривается **только при действительно отсутствующей цели** после этих границ.
Существующая цель проходит обычные проверки, включая parsed-selection/anchor;
её содержимое не читается вне явного corpus. Pack с symlink во входах по-прежнему
отклоняется как input failure, а не пропускает такой объект ради библиографии.
Обычные статьи 05–07, Django-справка и остальные ресурсы не исторические исключения:
их удаление сохраняет обычный `link.missing`.

Каждое употребление разрешённой отсутствующей ссылки отражается в JSON: текущие
13 пар дают 184 `link.source_not_shipped`, а не 184 разных исследования. Это не
сетевой fetch, подтверждение содержания, доступности или новой приёмки источника.
[Библиографическая рамка](../references/architecture/command-first/README.md)
объясняет область этих оснований. Исключение непрозрачных библиографических
маркеров исходной статьи 04 в конечном privacy-тесте независимо, не меняется и
не распространяется на 05–07.

Для `kind: guide` нужны language и source_revision основной версии. Перевод имеет
свой ID, translation_source=ID выбранного primary guide и translation_source_revision.
Source/translation одного языка или ссылка на самого себя ошибочны. У перевода
также есть human `translation_state`: current/outdated/unknown, не собственный
source_revision. Отставание — **warning** `translation.outdated` и computed state
`outdated`, даже при равных updated датах. Заявление current при разных редакциях —
**error** `translation.contradiction`. При равных редакциях сохраняется консервативный
human state: совпадение не доказывает качество перевода. Обязательный для выпуска
перевод синхронизируется по решению release owner, warning не даёт права его игнорировать.

## Выход и достаточность

При разобранной команде — один JSON stdout: `exit_code`, `checked`, `findings` с
path/code/severity/message, `translations`, `external_links_not_checked`, `limitations`.
Ошибка синтаксиса CLI может дать argparse stderr/exit2 без JSON; это не PASS.

- **0** — нет error; возможны warnings/not_checked. Это не принятие текста/продукта.
- **1** — ошибки выбранных документов; исправить свою действительную delta.
- **2** — input/dependency/usage failure; не считать пустым успехом.

`--pack` проверяет ровно десять именованных навыков: `pf-bootstrap`, `pf-plan`, `pf-maintain`,
`pf-quality`, `pf-guides`, `pf-ui-design`, `pf-command-first`, `pf-retrospective`,
`pf-memory-inventory`, `pf-caveman`, их name/resource links, native
Markdown и `.base`, наличие/UTF-8 templates. Отсутствие любого именованного каталога
или его `SKILL.md`, лишний каталог либо подмена имени дают exit2.

Контрольные суммы 13 оригиналов, сохранность полного payload при переносе и
конечный набор wiki-целей/заголовков серии проверяют отдельные тесты репозитория,
не новый режим checker-а. Оригиналы выбираются по
[карте command-first](../references/architecture/command-first/README.md) и
[маршруту FigCraft](../skills/pf-ui-design/references/figcraft-handoff.md).
Общий checker по-прежнему сообщает `link.wiki: not_checked`: конечный тест серии
не обещает поддержку произвольных wiki-ссылок или их отрисовку.

Checker не тестирует загрузку навыка клиентом, выполнение проектной процедуры,
истинность архитектуры или отрисовку Obsidian/GUI. Примеры и наблюдения в оригиналах
не являются свежими runtime-доказательствами PFK.
Проверка privacy/log outputs принадлежит [качеству](../references/quality.md),
а не структурному checker-у. Повторное агентское развёртывание проверяется реальным
исполнителем, не hash-equality или генератором шаблонов.
