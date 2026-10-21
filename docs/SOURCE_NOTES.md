# Sources and extraction boundaries

## Origin

The engineering documentation process developed for Whisper Voice Machine informed this kit. Only general process ideas were extracted: proportionate changes, one primary owner per rule, preservation of existing decisions, risk-based evidence, privacy-aware diagnostics and finite completion.

The original kit contains general-purpose instructions and adaptable forms. Version 0.2.0 also translates and substantially adapts selected ECC procedures and the UIZZE UI state/evidence lineage; these are not claimed to be authored from scratch. The single portable source/commit/path → recipient map is [pack/UPSTREAM.md](../pack/UPSTREAM.md), with both complete MIT notices in [THIRD_PARTY_NOTICES.md](../pack/THIRD_PARTY_NOTICES.md). Full ECC, its Pi adapter/runtime/hooks, and UIZZE services/assets are not included. Neither source-product implementation nor private runtime information or development reports are included. External references alone are not bundled dependencies or endorsements.

## Primary references

| Reference | Use and boundary |
|---|---|
| [Agent Skills specification](https://agentskills.io/specification) | Native SKILL structure and progressive disclosure; not proof of client trigger behavior |
| [AGENTS.md](https://agents.md/) | Markdown agent entry; discovery is client-specific |
| [Pi repository](https://github.com/earendil-works/pi) | Client source and integration documentation |
| [Pi skills](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/skills.md), [settings](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/settings.md), [CLI](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/cli.md) | Paths, explicit skill selection, discovery and settings boundaries |
| [Hermes skills](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills/) | Explicit reading, discovery and trust boundaries; no global profile change required by this kit |
| [Obsidian Help](https://help.obsidian.md/), [Templates source](https://github.com/obsidianmd/obsidian-help/blob/master/en/Plugins/Templates.md) | Markdown-first use and built-in template variables; no visual qualification |
| [PyYAML](https://pyyaml.org/wiki/PyYAMLDocumentation) | Safe YAML parsing used by the optional checker |

Live documentation may advance. Integration documents distinguish explicit reading, selected resource access and client discovery; one does not prove the others.

## Distribution

No private source paths, personal contacts, session records, environment files, databases, logs or source-product code are included. No complete third-party skill package is redistributed; selected adapted portions retain the notices above. The owner's material is distributed under [MIT](../LICENSE); linked products and primary React/W3C/Qt documentation retain their own licenses. Those technical docs are references and original summaries, not bulk copied text/code/assets. MIT ECC does not relicense Qt documentation.
