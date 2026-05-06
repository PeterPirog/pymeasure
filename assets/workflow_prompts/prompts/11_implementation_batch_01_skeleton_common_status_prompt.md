# Prompt 11 — Implementation batch 1: skeleton, common/status, safe basics

```text
WORK IN THE LOCAL PYMEASURE REPOSITORY.


MODEL AND HARDWARE ACCESS

Recommended model for this step: qwen3-coder-next:cloud
Physical instrument access required: NO for protocol tests. Optional only for a manual smoke test outside this prompt.

VISA_ADDRESS_EXAMPLE, if present, is only metadata for local instructions and generated commands.
A cloud model cannot access a local GPIB/USB/LAN/RS-232 instrument directly.
Real hardware communication may only happen on the operator's local computer or explicitly configured local runner.


UPSTREAM PYMEASURE AGENTS.MD COMPLIANCE

Before editing, read the repository-level `AGENTS.md` file if it exists.
Follow it as the highest-priority local repository rule set.
In particular:

- Use Python 3.9+ compatible code.
- Keep line length at or below 100 characters.
- Follow PEP8 and PEP257.
- Use lowercase filenames for instrument modules.
- Place instrument drivers under `pymeasure/instruments/<manufacturer>/`.
- Update the manufacturer `__init__.py` when a driver class is added.
- Add protocol tests under `tests/instruments/<manufacturer>/`.
- Name hardware/device tests with the `_with_device.py` suffix.
- Add documentation under `docs/api/instruments/<manufacturer>/`.
- Prefer PyMeasure property creators: `control`, `measurement`, and `setting`.
- Do not create public `get_*` or `set_*` methods.
- Use validators only when ranges/discrete sets are confirmed by manuals.
- Use `map_values=True` when Python-facing names differ from device tokens.
- For channels with fewer than 16 channels, prefer `Instrument.ChannelCreator`.
- For more than 16 channels, prefer `Instrument.MultiChannelCreator`.
- Use `expected_protocol` / `ProtocolAdapter` for communication tests without hardware.
- Use imperative docstring summaries with a period at the end.
- Document properties with wording such as "Control", "Measure", "Get", or "Set".
- Do not use comments for obvious code; comments should explain non-obvious reasons.



STEP METADATA

STEP_ID = 11
STEP_NAME = implementation_batch_01_skeleton_common_status

Instrument parameters:

VENDOR = fluke
MODEL = 5560A
CLASS_NAME = Fluke5560A
INSTRUMENT_TYPE = multifunction precision calibrator / precision source calibrator
PYMEASURE_VENDOR_PACKAGE = fluke
MODEL_LOWER = 5560a

Paths:

ARCHITECTURE_PLAN = assets/<VENDOR>/<MODEL>/architecture_plan.md
COMMAND_COVERAGE = assets/<VENDOR>/<MODEL>/command_coverage.md
DRIVER_FILE = pymeasure/instruments/<PYMEASURE_VENDOR_PACKAGE>/<MODEL_LOWER>.py
VENDOR_INIT = pymeasure/instruments/<PYMEASURE_VENDOR_PACKAGE>/__init__.py
PROTOCOL_TEST_FILE = tests/instruments/<PYMEASURE_VENDOR_PACKAGE>/test_<MODEL_LOWER>.py
HARDWARE_TEST_FILE = tests/instruments/<PYMEASURE_VENDOR_PACKAGE>/test_<MODEL_LOWER>_with_device.py

MAIN GOAL

Implement batch 1 only:

- driver skeleton,
- class definition,
- safe constructor/default connection settings,
- SCPI/common/status/error methods selected in `architecture_plan.md`,
- minimal protocol tests,
- minimal safe hardware test that only checks identity and safe query behavior,
- update vendor `__init__.py`.

Do not implement input/source/trigger/calculate/display/memory subsystems yet.
Do not implement destructive, calibration, format/delete/store, power-off, or long self-test commands.
Do not run hardware tests unless a device address is explicitly provided outside this prompt.

PYMEASURE RULES

1. Use `SCPIMixin, Instrument` if `architecture_plan.md` says SCPI/IEEE-488.2 is confirmed.
2. Do not use `includeSCPI=True`.
3. Use properties via `Instrument.control`, `Instrument.measurement`, `Instrument.setting`.
4. Use methods for command-only actions.
5. No public `get_*` or `set_*` methods.
6. Docstrings must start with imperative verbs.
7. Use `self.write`, `self.ask`, `self.read`.
8. Every implemented command must have an `expected_protocol` test.

TASKS

1. Read `architecture_plan.md` and `command_coverage.md`.
2. Create driver file.
3. Add class `CLASS_NAME`.
4. Add safe constructor with interface-specific defaults only if justified by manuals.
5. Add safe common/status API selected for batch 1.
6. Add `check_id()` if useful and consistent with existing PyMeasure style.
7. Add error queue method only if command is confirmed in Programming Guide.
8. Update vendor `__init__.py`.
9. Create protocol tests.
10. Create hardware test file with skip-without-device behavior.
11. Update local `command_coverage.md` statuses only for implemented commands.

HARDWARE TEST RULES

- Identity query only.
- No output/source activation.
- No reset unless explicitly safe and already agreed.
- Use timeout at least 20000 ms for older GPIB unless manual says otherwise.
- Query error queue if safe and implemented.
- Leave instrument in safe state.

ACCEPTANCE COMMANDS

Run:

```powershell
$vendor = "fluke"
$model = "5560a"

