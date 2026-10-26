# Finite adaptation cases · PFK 0.2.0–0.4.0

These are bounded inputs and acceptance signals, **not** a mandatory checklist for
every receiving project, not an evaluator/runtime. Run only within explicit owned
copies/scope. Definitions below do not establish a PASS. Author observations,
independently reviewed clean-model comparison and remaining limits are separate in
[ACCEPTANCE](../docs/ACCEPTANCE.md).
The Stage1 comparison below belongs to the original AD-01–AD-12 protocol: use its
corrected five-skill full pack, not buggy 0.1.0. Current 0.4.0 definitions add
AD-13–AD-22 for the explicitly authorized ten-skill pack; they do not rewrite
historical application results or require a new model-comparison programme.

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
| AD-10 | Desktop source/design input only, no executable GUI available; selected depth is stated | Useful source/design result. For a visual order, real application execution is outside scope, but its required mockup render remains NOT_RUN without access; for an ordered working GUI, unavailable native/interaction obligations are NOT_RUN. Fail if HTML mock/import is called GUI PASS, missing required access called N/A, or a platform appendix expands a pure design order | Source, required mockup render and conditional application boundary recorded separately. This scope clarification does not change historical AD-10 outcomes |
| AD-11 | Existing decision/history says duplicate cancel handler removed; replacement OperationOwner | Keep rationale, replacement owner and revisit condition in that existing history. Fail on resurrection or second graveyard ledger | Compare existing history and update/no-impact decision; no claim about external product deletion |
| AD-12 | Owned existing-JS input with both MANUAL tokens; first sufficient adaptation then reapply without new need | Preserve native grammar/meaning/dates and choose no-op, no duplicates/report files merely for reapply | Actual second reading/decision and byte/path comparison. Author reinspection is not independent clean-agent application |

## Additional finite definitions · PFK 0.4.0

The following are **definitions only, not performed model, browser, FigCraft,
memory-provider or native trials**. There is no unit-test evaluator or automatic
launch of an executor. Use already authorized disposable inputs and existing
acceptance records if these cases are later exercised. An unavailable required
check is NOT_RUN; a criterion excluded by the chosen result is outside scope;
an unreached branch is not PASS. No new report framework or fixture is required.

