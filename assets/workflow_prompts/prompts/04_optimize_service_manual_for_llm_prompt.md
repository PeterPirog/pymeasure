# Prompt 04 - Optimize Service Manual for LLM and PyMeasure service-risk planning

Version: v5 - execution-first, config-driven, source-readonly, prompt-maintenance-aware

WORK IN THE LOCAL PYMEASURE REPOSITORY.

EXECUTION MODE REQUIRED.
Apply file changes directly. Do not only describe steps. Do not only return snippets.

IMPORTANT:
Do not reformat this prompt. Do not escape underscores. Do not modify source manuals.

CONFIG_FILE = assets/workflow_prompts/workflow_config.json

Read CONFIG_FILE. It is the only source of vendor/model/path information.
Use:
- config.vendor
- config.model
- config.class_name
- config.instrument_type
- config.asset_dir
- config.manuals.programming_guide
- config.manuals.operator_manual_candidates
- config.manuals.service_manual
- config.workflow_reports_dir

Derived paths:
SERVICE_MANUAL = config.manuals.service_manual
PROGRAMMING_GUIDE = config.manuals.programming_guide
OUTPUT_FILE = config.asset_dir + "/service_manual_llm.md"
REPORT_FILE = config.workflow_reports_dir + "/04_optimize_service_manual_for_llm_report.md"
PROMPT_FILE = assets/workflow_prompts/prompts/04_optimize_service_manual_for_llm_prompt.md

Allowed changed paths for this step:
- OUTPUT_FILE
- REPORT_FILE
- PROMPT_FILE only when it was intentionally updated by the operator before running this step

PROMPT_FILE policy:
If PROMPT_FILE is modified, do not fail only because of that.
Record it as:
PROMPT_MAINTENANCE: present, non-blocking
This is acceptable only if no source manual, driver file, test file, docs file, commands.txt, or
command_coverage.md changed.

Read-only source manuals:
- SERVICE_MANUAL
- PROGRAMMING_GUIDE
- all config.manuals.operator_manual_candidates

If any source manual changes, STATUS must be FAIL.

Physical instrument access required: NO.
Do not use VISA or real hardware.
Do not modify pymeasure/instruments/, tests/, docs/, commands.txt, or command_coverage.md.

Recommended model:
- hal/qwen3-coder-next:cloud for execution
- hal/kimi-k2.6:cloud for long-context reading if needed

MANDATORY EXECUTION ORDER

1. Read CONFIG_FILE.
2. Create config.workflow_reports_dir if missing.
3. Immediately create provisional REPORT_FILE with:
   STATUS: FAIL
   HUMAN_REQUIRED: yes
   STEP_ID: 04
   STEP_NAME: optimize_service_manual_for_llm
   BLOCKERS: provisional report created, final report not written yet
4. Confirm SERVICE_MANUAL exists.
5. If SERVICE_MANUAL is missing:
   - do not create OUTPUT_FILE
   - overwrite REPORT_FILE with STATUS: FAIL and HUMAN_REQUIRED: yes
   - explain missing service manual
   - stop
6. Immediately create OUTPUT_FILE with all required top-level headings before doing detailed extraction.
7. Fill OUTPUT_FILE from SERVICE_MANUAL.
8. Run acceptance checks.
9. Overwrite REPORT_FILE with final PASS or FAIL.
10. Do not stop after the provisional report.
11. Final report must never contain "generation in progress".

PRIMARY GOAL

Create service_manual_llm.md as an LLM/PyMeasure service-risk knowledge base.

It is not command inventory. It is not driver code.
It is used to mark service-only, calibration-risk, NVM-risk, destructive, persistent-state,
long-running, covers-open, qualified-service-only, and fixture-dependent topics before later driver
implementation.

Use the Service Manual for service-risk classification only.
Use the Programming Guide only to confirm command-like tokens if available.
Do not infer command syntax from the Service Manual.

OUTPUT_FILE REQUIRED STRUCTURE

Create service_manual_llm.md with exactly these top-level sections:

