# 09 — Implementacja jednej bezpiecznej paczki subsystemu

## DLA CZŁOWIEKA — co robi ten prompt

Ten prompt powtarzasz wiele razy — osobno dla każdej paczki komend z `architecture_plan.md`.

Wypełniasz `BATCH_NAME`, `COMMAND_IDS` i `SUBSYSTEMS`. Codex implementuje tylko tę paczkę, testuje protokół i aktualizuje coverage.

## PROMPT DO CODEXA

Przed tym promptem wklej uzupełniony blok `SOURCE DATA FOR CODEX` z pliku `00_PROJECT_CONTEXT_TEMPLATE.md`.

```text
Goal: implement exactly one command batch from COMMAND_COVERAGE.

Batch parameters:
BATCH_NAME = <batch name>
COMMAND_IDS = <IDs or range>
SUBSYSTEMS = <subsystems>

Rules:
1. Implement only commands from COMMAND_IDS.
2. Implement only status `todo`, or `needs-verification` after manual confirmation in PROGRAMMING_GUIDE.
3. Do not implement commands with risk level:
   - calibration
   - adjustment
   - destructive-file
   - destructive-log-clear
   - destructive-memory
   - factory/service
   - power-affecting
   - hazardous-output
   - service-only
   unless this prompt explicitly permits it.
4. For command/query as state, use Instrument.control.
5. For query-only simple value, use Instrument.measurement.
6. For command-only action, use a method.
7. For setting-only, use Instrument.setting if it is not an action.
8. For manufacturer tokens, use values={...}, map_values=True.
9. Use validators only with ranges/sets explicitly documented in the manual.
10. Do not use properties for block/data commands; use parser methods.
11. Every command must have an expected_protocol test.
12. Add hardware tests only for policies:
    - yes
    - query-only
    - roundtrip-safe
    - output-off-only
13. Hardware tests must leave the instrument in a safe final state.

Update:
- DRIVER_FILE
- PROTOCOL_TEST
- HARDWARE_TEST, if applicable
- DOC_FILE, if public API is added
- COMMAND_COVERAGE

Run:
python -m pytest tests/instruments/<VENDOR>/test_<MODEL_LOWER>.py -q
git diff --check
git diff --stat
```
