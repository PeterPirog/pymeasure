# 15 — Final cleanup przed PR

## DLA CZŁOWIEKA — co robi ten prompt

Ostatni prompt przed PR.

Codex ma sprawdzić wyłącznie pliki, które powinny wejść do upstream PyMeasure, uruchomić testy i wypisać, co wchodzi do PR, a co nie. `assets/`, `AGENTS.md`, manuale i worklogi nie powinny wejść do finalnego diffu.

## PROMPT DO CODEXA

Przed tym promptem wklej uzupełniony blok `SOURCE DATA FOR CODEX` z pliku `00_PROJECT_CONTEXT_TEMPLATE.md`.

```text
Goal: perform final cleanup before pull request.

Check and fix:
- DRIVER_FILE
- VENDOR_INIT
- PROTOCOL_TEST
- HARDWARE_TEST
- DOC_FILE
- DOC_INDEX

Checklist:
1. Class imports from pymeasure.instruments.<VENDOR>.
2. If the instrument is SCPI, class inherits from SCPIMixin, Instrument.
3. No includeSCPI=True.
4. No get_* and no set_* methods.
5. Properties use Instrument.measurement/control/setting.
6. Methods are only for actions, data transfers, parsers, and multi-step operations.
7. Every property has a docstring with units/types/ranges if known.
8. Every validator uses manual data.
9. Every values={...} mapping uses manual tokens.
10. expected_protocol tests are complete for implemented commands.
11. Hardware tests skip without a device address.
12. Hardware tests do not run destructive/service/power/calibration commands.
13. Hardware tests leave sources/outputs disabled if applicable.
14. Sphinx documentation exists.
15. Vendor index is updated.
16. assets/, AGENTS.md, manual PDFs, logs, worklogs, coverage files do not enter final PR.

Run:
python -m pytest tests/instruments/<VENDOR>/test_<MODEL_LOWER>.py -q
git diff --check
git diff --stat
git status --short

Report:
- files that should enter the PR,
- files that should not enter the PR,
- deferred/not-implemented commands and reasons,
- whether the driver is ready for review.
```
