# Existing synthetic project rules

Read [the local instruction](docs/instructions/local.md) before changing the formatter
or its description. This file is native agent guidance, not a durable-doc passport.

MANUAL-RULE-KEEP: public function name `formatLabel` must stay stable; no new runtime
dependency for a formatting change. Use named exports and two-space indentation.

This fixture has no verified test command. Do not invent `npm test` or install a web
stack. Documentation may be adapted without replacing this rule with a starter template.
