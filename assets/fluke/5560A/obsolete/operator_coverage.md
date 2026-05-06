# Fluke 5560A — operator_coverage.md

## Operator manual metadata

- vendor: fluke
- model: 5560A
- instrument family: 5560A / 5550A / 5540A / 5530A
- instrument type: multifunction precision calibrator / precision source calibrator
- operators guide path: assets/fluke/5560A/operators_guide.md
- programming guide path (command authority): assets/fluke/5560A/programming_guide.md
- service manual path (risk boundary): assets/fluke/5560A/service_manual.md
- remote command syntax extracted from operators guide: no (semantic/safety use only)

## User-facing function map

| User function | Front-panel term | Remote command candidate | Programming guide confirmation | PyMeasure API implication | Notes |
|---|---|---|---|---|---|
| Enable output | Operate | `OPER` / `OUT` | yes (present in command inventory) | explicit method (not property side-effect) | `operator-confirmed-only`; never auto-enable in broad tests. |
| Disable output / safe state | Standby | `STBY` | yes (present in command inventory) | explicit `standby()`-style method candidate | Preferred remote safe-final-state action for hardware tests. |
| Select/source function and setpoint | Function menus (DCV/ACV/DCI/ACI/Ohms/Cap/TC/RTD) | `OUT`, `RANGE`, `WAVE`, `PHASE`, `DUTY`, `TC_*`, `RTD_TYPE*` | yes (present in command inventory) | grouped source APIs with explicit gating | Keep output activation separate from value/configuration. |
| Read measurement/actual value | Readback/measurement screens | `VAL?`, `VVAL?`, `OUT?` | yes (present in command inventory) | measurement properties + parser methods | `VAL?` remains parser candidate. |
| Thermocouple measurement mode | TC Measure | `TC_MEAS` | yes (present in command inventory) | explicit method with fixture preconditions | Require matching TC connector/wire and RJ handling notes. |
| Interface configuration | Remote interface setup | `ADDR`, `COMM_*`, `DHCP`, `ENETPORT`, `SUBNETMASK` | yes (present in command inventory) | explicit comm-config methods; avoid routine use | May drop active session; operator confirmation required. |
| Scope functions | Scope menu / SCOPE OUT / TRIG | `SCOPE`, `TRIG`, scope-related commands | partial (commands present; option semantics from operator manual) | option-gated subsystem/API | Enable only when scope option detected. |
| Persistent strings/security | Report string / calibration security topics | `RPT_STR`, `CAL_SECURE`, `CAL_PASSCODE` | yes (present in command inventory) | not for routine driver workflow | Keep protocol-only or never in broad hardware tests. |

## Connector and output safety

| Connector/output | Function | Hazard | Safe final state | Hardware-test implication | Notes |
|---|---|---|---|---|---|
| OUTPUT HI/LO (+ sense) | Voltage/resistance/capacitance/inductance paths | Hazardous voltage/current depending mode | Standby (`STBY`) and verify inactive output | `operator-confirmed-only` | Do not rewire DUT while output may be active. |
| VI AUX and 30A terminal | Current sourcing | High current and terminal-selection risk | Standby before terminal changes | `operator-confirmed-only` | >3.1 A path requires dedicated terminal/load policy. |
| TC connector | Thermocouple source/measure | Thermal EMF, wrong TC type, RJ errors | Standby + fixture unchanged until confirmed | `operator-confirmed-only` | Use matching TC wire/connectors and reference-junction handling. |
| Guard / earth reference | Grounding strategy | Ground loops and safety-ground errors | Single earth-to-LO tie, protective earth intact | `operator-confirmed-only` | Do not defeat protective earth; avoid automatic guard changes. |
| SCOPE OUT / TRIG | Scope calibration outputs | Option-dependent active outputs | Standby / function exit to inactive output | `operator-confirmed-only` | Only when scope option is installed and confirmed. |
| 50 Ω overload test path | Scope overload functions | Can damage DUT/input | Not used in generic runs | `never` (broad tests) | Only explicit fixture-scoped procedures. |

## Normal operation sequences

| Sequence | Steps | Remote automation candidate | Risk | Notes |
|---|---|---|---|---|
| Safe source setup (recommended) | Enter standby → select function/range/parameters → validate query readback → explicit enable output if approved | yes (split config + explicit enable) | cautious-output | Output activation must be separate and operator-confirmed. |
| Safe shutdown/final state | Disable output (`STBY`) → query status/value as needed (`OUT?`, `VAL?`) → end session | yes | safe-state-readwrite | Preferred final-state sequence for hardware tests. |
| Interface setup/change | Read current comm settings → apply one change → reconnect/verify identity | limited | network/address-affecting | Session may drop after address/interface changes. |
| Option-gated scope flow | Verify options/model → configure scope function → run explicit guarded action → return to safe state | limited | hazardous-output | Skip when option absent. |
| Warm-up-aware metrology flow | Confirm warm-up requirement met → run metrology-sensitive actions | limited | cautious-state-change | At least 30 min warm-up (or 2× off-time, max 30 min). |

## Model/option dependencies

| Feature | Models/options | Driver implication | Hardware-test implication | Notes |
|---|---|---|---|---|
| Inductance | 5560A/5550A only | Gate inductance APIs by detected model | Skip on 5540A/5530A | Do not expose unsupported feature paths. |
| Dual output and simulated power | Not available on 5540A | Gate dual-output/power APIs | `operator-confirmed-only` / skip unsupported | High-risk output class; never broad auto-test. |
| Scope subsystem | Requires scope option | Option-gated command grouping/API surface | Skip if option absent | Include detection check before tests. |
| 600M/1G/2G scope options | Model-specific option availability | Option-dependent capabilities/limits | Operator-confirmed fixture tests only | Enforce model+option compatibility checks. |
| 52120A amplifier path | External amplifier option | Separate feature flag and fixture assumptions | `operator-confirmed-only` | External hardware dependency must be explicit. |