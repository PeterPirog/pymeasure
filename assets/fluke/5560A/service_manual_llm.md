---
title: "Fluke 5560A Service Manual — LLM-Optimized Service-Risk Artifact"
source_file: "assets/fluke/5560A/service_manual.md"
vendor: fluke
model: "5560A"
class_name: "Fluke5560A"
instrument_type: "multifunction precision calibrator / precision source calibrator"
workflow_step: 04
source_role: "service risk and calibration boundary planning"
command_inventory_created: false
command_syntax_authority: "programming_guide.md"
generated_on: "2026-05-08"
local_artifact: true
upstream_pr: false
---

# LLM_AGENT_CONTRACT

- Treat the instrument as safety-critical and metrology-critical hardware.
- Do not use this file as command inventory.
- Do not implement code from this file alone.
- Do not run hardware tests from this file alone.
- Do not run service, calibration, adjustment, NVM, passcode, firmware, covers-open, or destructive procedures automatically.
- Use Programming Guide for command syntax.
- Use Operator Manual for operator-safe physical setup.
- Service-only procedures require qualified personnel and are not normal PyMeasure hardware tests.

# DOCUMENT ROLE IN PYMEASURE WORKFLOW

This artifact is a **service-risk and calibration-boundary knowledge base** for the Fluke 5560A/5550A/5540A/5530A calibrator family. It is **not** a command inventory and **must not** be used to infer remote command syntax. Its purpose is to:

- Classify risk levels for service, calibration, verification, and adjustment procedures.
- Define hardware-test policies (query-only, output-off-only, roundtrip-safe, operator-confirmed-only, protocol-only, never).
- Capture model/option dependencies, fixture requirements, and persistent-state risks.
- Provide cross-references to command-like tokens that require confirmation from `programming_guide.md`.
- Feed into Step 05 (command inventory extraction) as a risk-hint and exclusion-rules reference only.

# QUICK FACTS FOR RETRIEVAL

| Field | Value |
|---|---|
| Instrument family | Fluke 5560A / 5550A / 5540A / 5530A Calibrators |
| Manual type | Service Manual (September 2023 Rev. 2, 9/25) |
| Primary role | Service, calibration, verification, adjustment, theory, maintenance, replaceable parts |
| Remote interfaces mentioned | IEEE-488/GPIB, RS-232, USBTMC, Ethernet/LAN |
| Command syntax source | Remote Programmers Manual / Programming Guide, not this Service Manual |
| Key hazard class | Precision source: high voltage, high current, simulated power, guarded analog outputs |
| PyMeasure role | Risk classification, hardware-test policy, service coverage, option constraints |

## Output capability summary from manual

- DC voltage: 0 V to ±1020 V.
- DC current: 0 A to ±30.2 A.
- AC voltage: 1 mV to 1020 V.
- AC current: 10 μA to 30.2 A.
- Synthesized resistance: short circuit to 1200 MΩ.
- Synthesized capacitance: 220 pF to 120 mF.
- Synthesized inductance: 12 μH to 120 H, **not available on 5540A or 5530A**.
- RTD and thermocouple simulation.
- Simulated power output, **not available on 5540A**.
- Scope calibration option sections apply only when the relevant 600M/1G/2G option exists.

# SERVICE SAFETY SUMMARY