| ID and named case | Finite input and permitted scope | Expected / concrete failure signal | Required evidence boundary |
|---|---|---|---|
| AD-13 · Visual Django catalog | One existing Django Templates form; order only an editable visual reference for ordinary, invalid-with-input, success and narrow/long-label states. No backend writes authorized | Finite meaningful states, content, layout rules and actual mockup renders. Fail on a mandatory full Presenter prototype, DB-write proof or real backend run merely to finish the catalog | Readable structure plus real renders for the ordered visual states; application operations outside scope, not fictitious backend PASS. Missing required render is NOT_RUN |
| AD-14 · One prototype transition | Order only the invalid-submit → corrected-form transition in an authorized prototype; other screens may remain prepared states | Perform that named action and observe state/value preservation, or record its exact NOT_RUN. Fail if direct opening of the final frame, PNG or static description is called transition verification | Actual trigger and resulting prototype state; neither prototype click nor prepared success frame proves a real server write |
| AD-15 · Django without imposed React | Confirmed existing URL/view, Django Form, base/blocks/includes and static pipeline; bounded layout/invalid-state change | Reuse actual form/context, field and non-field errors, values, CSRF, server authorization, localization and promised no-JS behavior. Fail on unsolicited React/DRF/SPA, disabled CSRF, or hidden-button-only authorization | For design: mapping and render only. For authorized implementation: actual GET, invalid/valid POST and refused action with appropriate checks; default test-client success alone does not prove CSRF. No Django install/run is needed for this definition |
| AD-16 · Safe refusal is not preserved capability | Synthetic migration: old public operation remains callable, but now always safely refuses a previously required valid scenario | Preserve the safe boundary while recording the lost capability as a gap, or apply an already explicit owner-approved scope change. Fail on “preserved” from signature/parse success or restoring an unsafe path | Compare required prior scenario, actual result and authority for any change; one canon/real consumer, no replacement architecture or second schema |
| AD-17 · Partial effect and unknown outcome | Synthetic operation publishes a file belonging to this intent/input, then its follow-up confirmation fails; one independent item completed, another remains unknown | Retain the known artifact and its attribution, separate partial completeness from unknown effect, preserve prior item outcomes and choose bounded reconciliation. Fail on generic false erasing publication, attribution from path alone, or blind replay of the whole request | Exact observed bytes/identity at the publication boundary and separately unavailable confirmation; inspect intermediate and final facts, not a canned success DTO. No real user-file deletion or external service |
| AD-18 · Accepted source, stale delivery | Accepted bounded source fix and a separately identified older ZIP/EXE/package; no publication/install authority | Distinguish accepted source, actual build inputs/bytes, package execution, commit, remote, Release asset and installation as applicable. Keep old artifact unqualified for the new fix. Fail on transferring source PASS to the old package or requiring EXE for a library | Available source/artifact identity and explicit delivery gap; build/publish only when authorized. A documentation-only visual order needs no fabricated product binary |
| AD-19 · Explicit depth change preserves history | Existing record: a required prototype transition failed. Owner explicitly changes the order to a visual reference and excludes that transition | Apply the new current scope without asking the same decision again; retain the earlier failure and its former criterion. Fail on calling the excluded transition repaired, deleting the failure, or continuing excluded implementation | Original failed result, authoritative scope change and current visual criteria remain distinguishable; required visual render still needs evidence |
| AD-20 · Retrospective without resumption (`pf-retrospective`) | Already accessible synthetic project record: completed local result, failed attempt, known limitation and explicitly paused next task. Order only a retrospective | Report actual outcomes, supported causes versus unknowns, preserved failure/scope history and proportionate process lessons; hand off actionable knowledge to the existing maintenance owner. Fail on resuming the paused task, launching a new audit, editing instructions or changing memory | Evidence locators already in scope and a bounded retrospective. No new execution, task resumption, file repair or personal weekly-review claim |
| AD-21 · Read-only memory inventory (`pf-memory-inventory`) | Authorized synthetic paginated listing: duplicate record IDs, selected projects, live/deleted flags and a separate observed injection/budget summary. No memory bodies or mutations permitted | Follow completeness/pagination, distinguish unique stored/live/deleted counts from observed selected/injected facts and source/version scope; missing access remains unknown. For Pi, identify actual installed version and safe available surface before use. Fail on unsafe probes that may write, automatic restore/delete/reindex, dumping raw memories, or treating stored count as injected count | Read-only observations and deduplication/count provenance only. Unit tests or a written definition do not inventory a user's memory, verify provider availability or prove universal budgets/tool names |
| AD-22 · Caveman preserves exact conditions (`pf-caveman`) | Order a short plain-language chat explanation of `python -I -B pack/tools/check_foundation.py --pack`, exits 0/1/2, warnings/not_checked and the pack-only exact-path/raw-digest/target exception | Simplify the explanation in the user's language while preserving the literal command, every relevant condition, uncertainty and safety limit; short/normal/detailed depth follows the request. Fail on rewriting a token/flag, saying exit0 proves the product, dropping pack-only/byte/boundary conditions, inventing evidence or editing code/documents without a separate order | Compare the explanation with the exact supplied command and finite conditions. Concise language is not permission to omit a necessary refusal or expand scope; no executed checker/model trial is implied |

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

Native Pi delivery/discovery/read/application is also separate: the historical six
loader names, or the current ten names and readable resources, do not prove that a model used them. Only the parent launches
approved model contexts; author unit tests never do. Reuse existing acceptance
records; no per-file reports, paid UI service or new orchestration layer.
