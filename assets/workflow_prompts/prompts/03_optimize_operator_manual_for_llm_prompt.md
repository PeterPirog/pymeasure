# Prompt 03 — Optimize Operator / Operation Manual for LLM/PyMeasure safety planning

WORK IN THE LOCAL PYMEASURE REPOSITORY.

EXECUTION MODE REQUIRED.

You must apply file changes directly in the repository.
You must not only describe the steps.
You must not only return snippets.

This prompt intentionally avoids nested Markdown code fences and avoids fragile PowerShell constructs
such as pipeline `$_` placeholders and path backslash replacement. Use named variables in PowerShell.

CRITICAL READ-ONLY SOURCE POLICY:

- Source manuals are read-only inputs.
- Never modify, rewrite, normalize, reformat, rename, move, or clean any source manual.
- Never modify any file listed in:
  - config.manuals.programming_guide
  - config.manuals.operator_manual_candidates
  - config.manuals.service_manual
- This step may create or update only:
  - config.asset_dir + "/operators_manual_llm.md"
  - config.workflow_reports_dir + "/03_optimize_operator_manual_for_llm_report.md"
- If any source manual changes, set STATUS: FAIL.

Before running this prompt, the operator should have no unrelated uncommitted changes. If unrelated
changes exist, the allowed-path check may correctly fail.

============================================================
CENTRAL WORKFLOW CONFIGURATION
============================================================

Read the instrument configuration from:

CONFIG_FILE = assets/workflow_prompts/workflow_config.json

Do not hard-code vendor/model paths. Do not use fallback paths.

CONFIG_FILE is the single source of truth for:

- vendor
- model
- class_name
- instrument_type
- pymeasure_vendor_package
- model_lower
- visa_address_example
- asset_dir
- manuals.programming_guide
- manuals.operator_manual_candidates
- manuals.service_manual
- workflow_reports_dir

Derived paths for this step:

ASSET_DIR = config.asset_dir
INPUT_CANDIDATES = config.manuals.operator_manual_candidates
PROGRAMMING_GUIDE = config.manuals.programming_guide
OUTPUT_FILE = config.asset_dir + "/operators_manual_llm.md"
REPORT_DIR = config.workflow_reports_dir
REPORT_FILE = config.workflow_reports_dir + "/03_optimize_operator_manual_for_llm_report.md"

If CONFIG_FILE is missing, stop and report in chat:

STATUS: FAIL
HUMAN_REQUIRED: yes
BLOCKER: missing workflow_config.json

Do not continue using fallback hard-coded paths.

============================================================
MANDATORY FAIL-SAFE REPORT RULE
============================================================

The report file is mandatory.

After reading CONFIG_FILE and deriving REPORT_DIR and REPORT_FILE, immediately create REPORT_DIR
and write a provisional REPORT_FILE with STATUS: FAIL.

The provisional report must contain:

STATUS: FAIL
HUMAN_REQUIRED: yes
STEP_ID: 03
STEP_NAME: optimize_operator_manual_for_llm
CONFIG_FILE: assets/workflow_prompts/workflow_config.json

BLOCKERS:
- Step started. This is a provisional fail-safe report.
- Final report has not been written yet.

Then continue to input discovery and output generation.

At the end, overwrite REPORT_FILE with the final report.

If terminal execution is blocked, still create REPORT_FILE using the file editing tool.
If file writing is blocked, stop and report in chat exactly:

BLOCKED: missing file-write permission

============================================================
MANDATORY PREFLIGHT COMMANDS
============================================================

Run these PowerShell commands exactly, using CONFIG_FILE. Do not skip them.

POWERSHELL_PREFLIGHT_START

$configPath = "assets/workflow_prompts/workflow_config.json"
$configExists = Test-Path $configPath
Write-Output ("CONFIG_EXISTS: {0}" -f $configExists)

