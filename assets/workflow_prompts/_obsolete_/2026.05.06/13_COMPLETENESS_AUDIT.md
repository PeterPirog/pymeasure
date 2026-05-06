# 13 — Audyt kompletności względem manuali

## DLA CZŁOWIEKA — co robi ten prompt

Ten prompt wykonuje audyt: czy każda komenda z Programming Guide ma decyzję w coverage, czy każda implementacja ma test, czy ryzykowne komendy nie są uruchamiane sprzętowo i czy Service/Operators Manual nie wprowadziły niepotwierdzonych komend.

To etap przed pełniejszym hardware regression.

## PROMPT DO CODEXA

Przed tym promptem wklej uzupełniony blok `SOURCE DATA FOR CODEX` z pliku `00_PROJECT_CONTEXT_TEMPLATE.md`.

```text
Goal: audit implementation completeness against PROGRAMMING_GUIDE, SERVICE_MANUAL, and OPERATORS_GUIDE.

Check:
1. Every command in COMMANDS_TXT has a row in COMMAND_COVERAGE.
2. Every command in COMMAND_COVERAGE has:
   - Form
   - Transport
   - PyMeasure API decision
   - Risk level
   - Hardware-test policy
   - Status
3. Every implemented command has an expected_protocol test.
4. Every hardware-tested command has a safe hardware-test policy.
5. Query-only commands are not setters.
6. Command-only actions are not Instrument.control.
7. Data/block commands have parsers or are deferred.
8. SERVICE_MANUAL did not introduce unconfirmed command syntax.
9. OPERATORS_GUIDE did not introduce unconfirmed command syntax.
10. Destructive/service/calibration/power/factory commands are not run in hardware tests.
11. No includeSCPI=True.
12. No get_* / set_* methods.
13. Docstrings start with an imperative verb.
14. Validators and mappings come from the manual.
15. Safe final state is defined.

Add Final summary to COMMAND_COVERAGE:
- total commands
- implemented
- protocol-tested
- hardware-tested
- unsafe
- deferred
- not-implemented
- needs-verification
- needs-operator-decision

Run:
python -m pytest tests/instruments/<VENDOR>/test_<MODEL_LOWER>.py -q
git diff --check
git diff --stat
```
