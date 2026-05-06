# Prompt 17 — Documentation and final PR cleanup

```text
WORK IN THE LOCAL PYMEASURE REPOSITORY.


MODEL AND HARDWARE ACCESS

Recommended model for this step: qwen3-coder-next:cloud or deepseek-v4-pro:cloud
Physical instrument access required: NO unless the operator intentionally repeats safe hardware tests before PR.

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

STEP_ID = 17
STEP_NAME = docs_and_final_cleanup

Instrument parameters:

VENDOR = fluke
MODEL = 5560A
CLASS_NAME = Fluke5560A
PYMEASURE_VENDOR_PACKAGE = fluke
MODEL_LOWER = 5560a

Paths:

DRIVER_FILE = pymeasure/instruments/<PYMEASURE_VENDOR_PACKAGE>/<MODEL_LOWER>.py
VENDOR_INIT = pymeasure/instruments/<PYMEASURE_VENDOR_PACKAGE>/__init__.py
PROTOCOL_TEST_FILE = tests/instruments/<PYMEASURE_VENDOR_PACKAGE>/test_<MODEL_LOWER>.py
HARDWARE_TEST_FILE = tests/instruments/<PYMEASURE_VENDOR_PACKAGE>/test_<MODEL_LOWER>_with_device.py
DOC_FILE = docs/api/instruments/<PYMEASURE_VENDOR_PACKAGE>/<MODEL_LOWER>.rst
DOC_INDEX = docs/api/instruments/<PYMEASURE_VENDOR_PACKAGE>/index.rst
COMMAND_COVERAGE = assets/<VENDOR>/<MODEL>/command_coverage.md

MAIN GOAL

Finalize the driver for an upstream PyMeasure-style pull request.

Do not add new features unless required to fix tests or documentation import errors.

TASKS

1. Verify driver style:
   - no `includeSCPI=True`,
   - no public `get_*` or `set_*` API methods,
   - `SCPIMixin, Instrument` if appropriate,
   - command-only actions are methods,
   - query-only scalar values are measurements or read methods,
   - data transfers use parser methods,
   - docstrings start with imperative verbs.

2. Verify tests:
   - every implemented command has protocol coverage,
   - hardware tests skip without device address,
   - destructive commands are not run in hardware tests.

3. Add/update Sphinx documentation:
   - create `docs/api/instruments/<vendor>/<model_lower>.rst`,
   - update vendor `index.rst`,
   - if manufacturer is new, update `docs/api/instruments/index.rst`.

4. Ensure vendor `__init__.py` exports `CLASS_NAME`.

5. Update `command_coverage.md` final checklist.

6. Ensure final PR diff does not include:
   - assets/,
   - AGENTS.md,
   - manual PDFs,
   - local worklogs,
   - temporary scripts.

ACCEPTANCE COMMANDS

Run:

```powershell
$vendor = "fluke"
$model = "5560a"

python -m pytest tests/instruments/$vendor/test_$model.py -q
python -m pytest tests/instruments/$vendor/test_${model}_with_device.py -q
python -c "from pymeasure.instruments.$vendor import Fluke5560A; print(Fluke5560A)"
git diff --check
git diff --stat
git status --short
git diff --name-only
```


EXTRA VERIFICATION FOR STEP 11

Run a final PR hygiene check:

```powershell
git diff --name-only
```

Fail if the final PR diff includes:

```text
assets/
AGENTS.md
Agents.md
*.pdf
*_worklog*
workflow_reports/
temporary scripts
manual conversion artifacts
```

Also fail if docs are missing, vendor `__init__.py` does not export the class, or protocol tests do not pass.


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

Report driver status, vendor init status, protocol and hardware test status, documentation status, final diff file list, whether `assets/` or `AGENTS.md` appear in final diff, pytest result, import check result, `git diff --check`, and `git diff --stat`.
```