| Topic | Risk value | Risk description | PyMeasure implication | Hardware-test policy | Source evidence |
|---|---|---|---|---|---|
| High-voltage output (up to 1020 V) | hazardous-output | Can produce lethal voltages and arcs. | Never enable output in automated tests unless explicitly scoped, loaded, and operator-confirmed. | operator-confirmed-only | Service Manual Introduction, Specifications |
| High-current output (up to 30.2 A) | hazardous-output | Can produce high current causing burns, fire, or damage to wiring. | Do not roundtrip current output automatically; require external shunts/load and operator-confirmed fixture. | operator-confirmed-only | Service Manual Introduction |
| Simulated power (up to 30.9 kW, not on 5540A) | hazardous-output | High power output can damage DUT or cause injury. | Mark power-source commands as operator-confirmed-only; never run broad hardware tests. | operator-confirmed-only | Service Manual Introduction |
| Guard/ground strap configuration | fixture-dependent | Capacitance/inductance require Guard disconnected from Ground; all others require Guard connected to Ground. | Hardware tests must state guard strap requirements; avoid automatic tests without physical fixture. | operator-confirmed-only | Warmup Procedure |
| Verification zero (Total Zero) | long-running / state-changing | Required every 7 days or >5 °C ambient change; takes ~20 minutes. | Do not silently run zero in unit tests; expose only as explicit method if Programming Guide confirms syntax. | protocol-only / operator-confirmed-only | Warmup Procedure |
| Adjustment workflow | calibration-risk | Secured calibration adjustment; correction factors stored in NVM. | Protocol-only or not-implemented unless user explicitly requests; no automated hardware tests. | never / protocol-only | Adjustment section |
| Scope option calibration/adjustment | service-only / option-dependent | 600M/1G/2G option-specific; requires external equipment and qualified personnel. | Skip unless option present; separate option subsystem if implemented. | never / protocol-only | Scope Option sections |
| Warm-up before verification | long-running | Minimum 30 minutes; up to 2 hours if humidity >70%; up to 4 days after extended storage. | Do not run verification as part of normal unit tests; requires explicit operator confirmation. | operator-confirmed-only | Warmup Procedure |
| Covers-open service / replaceable parts | service-only | Internal assemblies (A3, A4, A5, A6, A7, A8, A12, A14) require physical access. | Not part of PyMeasure driver; never run automatically. | never | Maintenance / Replaceable Parts |
| Passcode-protected adjustment | persistent-state / service-only | CAL_PASSCODE required to enter adjustment; writes NVM correction factors. | Do not expose as public API; protocol-only or omitted. | never | Adjustment section; Programming Guide CAL_PASSCODE, CAL_SECURE |

# SERVICE-ONLY PROCEDURES

| Procedure or topic | Service-only reason | Required qualification / equipment | PyMeasure implication | Hardware-test policy | Source evidence |
|---|---|---|---|---|---|
| Product adjustment (calibration adjustment) | Secured mode requiring passcode; writes NVM correction factors; qualified personnel required. | Passcode, external standards (732C, 8588A, A40B, etc.), guardbanding knowledge. | Not implemented as public API; protocol-only or deferred. | never / protocol-only | Adjustment section |
| Scope option adjustment | Requires option hardware and specialized equipment (power meter, power sensor, leveled sine setup). | Qualified personnel, Keysight N1913B/E9304A, Tektronix AFG1022, adapters. | Skip unless option present; not normal driver API. | never / protocol-only | Scope Option Adjustment section |
| Replaceable parts / maintenance | Covers-open, internal assemblies, physical replacement, ESD precautions, torque specs. | Qualified service technician, ESD protection, factory parts. | Not part of PyMeasure driver. | never | Maintenance / Replaceable Parts |
| Firmware update via USB Host port | Changes instrument firmware; risk of bricking if interrupted. | Qualified personnel, USB flash drive, power stability. | Do not implement as driver method; never run automatically. | never | Product features (USB Host port for firmware updates) |
| Internal DC Zero Calibration (Total Zero) | Adjusts internal circuitry offsets across all ranges; service/calibration context. | Operator-visible but long-running; may be initiated from front panel or remote if command exists. | Expose only as explicit method if Programming Guide confirms; do not run silently. | protocol-only | Warmup Procedure / Zero Product |

# CALIBRATION / ADJUSTMENT / NVM RISK

| Topic | Risk | Persistent state affected? | Calibration constants affected? | PyMeasure implication | Hardware-test policy | Source evidence |
|---|---|---|---|---|---|---|
| Adjustment workflow (all functions) | calibration-risk | Yes — correction factors stored in NVM. | Yes | Do not implement as normal property; protocol-only or explicit method. | never / protocol-only | Adjustment section |
| CAL_PASSCODE / CAL_SECURE entry | persistent-state / calibration-risk | Yes — enables secured adjustment mode. | Yes — enables writing correction factors. | Do not expose as public get/set property; omitted or private. | never | Programming Guide CAL_PASSCODE, CAL_SECURE; Service Manual adjustment entry |
| Scope option adjustment | calibration-risk | Yes — option-specific correction factors stored in NVM. | Yes — scope option calibration constants. | Skip unless option present; not normal driver API. | never / protocol-only | Scope Option Adjustment |
| Total Zero (ZERO) | persistent-state | Yes — adjusts internal zero offsets stored in NVM. | No — not calibration constants, but internal zero offsets. | Expose only as explicit method if command exists; do not run silently. | protocol-only / operator-confirmed-only | Warmup Procedure |
| Guardbanding and specification limit calculation | calibration-risk | No — calculation only. | No — used for evaluation. | Do not use as driver validators unless tied to output command limits. | protocol-only | Applying Guardbands section |
| IP address / Network Socket Port / Subnet Mask | persistent-state | Yes — stored in non-volatile memory. | No | Normal configuration queries may be safe; changes require care. | query-only / operator-confirmed-only | Programming Guide DHCP, IPADDR, ENETPORT, SUBNETMASK notes |

