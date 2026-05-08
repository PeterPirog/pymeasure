# Prompt 04 - Create LLM-optimized Service Manual risk artifact for PyMeasure

Version: v8 - output-required, no-provisional-report-first, dictionary-validated

WORK IN THE LOCAL PYMEASURE REPOSITORY.

EXECUTION MODE REQUIRED.
Apply file changes directly. Do not only describe steps. Do not only return snippets.

IMPORTANT:
Do not reformat this prompt.
Do not escape underscores.
Do not modify source manuals.

CONFIG_FILE = assets/workflow_prompts/workflow_config.json

Read CONFIG_FILE and use it as the only source of paths and metadata.

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
- SERVICE_MANUAL = config.manuals.service_manual
- PROGRAMMING_GUIDE = config.manuals.programming_guide
- OUTPUT_FILE = config.asset_dir + "/service_manual_llm.md"
- REPORT_FILE = config.workflow_reports_dir + "/04_optimize_service_manual_for_llm_report.md"
- PROMPT_FILE = assets/workflow_prompts/prompts/04_optimize_service_manual_for_llm_prompt.md

Allowed changed paths:
- OUTPUT_FILE
- REPORT_FILE
- PROMPT_FILE only if it was intentionally updated before this run

Read-only source manuals:
- SERVICE_MANUAL
- PROGRAMMING_GUIDE
- every path in config.manuals.operator_manual_candidates

Forbidden changes:
- source manuals
- pymeasure/instruments/
- tests/
- docs/
- commands.txt
- command_coverage.md

Physical instrument access required: NO.
Do not use VISA or real hardware.

Recommended execution model:
- hal/qwen3-coder-next:cloud

CRITICAL EXECUTION RULE

Do not create REPORT_FILE first.
The first generated artifact must be OUTPUT_FILE.
If SERVICE_MANUAL exists, create OUTPUT_FILE before writing REPORT_FILE.
Never leave only REPORT_FILE without OUTPUT_FILE.

MANDATORY EXECUTION ORDER

1. Read CONFIG_FILE.
2. Confirm SERVICE_MANUAL exists.
3. If SERVICE_MANUAL is missing:
   - create REPORT_FILE with STATUS: FAIL
   - do not create OUTPUT_FILE
   - stop
4. Create OUTPUT_FILE immediately.
5. Fill OUTPUT_FILE by transforming SERVICE_MANUAL into a service-risk artifact.
6. Use PROGRAMMING_GUIDE only to confirm command-like tokens if available.
7. Run acceptance checks.
8. Create or overwrite REPORT_FILE with final PASS or FAIL.
9. Final report must not contain "provisional", "pending", or "generation in progress".

PRIMARY GOAL

Create service_manual_llm.md as an LLM/PyMeasure service-risk knowledge base.

It is not command inventory.
It is not driver code.

Use it to classify:
- service-only procedures
- calibration-risk procedures
- adjustment procedures
- NVM / persistent-state risks
- passcode/security risks
- destructive operations
- long-running operations
- covers-open/internal-access procedures
- qualified-service-only procedures
- fixture-dependent verification procedures
- model and option dependencies
- command-like tokens requiring Programming Guide confirmation

Do not infer remote command syntax from the Service Manual.
Do not treat service procedures as operator-safe.
Do not implement driver code.

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

REQUIRED TABLES

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
- confirmed-by-programming-guide
- not-found-in-programming-guide
- programming-guide-missing
- needs-verification

Do not use any other Decision value.
Do not write misspellings such as needs-veribration.
If any Decision value is outside the allowed set, set STATUS: FAIL.

HARDWARE-TEST EXCLUSION LIST:
| Excluded topic | Reason for exclusion | Scope | Suggested safer alternative | Source evidence |

PYMEASURE API DECISION RULES must include:
- Service procedures must not become normal public driver APIs unless explicitly designed and approved.
- Calibration, adjustment, NVM, firmware, passcode, destructive, and service-only actions should normally be omitted, protocol-only, private, or operator-confirmed-only.
- Query-only service/status information may be exposed only if Programming Guide confirms syntax.
- Hardware tests must skip without VISA address.
- Hardware tests must not run service/calibration/destructive commands automatically.
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

OCR_AND_CONVERSION_NOTES must be conservative:
- Mention OCR or conversion ambiguity if visible.
- Do not claim OCR is perfect.
- Do not use service-manual numeric tolerances as driver validators without Programming Guide confirmation.

STEP 05 HANDOFF CHECKLIST must state:
- Step 05 must use Programming Guide, not Service Manual, for complete command inventory.
- Step 05 may use this file only for risk hints, exclusion rules, and command-like token cross-references.
- Calibration, NVM, destructive, and service-only items must be restrictive in command coverage.
- Service-only and calibration-risk commands must not be implemented in early batches.

MINIMUM CONTENT REQUIREMENTS FOR PASS

OUTPUT_FILE must contain extracted content, not only headings.

Minimum acceptable counts:
- at least 5 rows in SERVICE SAFETY SUMMARY
- at least 3 rows in SERVICE-ONLY PROCEDURES
- at least 3 rows in CALIBRATION / ADJUSTMENT / NVM RISK
- at least 3 rows in VERIFICATION PREREQUISITES
- at least 3 rows in HARDWARE-TEST EXCLUSION LIST
- at least 3 command-like tokens or explicit statement that none were found

If any minimum count is not met, still create OUTPUT_FILE, but set STATUS: FAIL.

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
DECISION_VALUE_CHECK:
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
- final report says provisional, pending, or generation in progress
- OUTPUT_FILE is only a skeleton with no extracted service-risk rows
- minimum content requirements are not met
- files outside allowed scope changed, except PROMPT_FILE under PROMPT_MAINTENANCE policy
- any source manual changed
- any file under pymeasure/instruments/, tests/, docs/, commands.txt, or command_coverage.md changed
- command-like tokens are treated as command inventory
- any Decision value in COMMAND-LIKE TOKENS table is outside the allowed set
- any misspelled Decision value such as needs-veribration appears
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
Select-String -Path $report -Pattern "provisional","pending","generation in progress","Copied service_manual.md to service_manual_llm.md","HUMAN_REQUIRED: yes","Needs-verification items: 0","NEEDS_VERIFICATION_ITEMS:\\s*None"
Select-String -Path $output,$report -Pattern "needs-veribration"

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

FINAL CHAT RESPONSE:
Report input file, output file, report file, service-only topics, calibration/NVM risks,
hardware-test exclusions, source integrity, prompt maintenance status, allowed path check,
decision value check, git diff --check exit code, git diff --stat, STATUS, and HUMAN_REQUIRED.
