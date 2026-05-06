# 11 — Komendy ryzykowne: implementować, odroczyć albo tylko protocol-only

## DLA CZŁOWIEKA — co robi ten prompt

Ten prompt obsługuje komendy ryzykowne: kalibracja, adjustment, zapis NVM, format/delete, firmware, power off, factory, long self-test, hazardous output.

Nie chodzi o masową implementację. Codex ma zdecydować, które metody mają sens jako jawne API, a które trzeba oznaczyć jako deferred/not-implemented.

## PROMPT DO CODEXA

Przed tym promptem wklej uzupełniony blok `SOURCE DATA FOR CODEX` z pliku `00_PROJECT_CONTEXT_TEMPLATE.md`.

```text
Goal: analyze risky commands and decide which should enter public API as explicit conscious methods and which should remain deferred/not-implemented.

Scope:
- calibration
- adjustment
- correction factors
- save/store nonvolatile memory
- delete/format/initialize
- factory/service password
- firmware update
- power off/reboot
- network/GPIB address changes
- long self-tests
- hazardous output enable

Rules:
1. Do not implement risky commands as normal properties.
2. If implemented, use an explicit method name that shows the effect.
3. The docstring must state:
   - what the command does,
   - whether it is destructive,
   - whether it changes NVM/calibration/configuration,
   - that it is not run in automatic hardware tests.
4. Add expected_protocol tests only.
5. Do not call these methods in HARDWARE_TEST.
6. If a command is too dangerous or requires a service procedure, mark it:
   - deferred
   - not-implemented
   - needs-operator-decision
7. Update SERVICE_COVERAGE and COMMAND_COVERAGE.

Run:
python -m pytest tests/instruments/<VENDOR>/test_<MODEL_LOWER>.py -q
git diff --check
git diff --stat
```