# VERIFICATION PREREQUISITES

| Verification topic | Required prerequisite | Equipment / fixture | Model or option scope | PyMeasure implication | Hardware-test policy | Source evidence |
|---|---|---|---|---|---|---|
| Volts DC verification | Warm-up >=30 min, total zero, Guard-Ground strap connected, DUT in STBY. | 8588A, 732C DC Reference, low thermal cables, 4-wire short. | 5560A/5550A/5540A/5530A | Do not run as normal hardware test; requires standards. | operator-confirmed-only | Table 2, Warmup Procedure |
| Amps DC verification | Warm-up, total zero, Guard-Ground strap, DUT STBY, shunt resistance known from records. | 8588A, A40B shunts (1mA to 50A), 742A-1k, adapters. | All models | Do not run current output automatically; requires shunts. | operator-confirmed-only | Table 6, Amps DC section |
| Resistance verification | Warm-up, total zero, DUT STBY, Guard-Ground strap, 8588A configured correctly. | 8588A, 742A standards, MI 9331G for high ohms, low thermal cables, adapters. | All models | Complex fixture (4W/2W, LoI); not a unit test. | operator-confirmed-only | Table 8, Resistance section |
| Capacitance verification | Warm-up, total zero, Guard-Ground strap **DISCONNECTED** for capacitance, LCR or charge method. | Hioki IM3533 LCR meter, or charge method with 5730A/8588A. | All models | Guard strap policy differs from other functions; fixture-dependent. | operator-confirmed-only | Capacitance section, Warmup Procedure |
| Inductance verification | Warm-up, total zero, Guard-Ground strap **DISCONNECTED**, LCR meter. | Hioki IM3533 LCR meter. | 5550A and 5560A only (not 5540A/5530A) | Option/model dependent; skip if unsupported. | operator-confirmed-only | Inductance section |
| Scope option verification | Warm-up, option present, external equipment per function. | Power meter, power sensor, signal generator, scope, adapters. | Models with 600M/1G/2G option | Skip unless option detected. | operator-confirmed-only | Scope Option sections |

# DIAGNOSTIC / SELF-TEST / LONG-RUNNING PROCEDURES

| Procedure | Duration / blocking risk | State risk | PyMeasure implication | Hardware-test policy | Source evidence |
|---|---|---|---|---|---|
| Total Zero (ZERO) | ~20 minutes; blocks output usage. | Adjusts internal offsets; changes instrument state. | Expose only as explicit method if Programming Guide confirms syntax; do not run silently. | protocol-only / operator-confirmed-only | Warmup Procedure |
| Warm-up before verification | 30 min to 4 days depending on environmental history. | N/A — precondition, not a state change. | Do not run as part of normal test suite. | operator-confirmed-only | Warmup Procedure |
| Amps DC high-current settling | Up to 3 minutes for A40B-20A / A40B-50A steps. | Output active during settling; thermal drift risk. | Do not run as automated loop; requires operator and shunt. | operator-confirmed-only | Amps DC section |
| Adjustment workflow | Duration varies; blocking while correction factors are written. | Writes NVM correction factors; secured mode. | Not a normal hardware test; protocol-only or never. | never / protocol-only | Adjustment section |
| Scope option leveled sine adjustment | Sequential adjustment points; multiple equipment setups. | Writes option-specific NVM. | Not a normal hardware test; skip if option absent. | never / protocol-only | Scope Option Adjustment |

# DESTRUCTIVE OR PERSISTENT-STATE ACTIONS

| Action | Destructive or persistent effect | Reversibility | PyMeasure implication | Hardware-test policy | Source evidence |
|---|---|---|---|---|---|
| Adjustment and storage of correction factors | Persistent state (NVM correction factors overwritten). | Not reversible without recalibration. | Do not implement as normal API; protocol-only or never. | never / protocol-only | Adjustment section |
| CAL_PASSCODE / secured adjustment mode entry | Persistent state (enables secured adjustment mode). | Reversible by aborting adjustment or power cycle. | Do not expose as simple property; requires explicit method. | never | Service Manual Adjustment; Programming Guide CAL_PASSCODE, CAL_SECURE |
| *RST (instrument reset) | Resets instrument to power-up defaults. | Reversible by reconfiguration. | Use intentionally; not a harmless query. | operator-confirmed-only | Programming Guide *RST description |
| Firmware update via USB Host port | Destructive if interrupted (bricking risk). | Not reversible without service recovery. | Do not implement as driver method. | never | Product features / USB Host port |
| FORMAT command (Setup/Utility) | Potential destructive NVM effect if it erases stored calibration or user data. | Likely irreversible. | Do not use without verification from Programming Guide. | never | Programming Guide lists FORMAT under Setup and utility commands; exact effect unverified in this artifact |
| ENETPORT / IPADDR / SUBNETMASK / DHCP changes | Persistent network configuration stored in NVM. | Reversible by reconfiguration. | Query-only safe; changes require operator confirmation. | operator-confirmed-only | Programming Guide notes these are stored in non-volatile memory |