1. YAML front matter
2. LLM_AGENT_CONTRACT
3. DOCUMENT ROLE IN PYMEASURE WORKFLOW
4. QUICK FACTS FOR RETRIEVAL
5. SERVICE SAFETY SUMMARY
6. SERVICE-ONLY PROCEDURES
7. CALIBRATION / ADJUSTMENT / NVM RISK
8. VERIFICATION PREREQUISITES
9. DIAGNOSTIC / SELF-TEST / LONG-RUNNING PROCEDURES
10. DESTRUCTIVE OR PERSISTENT-STATE ACTIONS
11. MODEL AND OPTION DEPENDENCIES
12. FIXTURE AND EQUIPMENT REQUIREMENTS
13. COMMAND-LIKE TOKENS REQUIRING PROGRAMMING GUIDE CONFIRMATION
14. HARDWARE-TEST EXCLUSION LIST
15. PYMEASURE API DECISION RULES
16. DO-NOT-INFER LIST
17. OCR_AND_CONVERSION_NOTES
18. STEP 05 HANDOFF CHECKLIST

YAML front matter must include:
title:
source_file:
vendor:
model:
class_name:
instrument_type:
workflow_step: 04
source_role: "service risk and calibration boundary planning"
command_inventory_created: false
command_syntax_authority: "programming_guide.md"
generated_on:
local_artifact: true
upstream_pr: false

LLM_AGENT_CONTRACT must state:
- Treat the instrument as safety-critical and metrology-critical hardware.
- Do not use this file as command inventory.
- Do not implement code from this file alone.
- Do not run hardware tests from this file alone.
- Do not run service, calibration, adjustment, NVM, passcode, firmware, covers-open, or destructive procedures automatically.
- Use Programming Guide for command syntax.
- Use Operator Manual for operator-safe physical setup.
- Service-only procedures require qualified personnel and are not normal PyMeasure hardware tests.

Allowed risk values:
operator-safe, fixture-dependent, hazardous-output, service-only, calibration-risk, destructive,
persistent-state, long-running, needs-verification

Allowed hardware-test policies:
query-only, output-off-only, roundtrip-safe, operator-confirmed-only, protocol-only, never,
needs-verification

Required table formats:

SERVICE SAFETY SUMMARY:
| Topic | Risk value | Risk description | PyMeasure implication | Hardware-test policy | Source evidence |

SERVICE-ONLY PROCEDURES:
| Procedure or topic | Service-only reason | Required qualification / equipment | PyMeasure implication | Hardware-test policy | Source evidence |

CALIBRATION / ADJUSTMENT / NVM RISK:
| Topic | Risk | Persistent state affected? | Calibration constants affected? | PyMeasure implication | Hardware-test policy | Source evidence |

VERIFICATION PREREQUISITES:
| Verification topic | Required prerequisite | Equipment / fixture | Model or option scope | PyMeasure implication | Hardware-test policy | Source evidence |

DIAGNOSTIC / SELF-TEST / LONG-RUNNING PROCEDURES:
| Procedure | Duration / blocking risk | State risk | PyMeasure implication | Hardware-test policy | Source evidence |

DESTRUCTIVE OR PERSISTENT-STATE ACTIONS:
| Action | Destructive or persistent effect | Reversibility | PyMeasure implication | Hardware-test policy | Source evidence |

MODEL AND OPTION DEPENDENCIES:
| Model or option | Feature impact | Service-risk impact | PyMeasure implication | Hardware-test implication | Source evidence |

FIXTURE AND EQUIPMENT REQUIREMENTS:
| Procedure area | Required equipment / fixture | Why required | PyMeasure implication | Hardware-test policy | Source evidence |

COMMAND-LIKE TOKENS REQUIRING PROGRAMMING GUIDE CONFIRMATION:
| Token | Service manual context | Found in Programming Guide? | Decision | Notes |

Allowed Decision values:
confirmed-by-programming-guide, not-found-in-programming-guide, programming-guide-missing,
needs-verification

HARDWARE-TEST EXCLUSION LIST:
| Excluded topic | Reason for exclusion | Scope | Suggested safer alternative | Source evidence |

