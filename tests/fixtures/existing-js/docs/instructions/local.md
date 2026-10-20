# Local formatter instruction (native legacy format)

Read when changing `formatLabel` or its public contract. Existing native instructions
remain valid without mechanically adding a new metadata grammar.

MANUAL-NOTE-KEEP: trimming surrounding whitespace is current behavior. Preserve the
named export and update its public description when the contract changes. Do not
silently add case folding, change the function name or add a dependency.

No automated test runner is configured. A code review is static evidence, not a
JavaScript execution. Any future command must first be verified on this fixture.