# MODEL AND OPTION DEPENDENCIES

| Model or option | Feature impact | Service-risk impact | PyMeasure implication | Hardware-test implication | Source evidence |
|---|---|---|---|---|---|
| 5540A | Lacks inductance, simulated power, dual output, 52120-related commands. | Lower output capability but same hazardous voltage/current risks. | Driver must disable inductance/power/dual-output APIs for 5540A. | Hardware-test scope limited; do not assume full family capability. | Service Manual Introduction; Programming Guide |
| 5530A | Lacks inductance, simulated power, dual output, 52120-related commands. | Same as 5540A. | Driver must disable inductance/power/dual-output APIs for 5530A. | Hardware-test scope limited. | Service Manual Introduction |
| 5550A | Lacks some high-end specs vs 5560A; inductance present. | Service-risk same family but different tolerances and specs. | Driver should query model/options before enabling dependent API. | Hardware-test must know model to apply correct limits. | Service Manual Introduction / Specifications note |
| Scope option (600M, 1G, 2G) | Adds oscilloscope calibration features (DCV, ACV, edge, leveled sine, etc.). | Service-only calibration and adjustment for scope subsystem. | Skip unless option detected; separate subsystem if implemented. | Hardware tests must verify option presence before scope commands. | Service Manual Scope Option sections |
| Firmware version 4.0+ | Some functions require firmware 4.0+. | Service-risk if firmware mismatch during verification. | Driver may need firmware check for certain commands. | Query firmware version before enabling features. | Service Manual mentions firmware dependency |

# FIXTURE AND EQUIPMENT REQUIREMENTS

| Procedure area | Required equipment / fixture | Why required | PyMeasure implication | Hardware-test policy | Source evidence |
|---|---|---|---|---|---|
| Volts DC verification | 8588A DMM, 732C DC Reference, low thermal cables, 4-wire short. | Traceable DC voltage measurement with low thermal EMF. | Do not run as normal unit test. | operator-confirmed-only | Table 2 |
| Amps DC verification | 8588A, A40B shunts (1mA to 50A), 742A-1k, adapters. | Shunt resistance must be known from calibration records for accurate current conversion. | Do not run current output automatically; requires shunts. | operator-confirmed-only | Table 6 |
| Resistance verification | 8588A, 742A standards, MI 9331G for high ohms, low thermal cables, adapters. | 4W/2W measurement modes, LoI considerations, transfer methods. | Not a unit test. | operator-confirmed-only | Table 8 |
| Capacitance verification | Hioki IM3533 LCR meter or charge method with 5730A/8588A. | Different methods for <1 mF vs >=1 mF. | Guard strap must be disconnected. | operator-confirmed-only | Table 20 |
| Inductance verification | Hioki IM3533 LCR meter. | Only for 5550A/5560A. | Guard strap must be disconnected. | operator-confirmed-only | Table 23 |
| Phase verification | Clarke-Hess 6000A phase meter, A40B shunts for V/I. | Shunt required for V/I to avoid phase meter damage. | Fixture-critical. | operator-confirmed-only | Table 29 |
| Scope option verification | Power meter, power sensor, signal generator, scope, adapters. | Option-specific external equipment for leveled sine, edge, waveform. | Skip if option absent. | operator-confirmed-only | Table 36 |

# COMMAND-LIKE TOKENS REQUIRING PROGRAMMING GUIDE CONFIRMATION