if (-not $configExists) {
    Write-Output "CONFIG_MISSING"
} else {
    $config = Get-Content $configPath -Raw | ConvertFrom-Json
    $assetDir = $config.asset_dir
    $reportDir = $config.workflow_reports_dir
    $report = "$reportDir/03_optimize_operator_manual_for_llm_report.md"

    New-Item -ItemType Directory -Force -Path $reportDir | Out-Null

    @"
STATUS: FAIL
HUMAN_REQUIRED: yes
STEP_ID: 03
STEP_NAME: optimize_operator_manual_for_llm
CONFIG_FILE: $configPath

BLOCKERS:
- Step started. This is a provisional fail-safe report.
- Final report has not been written yet.
"@ | Set-Content $report -Encoding UTF8

    Write-Output ("CONFIG vendor: {0}" -f $config.vendor)
    Write-Output ("CONFIG model: {0}" -f $config.model)
    Write-Output ("CONFIG asset_dir: {0}" -f $config.asset_dir)
    Write-Output ("CONFIG workflow_reports_dir: {0}" -f $config.workflow_reports_dir)
    Write-Output ("REPORT_FILE: {0}" -f $report)
    Write-Output ("REPORT_EXISTS_AFTER_PROVISIONAL_WRITE: {0}" -f (Test-Path $report))
    Write-Output ("PROGRAMMING_GUIDE_EXISTS: {0}" -f (Test-Path $config.manuals.programming_guide))
    Write-Output ("SERVICE_MANUAL_EXISTS: {0}" -f (Test-Path $config.manuals.service_manual))
    Write-Output "OPERATOR_MANUAL_CANDIDATES:"

    foreach ($candidate in $config.manuals.operator_manual_candidates) {
        $exists = Test-Path $candidate
        Write-Output ("{0}: {1}" -f $exists, $candidate)
    }

    Write-Output "SOURCE_FILE_HASHES_BEFORE:"
    $sourceFiles = @()
    if ($config.manuals.programming_guide) {
        $sourceFiles += $config.manuals.programming_guide
    }
    if ($config.manuals.service_manual) {
        $sourceFiles += $config.manuals.service_manual
    }
    foreach ($candidate in $config.manuals.operator_manual_candidates) {
        $sourceFiles += $candidate
    }
    $sourceFiles = $sourceFiles | Select-Object -Unique
    foreach ($sourceFile in $sourceFiles) {
        if (Test-Path $sourceFile) {
            $hash = (Get-FileHash $sourceFile -Algorithm SHA256).Hash
            Write-Output ("{0}: {1}" -f $hash, $sourceFile)
        }
    }
}

POWERSHELL_PREFLIGHT_END

Important interpretation:

- At least one operator manual candidate must be True.
- Select the first candidate whose Test-Path result is True.
- If all candidates are False, keep STATUS: FAIL and write the checked paths into REPORT_FILE.
- Do not stop after creating the provisional report unless all candidates are missing or a blocker occurs.
- Preserve source-file hashes. The same source files must have identical hashes after generation.

============================================================
MODEL AND HARDWARE ACCESS
============================================================

Recommended model for this step: hal/kimi-k2.6:cloud
Fallback model: hal/qwen3.5:397b-cloud
Execution-agent fallback: hal/qwen3-coder-next:cloud

Physical instrument access required: NO.
This step is manual transformation only.

visa_address_example from CONFIG_FILE is only metadata for local instructions and generated commands.
A cloud model cannot access a local GPIB/USB/LAN/RS-232 instrument directly.
Real hardware communication may only happen on the operator's local computer or explicitly configured
local runner.

============================================================
UPSTREAM PYMEASURE AGENTS.MD COMPLIANCE
============================================================

Before editing, read the repository-level AGENTS.md file if it exists.
Follow it as the highest-priority local repository rule set.

For this step:

- Do not invent device-specific SCPI commands.
- Use source manuals as authority for device-specific behavior.
- Preserve safety, model, option, and physical setup constraints exactly as documented.
- Do not implement any driver in this step.
- Do not modify pymeasure/instruments/, tests/, or docs/.
- Do not modify source manual files.
- Keep generated Markdown readable and structured.
- Prepare later PyMeasure work to use property creators, expected_protocol tests, hardware tests
  with _with_device.py suffix, and Sphinx documentation, but do not create them now.

============================================================
STEP METADATA
============================================================

STEP_ID = 03
STEP_NAME = optimize_operator_manual_for_llm

Use metadata from CONFIG_FILE:

VENDOR = config.vendor
MODEL = config.model
CLASS_NAME = config.class_name
INSTRUMENT_TYPE = config.instrument_type

============================================================
MAIN GOAL
============================================================

Create or update:

- OUTPUT_FILE
- REPORT_FILE

The report file is mandatory.
The step is not complete until REPORT_FILE exists.
REPORT_FILE must exist even if no operator manual candidate is found.