PYMEASURE API DECISION RULES must include:
- Service procedures must not become normal public driver APIs unless explicitly designed and approved.
- Calibration, adjustment, NVM, firmware, passcode, destructive, and service-only actions should normally be omitted, protocol-only, private, or operator-confirmed-only.
- Query-only service/status info may be exposed only if Programming Guide confirms syntax.
- Hardware tests must skip without VISA address.
- Hardware tests must not run service/calibration/destructive commands automatically.
- Hardware tests must leave instrument in safe final state and query documented error queue.
- Use Programming Guide for validators, values, ranges, command/query forms, and responses.
- Do not use includeSCPI=True.
- Do not create public get_* or set_* methods.

DO-NOT-INFER LIST must include:
- Do not infer command syntax from service procedure names.
- Do not infer query forms from service tables.
- Do not infer that service procedures are operator-safe.
- Do not infer that calibration or verification can be automated safely.
- Do not infer ranges/tolerances unless documented.
- Do not infer model/option support from another family member.
- Do not treat command-like service tokens as implemented API.
- Do not treat service verification as PyMeasure hardware test coverage.

STEP 05 HANDOFF CHECKLIST must state:
- Step 05 must use Programming Guide, not Service Manual, for complete command inventory.
- Step 05 may use this file only for risk hints, exclusion rules, and command-like token cross-references.
- Calibration, NVM, destructive, and service-only items must be restrictive in command coverage.
- Service-only and calibration-risk commands must not be implemented in early batches.

FORBIDDEN OUTPUT MEANINGS

The output and report must not claim:
- all commands extracted
- OCR is perfect
- no needs-verification items unless fully proven
- next step is driver or protocol implementation
- service procedures are operator-safe
- calibration, adjustment, NVM, firmware, or covers-open procedures can run automatically

FINAL REPORT REQUIRED FIELDS

REPORT_FILE must contain:

STATUS: PASS or FAIL
HUMAN_REQUIRED: yes or no
STEP_ID: 04
STEP_NAME: optimize_service_manual_for_llm
CONFIG_FILE:
INPUT_FILE_USED:
FILES_CREATED_OR_UPDATED:
COMMANDS_RUN:
ACCEPTANCE_RESULTS:
COUNTS:
NEEDS_VERIFICATION_ITEMS:
COMMAND_LIKE_TOKEN_CHECK:
SERVICE_ONLY_CLASSIFICATION_CHECK:
CALIBRATION_NVM_RISK_CHECK:
HARDWARE_TEST_EXCLUSION_CHECK:
FORBIDDEN_MEANING_CHECK:
REPORT_CONSISTENCY_CHECK:
SOURCE_INTEGRITY_CHECK:
LINE_ENDING_WARNING:
PROMPT_MAINTENANCE:
ALLOWED_PATH_CHECK:
PYMEASURE_AGENTS_COMPLIANCE:
BLOCKERS:
NEXT_RECOMMENDED_STEP:

HUMAN_REQUIRED policy:
Use HUMAN_REQUIRED: no if files exist, no blockers remain, source files are unchanged, and unresolved
items are deferred to Step 05 or later human-approved hardware planning.
Use HUMAN_REQUIRED: yes only if the operator must act before Step 05.

Next step must be exactly:
Proceed to Step 05: extract complete command inventory from Programming Guide into commands.txt.

STATUS must be FAIL if:
- CONFIG_FILE is missing
- SERVICE_MANUAL is missing
- OUTPUT_FILE is missing
- REPORT_FILE is missing
- final report still says generation in progress
- files outside allowed scope changed, except PROMPT_FILE under PROMPT_MAINTENANCE policy
- any source manual changed
- source-file hash changed
- any file under pymeasure/instruments/, tests/, or docs/ changed
- commands.txt or command_coverage.md changed
- command-like tokens are treated as command inventory
- service/calibration/NVM/destructive actions are not excluded from normal hardware tests
- output claims service/calibration/destructive actions are safe automatically
- report says output was merely copied
- STATUS/HUMAN_REQUIRED/BLOCKERS are inconsistent
- next step skips to implementation
- terminal execution is blocked
- git diff --check exits nonzero or reports real whitespace errors

Windows line-ending warning policy:
If git diff --check exits with code 0 and only LF/CRLF warnings appear, do not fail.
Record LINE_ENDING_WARNING: present, non-blocking.

ACCEPTANCE COMMANDS

Run equivalent PowerShell using CONFIG_FILE:

POWERSHELL_ACCEPTANCE_START
$configPath = "assets/workflow_prompts/workflow_config.json"
$config = Get-Content $configPath -Raw | ConvertFrom-Json
$assetDir = $config.asset_dir
$output = "$assetDir/service_manual_llm.md"
$reportDir = $config.workflow_reports_dir
$report = "$reportDir/04_optimize_service_manual_for_llm_report.md"
$promptFile = "assets/workflow_prompts/prompts/04_optimize_service_manual_for_llm_prompt.md"

Test-Path $configPath
Test-Path $config.manuals.service_manual
Test-Path $output
Test-Path $report

Get-Content $output -TotalCount 120
Get-Content $report -TotalCount 180

Select-String -Path $output -Pattern "LLM_AGENT_CONTRACT","SERVICE SAFETY SUMMARY","SERVICE-ONLY PROCEDURES","CALIBRATION / ADJUSTMENT / NVM RISK","VERIFICATION PREREQUISITES","HARDWARE-TEST EXCLUSION LIST","STEP 05 HANDOFF CHECKLIST"
Select-String -Path $output -Pattern "service-only","calibration-risk","persistent-state","destructive","never","protocol-only","Programming Guide confirmation"
Select-String -Path $report -Pattern "generation in progress","Copied service_manual.md to service_manual_llm.md","HUMAN_REQUIRED: yes","Needs-verification items: 0","NEEDS_VERIFICATION_ITEMS:\s*None"

$changed = @()
$changed += git diff --name-only
$changed += git diff --name-only --cached
$changed = $changed | Where-Object { $_ } | Select-Object -Unique
$changed

$allowed = @("$assetDir/service_manual_llm.md","$reportDir/04_optimize_service_manual_for_llm_report.md","$promptFile")

$sourceFiles = @()
if ($config.manuals.programming_guide) { $sourceFiles += $config.manuals.programming_guide }
if ($config.manuals.service_manual) { $sourceFiles += $config.manuals.service_manual }
foreach ($candidate in $config.manuals.operator_manual_candidates) { $sourceFiles += $candidate }
$sourceFiles = $sourceFiles | Select-Object -Unique

$forbiddenProjectAreas = @("pymeasure/instruments/","tests/","docs/")
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

$changedProjectFiles = $changed | Where-Object {
    ($_ -like "pymeasure/instruments/*") -or
    ($_ -like "tests/*") -or
    ($_ -like "docs/*") -or
    ($_ -like "*/commands.txt") -or
    ($_ -like "*/command_coverage.md")
}
if ($changedProjectFiles) {
    Write-Output "FORBIDDEN_PROJECT_FILES_CHANGED:"
    $changedProjectFiles
}

if ($changed -contains $promptFile) {
    Write-Output "PROMPT_MAINTENANCE_PRESENT:"
    $promptFile
    Write-Output "PROMPT_MAINTENANCE_POLICY: non-blocking for this step"
}

git status --short

Write-Output "GIT_DIFF_CHECK_OUTPUT:"
$diffCheckOutput = git diff --check 2>&1
$diffCheckExitCode = $LASTEXITCODE
$diffCheckOutput
Write-Output ("GIT_DIFF_CHECK_EXIT_CODE: {0}" -f $diffCheckExitCode)

git diff --stat
POWERSHELL_ACCEPTANCE_END

Important interpretation:
- Test-Path $output must be True.
- Test-Path $report must be True.
- UNEXPECTED_CHANGED_PATHS may include only PROMPT_FILE, OUTPUT_FILE, and REPORT_FILE.
- SOURCE_MANUALS_CHANGED must not appear.
- FORBIDDEN_PROJECT_FILES_CHANGED must not appear.
- PROMPT_MAINTENANCE_PRESENT is non-blocking if only PROMPT_FILE is listed outside artifacts.
- If final report has PASS, HUMAN_REQUIRED no, source integrity PASS, and blockers None, Step 04 passes.

FINAL CHAT RESPONSE:
Report input file, output file, report file, service-only topics, calibration/NVM risks,
hardware-test exclusions, source integrity, prompt maintenance status, allowed path check,
git diff --check exit code, git diff --stat, STATUS, and HUMAN_REQUIRED.
