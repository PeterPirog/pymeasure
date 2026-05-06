# Prompt 04 — Optimize Service Manual for PyMeasure service-risk planning

```text
WORK IN THE LOCAL PYMEASURE REPOSITORY.


MODEL AND HARDWARE ACCESS

Recommended model for this step: kimi-k2.6:cloud or qwen3.6:latest
Physical instrument access required: NO. Manual transformation only.

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

STEP_ID = 04
STEP_NAME = optimize_service_manual_for_llm

Instrument parameters:

VENDOR = fluke
MODEL = 5560A
CLASS_NAME = Fluke5560A
INSTRUMENT_TYPE = multifunction precision calibrator / precision source calibrator

Paths:

ASSET_DIR = assets/<VENDOR>/<MODEL>
INPUT_FILE = assets/<VENDOR>/<MODEL>/service_manual.md
OUTPUT_FILE = assets/<VENDOR>/<MODEL>/service_manual_llm.md

MAIN GOAL

Create `service_manual_llm.md`, an LLM/PyMeasure-oriented service-risk knowledge base.

Use it for service-only boundaries, calibration/adjustment risk, destructive actions, NVM/persistent-state risk, qualified-personnel warnings, safe hardware-test exclusion rules, and option/model dependencies.

Do not use the Service Manual as the authoritative source for remote command syntax. If command-like tokens appear only in the Service Manual, list them as candidates requiring Programming Guide confirmation.

Do not implement code.
Do not modify `pymeasure/instruments/`, `tests/`, or `docs/`.
Do not use VISA or hardware.

Only create or update:

assets/<VENDOR>/<MODEL>/service_manual_llm.md

TASKS

1. If `service_manual.md` does not exist, stop and report missing file.
2. Extract service-risk knowledge.
3. Preserve safety warnings and service-only boundaries.
4. Mark ambiguous OCR/conversion artifacts as `needs-verification`.

OUTPUT STRUCTURE

1. YAML front matter.
2. `LLM_AGENT_CONTRACT`.
3. `DOCUMENT ROLE`.
4. `SERVICE SAFETY SUMMARY`.
5. `SERVICE-ONLY PROCEDURES`.
6. `CALIBRATION / ADJUSTMENT / NVM RISK`.
7. `VERIFICATION PREREQUISITES`.
8. `MODEL AND OPTION DEPENDENCIES`.
9. `COMMAND-LIKE TOKENS REQUIRING PROGRAMMING GUIDE CONFIRMATION`.
10. `HARDWARE-TEST EXCLUSION LIST`.
11. `PYMEASURE API DECISION RULES`.
12. `OCR_AND_CONVERSION_NOTES`.

Risk values:

- operator-safe
- fixture-dependent
- hazardous-output
- service-only
- calibration-risk
- destructive
- persistent-state
- long-running
- needs-verification

Hardware-test policies:

- query-only
- output-off-only
- roundtrip-safe
- operator-confirmed-only
- protocol-only
- never
- needs-verification

ACCEPTANCE COMMANDS

Run:

```powershell
$vendor = "fluke"
$model = "5560A"
$assetDir = "assets/$vendor/$model"
$output = "$assetDir/service_manual_llm.md"

Test-Path $output
Get-Content $output -TotalCount 160
Select-String -Path $output -Pattern "LLM_AGENT_CONTRACT", "SERVICE SAFETY", "CALIBRATION", "NVM", "HARDWARE-TEST EXCLUSION"
git status --short
git diff --check
git diff --stat
```


EXTRA VERIFICATION FOR STEP 04

Verify that service-only and calibration-risk procedures are excluded from normal hardware tests.
Run:

```powershell
Select-String -Path $output -Pattern "service-only", "calibration-risk", "persistent-state", "never", "protocol-only"
git diff --name-only
```

Allowed changed paths are `service_manual_llm.md` and this step report only.


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

Report output path, service-only topics, calibration/NVM risks, highest-risk topics, option dependencies, command-like tokens isolated, and results of `git diff --check` and `git diff --stat`.
```