The output file must be an LLM/PyMeasure-oriented safety and operation knowledge base derived
from the first existing operator/operation manual candidate listed in CONFIG_FILE.

Do not merely copy the operator manual. Transform it into the required structured sections below.
If the final report says "Copied operators_guide.md to operators_manual_llm.md", set STATUS: FAIL.
Use "Generated LLM/PyMeasure-optimized operator safety artifact" instead.

Use this output file later for:

- safe hardware-test policy,
- physical DUT connection constraints,
- remote interface setup context,
- warm-up and reset behavior,
- Operate/Standby behavior,
- model and option constraints,
- user-visible feature map,
- persistent setting and calibration-security risk,
- error-code interpretation,
- safe final-state planning.

Do not use the Operator/Operation Manual as the authoritative source for complete remote command
syntax. If command-like tokens are mentioned, list them only as cross-references requiring
Programming Guide confirmation.

Do not implement code.
Do not create commands.txt.
Do not create or fill command_coverage.md.
Do not modify source manuals.
Do not modify pymeasure/instruments/.
Do not modify tests/.
Do not modify docs/.
Do not use VISA.
Do not communicate with real hardware.

Allowed changed paths for this step are exactly:

- OUTPUT_FILE
- REPORT_FILE

If any other path is modified by this step, set STATUS: FAIL.

============================================================
INPUT DISCOVERY RULES
============================================================

1. Use the preflight result. Do not guess.
2. Select the first existing path from config.manuals.operator_manual_candidates.
3. Store it as INPUT_FILE.
4. Read INPUT_FILE only as input. Do not modify it.
5. If all candidates are missing:
   - do not create OUTPUT_FILE,
   - keep REPORT_FILE,
   - set STATUS: FAIL,
   - set HUMAN_REQUIRED: yes,
   - list every checked candidate and its False result,
   - set BLOCKERS to operator manual missing,
   - set NEXT_RECOMMENDED_STEP to:
     Fix workflow_config.json or place the operator/operation manual at one of the configured paths.
6. If PROGRAMMING_GUIDE exists, use it only to confirm command-like references.
7. If PROGRAMMING_GUIDE does not exist, still create OUTPUT_FILE from INPUT_FILE, but mark command-like
   confirmation as programming-guide-missing.

============================================================
SOURCE AUTHORITY RULES
============================================================

The Operator/Operation Manual is authoritative for:

- operator-level safety,
- front-panel behavior,
- Operate and Standby behavior,
- DUT connection requirements,
- remote interface context,
- remote port setup information,
- model and option availability,
- output capabilities,
- warm-up requirements,
- user-accessible settings,
- error-code descriptions,
- hardware-test safety policy.

The Operator/Operation Manual is not authoritative for complete remote command syntax.

If literal command-like tokens appear in INPUT_FILE:

- list them only in COMMAND-LIKE REFERENCES REQUIRING PROGRAMMING GUIDE CONFIRMATION,
- confirm them against PROGRAMMING_GUIDE if possible,
- do not add them to any command inventory,
- do not infer query/set variants.

Do not invent:

- commands,
- command forms,
- query forms,
- parameters,
- value ranges,
- safety limits,
- wiring requirements,
- warm-up requirements,
- option dependencies,
- error meanings,
- remote interface settings.

Preserve model and option limitations exactly as stated.

Mark OCR or Markdown conversion ambiguity as:

needs-verification

If a statement is inferred, mark it as:

inference-needs-verification

============================================================
OUTPUT STRUCTURE
============================================================

Create operators_manual_llm.md with exactly these top-level sections:

1. YAML front matter
2. LLM_AGENT_CONTRACT
3. DOCUMENT ROLE IN PYMEASURE WORKFLOW
4. QUICK FACTS FOR RETRIEVAL
5. SAFETY SUMMARY FOR DRIVER AND HARDWARE TEST PLANNING
6. REMOTE OPERATION AND INTERFACE SUMMARY
7. REMOTE PORT SETUP FACTS
8. OPERATE / STANDBY / RESET BEHAVIOR
9. DUT CONNECTION AND FIXTURE CONSTRAINTS
10. OUTPUT / INPUT FUNCTION MAP FOR PYMEASURE PLANNING
11. MODEL AND OPTION DEPENDENCIES
12. WARM-UP, ZEROING, AND METROLOGY PREREQUISITES
13. PERSISTENT SETTINGS / CALIBRATION SECURITY
14. ERROR-CODE KNOWLEDGE BASE
15. HARDWARE-TEST POLICY
16. COMMAND-LIKE REFERENCES REQUIRING PROGRAMMING GUIDE CONFIRMATION
17. PYMEASURE DESIGN IMPLICATIONS
18. DO-NOT-INFER LIST
19. OCR_AND_CONVERSION_NOTES
20. STEP 04 AND STEP 05 HANDOFF CHECKLIST

