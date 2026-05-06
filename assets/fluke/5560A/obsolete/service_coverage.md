# Fluke 5560A — service_coverage.md

## Service manual metadata

- vendor: fluke
- model: 5560A
- class name: Fluke5560A
- instrument type: multifunction precision calibrator
- service manual path: assets/fluke/5560A/service_manual.md
- source manual revision: September 2023 Rev. 2, 9/25
- generated on: 2026-05-06 10:59
- scope: safety, calibration/adjustment risk, hardware-test policy, fixtures/equipment
- note: command syntax authority remains `programming_guide.md` only.

## Safety classification

| Area | Manual section | Operator-safe | Service-only | Hazard | Driver implication | Hardware-test implication | Notes |
|---|---|---|---|---|---|---|---|
| Identity/status/error queries | #5 Hardware-test policy (`query-only`) | yes | no | low | Keep as measurement/query methods. | query-only | Safe diagnostic telemetry without output enable. |
| Output enable and sourcing (V/A/power) | #1 Quick facts + #3 service-risk classification | no | no | hazardous-output | Expose as explicit methods/properties with strong safeguards. | operator-confirmed-only | Up to 1020 V and 30.2 A; simulated power up to 30.9 kW. |
| Calibration/adjustment workflows | #3 service-risk classification, #4 API decision rules | no | yes | calibration / adjustment | Mark as deferred or explicit service methods only. | never | Passcode-protected, may store correction factors in NVM. |
| Internal maintenance/disassembly/fuse/test points | LLM_AGENT_CONTRACT + routing map (maintenance/parts) | no | yes | service-only | No driver API for internal operations. | never | Cover removal/internal voltages are out of scope for driver automation. |
| Guard/ground dependent functions | #3 service-risk classification | conditional | no | unknown (fixture-dependent) | Require fixture notes in API docs/tests. | needs-fixture-or-load | Capacitance/inductance and similar routines require explicit wiring policy. |
| Warm-up / verification readiness | #2 routing map + warm-up references | yes | no | cautious-state-change | Provide precondition notes (not hidden automation). | needs-verification | Warm-up and environment prerequisites must be satisfied before verification. |

## Service procedures

| Procedure | Manual section | Requires cover removal | Requires calibration equipment | Affects calibration | Affects NVM/logs/files | Remote command known? | Related command | Policy | Notes |
|---|---|---|---|---|---|---|---|---|---|
| Warm-up before verification | Warmup Procedure / verification prerequisites | no | yes | maybe | no | no | n/a | needs-verification | Minimum warm-up depends on context (30 min / up to 2 h in noted conditions). |
| Total zero / verification preparation | Calibration and Verification sections | no | yes | yes | maybe | partial | ZERO_MEAS / ZERO_MEAS? | protocol-only | Treat as explicit maintenance action, not implicit in normal driver flow. |
| Adjustment sequence (ADJ_*) | Adjustment sections | no | yes | yes | yes | yes | ADJ_START, ADJ_NEXT, ADJ_ABORT, ADJ_RETRY, ADJ_*? | never | Service workflow, correction factors/state impact. |
| Calibration security and passcode | Calibration security sections | no | yes | yes | yes | yes | CAL_SECURE, CAL_PASSCODE, CAL_INTV | never | Access control + calibration-state modifications. |
| Diagnostic/self-test runs | Diagnostic/service sections | no | maybe | no | maybe | yes | DIAG, DIAG_FAULT, *TST? | protocol-only | May be long-running and unsuitable for broad hardware CI. |
| Internal repair/replaceable parts/fuse work | Maintenance/replaceable parts | yes | yes | maybe | maybe | no | n/a | never | Internal service procedure only; exclude from remote automation. |

## Service-related remote commands

