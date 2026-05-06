# 07 — Implementacja szkieletu i Common/Status

## DLA CZŁOWIEKA — co robi ten prompt

To pierwszy prompt, który modyfikuje właściwe pliki PyMeasure.

Tworzy klasę drivera, eksport w `__init__.py`, testy protokołowe, minimalne testy sprzętowe i dokumentację Sphinx. Zakres ma być minimalny: Common/Status/System i bezpieczne query.

## PROMPT DO CODEXA

Przed tym promptem wklej uzupełniony blok `SOURCE DATA FOR CODEX` z pliku `00_PROJECT_CONTEXT_TEMPLATE.md`.

```text
Goal: implement the first driver batch: skeleton + safe Common/Status/System query. Do not implement measurement subsystems yet.

Modify:
- DRIVER_FILE
- VENDOR_INIT
- PROTOCOL_TEST
- HARDWARE_TEST
- DOC_FILE
- DOC_INDEX
- COMMAND_COVERAGE

Requirements:
1. Create class CLASS_NAME.
2. If ARCHITECTURE_PLAN confirms SCPI/IEEE-488.2:
   class CLASS_NAME(SCPIMixin, Instrument)
3. Never use includeSCPI=True.
4. Do not create get_* or set_* methods.
5. Do not duplicate standard SCPIMixin properties/methods.
6. Add only commands from the Skeleton/Common/Status batch marked safe-query, safe-state-readwrite, or cautious-state-change.
7. Implement reset/preset/clear only if PROGRAMMING_GUIDE confirms them.
8. Skip hardware tests for reset/preset unless COMMAND_COVERAGE explicitly permits them.
9. Add expected_protocol tests for every implemented command.
10. Add hardware tests only for:
    - identity query,
    - safe query-only,
    - error queue query, if available.
11. Hardware tests must be skipped when DEVICE_ADDRESS is empty.

After implementation, update COMMAND_COVERAGE:
- Proposed Python API
- Protocol test
- Hardware test
- Status
- Notes

Run:
python -m pytest tests/instruments/<VENDOR>/test_<MODEL_LOWER>.py -q
git diff --check
git diff --stat
```