YAML front matter must include:

title:
source_file:
vendor:
model:
class_name:
instrument_type:
workflow_step: 03
source_role: "operator safety and operation planning"
command_inventory_created: false
command_syntax_authority: "programming_guide.md"
generated_on:
local_artifact: true
upstream_pr: false

LLM_AGENT_CONTRACT must state:

- Treat the instrument as safety-critical hardware.
- Use this file for operator safety, physical setup, and safe hardware-test planning.
- Do not use this file as a complete command inventory.
- Do not implement code from this file alone.
- Do not run hardware tests from this file alone.
- Do not enable source/output automatically in later tests without operator confirmation.
- Do not infer command syntax from front-panel or procedure names.
- Use Programming Guide for remote command syntax.
- Use Service Manual later for service/calibration risk and qualified-service-only procedures.

DOCUMENT ROLE IN PYMEASURE WORKFLOW must contain this table:

| File | Role | Not allowed |
|---|---|---|
| operator/operation manual | safety, operation, DUT setup, feature map, safe hardware-test policy | complete command inventory |
| operators_manual_llm.md | LLM/RAG planning aid for safety and operator workflow | driver implementation by itself |
| programming_guide.md | authoritative source for remote command syntax | physical setup rules unless stated |
| service_manual.md | service/calibration risk and qualified service boundaries | operator-safe assumptions |
| commands.txt | complete command inventory from Prompt 05 | invented commands |

QUICK FACTS FOR RETRIEVAL must list concise facts:

- instrument family,
- instrument type,
- output/input capability summary,
- supported interfaces if documented,
- local/remote operation modes if documented,
- warm-up requirement if documented,
- default power-up/reset state if documented,
- safety-critical notes,
- model/option limitations.

Do not invent missing values. Use not specified where needed.

SAFETY SUMMARY FOR DRIVER AND HARDWARE TEST PLANNING must classify each safety topic:

| Topic | Risk | PyMeasure implication | Hardware-test policy | Source evidence |
|---|---|---|---|---|

Use only these hardware-test policies:

- query-only
- output-off-only
- roundtrip-safe
- operator-confirmed-only
- protocol-only
- never
- needs-verification

Include documented risks such as hazardous voltage/current/power, protective earth, live terminals
in Operate, Standby/Reset before connections, DUT protection, cooling, overload/reverse-power
protection, and qualified-service-only boundaries.

REMOTE OPERATION AND INTERFACE SUMMARY must list only interfaces confirmed in INPUT_FILE.

| Interface | Confirmed? | Setup facts | Termination/EOL | Remote/local notes | Source evidence | Notes |
|---|---:|---|---|---|---|---|

If a resource string or exact setting is not documented, write:

not specified

Do not invent USB VID/PID, TCP ports, baud rates, or terminators.

REMOTE PORT SETUP FACTS must use:

| Interface | Setting | Values/defaults from manual | PyMeasure implication | Source evidence | Notes |
|---|---|---|---|---|---|

OPERATE / STANDBY / RESET BEHAVIOR must include:

- Operate mode,
- Standby mode,
- reset or power-up state,
- automatic transitions to Standby,
- conditions that force Standby,
- output-enable behavior,
- safe final-state candidate.

Include this policy statement exactly:

Output-enable or Operate actions must not be used in broad automated hardware tests.
They require operator-confirmed-only policy unless a later human-approved test scope defines
safe load, wiring, range, and final state.

DUT CONNECTION AND FIXTURE CONSTRAINTS must use:

| Function area | Required physical setup | Risk | Hardware-test policy | Source evidence | Notes |
|---|---|---|---|---|---|

OUTPUT / INPUT FUNCTION MAP FOR PYMEASURE PLANNING must use:

