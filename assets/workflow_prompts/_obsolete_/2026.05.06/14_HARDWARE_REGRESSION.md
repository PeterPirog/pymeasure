14A_SAFE_HARDWARE_COVERAGE.md
DLA CZŁOWIEKA — co robi ten prompt
Ten prompt wymusza pełne pokrycie testami sprzętowymi dla wszystkich komend, które:
są już zaimplementowane w driverze,
mają test `expected_protocol`,
są oznaczone jako bezpieczne do sprawdzenia na realnym urządzeniu,
nie wymagają specjalnego fixture, obciążenia, kalibratora pomocniczego, DUT ani świadomego potwierdzenia operatora.
Prompt nie uruchamia komend niebezpiecznych. Dla każdej komendy bez testu sprzętowego Codex ma dopisać test albo jawnie oznaczyć powód pominięcia w `command_coverage.md`.
Użyj tego promptu dopiero po implementacji głównych bezpiecznych subsystemów i po przejściu testów protokołowych. Ten prompt najlepiej wykonać po audycie kompletności, a przed finalnym hardware regression i final cleanup.
Jak podać kontekst projektu, żeby Chat i Codex miały stałe dane
Przed użyciem tego promptu wypełnij blok `SOURCE DATA FOR CODEX`. Najważniejsze pola:
```text
VENDOR = <vendor>
MODEL = <model>
MODEL_LOWER = <model_lower>
CLASS_NAME = <ClassName>
DEVICE_ADDRESS = <VISA address or empty string>
```
Przykład:
```text
VENDOR = fluke
MODEL = 5560A
MODEL_LOWER = 5560a
CLASS_NAME = Fluke5560A
DEVICE_ADDRESS = GPIB0::4::INSTR
```
Jeżeli nie chcesz jeszcze wykonywać testów na fizycznym urządzeniu, ustaw:
```text
DEVICE_ADDRESS =
```
Wtedy Codex ma przygotować testy sprzętowe, ale ich nie uruchamiać.
---
PROMPT DLA CODEXA
SOURCE DATA FOR CODEX
Work in the local PyMeasure repository.
Instrument parameters:
```text
VENDOR = <vendor>
MODEL = <model>
MODEL_LOWER = <model_lower>
CLASS_NAME = <ClassName>
DEVICE_ADDRESS = <VISA address or empty string>
```
Paths:
```text
COMMAND_COVERAGE = assets/<VENDOR>/<MODEL>/command_coverage.md
SERVICE_COVERAGE = assets/<VENDOR>/<MODEL>/service_coverage.md
OPERATOR_COVERAGE = assets/<VENDOR>/<MODEL>/operator_coverage.md
DRIVER_FILE = pymeasure/instruments/<VENDOR>/<MODEL_LOWER>.py
PROTOCOL_TEST = tests/instruments/<VENDOR>/test_<MODEL_LOWER>.py
HARDWARE_TEST = tests/instruments/<VENDOR>/test_<MODEL_LOWER>_with_device.py
CODEX_WORKLOG = assets/<VENDOR>/<MODEL>/codex_worklog.md
```
Global PyMeasure rules:
Do not invent commands.
Command syntax must come only from `programming_guide.md`, `commands.txt`, or another explicit remote programming command reference.
`service_manual.md` may only affect risk, safety, calibration, adjustment, hardware-test policy, and service-only classification.
`operators_guide.md` may only affect user-facing semantics, safe operating sequence, connector terminology, and final safe state.
Use `SCPIMixin, Instrument` for SCPI/IEEE-488.2 instruments.
Never use `includeSCPI=True`.
Do not create `get_*` or `set_*` methods.
Use `Instrument.measurement`, `Instrument.control`, and `Instrument.setting`.
Use explicit methods for command-only actions, destructive operations, long operations, and data-transfer parsers.
Every implemented command must have an `expected_protocol` test.
Hardware tests must be skipped when `DEVICE_ADDRESS` is empty.
Never run destructive, calibration, adjustment, format, delete, store, power-off, firmware, factory, or long self-test commands in automatic hardware tests.
After hardware tests, leave the instrument in a safe state and query the error queue if available.
---
MAIN GOAL
Create or update hardware tests so that every implemented safe command has one of these outcomes:
`hardware-tested`
`hardware-skipped-with-reason`
`operator-confirmed-only`
`protocol-only`
`never`
Do not leave any implemented safe command with an empty or vague hardware-test decision.
This prompt is a hardware coverage enforcement step. It is not a feature implementation prompt unless a missing hardware test requires a small helper or restoration method that is clearly safe and already supported by the driver.
---
DEFINITIONS
Hardware-test eligible command
A command is hardware-test eligible if all are true:
Status is `implemented` or `protocol-tested`.
Risk level is one of:
`safe-query`
`safe-state-readwrite`
`safe-display-only`
`cautious-state-change`
Hardware-test policy is one of:
`yes`
`query-only`
`roundtrip-safe`
`output-off-only`
It does not require:
external load,
DUT,
fixture,
calibration standard,
service access,
high voltage,
high current,
high power,
RF load,
destructive memory operation,
option not present,
operator confirmation.
Not hardware-test eligible command
A command is not hardware-test eligible if any are true:
Risk level is one of:
`calibration`
`adjustment`
`destructive-file`
`destructive-log-clear`
`destructive-memory`
`factory/service`
`power-affecting`
`network/address-affecting`
`hazardous-output`
`service-only`
`unknown`
Hardware-test policy is one of:
`operator-confirmed-only`
`protocol-only`
`never`
`skip-unless-option-present`
`needs-fixture-or-load`
`needs-verification`
The command:
enables output,
switches the instrument to operate,
changes calibration data,
saves to nonvolatile memory,
deletes data,
formats media,
changes communication address,
powers off or reboots the unit,
starts a long self-test,
requires a connected load or DUT.
---
TASKS
Read `COMMAND_COVERAGE`.
Read `SERVICE_COVERAGE` if it exists.
Read `OPERATOR_COVERAGE` if it exists.
Read `DRIVER_FILE`.
Read `PROTOCOL_TEST`.
Read `HARDWARE_TEST` if it exists.
Build a list of all commands with status `implemented` or `protocol-tested`.
For each command, determine whether it is hardware-test eligible.
Update `HARDWARE_TEST` so that every hardware-test eligible command has a real test.
For every command that is not hardware-test eligible, do not add a hardware test; instead update `COMMAND_COVERAGE` with a precise reason.
Update `CODEX_WORKLOG` with a hardware coverage session entry.
Run protocol tests.
Run hardware tests only if `DEVICE_ADDRESS` is not empty.
Report hardware coverage numbers and unresolved exceptions.
---
HARDWARE TEST DESIGN RULES
General rules
Tests must skip if `DEVICE_ADDRESS` is empty.
Tests must use the repository convention for connected hardware tests.
Tests must accept `--device-address "<DEVICE_ADDRESS>"` if this is the local convention.
Use `timeout >= 20000 ms` unless the manual requires a longer timeout.
Open the real instrument only inside hardware tests.
Do not use `expected_protocol` in hardware tests.
Do not run broad hardware tests through mocks.
Do not mark a command as `hardware-tested` unless an actual hardware test exists and passes on the real instrument.
Remote-state proof
Add one explicit smoke test that sends a real identity query to the instrument.
The smoke test must:
Open the instrument using `DEVICE_ADDRESS`.
Send a real identity query, usually `*IDN?` or the driver’s equivalent identity property.
Print or log the actual identity response when pytest is run with `-s`.
Query the error queue if the driver supports it.
Record the actual identity response in `CODEX_WORKLOG`.
Do not consider hardware tests executed unless at least one real query response from the device is captured.
Safe query-only commands
For query-only commands:
Test by reading the property or method.
Assert only:
type,
non-empty response,
parseability,
documented token set,
numeric range if the manual clearly defines it.
Do not over-constrain firmware-specific strings unless the manual requires it.
If the real device response differs from the documentation, mark the row as `needs-verification` and record the actual response in `CODEX_WORKLOG`.
Safe command/query controls
For safe read/write controls, prefer non-destructive roundtrip:
Query the original value.
Set a documented safe value.
Query and assert the safe value.
Restore the original value.
Query and assert restoration if feasible.
Query the error queue if available.
If restore cannot be guaranteed, do not hardware-test automatically. Mark the command as:
```text
hardware-skipped-with-reason: restore cannot be guaranteed
```
Output/source commands
For output/source commands:
Do not enable output unless explicitly marked `roundtrip-safe` and low-risk.
For source/output settings, test only with output disabled or standby.
Before test: force safe standby/output-off state if the driver provides it.
After test: force safe standby/output-off state if the driver provides it.
If output state cannot be controlled safely, mark `operator-confirmed-only`.
Never test hazardous voltage, current, power, RF, or energy output automatically.
Display commands
For display-only state changes:
They may be hardware-tested if they do not affect output, NVM, calibration, files, or communication settings.
Save original display state when a query exists.
Restore original display state after test.
If original state cannot be queried, test only if the display state is harmless and clearly reversible.
Parser/data commands
For parser or data-transfer commands:
Hardware-test only small, bounded, query-only reads.
Do not request large traces, screenshots, full memory dumps, calibration reports, or long transfers unless explicitly marked safe.
If data transfer requires prior measurement, external signal, DUT, trigger, fixture, or long acquisition, mark `needs-fixture-or-load` or `operator-confirmed-only`.
Keep robust parser tests in `expected_protocol` tests.
Error queue handling
If the instrument has an error queue method:
Query it at the end of each hardware test or test group.
Normalize known no-error formats according to the driver parser.
Do not fail on harmless no-error format differences.
If an unexpected error appears, fail the test and record it in `CODEX_WORKLOG`.
Safe final state
At the end of each hardware test or test group:
Put the instrument into standby/output-off state if the driver supports it.
Disable source/output if applicable.
Restore changed settings if possible.
Query error queue if available.
Never leave the instrument sourcing energy unless the test explicitly requires it and the operator confirmed it outside this prompt.
---
COMMAND_COVERAGE UPDATES
For each implemented command, update these fields:
```text
Hardware test:
- yes
- skipped: <reason>
- operator-confirmed-only
- protocol-only
- never
```
```text
Status:
- hardware-tested only after an actual hardware test exists and passes
- protocol-tested if only expected_protocol exists
- unsafe if not safe
- needs-verification if device response differs from documentation
- needs-operator-decision if safe automation cannot be decided from manuals
```
Add this section to `COMMAND_COVERAGE`:
```markdown
## Hardware coverage summary

| Category | Count |
|---|---:|
| Implemented commands | |
| Hardware eligible commands | |
| Hardware tests implemented | |
| Hardware skipped with reason | |
| Operator-confirmed only | |
| Protocol-only | |
| Never hardware test | |
| Needs verification | |
```
Add this section to `COMMAND_COVERAGE`:
```markdown
## Hardware coverage exceptions

| Command | Reason not hardware-tested | Required operator action | Notes |
|---|---|---|---|
```
No implemented safe command may have an empty hardware-test field after this prompt.
---
HARDWARE TEST FILE REQUIREMENTS
Update or create:
```text
tests/instruments/<VENDOR>/test_<MODEL_LOWER>_with_device.py
```
The file must:
Use the repository’s existing convention for connected-device tests.
Skip all tests if no device address is provided.
Use timeout at least 20000 ms unless the manual requires more.
Include a smoke identity test.
Include hardware tests for every eligible safe implemented command.
Never call dangerous commands automatically.
Restore safe final state whenever possible.
Avoid brittle assertions based on exact firmware strings unless the manual or driver requires them.
Print or otherwise expose identity response under `pytest -s` for operator verification.
Recommended structure:
```python
import pytest

from pymeasure.instruments.<VENDOR> import <CLASS_NAME>


def make_instrument(address):
    return <CLASS_NAME>(address, timeout=20000)


def test_hardware_identity(connected_device_address):
    inst = make_instrument(connected_device_address)
    identity = inst.id
    print(f"Instrument identity: {identity}")
    assert identity
    assert "<MODEL>".upper() in identity.upper() or "<VENDOR>".upper() in identity.upper()
```
Adapt this structure to the repository’s actual fixtures and style. Do not duplicate fixtures if the repository already provides them.
---
CODEX_WORKLOG UPDATES
Append a new session to `CODEX_WORKLOG`:
```markdown
### Session — SAFE_HARDWARE_COVERAGE

#### Goal

Enforce hardware-test coverage for all implemented safe commands.

#### DEVICE_ADDRESS present

yes/no

#### Commands considered

<paste count and list or summary>

#### Commands hardware-tested

<paste list>

#### Commands skipped with reason

<paste list>

#### Commands not eligible for automatic hardware tests

<paste list>

#### Commands run

```powershell
python -m pytest tests/instruments/<VENDOR>/test_<MODEL_LOWER>.py -q
python -m pytest tests/instruments/<VENDOR>/test_<MODEL_LOWER>_with_device.py --device-address "<DEVICE_ADDRESS>" -q -s
```
Test output
```text
<paste full output>
```
Actual instrument identity response
```text
<paste response or "not run">
```
Error queue response
```text
<paste response or "not available">
```
Final safe state
```text
Output/source disabled: yes/no/not applicable
Instrument left in standby: yes/no/not applicable
Unexpected errors: yes/no
```
Notes for architect
```text
<paste issues, skipped commands, operator decisions needed>
```
```

