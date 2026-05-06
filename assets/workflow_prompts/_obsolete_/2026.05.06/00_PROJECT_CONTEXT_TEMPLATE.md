# 00 — PROJECT CONTEXT TEMPLATE

## DLA CZŁOWIEKA

Ten plik wypełniasz raz na początku pracy nad przyrządem.

Masz dwa zastosowania:

1. **Dla ChatGPT / Architekta** — wklej sekcję `PROJECT CONTEXT FOR CHATGPT`, żeby Chat znał katalog roboczy, vendor, model, typ przyrządu i adres VISA.
2. **Dla Codexa w PyCharm** — wklej sekcję `SOURCE DATA FOR CODEX` na początku każdego promptu roboczego.

Adres VISA może być pusty. Wtedy workflow nadal działa, ale hardware tests będą pomijane.

---

## PROJECT CONTEXT FOR CHATGPT

```text
PROJECT_CONTEXT

Repozytorium PyMeasure:
REPO_ROOT = <absolute path to local PyMeasure repo>

Instrument:
VENDOR = <vendor, lowercase, e.g. fluke>
MODEL = <model, e.g. 5560A>
MODEL_LOWER = <model lowercase/safe filename, e.g. 5560a>
CLASS_NAME = <planned class name, e.g. Fluke5560A>
INSTRUMENT_TYPE = <instrument type, e.g. multifunction precision calibrator>
DEVICE_ADDRESS = <VISA address or empty string, e.g. GPIB0::4::INSTR>

Manuals:
PROGRAMMING_GUIDE = assets/<VENDOR>/<MODEL>/programming_guide.md
SERVICE_MANUAL = assets/<VENDOR>/<MODEL>/service_manual.md
OPERATORS_GUIDE = assets/<VENDOR>/<MODEL>/operators_guide.md

Workflow rule:
Use these values as defaults in this workflow unless I explicitly change them.
```

Po wklejeniu tego do Chata napisz:

```text
Zapamiętaj ten kontekst dla bieżącego workflow i używaj go w kolejnych promptach dla Codexa.
```

Jeżeli chcesz pamięć między rozmowami, napisz jawnie:

```text
Zapamiętaj w pamięci: pracuję nad driverem PyMeasure dla <vendor> <model>, repozytorium jest w <repo_root>, a robocze materiały są w assets/<vendor>/<model>.
```

Nie zapisuj w pamięci haseł, tokenów ani prywatnych danych.

---

## SOURCE DATA FOR CODEX

```text
SOURCE DATA FOR CODEX

Work in the local PyMeasure repository.

Repository:
REPO_ROOT = <absolute path to local PyMeasure repo>

Instrument parameters:
VENDOR = <vendor>
MODEL = <model>
MODEL_LOWER = <model_lower>
CLASS_NAME = <ClassName>
INSTRUMENT_TYPE = <instrument type>
DEVICE_ADDRESS = <VISA address or empty string>

Asset paths:
ASSET_DIR = assets/<VENDOR>/<MODEL>
PROGRAMMING_GUIDE = assets/<VENDOR>/<MODEL>/programming_guide.md
SERVICE_MANUAL = assets/<VENDOR>/<MODEL>/service_manual.md
OPERATORS_GUIDE = assets/<VENDOR>/<MODEL>/operators_guide.md
COMMANDS_TXT = assets/<VENDOR>/<MODEL>/commands.txt
COMMAND_COVERAGE = assets/<VENDOR>/<MODEL>/command_coverage.md
SERVICE_COVERAGE = assets/<VENDOR>/<MODEL>/service_coverage.md
OPERATOR_COVERAGE = assets/<VENDOR>/<MODEL>/operator_coverage.md
ARCHITECTURE_PLAN = assets/<VENDOR>/<MODEL>/architecture_plan.md
CODEX_WORKLOG = assets/<VENDOR>/<MODEL>/codex_worklog.md

Planned PyMeasure files:
DRIVER_FILE = pymeasure/instruments/<VENDOR>/<MODEL_LOWER>.py
VENDOR_INIT = pymeasure/instruments/<VENDOR>/__init__.py
PROTOCOL_TEST = tests/instruments/<VENDOR>/test_<MODEL_LOWER>.py
HARDWARE_TEST = tests/instruments/<VENDOR>/test_<MODEL_LOWER>_with_device.py
DOC_FILE = docs/api/instruments/<VENDOR>/<MODEL_LOWER>.rst
DOC_INDEX = docs/api/instruments/<VENDOR>/index.rst

Global rules:
- Do not invent commands.
- Command syntax must come only from programming_guide.md or another explicit remote programming command reference.
- service_manual.md may only affect risk, safety, calibration, adjustment, hardware-test policy, and service-only classification.
- operators_guide.md may only affect user-facing semantics, safe operating sequence, front-panel terminology, connector names, and final safe state.
- Use PyMeasure patterns: SCPIMixin + Instrument for SCPI instruments; never use includeSCPI=True.
- Do not create get_* or set_* methods.
- Use Instrument.measurement, Instrument.control, Instrument.setting.
- Use explicit methods for command-only actions, destructive operations, long operations, and data transfer parsers.
- Every implemented command must have an expected_protocol test.
- Hardware tests must be skipped when DEVICE_ADDRESS is empty.
- Never run destructive, calibration, adjustment, format, delete, store, power-off, firmware, factory, or long self-test commands in automatic hardware tests.
- After hardware tests, leave the instrument in a safe state and query the error queue if available.
```