| Function group | Operator function | Availability | Main risks | PyMeasure planning note | Source evidence |
|---|---|---|---|---|---|

MODEL AND OPTION DEPENDENCIES must use:

| Model or option | Feature impact | PyMeasure implication | Hardware-test implication | Source evidence | Notes |
|---|---|---|---|---|---|

For the Fluke 5560A family, check references to:

- 5560A,
- 5550A,
- 5540A,
- 5530A,
- 52120A amplifier,
- scope options,
- dual output,
- inductance,
- thermocouple,
- RTD,
- power simulation,
- 600M,
- 1G,
- 2G.

WARM-UP, ZEROING, AND METROLOGY PREREQUISITES must use:

| Requirement | Condition | Driver implication | Hardware-test policy | Source evidence |
|---|---|---|---|---|

Do not turn zeroing, adjustment, or calibration into automatic tests.

PERSISTENT SETTINGS / CALIBRATION SECURITY must use:

| Topic | Risk | Command-like reference? | PyMeasure implication | Hardware-test policy | Source evidence |
|---|---|---|---|---|---|

If literal command names are mentioned, put them in the command-like reference section too.

ERROR-CODE KNOWLEDGE BASE must use:

| Code | Message | Category | PyMeasure implication | Suggested handling | Source evidence |
|---|---|---|---|---|---|

If the manual does not include a usable error-code table, write:

not found in operator/operation manual

Do not invent error codes.

HARDWARE-TEST POLICY must use:

| Test type | Allowed automatically? | Required preconditions | Required final state | Policy | Notes |
|---|---:|---|---|---|---|

Include relevant test types such as:

- identity/options query,
- error queue query,
- remote port readback,
- output configuration while in standby,
- low-level output,
- high-voltage output,
- high-current output,
- power simulation,
- resistance/capacitance/inductance output,
- RTD/TC output,
- TC measurement,
- external amplifier operation,
- scope outputs,
- overload tests,
- calibration security,
- zero adjustment,
- restore defaults,
- firmware update.

COMMAND-LIKE REFERENCES REQUIRING PROGRAMMING GUIDE CONFIRMATION must use:

| Token | Operator manual context | Found in Programming Guide? | Decision | Notes |
|---|---|---:|---|---|

Decision values:

- confirmed-by-programming-guide
- not-found-in-programming-guide
- programming-guide-missing
- needs-verification

Do not add these to any command inventory.

PYMEASURE DESIGN IMPLICATIONS must be concise and practical:

- likely use SCPIMixin, Instrument only if Programming Guide confirms common commands,
- do not use includeSCPI=True,
- do not create public get_* or set_* methods,
- output activation methods must be explicit and hardware tests must be safety-gated,
- source/output controls must be separated from output-enable actions,
- use safe final state such as Standby only if documented,
- command/query properties need validation from Programming Guide,
- model/option checks are needed before exposing option-dependent APIs,
- high-risk commands should be protocol-only, never, or operator-confirmed-only,
- hardware tests must skip without VISA address.

DO-NOT-INFER LIST must include:

- Do not infer command syntax from front-panel labels or procedure names.
- Do not infer query forms from natural-language descriptions.
- Do not infer output safety from low-level command names.
- Do not infer that a physical setup is safe without documented wiring and load.
- Do not infer model/option availability from one family member to another.
- Do not infer that service/calibration procedures are operator-safe.
- Do not treat command-like references as implemented API.

OCR_AND_CONVERSION_NOTES must be conservative.

Allowed wording:

- No obvious OCR artifacts detected in reviewed sections.
- Some sections may still require verification during later prompts.
- Safety-critical values must be checked against the official manual before real hardware tests.

Forbidden wording unless fully proven:

- No OCR errors detected.
- Documentation quality is high.
- Needs-verification items: none.

STEP 04 AND STEP 05 HANDOFF CHECKLIST must state:

- Step 04 must use Service Manual for service/calibration risk only.
- Step 04 must not infer operator-safe behavior from service procedures.
- Step 05 must use Programming Guide, not Operator Manual, for command inventory.
- Step 05 may use this file only for risk hints and hardware-test policy.
- Command-like references from this file must remain cross-references until confirmed.

============================================================
FORBIDDEN OUTPUT MEANINGS
============================================================

The output file and report must not claim or imply any of these meanings:

