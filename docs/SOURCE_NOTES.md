# Sources and extraction boundaries

## Origin

The engineering documentation process developed for Whisper Voice Machine informed this kit. Only general process ideas were extracted: proportionate changes, one primary owner per rule, preservation of existing decisions, risk-based evidence, privacy-aware diagnostics and finite completion.

The kit contains newly authored general-purpose instructions and adaptable forms. It does not include that product's implementation, private runtime information, development reports or third-party skill packages. External references are sources, not bundled dependencies or a claim of endorsement.

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

No private source paths, personal contacts, session records, environment files, databases, logs or source-product code are included. No third-party skill package is redistributed. The owner's material is distributed under [MIT](../LICENSE); linked products and documentation retain their own licenses.