---

## ACCEPTANCE COMMANDS

Run protocol tests:

```powershell
python -m pytest tests/instruments/<VENDOR>/test_<MODEL_LOWER>.py -q
```
If `DEVICE_ADDRESS` is not empty, run hardware tests:
```powershell
python -m pytest tests/instruments/<VENDOR>/test_<MODEL_LOWER>_with_device.py --device-address "<DEVICE_ADDRESS>" -q -s
```
Then run:
```powershell
git diff --check
git diff --stat
git status --short
```
If `DEVICE_ADDRESS` is empty, do not run hardware tests. Instead report:
```text
Hardware tests were prepared but not run because DEVICE_ADDRESS is empty.
```
---
FINAL REPORT
At the end, report:
Whether hardware tests actually ran.
The actual identity response from the device, if hardware tests ran.
Number of implemented commands.
Number of hardware-eligible commands.
Number of commands now hardware-tested.
Number of commands skipped with reason.
Number of `operator-confirmed-only` commands.
Number of `protocol-only` commands.
Number of `never` hardware-test commands.
Any unexpected instrument errors.
Whether the instrument was left in a safe state.
Whether `COMMAND_COVERAGE` has no empty hardware-test decisions for implemented commands.
The output of:
`git diff --check`
`git diff --stat`
`git status --short`
Do not claim hardware coverage if the hardware tests did not run against a real `DEVICE_ADDRESS`.