- all commands have been extracted,
- all SCPI commands have been extracted,
- OCR is perfect,
- there are certainly no needs-verification items,
- the next step is driver implementation,
- the next step is protocol implementation,
- it is safe to enable output automatically,
- output tests can run automatically,
- calibration can run automatically,
- service procedures are operator-safe.

The phrase complete command inventory is allowed only when saying that the Operator/Operation Manual
is not the complete command inventory source, or that Prompt 05 creates it from the Programming Guide.

============================================================
MANDATORY FINAL REPORT FILE
============================================================

Always create or update REPORT_FILE.

The report file must be created even if the step fails.

If OUTPUT_FILE is created but REPORT_FILE is missing, the step is FAIL.

The final report must contain these exact fields:

STATUS: PASS or FAIL
HUMAN_REQUIRED: yes or no
STEP_ID: 03
STEP_NAME: optimize_operator_manual_for_llm
CONFIG_FILE:
INPUT_CANDIDATES_CHECKED:
INPUT_FILE_USED:
FILES_CREATED_OR_UPDATED:
COMMANDS_RUN:
ACCEPTANCE_RESULTS:
COUNTS:
NEEDS_VERIFICATION_ITEMS:
COMMAND_LIKE_REFERENCE_CHECK:
FORBIDDEN_MEANING_CHECK:
REPORT_CONSISTENCY_CHECK:
SOURCE_INTEGRITY_CHECK:
ALLOWED_PATH_CHECK:
PYMEASURE_AGENTS_COMPLIANCE:
BLOCKERS:
NEXT_RECOMMENDED_STEP:

Human-required policy for this step:

- Use HUMAN_REQUIRED: no if all required files exist, no blockers remain, source files are unchanged,
  and any unresolved items are explicitly deferred to Prompt 04 or Prompt 05.
- Use HUMAN_REQUIRED: yes only if the operator must act before Step 04 can run.
- If STATUS: PASS and BLOCKERS: None, then HUMAN_REQUIRED must normally be no.
- If HUMAN_REQUIRED: yes appears with STATUS: PASS, the report must include a concrete operator action
  that is required before Step 04. Otherwise set HUMAN_REQUIRED: no.

Needs-verification reporting policy:

- If any command-like reference has Decision = needs-verification, then NEEDS_VERIFICATION_ITEMS must
  list it explicitly.
- Do not write "None" or "0" for needs-verification when any needs-verification item exists elsewhere
  in the report.
- Items that can be handled automatically by Prompt 04 or Prompt 05 may be listed as deferred, not as
  blockers.
- If a contradiction appears between COUNTS, NEEDS_VERIFICATION_ITEMS, and COMMAND_LIKE_REFERENCE_CHECK,
  set STATUS: FAIL.

Command-like reference counting policy:

- The reported number of command-like references must match the number of rows in the
  COMMAND-LIKE REFERENCES REQUIRING PROGRAMMING GUIDE CONFIRMATION table, excluding the header row.
- If the count does not match, set STATUS: FAIL.

Source integrity policy:

- Source manuals must be unchanged after this step.
- If git diff --name-only includes INPUT_FILE, PROGRAMMING_GUIDE, SERVICE_MANUAL, or any
  operator_manual_candidates path, set STATUS: FAIL.
- If source-file hash before/after differs, set STATUS: FAIL.
- If report lists any source manual in FILES_CREATED_OR_UPDATED or ALLOWED_PATH_CHECK modified paths,
  set STATUS: FAIL.

The only valid next-step recommendation is:

Proceed to Step 04: optimize Service Manual for service/calibration-risk planning.

If no service manual is available, recommend:

Proceed to Step 04 and mark it as skipped only after checking config.manuals.service_manual.

Use STATUS: FAIL if:

- CONFIG_FILE is missing,
- no operator/operation manual candidate exists,
- OUTPUT_FILE was not created when input exists,
- REPORT_FILE was not created,
- files outside allowed scope were modified,
- any source manual was modified,
- any forbidden meaning appears,
- command-like references are treated as command inventory,
- output claims complete command extraction,
- output claims output-enable tests are safe automatically,
- git diff --check reports whitespace errors,
- next-step recommendation skips to implementation,
- terminal execution is blocked,
- report says the output was merely copied instead of transformed,
- STATUS/HUMAN_REQUIRED/BLOCKERS are inconsistent,
- needs-verification reporting is inconsistent,
- command-like reference count is inconsistent.