python -m pytest tests/instruments/$vendor/test_$model.py -q
python -c "from pymeasure.instruments.$vendor import Fluke5560A; print(Fluke5560A)"
git diff --check
git diff --stat
git status --short
```

Do not run hardware tests automatically. Only print the command:

```powershell
python -m pytest tests/instruments/fluke/test_5560a_with_device.py --device-address "<VISA_ADDRESS>" -q -s
```


EXTRA VERIFICATION FOR STEP 08

Verify implementation scope and protocol coverage.
Run:

```powershell
git diff --name-only
Select-String -Path pymeasure/instruments/$vendor/$model.py -Pattern "includeSCPI=True", "def get_", "def set_"
Select-String -Path tests/instruments/$vendor/test_$model.py -Pattern "expected_protocol"
```

The search for `includeSCPI=True`, `def get_`, and `def set_` must return no driver violations.
Fail if any implemented command lacks an expected_protocol test.


MANDATORY AUTOMATED QUALITY GATE

At the end of this prompt, create or update a step report file:

assets/<VENDOR>/<MODEL>/workflow_reports/<STEP_ID>_<STEP_NAME>_report.md

If the directory does not exist, create it.

The report must contain:

1. `STATUS: PASS` or `STATUS: FAIL`.
2. `HUMAN_REQUIRED: yes/no`.
3. A short reason if human input is required.
4. Files created or modified.
5. Commands run.
6. Exact output or summary of acceptance commands.
7. Counts requested by this prompt.
8. Any `needs-verification` items.
9. Any deviation from `AGENTS.md` or PyMeasure conventions.
10. A clear next-step recommendation.

Use `STATUS: FAIL` and stop if:

- required input files are missing,
- commands or API are invented without manual evidence,
- files outside the allowed scope were changed,
- acceptance commands fail,
- `git diff --check` reports whitespace errors,
- implementation prompts add features outside their batch scope,
- hardware tests would require unsafe or operator-confirmed actions,
- final cleanup still includes `assets/`, `AGENTS.md`, PDFs, local logs, or worklogs in the PR diff.

Do not proceed to the next workflow step automatically if `STATUS: FAIL`.
Do not ask the operator for help unless the report marks `HUMAN_REQUIRED: yes` and explains why.

FINAL REPORT

Report files changed, commands implemented, protocol tests added, hardware tests added and why safe, excluded commands, pytest result, import check result, `git diff --check`, and `git diff --stat`.
```
