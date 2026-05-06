# Prompt 16 — Safe hardware tests prompt

```text
WORK IN THE LOCAL PYMEASURE REPOSITORY.


MODEL AND HARDWARE ACCESS

Recommended model for this step: qwen3-coder-next:cloud
Physical instrument access required: YES, but only on the operator machine with physical/network access to the instrument and an explicit VISA address.

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

STEP_ID = 16
STEP_NAME = safe_hardware_tests

Instrument parameters:

VENDOR = fluke
MODEL = 5560A
CLASS_NAME = Fluke5560A
PYMEASURE_VENDOR_PACKAGE = fluke
MODEL_LOWER = 5560a
VISA_ADDRESS = <paste real VISA address here, for example GPIB0::4::INSTR>

Paths:

COMMAND_COVERAGE = assets/<VENDOR>/<MODEL>/command_coverage.md
HARDWARE_TEST_FILE = tests/instruments/<PYMEASURE_VENDOR_PACKAGE>/test_<MODEL_LOWER>_with_device.py

MAIN GOAL

Add or refine safe hardware tests for already implemented APIs only.

Do not implement new driver features unless a test reveals a small bug.
Do not add hardware tests for destructive, calibration, adjustment, delete, format, store, power-off, long self-test, service-only, or operator-confirmed commands.

HARDWARE SAFETY RULES

1. Tests must skip without device address.
2. Use timeout at least 20000 ms unless the manual requires more.
3. Start with `*IDN?` / `id`.
4. Use `*CLS` only if already implemented and safe for this instrument.
5. Do not enable hazardous outputs.
6. Do not change persistent configuration unless explicitly marked roundtrip-safe.
7. After touching any source/output setting, restore safe final state in `try/finally`.
8. Query error queue after test sequences if safe API exists.
9. Do not assert exact firmware/version unless necessary.
10. Accept reasonable vendor-name variants in IDN.

TASKS

1. Read `command_coverage.md`.
2. Identify implemented commands with hardware policy query-only, output-off-only, or roundtrip-safe.
3. Add or refine tests in `test_<MODEL_LOWER>_with_device.py`.
4. Ensure all tests are skipped when no device address is provided.
5. Ensure hardware test file can be collected by pytest without hardware.
6. Update `command_coverage.md` hardware-test status only for tests added.

ACCEPTANCE COMMANDS

Run without hardware address first:

```powershell
$vendor = "fluke"
$model = "5560a"

python -m pytest tests/instruments/$vendor/test_$model.py -q
python -m pytest tests/instruments/$vendor/test_${model}_with_device.py -q
git diff --check
git diff --stat
git status --short
```

Then print the real hardware command, but do not run it unless operator confirms:

```powershell
python -m pytest tests/instruments/fluke/test_5560a_with_device.py --device-address "<VISA_ADDRESS>" -q -s
```

If hardware tests are run, report `*IDN?` response, option response if available, error queue response, and final source/output state.


EXTRA VERIFICATION FOR STEP 10

Before any real hardware test command is run, print a safety preflight checklist and require operator confirmation outside this prompt.
The checklist must include:

- VISA resource address,
- interface type,
- timeout,
- instrument identity query plan,
- output/source state policy,
- destructive command exclusion,
- final safe state,
- error queue plan.

Fail if any hardware test enables hazardous output, performs calibration/adjustment, deletes/formats/stores memory, powers off the instrument, or runs a long self-test.


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

Report hardware tests added, commands covered, skip behavior, safety final state, pytest without hardware result, hardware command to run, and results of `git diff --check` and `git diff --stat`.
```