============================================================
ACCEPTANCE COMMANDS
============================================================

Run in PowerShell. Use values from CONFIG_FILE, not hard-coded vendor/model paths.

POWERSHELL_ACCEPTANCE_START

$configPath = "assets/workflow_prompts/workflow_config.json"
$config = Get-Content $configPath -Raw | ConvertFrom-Json
$assetDir = $config.asset_dir
$output = "$assetDir/operators_manual_llm.md"
$reportDir = $config.workflow_reports_dir
$report = "$reportDir/03_optimize_operator_manual_for_llm_report.md"

Test-Path $configPath

foreach ($candidate in $config.manuals.operator_manual_candidates) {
    $exists = Test-Path $candidate
    Write-Output ("{0}: {1}" -f $exists, $candidate)
}

Test-Path $output
Test-Path $report

Get-Content $output -TotalCount 180
Get-Content $report -TotalCount 180

Select-String -Path $output -Pattern `
  "LLM_AGENT_CONTRACT", `
  "SAFETY SUMMARY FOR DRIVER AND HARDWARE TEST PLANNING", `
  "REMOTE OPERATION AND INTERFACE SUMMARY", `
  "OPERATE / STANDBY / RESET BEHAVIOR", `
  "DUT CONNECTION AND FIXTURE CONSTRAINTS", `
  "HARDWARE-TEST POLICY", `
  "COMMAND-LIKE REFERENCES REQUIRING PROGRAMMING GUIDE CONFIRMATION", `
  "STEP 04 AND STEP 05 HANDOFF CHECKLIST"

Select-String -Path $output -Pattern `
  "operator-confirmed-only", `
  "protocol-only", `
  "never", `
  "Programming Guide confirmation", `
  "Do not infer command syntax"

Select-String -Path $report -Pattern `
  "Copied operators_guide.md to operators_manual_llm.md", `
  "HUMAN_REQUIRED: yes", `
  "Needs-verification items: 0", `
  "NEEDS_VERIFICATION_ITEMS:\s*None"

$changed = git diff --name-only
$changed

$allowed = @(
  "$assetDir/operators_manual_llm.md",
  "$reportDir/03_optimize_operator_manual_for_llm_report.md"
)

$sourceFiles = @()
if ($config.manuals.programming_guide) {
    $sourceFiles += $config.manuals.programming_guide
}
if ($config.manuals.service_manual) {
    $sourceFiles += $config.manuals.service_manual
}
foreach ($candidate in $config.manuals.operator_manual_candidates) {
    $sourceFiles += $candidate
}
$sourceFiles = $sourceFiles | Select-Object -Unique

$unexpected = $changed | Where-Object { $allowed -notcontains $_ }

if ($unexpected) {
    Write-Output "UNEXPECTED_CHANGED_PATHS:"
    $unexpected
}

$changedSources = $changed | Where-Object { $sourceFiles -contains $_ }

if ($changedSources) {
    Write-Output "SOURCE_MANUALS_CHANGED:"
    $changedSources
}

git status --short
git diff --check
git diff --stat

POWERSHELL_ACCEPTANCE_END

Important interpretation:

- Test-Path $configPath must be True.
- At least one operator manual candidate must be True.
- Test-Path $output must be True.
- Test-Path $report must be True.
- UNEXPECTED_CHANGED_PATHS must not appear.
- SOURCE_MANUALS_CHANGED must not appear.
- If the report still contains "Copied operators_guide.md to operators_manual_llm.md", set STATUS: FAIL.
- If the report has STATUS: PASS and HUMAN_REQUIRED: yes without a required action before Step 04, set STATUS: FAIL.
- If report file is missing, set STATUS: FAIL.

============================================================
FINAL CHAT RESPONSE
============================================================

At the end, report in chat:

1. config file path,
2. input candidates checked,
3. input file used,
4. output file path,
5. report file path,
6. whether command-like references were isolated,
7. highest-risk hardware-test topics,
8. remote interfaces found,
9. model/option dependencies found,
10. any uncertainty or needs-verification,
11. forbidden meaning check result,
12. report consistency check result,
13. source integrity check result,
14. allowed path check result,
15. whether report file exists,
16. result of git diff --check,
17. result of git diff --stat,
18. STATUS: PASS or STATUS: FAIL,
19. HUMAN_REQUIRED: yes/no.
