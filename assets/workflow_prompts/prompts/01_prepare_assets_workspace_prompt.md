# Prompt 01 — Prepare local assets workspace

```text
WORK IN THE LOCAL PYMEASURE REPOSITORY.


MODEL AND HARDWARE ACCESS

Recommended model for this step: qwen3-coder-next:cloud or kimi-k2.6:cloud
Physical instrument access required: NO. This is workspace/file preparation only.

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

STEP_ID = 01
STEP_NAME = prepare_assets_workspace

Instrument parameters:

VENDOR = fluke
MODEL = 5560A
CLASS_NAME = Fluke5560A
INSTRUMENT_TYPE = multifunction precision calibrator / precision source calibrator
PYMEASURE_VENDOR_PACKAGE = fluke
MODEL_LOWER = 5560a
VISA_ADDRESS_EXAMPLE = GPIB0::4::INSTR

ASSET_DIR = assets/<VENDOR>/<MODEL>

MAIN GOAL

Prepare the local planning workspace for a new PyMeasure instrument driver.

This step must not implement the driver.

CREATE OR UPDATE ONLY LOCAL PLANNING FILES:

- assets/<VENDOR>/<MODEL>/README.md
- assets/<VENDOR>/<MODEL>/codex_worklog.md
- assets/<VENDOR>/<MODEL>/command_coverage.md

DO NOT MODIFY:

- pymeasure/instruments/
- tests/
- docs/
- pyproject.toml
- .gitignore

TASKS

1. Create `assets/<VENDOR>/<MODEL>/`.
2. Create `README.md` in that directory with:
   - vendor, model, class name, instrument type,
   - expected manual filenames,
   - expected generated planning artifacts,
   - warning that this is a local planning folder and not for upstream PR.
3. Create `codex_worklog.md` if missing.
4. Create `command_coverage.md` if missing with:
   - status legend,
   - hardware-test policy legend,
   - command coverage table,
   - implementation batches table,
   - final PR checklist.
5. Do not edit `.gitignore`. In the final report, suggest local exclusion with:

   ```powershell
   Add-Content .git\info\exclude "`nAGENTS.md`nAgents.md`nassets/`n"
   ```

ACCEPTANCE COMMANDS

Run:

```powershell
$vendor = "fluke"
$model = "5560A"
$assetDir = "assets/$vendor/$model"

Test-Path $assetDir
Get-ChildItem $assetDir
Get-Content "$assetDir/README.md" -TotalCount 80
Get-Content "$assetDir/command_coverage.md" -TotalCount 80
git status --short
git diff --check
git diff --stat
```


EXTRA VERIFICATION FOR STEP 01

Verify that only local planning files were changed. Run:

```powershell
git diff --name-only
```

Allowed changed paths for this step are only:

```text
assets/<VENDOR>/<MODEL>/README.md
assets/<VENDOR>/<MODEL>/codex_worklog.md
assets/<VENDOR>/<MODEL>/command_coverage.md
assets/<VENDOR>/<MODEL>/workflow_reports/01_prepare_assets_workspace_report.md
```


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

Report created/updated files, whether `.gitignore` was left untouched, and results of `git diff --check` and `git diff --stat`.
```
