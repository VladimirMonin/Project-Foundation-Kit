# Pi — проектное подключение без глобальной установки

Основания: [Agent Skills](https://agentskills.io/specification), [skills](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/skills.md), [settings](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/settings.md), [CLI](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/cli.md), [configuration](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/configuration.md).
Прежний официальный адрес [badlogic/pi-mono](https://github.com/badlogic/pi-mono) перенаправляет к `earendil-works/pi`; проверенная установка использует пакет `@earendil-works/pi-coding-agent`, версия **1.0.4**. У другого клиента/версии сначала сверить локальные `pi --version`, `pi --help` и его docs; не считать имя старого репозитория доказательством установленного поведения.

## Вариант 1 — явный путь, без изменения settings

Импортировать **весь** `pack/` как `tools/project-foundation/` (содержимое pack непосредственно внутри этой папки). Из корня целевого проекта, в уже установленном Pi:

```sh
pi --no-skills --skill "./tools/project-foundation/skills/pf-bootstrap/SKILL.md"
```

В интерактивном Pi:

```text
/skill:pf-bootstrap Разверни достаточную основу здесь, сохраняя местные правила. Сначала прочитай pack README и назови конечный список путей.
```

`--no-skills` отключает discovered/configured skills, но **явные `--skill` остаются**; так меньше риск получить чужой одноимённый экземпляр. Путь CLI относителен к cwd, поэтому сначала установить корень проекта; абсолютный путь допустим, заключить в кавычки при пробелах. Для другой процедуры заменить только выбранный `SKILL.md`; весь пакет/общие ресурсы остаются на месте.

Эта команда **не sandbox** и не выключает прочие extensions, MCP, providers, пользовательские instructions. Для специально разрешённой изолированной проверки ресурса можно дополнить `--no-extensions --no-mcp --no-prompt-templates --no-themes --offline --no-session`; это не требуется обычному bootstrap. `--offline` запрещает автоматическую startup-сеть, не является запретом произвольных инструментов или пользовательского запроса к модели. Не запускать новую агентскую сессию ради статического чтения без соответствующих прав.

## Вариант 2 — проектные settings

Только если разрешено менять **целевой проект**, адресно добавить к существующей `.pi/settings.json`, сохранив прочие поля:

```json
{
  "skills": ["../tools/project-foundation/skills"]
}
```

Это фрагмент, не разрешение заменить файл. Относительный ресурсный путь отсчитывается **от `.pi/`**, не root и не случайного терминала. Доверие проектной конфигурации определяется Pi; не менять глобальное доверие/профили. Настройка работает в scope cwd: запускать из согласованного корня. Skills-конвенции `.pi/skills`/`.agents/skills` не делают `tools/project-foundation` автоматически обнаруживаемым.

`skills` lists объединяются с пользовательскими ресурсами; проектный entry не гарантирует отсутствие одноимённого глобального навыка. В проверенном loader-е первая найденная копия сохраняется, collision получает diagnostic. При конфликте использовать явный вариант с `--no-skills`, не переименовывать глобальный навык. `/reload` обновляет resources текущей сессии; это не доказательство, что нужный навык уже прочитан моделью.

## Проверять четыре разных факта

1. **Обнаружение:** startup diagnostics/список skills содержит имя, описание и ожидаемый путь; нет collision/missing-path warning.
2. **Выбранный экземпляр:** открытый `SKILL.md` именно из импортированного полного pack, не совпадающий name из другого root. Если доступна source-path диагностика, сверить её; один slash-name недостаточен.
3. **Чтение ресурсов:** агент разрешает `../../references/lifecycle.md` относительно выбранного SKILL, читает и нужную форму, а не ищет ресурс в cwd.
4. **Применение:** отдельный чистый исполнитель проходит синтетический bootstrap/reapply без вымышленной архитектуры и потери местных правок. Чтение файла/статический loader check этого не доказывают.

В разработке комплекта проверены первичные/установленные docs, help/version, код loader-а (`loadSkills`: explicit paths, includeDefaults, name collision) и read-only вызов `loadSkills` с `includeDefaults: false` для `pf-bootstrap` и `pf-plan`: выбранные пути и чтение общего lifecycle подтвердились без модельного вызова/глобальных defaults. Это **не полный native agent-behavior PASS**, не запуск CLI с проектными settings и не аттестация остальных навыков. Фактический clean-executor результат фиксируется отдельно при интегрированной приёмке.

`AGENTS.md` — обычный Markdown, не автоматически загружаемая библиотека. Проверенный Pi ищет context files в agent dir/cwd/предках независимо от project trust; загрузка native контекста и чтение linked instructions — разные действия. Не создавать копию всех правил в каждом skill и не изменять глобальные settings ради этого комплекта.