| Token | Service manual context | Found in Programming Guide? | Decision | Notes |
|---|---|---|---|---|
| STBY | Service manual repeatedly says "Set the Product to STBY" / "DUT is in STBY". | Yes — `STBY` command listed under Output commands. | confirmed-by-programming-guide | Safe output-disable state; use before/after tests. |
| OPER | Service manual says "Set the Product to Operate" for output verification. | Yes — `OPER` command listed under Output commands. | confirmed-by-programming-guide | Enables hazardous output; never run automatically without operator confirmation. |
| ZERO (Total Zero) | Service manual describes "Zero the Product" and "Zero Adjustment" front-panel procedure (~20 min). | No — no general `ZERO` command found in Programming Guide command index (only `ZERO_MEAS` for scope). | not-found-in-programming-guide | Do not infer a remote zero command from the Service Manual alone. Verify in Programming Guide body or device test. |
| ADJ_START | Service manual says "To begin Product calibration adjustment, tap Continue." | Yes — `ADJ_START` listed under Adjustment/service commands. | confirmed-by-programming-guide | Enters secured adjustment; requires passcode context. Never run automatically. |
| CAL_PASSCODE | Service manual refers to secured adjustment mode requiring passcode. | Yes — `CAL_PASSCODE` listed under Setup and utility commands. | confirmed-by-programming-guide | Enables NVM-writing mode; do not expose as public property. |
| FORMAT | Not mentioned in Service Manual, but appears in Programming Guide Setup/Utility list. | Yes — `FORMAT` listed under Setup and utility commands. | needs-verification | Exact effect unverified here; treat as potentially destructive to NVM/data. Do not use without confirming Programming Guide semantics. |
| DIAG | Service manual discusses diagnostics in Theory of Operation; not as a remote procedure. | Yes — `DIAG` and `DIAG_FAULT?` listed under Setup and utility commands. | needs-verification | Service manual does not describe remote diagnostic command syntax; verify in Programming Guide before use. |

# HARDWARE-TEST EXCLUSION LIST

| Excluded topic | Reason for exclusion | Scope | Suggested safer alternative | Source evidence |
|---|---|---|---|---|
| Total Zero (ZERO) | Long-running (~20 min), state-changing, requires warm-up and operator context. | All models | Use protocol-only test if command confirmed; never run automatically on hardware. | Warmup Procedure |
| Calibration adjustment (all functions) | Writes NVM correction factors; requires passcode and external standards. | All models | Protocol-only or never; never run automatically. | Adjustment section |
| Scope option adjustment | Requires option, external equipment, qualified personnel. | Models with scope option | Protocol-only or never; skip if option absent. | Scope Option Adjustment |
| Firmware update | Destructive if interrupted; bricks instrument. | All models | Never implement as driver method; never run automatically. | Product features (USB Host port) |
| Replaceable parts / internal service | Covers-open, physical replacement, ESD risk. | All models | Not part of PyMeasure driver; never. | Maintenance / Replaceable Parts |
| Guardbanding / specification limit calculation | Metrology computation; not an operator command. | All models | Do not use as driver validators without Programming Guide confirmation. | Applying Guardbands section |

# PYMEASURE API DECISION RULES

- Service procedures must not become normal public driver APIs unless explicitly designed and approved.
- Calibration, adjustment, NVM, firmware, passcode, destructive, and service-only actions should normally be omitted, protocol-only, private, or operator-confirmed-only.
- Query-only service/status information may be exposed only if Programming Guide confirms syntax.
- Hardware tests must skip without VISA address.
- Hardware tests must not run service/calibration/destructive commands automatically.
- Use Programming Guide for validators, values, ranges, command/query forms, and responses.
- Do not use includeSCPI=True.
- Do not create public get_* or set_* methods.

# DO-NOT-INFER LIST

- Do not infer command syntax from service procedure names.
- Do not infer query forms from service tables.
- Do not infer that service procedures are operator-safe.
- Do not infer that calibration or verification can be automated safely.
- Do not infer ranges/tolerances unless documented.
- Do not infer model/option support from another family member.
- Do not treat command-like service tokens as implemented API.
- Do not treat service verification as PyMeasure hardware test coverage.

# OCR_AND_CONVERSION_NOTES

- The source Service Manual was converted from PDF and contains OCR/export artifacts (e.g., duplicated table headers, broken figure captions such as "GuardbandRegionGuardbandRegion", occasional character substitutions).
- Numeric tolerances and specification limits appearing in service tables must not be used as PyMeasure driver validators without explicit confirmation from the Programming Guide.
- Figure references and equipment part numbers should be cross-checked against the official Fluke manual before use in metrology-critical or safety-critical code.
- Some sections contain repeated chunk boundaries from the LLM-optimized conversion; content may be slightly redundant across chunk borders.
- Do not claim OCR is perfect.

# STEP 05 HANDOFF CHECKLIST

- Step 05 must use Programming Guide, not Service Manual, for complete command inventory.
- Step 05 may use this file only for risk hints, exclusion rules, and command-like token cross-references.
- Calibration, NVM, destructive, and service-only items must be restrictive in command coverage.
- Service-only and calibration-risk commands must not be implemented in early batches.
