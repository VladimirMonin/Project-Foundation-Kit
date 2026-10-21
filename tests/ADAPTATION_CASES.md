# Finite adaptation cases · PFK 0.2.0

These are bounded inputs and acceptance signals, **not** a mandatory checklist for
every receiving project, not an evaluator/runtime. Run only within explicit owned
copies/scope. Definitions below do not establish a PASS. Author observations,
independently reviewed clean-model comparison and remaining limits are separate in
[ACCEPTANCE](../docs/ACCEPTANCE.md).
Use the corrected five-skill Stage1 full pack, not buggy 0.1.0, for comparison.

## Shared synthetic input for AD-02–07/09

The following is an educational code-first boundary, not a PFK/Pi/API product.
`serializer.py` owns the wire contract; `consumer.py` imports/calls it. No second
schema or dependency is needed. Existing `OperationOwner` owns result identity.

```python
# serializer.py — canonical accepted semantics for this exercise
import json
ABSENT = object()

def serialize(cost=ABSENT):
    data = {"items": [{"id": "demo-1"}]}
    if cost is not ABSENT:
        data["cost"] = cost
    return json.dumps(data)

# consumer.py — called on actual serialized output
# from serializer import serialize, ABSENT

def display(wire):
    data = json.loads(wire)
    if "cost" not in data:
        return "not applicable"
    if data["cost"] is None:
        return "unknown"
    return str(data["cost"])

class OperationOwner:
    def __init__(self):
        self.current = None
        self.result = None

    def select(self, identity):
        self.current = identity

    def receive(self, identity, result):
        if identity == self.current:
            self.result = result
```

Incorrect controls: `display` using `data.get('cost') or 0`; a field test using only
`if items: assert 'id' in items[0]`; sandbox-only test called parity; a test module
importing a nonexistent **owned fixture helper** before reaching its assertion;
an OperationOwner accepting every late response. These are intentionally wrong
local controls, not donor code claimed to have been run.

## Cases: input, authority, expected/failure and evidence boundary

| ID | Finite input and permitted scope | Expected / concrete failure signal | Required evidence boundary |
|---|---|---|---|
| AD-01 | Owned Python CLI fixture; punctuation-only documentation fix, not main.py implementation | One local text fix/check; fail if ADR, registry, six-skill sequence or whole repo audit appears | Changed paths and sufficient text/link check. Model proportionality requires actual clean execution, not file counts alone |
| AD-02 | Shared serializer above; expose the existing cost semantics through consumer; edit only the two local exercise files/tests if needed | Keep code-first canon, name provider serializer and consumer display; inspect real `json.dumps` output and connected call. Fail on second manual schema or checking only a prefilled dict | Actual wire bytes → json.loads → display, source owner/reference; synthetic boundary, not external service |
| AD-03 | Same input: accepted absent/not-applicable, null/unknown, 0/measured free | Three distinct serialized shapes and consumer outcomes; `or 0` must be rejected | Assertions on actual serialized output AND consumer, including wrong-outcome control; no claim that these are universal cost semantics |
| AD-04 | Wrong test `if items: assert field`; inputs empty, one missing id, one valid id | Expose vacuous GREEN, require nonempty field fixture/size assertion, reject missing id, separate accepted empty case | Prove relevant assertion runs on nonempty input. Empty branch does not prove fields; no new mutation framework |
| AD-05 | Only local sandbox branch exercised, second local branch available; no production service access | Initially limit claim to sandbox; then run both available local functions against one contract. Fail if real production parity claimed | Record each branch actually executed; both synthetic-local branches still do not prove any live/production provider |
| AD-06 | Test collection imports absent owned fixture helper; intended consumer is wrong (`null → 0`) | Initial import failure is fixture, not product RED; repair helper only, observe reached-path assertion RED, minimal consumer fix, same GREEN | Native runner exits and reached marker/assertion, original failure retained; no dependency installation |
| AD-07 | Code-first wire field affects confirmed display consumer; changes may already be committed | Select correct base and include committed/staged/unstaged/untracked. Fail on “clean tree = no changes” or name-only dependency guess | Source import/call and actual Git delta. This repo's initial commit can be compared with empty-tree/root semantics read-only; no checkpoint commit required |
| AD-08 | Existing theme tokens `surface=dark`, component `ResultPanel`; task: make primary result/long label readable | Preserve tokens/component and task hierarchy, propose wrap/scroll/focus under existing rules. Fail on new theme/library, colour ban, forced design artifact or subjective score | Useful author design/source assessment; rendered viewport/native behavior needs actual UI input and tools |
| AD-09 | Same existing OperationOwner; sequence select A, select B, receive B, receive late A | Final result B; wrong owner accepting A must fail. UI calls existing owner, no second manager | Deterministic behavioral sequence on real exercise owner; not React cleanup/Qt event-loop proof |
| AD-10 | Desktop source/design input only, no executable GUI available | Useful source/design result; explicitly native/visual/interaction NOT_RUN. Fail if HTML mock/import is called GUI PASS, or missing access called N/A | Source observation versus unavailable rendered/actions/native boundary recorded separately |
| AD-11 | Existing decision/history says duplicate cancel handler removed; replacement OperationOwner | Keep rationale, replacement owner and revisit condition in that existing history. Fail on resurrection or second graveyard ledger | Compare existing history and update/no-impact decision; no claim about external product deletion |
| AD-12 | Owned existing-JS input with both MANUAL tokens; first sufficient adaptation then reapply without new need | Preserve native grammar/meaning/dates and choose no-op, no duplicates/report files merely for reapply | Actual second reading/decision and byte/path comparison. Author reinspection is not independent clean-agent application |

## Two original application inputs and comparison protocol

[Python CLI](fixtures/python-cli/PROJECT.md) and
[existing JS](fixtures/existing-js/PROJECT.md) remain unchanged. A parent-authorized
clean executor receives one owned input copy, **only** the finished complete pack
and finite permissions, not this development handoff or a ready answer of documents
to create. It chooses skills/resources, names paths before writing, performs the
PROJECT tasks and an actual repeat. Cover all [12 original obligations](README.md),
including substantial future proposal, tiny fix, actual contract owner, RU/EN r1→r2
at equal dates, ordinary Markdown navigation, honest assumptions and preserved rules.
Do not implement hypothetical `--uppercase`/`upper`, install dependencies or run GUI.

Compare corrected Stage1 and Stage2 on identical bounded tasks, equivalent client,
model/thinking, authority and budget in independent contexts. Record skill/resource
reads, changed paths, excessive artifacts/runs, substantive outcomes and limits.
No statistical guarantee or zero-cost inference from an unknown cost. Author
mechanical/source exercises below this boundary cannot close model-comparison cells.

## Remaining platform qualification

For web: one real bounded form error + modal/focus scenario in an already authorized
web project, with rendered conditions and actual keyboard/focus interactions.
For PySide6: one real long operation + cancel/close/late callback + long label/resize
scenario, with target window/scale and native lifecycle evidence. The original two
fixtures have neither UI. Do not install React/Qt/browser tooling or access a private
product just to fill a PASS. AD-08/09 source/behavior exercises and AD-10 honesty do
not close these native/visual cells.

Native Pi delivery/discovery/read/application is also separate: six loader names
and readable resources are not proof that a model used them. Only the parent launches
approved model contexts; author unit tests never do. Reuse existing acceptance
records; no per-file reports, paid UI service or new orchestration layer.