| Command | Form | Source in Programming Guide | Related service procedure | Risk level | PyMeasure policy | Hardware-test policy | Notes |
|---|---|---|---|---|---|---|---|
| ADJ_* | command/query mix | yes (atomic command reference) | Adjustment workflow | adjustment | not-implemented or explicit service method | never | Service/calibration workflow only. |
| CAL_SECURE / CAL_PASSCODE | command/query + command only | yes | Calibration security/unsecure | factory/service | not-implemented or explicit service method | never | Protected calibration-state operations. |
| CAL_INTV / CAL_INTV? | command/query | yes | Verification interval configuration | cautious-state-change | deferred unless explicitly requested | operator-confirmed-only | Changes maintenance/verification regime. |
| ZERO_MEAS / ZERO_MEAS? | command/query | yes | Verification preparation / zeroing cadence | long-running | explicit method only if needed | protocol-only | Treat as maintenance function with preconditions. |
| DIAG / DIAG_FAULT / *TST? | command/query + query | yes | Service diagnostics | long-running | explicit method, no broad automatic hw runs | protocol-only | Potentially lengthy; keep out of default hardware tests. |
| OPER / OUT / BOOST | command/query | yes | Output operation (hazard path) | hazardous-output | explicit API with safety wording | operator-confirmed-only | Never run unattended due to voltage/current/power risk. |
| STBY | command only | yes | Safe-state recovery | cautious-state-change | keep as explicit safe-state method | output-off-only | Prefer as teardown/final-state command. |
| COMM_* / ADDR / IPADDR / DHCP / GWADDR / SUBNETMASK / ENETPORT | command/query | yes | Interface/network service config | network/address-affecting | include with caution and clear notes | operator-confirmed-only | Can disrupt remote connectivity/test session addressing. |

## Do-not-automate list

| Item | Reason | Allowed only if | Notes |
|---|---|---|---|
| Calibration adjustment and correction-factor storage | Alters calibration state and can write NVM | operator explicitly requests service routine with full procedure | Includes ADJ_* and secured calibration workflows. |
| Internal maintenance (cover removal, fuse, test points, replacement) | Electrical/service hazard, not remote driver scope | manual service execution by qualified personnel | Excluded from driver/test automation. |
| Hazardous output sourcing at high V/A/power | Risk to user/equipment without validated fixture/load | operator-confirmed setup with documented load/wiring | Applies to OUT/OPER/BOOST classes of operations. |
| Network/address reconfiguration during generic tests | Can break communication path | isolated bench scenario and explicit operator confirmation | Includes IP/GPIB/LAN port/address commands. |
| Any destructive memory/log/init style operation | Persistent side effects / recoverability concerns | explicit operator-confirmed maintenance action | Keep default policy `never` or `operator-confirmed-only`. |

## Safe diagnostics list

| Item | Command | Why safe | Suggested hardware test |
|---|---|---|---|
| Device identity | *IDN? | Read-only metadata query | query-only smoke check |
| Installed options | *OPT? | Read-only capability query | query-only smoke check |
| Status byte / ESR | *STB?, *ESR? | Read-only status telemetry | query-only status validation |
| Error queue poll | ERR?, FAULT?, EXPLAIN? | Diagnostic queue reads without enabling output | query-only error-path checks |
| Environment telemetry | AMB_TEMP?, AMB_HUM? | Read-only ambient monitoring | query-only with range sanity |
| Output state readback | OUT?, OPER? | Observability without forcing output change | query-only before/after safe commands |

## Required equipment / fixtures

| Function | Required equipment | Required load/fixture | Hardware-test implication | Notes |
|---|---|---|---|---|
| Voltage/current output verification | High-accuracy DMM/standards and appropriate cabling | Rated load/shunt and safe terminals | needs-fixture-or-load | Do not run in generic CI hardware tests. |
| Guard/ground dependent verification | Fixture with explicit guard/ground strap configuration | Guard-to-ground strap/wiring as procedure requires | needs-fixture-or-load | Mandatory for capacitance/inductance-style scenarios. |
| Calibration/adjustment workflow | Calibration standards and service setup | Controlled service bench setup | never | Service laboratory procedure, not routine driver testing. |
| Warm-up/environment readiness | Stable ambient conditions, timing control | n/a | needs-verification | Warm-up/history prerequisites must be satisfied before verification. |
| High-risk output/power scenarios | Operator supervision + protective setup | Explicit load and interconnect validation | operator-confirmed-only | Required before any hazardous-output command validation. |
