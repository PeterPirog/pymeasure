---
title: "Fluke 5560A/5550A/5540A/5530A Service Manual — LLM/PyMeasure optimized"
source_file: "Service manual 5560A.md"
source_manual_title: "5560A/5550A/5540A/5530A Calibrator Service Manual"
source_manual_revision: "September 2023 Rev. 2, 9/25"
instrument_family: ["Fluke 5560A", "Fluke 5550A", "Fluke 5540A", "Fluke 5530A"]
instrument_type: "Multifunction precision calibrator"
interfaces_mentioned: ["GPIB/IEEE-488", "RS-232", "USBTMC", "Ethernet/LAN"]
optimized_for: ["LLM retrieval", "RAG", "GPT Codex", "PyMeasure driver planning", "service coverage", "hardware-test safety"]
content_policy: "Preserve service content; do not infer remote commands from service procedures."
generated_on: "2026-05-06"
original_line_count: 6589
cleaned_line_count: 5085
llm_chunk_count: 22
---

# 0. LLM_AGENT_CONTRACT

Use this file as a **service, calibration, verification, adjustment, safety, and hardware-test planning reference** for the Fluke 5560A/5550A/5540A/5530A calibrator family.

## Mandatory rules for agents

1. **Do not invent remote commands from this Service Manual.** Remote command syntax must come from the Remote Programmers Manual / Programming Guide.
2. **Treat calibration, adjustment, correction-factor storage, passcode-protected procedures, internal service, and NVM-changing operations as service/calibration-risk operations.**
3. **Never generate automatic hardware tests that enable hazardous voltage/current/power output unless the test is explicitly operator-confirmed and fixture-defined.**
4. **For PyMeasure, use this file to classify risk, model/option dependencies, warm-up requirements, guard/ground configuration, and safe final states.**
5. **For command implementation, cross-reference `programming_guide.md` and `command_coverage.md`; this file provides constraints, not command syntax.**
6. **When a procedure depends on equipment, standards, guardbanding, warm-up, humidity history, calibration interval, or model option, state the dependency.**
7. **If OCR/export artifacts are present, verify against the source PDF or the official manual before using values in metrology or safety-critical code.**

## Intended use in PyMeasure workflow

- Feed this file to Codex together with `programming_guide.md` and `command_coverage.md`.
- Use it to build `service_coverage.md`.
- Use it to mark hardware-test policy: `query-only`, `roundtrip-safe`, `output-off-only`, `operator-confirmed-only`, `protocol-only`, `never`.
- Keep this file under local `assets/<vendor>/<model>/`; do not include it in the upstream PyMeasure PR.

# 1. Quick facts for retrieval

| Field | Value |
|---|---|
| Instrument family | Fluke 5560A / 5550A / 5540A / 5530A Calibrators |
| Manual type | Service Manual |
| Revision/date | September 2023 Rev. 2, 9/25 |
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
- Synthesized inductance: 12 μH to 120 H, not available on 5540A or 5530A.
- RTD and thermocouple simulation.
- Simulated power output, not available on 5540A.
- Scope calibration option sections apply only when the relevant 600M/1G/2G option exists.

# 2. Document routing map

| User / Codex intent | Use this source region | PyMeasure implication |
|---|---|---|
| Instrument overview | Introduction, Product features, Operation overview | Identify model family, output capability, supported remote interfaces, option constraints. |
| Remote-control context | Remote Operation sections | Use only for interface context; exact command syntax must come from the Remote Programmers Manual. |
| Architecture / assemblies | Theory of Operation | Understand guarded analog system, output switching, high-voltage/current/impedance blocks; do not translate assembly names into SCPI commands. |
| Verification prerequisites | Calibration and Verification / Warmup Procedure | Use for hardware-test preconditions: standby before connection changes, warm-up, zeroing cadence, guard strap policy. |
| Guardbanding and limits | Determine Specification Limits / Applying Guardbands | Use for metrology calculations and report generation, not for PyMeasure validators unless tied to output command limits. |
| Main output verification | VDC, ADC, Ohms, VAC, AAC, Capacitance, Inductance, TC, Phase, Frequency | Use to design optional verification routines and safety policies; most steps are not unit tests. |
| Adjustment | Adjustment and per-function adjustment sections | Service/calibration workflow; requires secured adjustment mode and can write nonvolatile correction factors. |
| Scope option | Oscilloscope Calibration Option sections | Option-dependent routines for 600M/1G/2G; do not implement unless option detection and Programming Guide commands exist. |
| Maintenance / parts | Maintenance, Product Disposal, Scope Option Maintenance, Replaceable Parts | Use for operator guidance and service coverage; not driver command syntax. |

# 3. PyMeasure service-risk classification

| Service topic | Manual basis | Risk level | Driver / hardware-test implication |
|---|---|---|---|
| High-voltage output | DC/AC voltage up to 1020 V | `hazardous-output` | Never enable output in automated hardware tests unless explicitly scoped, loaded, and operator-confirmed. |
| High-current output | DC/AC current up to 30.2 A | `hazardous-output` | Do not roundtrip current output automatically; require external shunts/load and operator-confirmed fixture. |
| Simulated power | Up to 30.9 kW, not available on 5540A | `hazardous-output` | Mark power-source commands as operator-confirmed-only; never run broad hardware tests. |
| Guard/ground configuration | Capacitance/inductance require different Guard-Ground strap policy | `fixture-dependent` | Hardware tests must state guard strap requirements; avoid automatic tests without physical fixture. |
| Verification zero | Total zero required before verification every 7 days or >5 °C ambient change | `long-running/state-changing` | Do not silently run zero in unit tests; expose only as explicit method if command exists in Programming Guide. |
| Adjustment | Secured calibration adjustment; correction factors can be stored in NVM | `calibration/adjustment` | Protocol-only or not-implemented unless user explicitly requests; no automated hardware tests. |
| Scope option | 600M/1G/2G option-specific calibration and adjustment | `option-dependent` | Skip unless option present; separate option subsystem if implemented. |
| Firmware/model dependencies | Inductance unavailable on 5540A/5530A; power unavailable on 5540A; some functions require firmware 4.0+ | `needs-option-detection` | Driver should check model/options before enabling dependent API. |

# 4. PyMeasure API decision rules when cross-referencing the Programming Guide

| If Programming Guide shows... | Preferred PyMeasure shape | Service-manual constraint |
|---|---|---|
| Programming Guide command/query representing state | `Instrument.control` | Add validators and value mapping from Programming Guide only. |
| Programming Guide query-only status or scalar | `Instrument.measurement` | Use get_process for int/float/bool parsing. |
| Programming Guide command-only action | `method` | Use for standby/operate/zero/abort/self-test actions; never use control. |
| Programming Guide command-only write-only state | `Instrument.setting` | Use only when it is truly a setting and not an action. |
| Block/table/report transfer | `method + parser` | Do not hide large transfers behind simple properties. |
| Service Manual procedure without remote command | `not implemented` | Record in service_coverage.md; do not invent SCPI. |
| Calibration/adjustment/store/delete/format/power-off | `explicit method or deferred` | Expected_protocol only; hardware policy never/operator-confirmed-only. |

# 5. Hardware-test policy derived from this Service Manual

| Policy | Meaning | Examples for this calibrator family |
|---|---|---|
| `query-only` | Safe to query state/identity/options/errors without changing output. | ID, options, model, error queue, status registers, output state query. |
| `output-off-only` | May configure parameters only while output remains STBY/OFF. | Source amplitude/frequency ranges, function selection, terminal routing. |
| `roundtrip-safe` | Setter/getter can be tested if it does not enable output and can be restored. | Nonvolatile-safe display/preferences only if Programming Guide confirms no persistent side effect. |
| `operator-confirmed-only` | Requires physical setup, load, shunt, meter, wiring, guard strap, or risk acceptance. | Any voltage/current/power output, current shunts, phase tests, capacitance charge method. |
| `protocol-only` | Test only command string construction with `expected_protocol`; do not run on hardware automatically. | Zero, long self-test, adjustment entry, calibration workflow, NVM storage. |
| `never` | Do not expose as normal test or broad API without explicit project decision. | Factory/service passcode operations, calibration save/store, firmware update, deletion/formatting/power-off. |

## Hardware-test final-state rule

Every hardware test that touches output configuration must leave the calibrator in **STBY / output disabled** and must query the error queue if the Programming Guide exposes an error-query command.

# 6. Service coverage table template for this instrument

Copy this table into `assets/fluke/5560a/service_coverage.md` or adapt the path to the chosen vendor/model naming convention.

| Area | Manual section | Operator-safe? | Service/calibration-only? | Remote command confirmed in Programming Guide? | Related command/API | Risk level | Hardware-test policy | Notes |
|---|---|---:|---:|---:|---|---|---|---|
| Remote interface context | Operation Overview | yes | no | n/a | n/a | safe-query | query-only | Use Programming Guide for exact syntax. |
| Warm-up before verification | Warmup Procedure | yes | calibration context | maybe | explicit method only if command exists | long-running | protocol-only/operator-confirmed-only | 30 min minimum; longer if environmental history requires. |
| Total zero | Warmup Procedure / Zero Product | operator-visible | calibration-related | check Programming Guide | explicit method, not property | long-running/state-changing | protocol-only/operator-confirmed-only | Required before verification; may take about 20 min. |
| Guard strap configuration | Warmup Procedure | yes | fixture-dependent | no | documentation/test precondition | fixture-dependent | operator-confirmed-only | Capacitance/inductance differ from other functions. |
| Output voltage/current/power | Introduction / verification tables | yes with correct setup | hazardous | check Programming Guide | output controls | hazardous-output | operator-confirmed-only | Do not enable automatically. |
| Adjustment workflow | Adjustment | no for routine API | yes | check Programming Guide | deferred/not implemented by default | calibration/adjustment | never/protocol-only | Secured; may store correction factors in NVM. |
| Scope option adjustment | Scope Option Adjustment | no for routine API | yes | check Programming Guide | option subsystem or deferred | option-dependent/calibration | never/protocol-only | Requires option and external equipment. |
| Replaceable parts | Replaceable Parts | no driver impact | service | no | not implemented | service-only | never | Not part of PyMeasure driver. |

# 7. Verification and adjustment procedure index for RAG

The following index summarizes the main procedure families. Use it to route questions; do not treat it as executable automation.

## Main calibration / verification families

- Volts DC — main OUTPUT VZ and AUX output.
- Amps DC — low current to 30.2 A using resistance standards and A40B shunts.
- Resistance — direct and transfer methods; 4-wire and 2-wire; LoI considerations.
- Volts AC — low-frequency DMM and 5790B AC Measurement Standard paths.
- AC Power voltage/current — model and firmware dependent.
- Amps AC — A40B shunts, 8588A/5790B, settling time requirements.
- Capacitance — LCR method for lower values and charge method for higher values.
- Inductance — only 5550A and 5560A.
- Thermocouple source/measure — temperature compensation and Type J check.
- Phase — V/V and V/I; shunt required for V/I to avoid phase meter damage.
- Frequency — external frequency counter.
- Scope option — DCV, ACV, waveform, leveled sine, edge, pulse, marker period, resistance, capacitance, option adjustment.

## Autodetected procedure headings

- To zero the Product
- To calibrate the Volts dc function from the main output (see Table 3)
- To calibrate the Volts dc function from the secondary output
- To calibrate the Amps dc function (subsequent amps dc calibration and verification steps, see Table 7)
- To calibrate the Resistance function
- To proceed with volts ac out of the Sense VZ LO/Output VI AUX proceed as follows
- To calibrate the amps ac function
- To calibrate the Capacitance function for values <1 mF
- To proceed with this calibration and verification
- To calibrate the Inductance function
- To calibrate the Thermocouple Measure function including the temperature compensation
- To calibrate the Thermocouple Measure Function linearity with temperature compensation OFF
- To calibrate the Thermocouple Source function linearity with temperature compensation OFF
- To calibrate dual output V/V
- To calibrate dual output V/I
- To calibrate the Frequency function
- To begin Product calibration adjustment
- To begin a calibration adjustment, tap Continue. The firmware of the device proceeds with the first
- To use the high-accuracy mode (shunts with a meter), you must determine and connect the shunt
- To proceed
- To process the data, separate the data into two groups
- To process this data, separate the data into two groups
- To adjust dc voltage
- To adjust ac voltage
- To adjust Edge
- To adjust the calibration leveled sine wave MID and HIGH frequencies

# 8. Table index for retrieval

- Table 1. Required Equipment for Main Output
- Table 1. Required Equipment for Main Output (cont.)
- Table 2. Required Equipment for Volts DC (Normal Output)
- Table 3. Calibration and Verification Steps for Volts DC (OUTPUT VZ)
- Table 4. Required Equipment for Volts DC (AUX Output)
- Table 3. Calibration and Verification Steps for Volts DC (OUTPUT VZ) (cont.)
- Table 5. Calibration and Verification Steps for Volts dc (AUX Output)
- Table 6. Required Equipment for Amps DC
- Table 7. Calibration and Verification Steps for Amps DC
- Table 7. Calibration and Verification Steps for Amps DC (cont.)
- Table 8. Required Equipment for Resistance
- Table 9. 8588A 1G W Range Characterization
- Table 10. Calibration and Verification Steps for Resistance
- Table 10. Calibration and Verification Steps for Resistance (cont.)
- Table 11. Required Equipment Volts AC Main Output
- Table 12. Calibration and Verification steps for Volts AC
- Table 12. Calibration and Verification steps for Volts AC (cont.)
- Table 13. Calibration and Verification steps for AC Power - Volts AC
- Table 14. Required Equipment Volts AC from the AUX Output
- Table 15. Calibration and Verification steps for Volts AC Out of the AUX Output
- Table 16. Calibration and Verification steps for ACV ACV - Volts AC (Aux Output)
- Table 17. Required Equipment for Amps AC
- Table 17. Required Equipment for Amps AC (cont.)
- Table 18. Calibration and Verification Steps for Amps AC
- Table 18. Calibration and Verification Steps for Amps AC (cont.)
- Table 19. Calibration and Verification steps for AC Power - Amps AC
- Table 20. Required Equipment for Capacitance
- Table 19. Calibration and Verification steps for AC Power - Amps AC (cont.)
- Table 21. Calibration and Verification Steps for Capacitance with LCR Meter
- Table 22. Calibration and Verification Steps for Capacitance Using Charge Method
- Table 23. Required Equipment for Inductance
- Table 24. Calibration and Verification Steps for Inductance with LCR Meter
- Table 25. Required Equipment for Thermocouple
- Table 24. Calibration and Verification Steps for Inductance with LCR Meter (cont.)
- Table 26.
- Table 26. Type J Thermocouple Calibration and Verification
- Table 27. 10 μV/°C Measure Thermocouple Calibration and Verification
- Table 28. 10 μV/°C Source Thermocouple Calibration and Verification
- Table 29. Required Equipment for Phase
- Table 30. Phase Calibration and Verification Record for V/V
- Table 31. Phase Calibration and Verification Record for V/I
- Table 32. Required Equipment for Frequency
- Table 33. Frequency Calibration and Verification
- Table 31. Phase Calibration and Verification Record for V/I (cont.)
- Table 34. Adjustment Steps for Capacitance with LCR Meter
- Table 35. Adjustment Steps for Inductance with LCR Meter
- Table 35. Adjustment Steps for Inductance with LCR Meter (cont.)
- Table 36. Required Equipment for Scope Option
- Table 37. DC Voltage Calibration and Verification at 1 MΩ
- Table 37. DC Voltage Calibration and Verification at 1 MΩ (cont.)
- Table 38. 10 DC Voltage Calibration and Verification into 50 Ω
- Table 38. 10 DC Voltage Calibration and Verification into 50 Ω (cont.)
- Table 39. AC Voltage Calibration and Verification into 1 MΩ
- Table 39. AC Voltage Calibration and Verification into 1 MΩ (cont.)
- Table 40. AC Voltage Calibration and Verification into 50 Ω
- Table 40. AC Voltage Calibration and Verification into 50 Ω (cont.)
- Table 41. Waveform Generator Calibration and Verification - into 1 MΩ
- Table 41. Waveform Generator Calibration and Verification - into 1 MΩ (cont.)
- Table 42. Waveform Generator Calibration and Verification - into 50 Ω
- Table 42. Waveform Generator Calibration and Verification - into 50 Ω (cont.)
- Table 43. Leveled Sine Amplitude Calibration and Verification
- Table 44.
- Table 44. Low Frequency Leveled Sine Flatness Relative to 50 kHz Calibration and Verification
- Table 44. Low Frequency Leveled Sine Flatness Relative to 50 kHz Calibration and Verification (cont.)
- Table 45.
- Table 45. High Frequency Leveled Sine Flatness Relative to 50 kHz Calibration and Verification
- Table 45. High Frequency Leveled Sine Flatness Relative to 50 kHz Calibration and Verification (cont.)
- Table 46. Leveled Sine Reflection Coefficient Calibration and Verification
- Table 46. Leveled Sine Reflection Coefficient Calibration and Verification (cont.)
- Table 47. Edge Rise Time Calibration and Verification
- Table 48. Pulse Width Calibration and Verification
- Table 49. Time Marker Period Calibration and Verification
- Table 50. Measure Resistance Calibration and Verification
- Table 51. Measure Capacitance Calibration and Verification
- Table 52. Adjustment Points for Leveled Sine Wave - Before
- Table 52. Adjustment Points for Leveled Sine Wave - Before (cont.)
- Table 53. Sequential Adjustment Points and 8588A Aperture Setup for AC Voltage - 1 M Ohm
- Table 54. Sequential Adjustment Points and 8588A Aperture setup for AC Voltage - into 50 Ohm
- Table 56.
- Table 55. Sequential Adjustment Points and 8588A Aperture Setup for Edge
- Table 56. Sequential Adjustment Points for Leveled Sine LO Points Setup
- Table 57. Sequential Adjustment Points and 5790B or Power Meter Setup for Leveled Sine MID
- Table 58. Sequential Adjustment Points and Power Meter set up for Leveled Sine HIGH
- Table 58. Sequential Adjustment Points and Power Meter set up for Leveled Sine HIGH (cont.)
- Table 59. Replaceable Parts
- Table 59. Replaceable Parts (cont.)

# 9. Figure index for retrieval

- Figure 1. 5560A Calibrator
- Figure 2. Test Limits Established by Guardbanding
- Figure 3. Volts DC Calibration and Verification Direct
- Figure 4. Volts DC SENSE Output
- Figure 5.
- Figure 5. Amps DC with 742A-1k - Meter Zero
- Figure 6. Amps DC with742A-1k
- Figure 7. Amps DC with A40B-1mA
- Figure 8. Amps DC with A40B-10mA
- Figure 9. Amps DC with A40B-100mA
- Figure 10. Amps DC with A40B-1A
- Figure 11. Amps DC with A40B-5A
- Figure 12. Amps DC with A40B-10A
- Figure 13. Amps DC with A40B-20A
- Figure 14. Amps DC with A40B-50A
- Figure 15. Resistance 4W with 8588A
- Figure 16. Resistance 4W with Low Current with 5730A as Current Source
- Figure 17. Low frequency Volts AC Calibration
- Figure 18. Volts AC Calibration
- Figure 19. Connections with Jumpers
- Figure 20. Volts AC Out of the SENSE VZ LO/OUTPUT VI AUX Calibration Adjustment
- Figure 21. Amps AC with A40B-1mA
- Figure 22. Amps AC with A40B-10mA
- Figure 23. Amps AC with A40B-100mA
- Figure 24. Amps AC with A40B-1A
- Figure 25. Amps AC with A40B-5A
- Figure 26. Amps AC with A40B-10A
- Figure 27. Amps AC with A40B-20A
- Figure 28. Amps AC with A40B-50A
- Figure 29. ACP - Amps AC with A40B-10 mA
- Figure 30. ACP - Amps AC with A40B-100mA
- Figure 31. ACP - Amps AC with A40B-1A
- Figure 32. ACP-Amps AC with A40B-5A
- Figure 33. ACP -Amps AC with A40B-20A
- Figure 34.
- Figure 34. Capacitance Charge Connection
- Figure 35. Equipment Connections for Scope Option DCV, ACV and Edge Adjustment – into
- Figure 36. Equipment Connections Scope Option DCV, ACV and Edge Adjustment – into
- Figure 37. 5790B to Calibrator Connections
- Figure 38. Calibrator and Keysight Power Meter and Power Sensor Connections
- Figure 39. Tektronix AFG1022 Initial Connections
- Figure 40. Leveled Sine Reflection Coefficient - OPEN Connections
- Figure 41. Leveled Sine Reflection Coefficient - SHORT Connections
- Figure 42. Leveled Sine Reflection Coefficient Calibration and Verification Connections
- Figure 43. Time Base Measurement Connection
- Figure 37.
- Figure 44. The Keysight N1913B Power Meter and Keysight E9304A Power Sensor
- Figure 36.
- Figure 35.
- Figure 44.To learn how to connect these two instruments, refer to their operator manuals.
- Figure 45. Resistance Calibration Adjustment Connections
- Figure 46. Replacement Parts

# 10. Codex task card: build service coverage before coding

```text
Read:
- assets/<vendor>/<model>/service_manual.md
- assets/<vendor>/<model>/programming_guide.md
- assets/<vendor>/<model>/command_coverage.md

Create or update:
- assets/<vendor>/<model>/service_coverage.md

Do not implement code yet.

For each service/calibration/verification/adjustment area, classify:
- operator-safe vs service/calibration-only,
- required external equipment,
- output hazard level,
- model/option/firmware dependency,
- whether a remote command is confirmed in the Programming Guide,
- PyMeasure API decision: not implemented / explicit method / protocol-only / hardware-safe.

Never infer a remote command from this Service Manual alone.
```

# 11. Codex task card: hardware-test safety review

```text
Before adding or running hardware tests for this calibrator:
1. Confirm the command exists in the Programming Guide.
2. Confirm the test does not enable hazardous output unless explicitly operator-confirmed.
3. Confirm the calibrator is left in STBY/output disabled.
4. Confirm the required guard/ground strap and external load/shunt/meter are present.
5. Confirm timeout is long enough for GPIB/USBTMC/LAN and for any long operation.
6. Query and report the error queue after configuration if supported by the driver.
7. Do not run adjustment, zero, calibration store, firmware update, delete/format, or power-off commands automatically.
```

# 12. Full cleaned source text with retrieval chunks

<!-- llm_chunk_start id=service_chunk_0001 source=service_manual_5560a source_line_start=1 source_line_end=260 retrieval_priority=high -->

## service_chunk_0001: September 2023 Rev. 2, 9/25

September 2023 Rev. 2, 9/25
© 2023-2025 Fluke Corporation. All rights reserved. Specifications are subject to change without notice.
All product names are trademarks of their respective companies.
LIMITED WARRANTY AND LIMITATION OF LIABILITY
Each Fluke product is warranted to be free from defects in material and workmanship under normal use and
service. The warranty period is one year and begins on the date of shipment. Parts, product repairs, and services
are warranted for 90 days. This warranty extends only to the original buyer or end-user customer of a Fluke
authorized reseller, and does not apply to fuses, disposable batteries, or to any product which, in Fluke's opinion,
has been misused, altered, neglected, contaminated, or damaged by accident or abnormal conditions of operation
or handling. Fluke warrants that software will operate substantially in accordance with its functional specifications
for 90 days and that it has been properly recorded on non-defective media. Fluke does not warrant that software
will be error free or operate without interruption.
Fluke authorized resellers shall extend this warranty on new and unused products to end-user customers only but
have no authority to extend a greater or different warranty on behalf of Fluke. Warranty support is available only if
product is purchased through a Fluke authorized sales outlet or Buyer has paid the applicable international price.
Fluke reserves the right to invoice Buyer for importation costs of repair/replacement parts when product purchased
in one country is submitted for repair in another country.
Fluke's warranty obligation is limited, at Fluke's option, to refund of the purchase price, free of charge repair, or
replacement of a defective product which is returned to a Fluke authorized service center within the warranty
period.
To obtain warranty service, contact your nearest Fluke authorized service center to obtain return authorization
information, then send the product to that service center, with a description of the difficulty, postage and insurance
prepaid (FOB Destination). Fluke assumes no risk for damage in transit. Following warranty repair, the product will
be returned to Buyer, transportation prepaid (FOB Destination). If Fluke determines that failure was caused by
neglect, misuse, contamination, alteration, accident, or abnormal condition of operation or handling, including
overvoltage failures caused by use outside the product’s specified rating, or normal wear and tear of mechanical
components, Fluke will provide an estimate of repair costs and obtain authorization before commencing the work.
Following repair, the product will be returned to the Buyer transportation prepaid and the Buyer will be billed for the
repair and return transportation charges (FOB Shipping Point).
THIS WARRANTY IS BUYER'S SOLE AND EXCLUSIVE REMEDY AND IS IN LIEU OF ALL OTHER
WARRANTIES, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO ANY IMPLIED WARRANTY OF
MERCHANTABILITY OR FITNESS FOR A PARTICULAR PURPOSE. FLUKE SHALL NOT BE LIABLE FOR ANY
SPECIAL, INDIRECT, INCIDENTAL, OR CONSEQUENTIAL DAMAGES OR LOSSES, INCLUDING LOSS OF
DATA, ARISING FROM ANY CAUSE OR THEORY.
Since some countries or states do not allow limitation of the term of an implied warranty, or exclusion or limitation
of incidental or consequential damages, the limitations and exclusions of this warranty may not apply to every
buyer. If any provision of this Warranty is held invalid or unenforceable by a court or other decision-maker of
competent jurisdiction, such holding will not affect the validity or enforceability of any other provision.
11/99
Fluke Corporation
6920 Seaway Blvd.
Everett, WA 98203
U.S.A.
Fluke Europe B.V.
P.O. Box 1186
5602 BD Eindhoven
The Netherlands
Table of Contents
Title Page
Introduction................................................................................................ 1
Contact Fluke Calibration .......................................................................... 2
Product-Use Information............................................................................ 2
Safety Information ..................................................................................... 3
Specifications ............................................................................................ 3
Service Information.................................................................................... 3
Operation Overview................................................................................... 3
Local Operation .................................................................................... 3
Remote Operation (GPIB) .................................................................... 3
Remote Operation (RS-232)................................................................. 3
Remote Operation (USBTMC).............................................................. 4
Remote Operation (Ethernet) ............................................................... 4
Prepare the Product for Operation ............................................................ 4
Theory of Operation................................................................................... 4
System Architecture.............................................................................. 4
Out-guard.............................................................................................. 4
In-guard ................................................................................................ 5
A14 Output Switching ...................................................................... 5
A3 Motherboard ............................................................................... 5
A4..................................................................................................... 5
A5 Impedance .................................................................................. 6
A6 DDS ............................................................................................ 6
A7 Current........................................................................................ 6
A8 High Voltage ............................................................................... 6
A12 Supply....................................................................................... 6
Calibration and Verification of the Product ................................................ 7
Warmup Procedure for All Verification Tests........................................ 7
Determine Specification Limits for other Adjustment Intervals ............. 10
Applying Guardbands to Specification Limits ....................................... 10
Volts DC Calibration and Verification (OUTPUT VZ)............................ 12
Volts DC Calibration and Verification (AUX Output) (5530A, 5550A,
and 5560A) ........................................................................................... 15
Amps DC Calibration and Verification .................................................. 17
Resistance Calibration and Verification ................................................ 26
Volts AC Calibration and Verification (OUTPUT VZ) ............................ 33
AC Power. Volts AC Calibration and Verification (OUTPUT VZ)
(5530A, 5550A and 5560A) .................................................................. 39
Volts AC Calibration and Verification (AUX Output) (5530A, 5550A,
and 5560A) ........................................................................................... 40
ACV ACV. Volts AC Calibration and Verification (AUX Output)
(5530A, 5550A and 5560A) .................................................................. 42
Amps AC Calibration and Verification................................................... 42
AC Power. Amps AC Calibration and Verification (5530A, 5550A
and 5560A) ........................................................................................... 54
Capacitance Calibration and Verification.............................................. 58
Inductance Calibration and Verification (5550A and 5560A) ................ 62
Thermocouple Calibration and Verification........................................... 63
Phase Calibration and Verification (5530A, 5550A, and 5560A) .......... 66
Frequency Calibration and Verification................................................. 69
Adjustment ................................................................................................ 70
Start the Adjustment ............................................................................. 70
Volts DC Adjustment (OUTPUT VZ)..................................................... 71
Volts AC Adjustment (OUTPUT VZ) ..................................................... 71
Frequency Adjustment (OUTPUT VZ) .................................................. 72
Amps DC Adjustment ........................................................................... 72
Volts DC (DCV DCV) Adjustment (Secondary Output) (5530A,
5550A, and 5560A)............................................................................... 72
Amps AC Adjustment............................................................................ 73
Volts AC (ACV ACV) Adjustment (Secondary Output) (5530A,
5550A, and 5560A)............................................................................... 73
Resistance Adjustment ......................................................................... 74
Capacitance Adjustment....................................................................... 74
Inductance Adjustment ......................................................................... 76
TC Source Adjustment.......................................................................... 77
TC Measure Adjustment ....................................................................... 78
Oscilloscope Calibration Option (600M, 1G, and 2G) Calibration,
Verification, and Adjustment...................................................................... 78
Required Equipment for Calibration, Verification, and Adjustment....... 78
Scope Option Calibration and Verification ............................................ 79
DC Voltage Calibration and Verification........................................... 79
DC Voltage Signal into 1 MΩ Calibration and Verification ............... 80
DC Voltage Signal into 50 Ω Calibration and Verification ................ 82
AC Voltage Amplitude Calibration and Verification.......................... 83
AC Voltage Signal into 1 MΩ Calibration and Verification ............... 83
AC Voltage Signal into 50 Ω Calibration and Verification ................ 87
Waveform Generator Calibration and Verification ........................... 89
Low Frequency Leveled Sine Flatness Calibration and Verification 96
Leveled Sine Reflection Coefficient Calibration and Verification ..... 111
Edge Rise Time Calibration and Verification ................................... 117
Pulse Width Calibration and Verification.......................................... 119
Time Marker Period Calibration and Verification ............................. 119
Measure Resistance Calibration and Verification ............................ 120
Measure Capacitance Calibration and Verification .......................... 121
Scope Option Adjustment Setup........................................................... 122
Scope Option Adjustment ..................................................................... 122
Before Scope Option Adjustment..................................................... 123
DC Voltage Adjustment.................................................................... 125
AC Voltage Adjustment .................................................................... 126
Edge Measurement Adjustment....................................................... 130
Leveled Sine Wave Adjustment ....................................................... 131
Resistance Adjustment .................................................................... 136
Maintenance .............................................................................................. 138
Product Disposal................................................................................... 138
Scope Option Maintenance .................................................................. 138
Replaceable Parts ..................................................................................... 138
Introduction
The 5560A/5550A/5540A/5530A Calibrators (the Product or the Calibrator) addresses a wide
calibration workload that includes 6.5 digit bench Digital Multimeters (DMMs), and comes with internal
and external features that protect it against damage and make it easier to transport for on-site or
mobile calibration. The Product, shown in Figure 1, can also be fully automated with MET/CAL®.
The Product is a fully-programmable precision source for:
• DC voltage from 0 V to ±1020 V
• DC current from 0 A to ±30.2 A
• AC voltage from 1 mV to 1020 V
• AC current from 10 μA to 30.2 A
• AC waveforms include sine wave and square wave.
• Synthesized Resistance values from a short circuit to 1200 MΩ
• Synthesized Capacitance values from 220 pF to 120 mF
• Synthesized Inductance values from 12 μH to 120 H (Inductance not available on 5540A or 5530A).
• Simulated output for 10 types of Resistance Temperature Detectors (RTDs)
• Simulated output for 17 types of thermocouples
• Simulated power output (not available on 5540A)
Note
All images shown in this manual are the 5560A unless noted otherwise.
Figure 1. 5560A Calibrator
Product features include:
• Automatic meter error calculation, with user-selectable reference values.
• x (Multiply) and * (Divide) that change the output value by multiples of ten or to pre-determined
cardinal values for various functions, including standard oscilloscope timebase and gain steps.
• Programmable entry limits that prevent the operator from entering values that exceed preset output
limits.
• Simultaneous output of voltage and current, simulating power up to 30.9 kW (not available on
5540A).
• 10 MHz sync pulse reference input and output. Use this to input a high-accuracy 10 MHz reference
to transfer the frequency accuracy to the Calibrator, and/or to synchronize one or more additional
Calibrators to a primary 5560A/5550A/5540A/5530A.
• Simultaneous output of two voltages.
• Extended bandwidth mode outputs multiple waveforms down to 0.01 Hz, and sine waves to 2 MHz.
• Variable output between 10 MHz reference input and primary OUTPUT, and between voltage and
current outputs.
• Standard IEEE-488 (GPIB) interface, complying with ANSI/IEEE Standards 488.1-1987 and 488.2-
1987.
• EIA Standard RS-232 serial data interface for Calibrator remote control.
• Universal Serial Bus (USB) 2.0 high-speed interface device port for remote control of the Product
using USBTMC.
• Integrated 10/100/1000BASE-T Ethernet port for network connection remote control of the Product.
• USB Host port to save calibration reports to a flash drive and to provide firmware updates.
• Visual Connection Management input terminals illuminate to help show correct cable connection
configurations.
• Soft Power - automatic selection of line voltage/frequency.
• WVGA display with touch-screen and keypad control.
Contact Fluke Calibration
Fluke Corporation operates worldwide. For local contact information, go to our website: www.fluke.com
To register your product, view, print, or download the latest manual or manual supplement, go to our
website.
+1-425-446-5500
info@flukecal.com
Product-Use Information
For Product-use information, please see the 5560A/5550A/5540A/5530A Operators Manual available
online at www.fluke.com.
Safety Information
Safety Information
A Warning identifies conditions and procedures that are dangerous to the user. A Caution identifies
conditions and procedures that can cause damage to the Product or the equipment under test.
General Safety Information is located in the printed 5560A/5550A/5540A/5530A Safety Information
document that ships with the Product. It can also be found online at www.fluke.com. More specific
safety information is listed in this manual where applicable.
Specifications
Safety Specifications are located in the Safety Specifications section of the 5560A/5550A/5540A/
5530A Safety Information manual. Complete specifications are at www.fluke.com. See the 5560A
Product Specifications, 5550 A Product Specifications, or 5540A/5530A Product Specifications.
Service Information
Contact an authorized Fluke Calibration Service Center if the Product needs calibration and verification
or repair during the warranty period. See Contact Fluke Calibration. Please have Product information
such as the purchase date and serial number ready when you schedule a repair.
Operation Overview
Operate the Product from the front panel in the local mode, or remotely with the IEEE-488, RS-232,
USBTMC, or LAN ports. For remote operations, see the 5560A/5550A/5540A/5530A Remote
Programmers Manual at www.fluke.com. Several software options are available to integrate Product
operation into a wide variety of calibration requirements.
Local Operation
Typical local operations include front-panel connections to the Device Under Test (DUT), and then
manual keystroke and touch-screen entries from the front panel that place the Product in the necessary
output mode.
Remote Operation (GPIB)
The Product rear-panel GPIB port is a fully-programmable parallel interface bus meeting the GPIB
(IEEE-488.1) standard and supplemental IEEE-488.2 standard. Under the remote control of an
instrument controller, the Product operates exclusively as a talker/listener. Use the IEEE-488
command set or run MET/CAL software (optional) to write your own programs. See the 5560A/5550A/
5540A/5530A Remote Programmers Manual at www.fluke.com for a discussion of the commands
available for IEEE-488 operation.
Remote Operation (RS-232)
The rear panel RS-232 port is dedicated to serial data communications to operate and control the
Product during calibration and verification procedures complying with the supplemental IEEE-488.2
standard.
The RS-232 serial data port connects a host terminal or personal computer (PC) to the Product. See
the 5560A/5550A/5540A/5530A Remote Programmers Manual at www.fluke.com for a discussion of
the RS-232 commands.
Remote Operation (USBTMC)
The Product rear-panel USB 2.0 type B port is a fully-programmable USBTMC interface that meets the
USBTMC-USB488 interface standard and supplemental IEEE-488.2 standard. Use the USBTMC
command set. See the 5560A/5550A/5540A/5530A Remote Programmers Manual at www.fluke.com
for a discussion of the commands available for USBTMC operation.
Remote Operation (Ethernet)
The Product rear-panel Integrated 10/100/1000BASE-T Ethernet port is for network connection remote
control of the Calibrator and complies with supplemental IEEE-488.2 standard. The Ethernet port
connects a host PC to the Product. To send commands to the Product, enter commands from a telnet
session running on the host computer. See the 5560A/5550A/5540A/5530A Remote Programmers
Manual at www.fluke.com for a discussion of the Ethernet commands available for Ethernet operation.
Prepare the Product for Operation
This section provides instructions to unpack and install the Calibrator and connect to line power.
Instructions for cable connections other than line power can be found here:
• For DUT connections, see Front Panel Operation in the 5560A/5550A/5540A/5530A Operators
Manual.
For remote operation, and these topics, see the 5560A/5550A/5540A/5530A Remote Programmers
Manual at www.fluke.com:
• IEEE-488 parallel interface connection
• RS-232C serial interface connection
• LAN Interface Connections
• USB 2.0 Interface Connections
Theory of Operation

<!-- llm_chunk_end id=service_chunk_0001 -->

<!-- llm_chunk_start id=service_chunk_0002 source=service_manual_5560a source_line_start=241 source_line_end=500 retrieval_priority=high -->

## service_chunk_0002: command set. See the 5560A/5550A/5540A/5530A Remote Programmers Manual at www.fl

command set. See the 5560A/5550A/5540A/5530A Remote Programmers Manual at www.fluke.com
for a discussion of the commands available for USBTMC operation.
Remote Operation (Ethernet)
The Product rear-panel Integrated 10/100/1000BASE-T Ethernet port is for network connection remote
control of the Calibrator and complies with supplemental IEEE-488.2 standard. The Ethernet port
connects a host PC to the Product. To send commands to the Product, enter commands from a telnet
session running on the host computer. See the 5560A/5550A/5540A/5530A Remote Programmers
Manual at www.fluke.com for a discussion of the Ethernet commands available for Ethernet operation.
Prepare the Product for Operation
This section provides instructions to unpack and install the Calibrator and connect to line power.
Instructions for cable connections other than line power can be found here:
• For DUT connections, see Front Panel Operation in the 5560A/5550A/5540A/5530A Operators
Manual.
For remote operation, and these topics, see the 5560A/5550A/5540A/5530A Remote Programmers
Manual at www.fluke.com:
• IEEE-488 parallel interface connection
• RS-232C serial interface connection
• LAN Interface Connections
• USB 2.0 Interface Connections
Theory of Operation
System Architecture
The Product architecture consists of two systems:
• An out-guard system that is earth referenced and contains all digital control, user interface (UI), and
remote interfaces.
• An in-guard system with all precision analog circuitry enclosed in a guard box that is galvanically
isolated.
Out-guard
The out-guard system features:
• Touchscreen display
• Front-panel keypad A2
• A13 interconnect
• A11 out-guard motherboard
• A9 controller.
See the sections below for these individual assemblies.
Theory of Operation
In-guard
From front to back, the in-guard assemblies are:
• A15 terminal indicators
• A14 output switching
• A10 TC
• A3 analog motherboard
• Optional A4 scope option
• A5 impedance
• A6 DDS
• A8 HV amplifiers
• A7 current
• A12 IG power
• Mains transformer secondaries
A14 Output Switching
The A14 contains all the necessary switching for the various functions to the output terminals. The A14
also has some of the circuitry that prevents damage from situations such as connecting the Product
outputs to line voltage or other high-current power supplies. Firmware control is accomplished with an
MSP430 microcontroller via a serial link to the in-guard processor on the A6 DDS. The output terminal
binding posts are directly connected to the A14. This connection eliminates cables and improves the
reproducibility over a number of units.
A3 Motherboard
The A3 motherboard is a simple analog and digital backplane that consists only of thru-hole
connectors, a relay, and a common-mode choke. This assembly was designed to be as simple as
possible to improve reliability and reduce the possibility of manufacturing defects. It interconnects all
the in-guard assemblies and to the A9 out-guard controller.
A4
The A4 board provides the oscilloscope adjustment feature. See Oscilloscope Calibration Option
(600M, 1G, and 2G) Calibration, Verification, and Adjustment. Use this functionality to maintain these
oscilloscope characteristics:
• Voltage Mode
• Edge Mode
• Leveled Sine Wave Mode
• Time Marker Specifications
• Wave Generator Mode
• Pulse Mode
• Spike Trigger Mode
• Input Impedance Mode (Resistance)
• Input Impedance Mode (Capacitance)
• Overload
For explanations of these functions, see the Operators Manual.
A5 Impedance
The A5 provides synthesized equivalents of Resistance, Capacitance, and Inductance. This feature
shares some of the circuitry with the Resistance and Capacitance functions.
A6 DDS
The A6 is the heart of the analog system. The A6 provides digital control for all the in-guard assemblies
through serial links to MSP430s.
The A6 has:
• The precision, ovenized 7 V reference
• Direct Digital dual channel synthesizer (DDS)
• Precision PWM DACs for both voltage and current
• Averaging ac/dc converter for acv
• Sense dividers and buffers for acv and dcv up to 120 V
• The acv/dcv loop error integrator
• A high-resolution adc for calibration, diagnostics, and monitor functions
A7 Current
The A7 contains most of the circuitry that generates the ACI and DCI functions.
These circuits include:
• A low current (120 μA and 1.2 mA ranges) transconductance amplifier
• A mid-current (12 mA and 120 mA ranges) transconductance amplifier
• A high current linear transconductance amplifier for the 1.2 A and 3.1 A ranges
• A class D 30 A transconductance amplifier for the 12 A and 30 A ranges
• Averaging ac/dc converter
• Precision shunts and shunt amplifier
• The loop error integrator
The A6 DDS provides the precision dc reference and the aci waveforms.
A8 High Voltage
The A8 contains all circuits to generate acv and dcv above 12 V.
The A8 is comprised of:
• A 120 V, 100 kHz dc coupled amplifier
• A 1000 V, 10 kHz dc coupled amplifier
The 120V amplifier is also routed through a step-up autotransformer to generate 120 V to 330 V from
10 kHz to 100 kHz. The A8 also contains the sense dividers and buffers for the 330 V and 1000 V
ranges.
A12 Supply
The A12 contains all power supplies for the in-guard circuits.
Calibration and Verification of the Product
Calibration and Verification of the Product
Verification is the process of measurement data evaluation collected during the process of calibration
and evaluating whether the data is within the published specifications for the Product. Verification is
recommended annually for the Product. Calibration and verification should also be done before and
after normal periodic adjustment or repair of the Product. Verification also serves to check that internal
adjustment processes are in control.
Notes
Performance limits specified in the test record tables in this section are based on the 90-day
specifications for the 5560A at a 99 % level of confidence. For the 5550A, 5540A, and 5530A
and/or if limits to other specifications are necessary, the test records must be modified. A
description of how to determine a guardband test limit is included in this section. This manual
is not updated for changes to specifications. Before you do a verification, download the latest
specifications from www.fluke.com.
Equivalent equipment and methods, either manual or automated, may be substituted for the
verification tests as long as the same points are tested, and equipment and standards used
provide for adequate (determined by process requirements) test uncertainty ratio (TUR). If
standards are less accurate than specified, appropriate tolerance limit and/or accuracy
reductions must be made to achieve equivalent results.
The verification points are selected based on knowledge about the hardware and the electronic circuits
of the Product. Although a limited set of the Product capabilities, these calibration and verification
points are adequate to guarantee the performance of the Product for its functions and ranges.
Warmup Procedure for All Verification Tests
Notes
Consider these grounding and guarding suggestions:
• For capacitance and inductance, disconnect the Guard from the Ground strap.
• For all other functions, connect the Guard to ground strap.
• When possible, set to external guard to control the guard of measurement instruments that are
connected to the Product.
Before verification:
1. Verify that the Product has warmed up for at least 30 minutes.
Note
If the Product has been powered off in an environment outside of operating environment
specifications, particularly with humidity above 70 %, allow a minimum of 2 hours for warm-up.
Extended storage at high temperatures and humidity can require up to 4 days of power-on
stabilization.
2. Ensure that the specified warm-up period for all test equipment has been satisfied per operational
requirements.
3. Ensure that the Product is in Standby (STANDBY annunciator lit).
4. Zero the Product. Zeroing adjusts internal circuitry, most notably dc offsets in all ranges of
operation. To meet the specifications, zeroing is required every 7 days, or when the Product
ambient temperature changes by more than 5 °C. There are two Calibrator zero functions: total
instrument zero (ZERO) and ohms-only zero (OHMS ZERO). Before you do the verification tests,
do the total Product zero.
To zero the Product:
1. Turn on the Product and allow a warm-up period of at least 30 minutes.
2. Tap the Setup softkey to open the Setup Menu.
3. Under Zero Adjustment, tap Run to open the calibration activity menu.
4. Push Continue as needed to step through the Zero Adjustment process. Push Abort to exit this
function. When the zero procedure is done (20 minutes), push R to reset the Product.
An abbreviated summary of required equipment for all the verification tests is given in Table 1.
Individual lists of required equipment are included at the beginning of each test. The equipment and
methods selected in this manual are simplified to make it possible to calibrate the Product without
advance metrological techniques and may result in low test uncertainty ratios. Use of guardbanding
techniques is recommended to minimize acceptance risks - see Applying Guardbands to Specification
Limits section in this manual.
Table 1. Required Equipment for Main Output
Equipment Description Manufacture/Model/PN Application
AC Measurement Standard Fluke Calibration 5790B Vac, Iac
Resistance Standards Fluke 742A Series (100, 1 k, 10 k,100 k, 1 M, 10 M) Ohms, Idc
DC Reference Standard Fluke 732C Vdc
Frequency Counter Tektronix FCA3100 (Option MS or HS) Frequency
Shunts Fluke A40B Series (1 mA, 10 mA,100 mA, 1 A, 5 A, 10 A, 20 A, 50 A) Idc, Iac, Phase
Calibrator (precision source) Fluke Calibration 5730A Ohms, Temperature, CapCharge
Resistance Standard MI 9331G/100 M Ohms
Resistance Standard MI 9331G/1 G Ohms
Digital Multimeter Fluke Calibration 8588A Ohms, Idc, Iac, Vdc, Vac,Cap Charge
LCR Meter Hioki IM3533 Capacitance, Inductance
Phase meter Clarke-Hess 6000A Phase
Calibration and Verification of the Product
Equipment Description Manufacture/Model/PN Application
Thermometer Fluke 1504 Temperature
Thermistor probe Fluke 5610-9-B Temperature
Type J thermocouple Omega TJ36-ICIN-18U-8-SMPW-M Temperature
Dewar flask with cap Various Temperature
Type B copper mini-plug
with copper wire Various Temperature
BANANA/DBL BANANA, 2
COND 24 in Pomona 1368-A-24 Idc, Vac
Low Thermal Cables
5730A-7003,TEST LEAD SET, LOW
THERMAL SPADE (Fluke Calibration
PN 4376018)
Various
Double banana RG58 cable Pomona Model 2BC-24 and 2BC-36 Ohms, Idc, Iac, Vdc, Vac
DBL BANANA N (M)
RG58C/U (≈ 16 in) (Fluke PN 900394) 5790-8026 Idc, Iac, Phase
BANANA/DBL BANANA, 2
COND 24 in Pomona 1368-A-24 Idc Zero, Vac AUX
BNC (M) to Binding Posts Pomona Model 1296 Idc, Iac, Phase
BNC (F) to BNC (M) Y
Adapter Pomona Model 6700 Capacitance, Inductance
BNC (F) To Single Banana
Plug Pomona Model 1894 Capacitance, Inductance
Type N (M) to dual banana
(M) E-Z-Hook PN 9415 Idc, Iac, Phase
Type N (M) On 50 Ohm
RG214/U Cable Pomona Model 1658-T Idc, Iac
Fluke 8508A short 4-wire short (Fluke PN 2540973) Vdc
Type N (F) to Type N (F)
adapter Various Idc, Iac
LC Male to LC Male adapter A40B-ADAPT/LC Idc, Iac
LC Female to N Male inter-
series adapter A40B-ADAPT/LCN Idc, Iac
N to 4 mm double banana
cable A40B-LEAD/4 mm Idc, Iac, Phase
Single banana to single
banana lead Various Various
BNC (F) to Type N (M) Pasternack PN PE9002 Ohms
Table 1. Required Equipment for Main Output (cont.)
Determine Specification Limits for other Adjustment Intervals
The verification procedures in this document tests to the 90-day, 99 % confidence specification limits of
the 5560A. For the 5550A, 5540A, and 5530A or for other adjustment intervals, you must calculate
limits based upon the specification that was selected. The subsequent examples show how the 1-year
specification limits are calculated. These examples illustrate how to calculate the specifications limits
for other intervals or levels of confidence.
The first example shows how to calculate a specification limit for a particular test point from the
combined specification which is listed as a percentage (or parts per million) of reading plus a floor error
in microvolts, millivolts, microamps, or nanoamps. The component of the specification in parts per
million is referred to as a range specification. The floor specification has the same base units of
measurement as the output value (volts, amps). Do not add a range specification and floor
specification together directly, because they are not in the same units of measurement. To add the two
quantities, convert one quantity so that they are both in the same unit of measurement.
Example: the 1 year, 99 % confidence specification for the 5560A at 1 mA, 1 kHz is 0.025 % + 100 nA.
Multiply the relative specification by the output value to convert the relative specification to the same
measurement unit as the floor specification:
1 mA x 0.025 % = [(1 x 10-3 ) A x (0.025 x 10-2)] = 2.5 x 10-7 A = 250 nA
This formula makes the combined absolute specification 250 nA + 100 nA = 350 nA
The specification limits at 1 mA would be 0.999650 mA to 1.000350 mA
Applying Guardbands to Specification Limits
The expanded uncertainty of measurement must be determined by each laboratory that calibrates the
Product. Even if the procedures for performance verification in this manual are followed completely,
there are different sources of uncertainty due to traceability, environment, electrical cabling, electro-
magnetic interference, uncertainty of the reference standards used, and operator influences that are
unique to each calibration laboratory. These must be accounted for their individual situations, so it is
not possible for Fluke Calibration to estimate uncertainty for all user calibrations.
Those doing the calibration and verification of the Product can verify to 99 % confidence limits, 95 %
confidence limits, 90-day, 1-year specifications, or 2-year specifications. While the calibration and
verification procedure included in this manual is applicable to testing every test point, the uncertainty
from the calibration and verification process as compared to the specification limit varies and can
require further consideration of measurement decision risk.
Some quality systems require adherence to particular rules for measurement decision risk when
making claims of compliance with a specification.
Examples of decision rules are:
1. The ratio of the specification tested to the expanded uncertainty of measurement (often referred to
as the Test Uncertainty Ratio) must be greater than 4:1.
2. The probability of a false accept risk must be less than 2 %.
3. The Product cannot be determined as meeting specifications unless the measurement at the test
point is less than the value of the specification minus the expanded uncertainty.
To comply with these decision rules, establish a guardband for each test point. A guardband creates a

<!-- llm_chunk_end id=service_chunk_0002 -->

<!-- llm_chunk_start id=service_chunk_0003 source=service_manual_5560a source_line_start=481 source_line_end=740 retrieval_priority=high -->

## service_chunk_0003: The expanded uncertainty of measurement must be determined by each laboratory th

The expanded uncertainty of measurement must be determined by each laboratory that calibrates the
Product. Even if the procedures for performance verification in this manual are followed completely,
there are different sources of uncertainty due to traceability, environment, electrical cabling, electro-
magnetic interference, uncertainty of the reference standards used, and operator influences that are
unique to each calibration laboratory. These must be accounted for their individual situations, so it is
not possible for Fluke Calibration to estimate uncertainty for all user calibrations.
Those doing the calibration and verification of the Product can verify to 99 % confidence limits, 95 %
confidence limits, 90-day, 1-year specifications, or 2-year specifications. While the calibration and
verification procedure included in this manual is applicable to testing every test point, the uncertainty
from the calibration and verification process as compared to the specification limit varies and can
require further consideration of measurement decision risk.
Some quality systems require adherence to particular rules for measurement decision risk when
making claims of compliance with a specification.
Examples of decision rules are:
1. The ratio of the specification tested to the expanded uncertainty of measurement (often referred to
as the Test Uncertainty Ratio) must be greater than 4:1.
2. The probability of a false accept risk must be less than 2 %.
3. The Product cannot be determined as meeting specifications unless the measurement at the test
point is less than the value of the specification minus the expanded uncertainty.
To comply with these decision rules, establish a guardband for each test point. A guardband creates a
zone that is less than the specification limits, and if the measured value obtained from the calibration
and verification is not in the guardband area, the level of measurement decision risk is sufficient. The
inner edge of the guardband is the test limit for the adjustment shown in Figure 2.
Calibration and Verification of the Product
Figure 2. Test Limits Established by Guardbanding
There are many ways to develop test limits from decision rules. Two of these rules are shown as
examples to develop test limits through guardbanding.
ILAC G8 (ISO 14253-1) Decision Rule
In this guardband strategy example, determine the test limit by the subtracting the uncertainty of the
measurement from the specification.
Test Limit = Specification Limit - Expanded Uncertainty of Measurement
Obtain the specification limits from the performance verification procedure or compute them with
information from Determine Specification Limits for other Adjustment Intervals as guidance.
Once the calibration laboratory determines the expanded uncertainty for a measurement, compute the
test limits for this method as follows:
Using the example test point in the previous section, for the 1-year, 99 % confidence specification for
1 mA at 1 kHz, the specification limits are 350 nA. If for example, the expanded uncertainty of
measurement at this test point was 55 nA, the test limit would be:
Test Limit = 350 nA - 55 nA = 295 nA
This creates upper and lower test limits of 0.999705 mA to 1.000295 mA. If the measured value from
the calibration and verification were between these limits, by this decision rule the Product would be in
tolerance or indicated as Pass.
If the measured value obtained was between 295 nA (the test limit) and 350nA (the specification limit)
this is known as an indeterminate measurement by ISO 14253-1. Some organizations elect to call this
a conditional pass as it is more likely that the measurement indicates an in tolerance condition than not.
GuardbandRegionGuardbandRegion
STD
UUT
-SL TL Nom Meas + TL + SL
If the measured value is >350 nA, but <405 nA (the sum of the specification limit plus the uncertainty)
ISO 14243-1 indicates that this is an indeterminate measurement as well. Some organizations choose
to call this a conditional fail because there is still a possibility that the measurement is in tolerance.
Most organizations consider this an out of tolerance result because although the value may exist
anywhere with the interval of the measured value plus and minus the uncertainty, the best estimate of
the value is the measured value.
RDS Method
Another guardbanding method that is the root difference of squares method. The test limit for this
method is defined as:
This method makes a less aggressive guardband while it still provides sufficient confidence in the
measurement result for most quality standards. The determination of pass and conditional pass is
generally used for this method in the same manner as the ILAC G8 method. Fluke Calibration and
other companies use the RDS method as a reasonable approach to ensure confidence that the verified
Product meets its published specifications.
This is not an all-inclusive list of guardbanding strategies. The method selected must meet the quality
system requirements of the owner of the Product being calibrated. The best uncertainty attainable at
some test points can be relatively large as compared to the specification. Fluke Calibration
recommends that when making conformity assessment decisions of in or out of tolerance to published
specifications during performance verification, the uncertainties of measurement should be evaluated
and appropriate guardbanding rules should be applied to have sufficient confidence in the adjustment
results.
Volts DC Calibration and Verification (OUTPUT VZ)
Table 2 lists the required equipment.
To calibrate the Volts dc function from the main output (see Table 3):
1. On the Fluke Calibration 8588A put a 4-wire short (Fluke PN 2540973) across the HI and LO input
and sense terminals.
2. Set the 8588A as follows: Volts dc, Range Auto, NPLC 50, Guard ON (external guard)
3. Push ZERO, and then ZERO FUNC. Allow the zero function to finish.
4. Make sure that the DUT (Device Under Test) is in STBY.
5. Complete an internal DC Zero Calibration on the Product.
6. Record the 732C standard values in the Vstd column.
Table 2. Required Equipment for Volts DC (Normal Output)
Equipment Description Manufacture/Model/PN Quantity
Digital Multimeter Fluke Calibration 8588A 1
DC Reference Standard Fluke Calibration 732C 1
Fluke 8508A short 4-wire short (Fluke PN 2540973) 1
Low Thermal Cables 5730A-7003 1
Test Limit= √ (Specification limit)2 - (Expanded Uncertainty of Measurement)2
Calibration and Verification of the Product
7. Connect the 8588A for vdc measurement with the low thermal cable to the 732C 100 mV (normal
polarity).
8. Record the 8588A measurement in the Vdmm_732C column for applicable steps.
9. Inverse the cable at the 732C 100 mV (negative polarity).
10. Record 8588A measurement in the Vdmm_732C column for applicable steps.
11. Connect the 8588A for vdc measurement with the low thermal cable to the 732C 1 V (normal
polarity).
12. Record the 8588A measurement in the Vdmm_732C column for applicable steps.
13. Inverse the cable at the 732C 1 V (negative polarity).
14. Record the 8588A measurement in the Vdmm_732C column for applicable steps.
15. Connect the 8588A for vdc measurement with the low thermal cable to the 732C 10 V (normal
polarity).
16. Record the 8588A measurement in the Vdmm_732C column for applicable steps.
17. Inverse the cable at the 732C 10 V (negative polarity).
18. Record the 8588A measurement in the Vdmm_732C column for applicable steps.
19. Connect the test equipment as shown in Figure 3.
20. Connect a strap between the Guard and Ground terminals of the DUT.
21. Output from the DUT/Measure with the meter and record the 8588A measured values when
connected to the Product in the Vdmm_prod column. Refer to the Product manual for how to set
and use range lock on the bottom range outputs.
Figure 3. Volts DC Calibration and Verification Direct
22. For steps other than ±100 mV, ±1 V, and ±10 V the output of the Product is the same as the 8588A
measurement recorded directly when connected to the Product output DMM Reading on Product
column. Copy the value to the Calculated Product Output column.
5560A 8588A
23. For the rest of the steps, calculate the Product output with this formula:
24. With the entire table populated, evaluate each step for compliance to limits. To apply
Guardbanding, create a table from the example in this manual, where the acceptance limits are
properly modified by your Guardbanding method.
Table 3. Calibration and Verification Steps for Volts DC (OUTPUT VZ)
Step ProductRangeProductOutput732C Value(Vstd)
DMM Reading
on 732C
(Vdmm_732C)
DMM Reading
on Product
(Vdmm_prod)
Calculated
Product
Output
Limits
1 120 mV 0 mV N/A N/A ±0.80 μV
2 120 mV -0.00001 mV N/A N/A ±0.80 μV
3 120 mV 10 mV N/A N/A ±0.90 μV
4 120 mV -10 mV N/A N/A ±0.90 μV
25 120 mV 100 mV ±1.8 μV
26 120 mV -100 mV ±1.8 μV
5 1.2 V 0 V N/A N/A ±1.0 μV
6 1.2 V -0.0000001 V N/A N/A ±1.0 μV
27 1.2 V 0.1 V ±1.7 μV
28 1.2 V -0.1 V ±1.7 μV
29 1.2 V 1 V ±7.6 μV
30 1.2 V -1 V ±7.6 μV
7 12 V 0 V N/A N/A ±10.0 μV
8 12 V -0.000001 V N/A N/A ±10.0 μV
31 12 V 1 V ±17 μV
32 12 V -1 V ±17 μV
33 12 V 10 V ±75 μV
34 12 V -10 V ±75 μV
9 120 V 0 V N/A N/A ±0.10 mV
10 120 V -0.00001 V N/A N/A ±0.10 mV
35 120 V 10 V ±0.19 mV
V Dmm
V Dmm
product
732C
Calculated Product Output = V std *
Calibration and Verification of the Product
Volts DC Calibration and Verification (AUX Output) (5530A, 5550A, and 5560A)
Table 4 lists the required equipment.
To calibrate the Volts dc function from the secondary output:
1. On the Fluke Calibration 8588A put a 4-wire short (Fluke PN 2540973) across the HI and LO input
and sense terminals.
2. Set the 8588A as follows: Volts dc, Range Auto, NPLC 50, Guard ON (external guard).
3. Push ZERO, and then ZERO FUNC. Allow the zero function to finish.
4. Make sure that the DUT is in STBY.
5. Complete an internal DC Zero Calibration on the Product.
6. Connect the test equipment as shown in Figure 4.
Step ProductRangeProductOutput732C Value(Vstd)
DMM Reading
on 732C
(Vdmm_732C)
DMM Reading
on Product
(Vdmm_prod)
Calculated
Product
Output
Limits
36 120 V -10 V ±0.19 mV
11 120 V 100 V N/A N/A ±1.03 mV
12 120 V -100 V N/A N/A ±1.03 mV
13 120 V 120 V N/A N/A ±1.22 mV
14 120 V -120 V N/A N/A ±1.22 mV
15 1020 V 0 V N/A N/A ±1.00 mV
16 1020 V -0.0001 V N/A N/A ±1.00 mV
17 1020 V 100 V N/A N/A ±1.9 mV
18 1020 V -100 V N/A N/A ±1.9 mV
19 1020 V 500 V N/A N/A ±5.7 mV
20 1020 V -500 V N/A N/A ±5.7 mV
21 1020 V 1000 V N/A N/A ±10.3 mV
22 1020 V -1000 V N/A N/A ±10.3 mV
23 1020 V 1020 V N/A N/A ±10.5 mV
24 1020 V -1020 V N/A N/A ±10.5 mV
Table 4. Required Equipment for Volts DC (AUX Output)
Equipment Description Manufacture/Model/PN Quantity
Digital Multimeter Fluke Calibration 8588A 1
Fluke 8508A short 4-wire short (Fluke PN 2540973) 1
Low Thermal Cables 5730A-7003 1
Table 3. Calibration and Verification Steps for Volts DC (OUTPUT VZ) (cont.)
Figure 4. Volts DC SENSE Output
7. Connect a strap between the Guard and Ground terminals of the DUT.
8. Output from the DUT/Measure with the meter and record the 8588A measured values when
connected to the Product in the Product Output column, see Table 5.
9. With the entire table populated, evaluate each step for compliance to limits. To apply
Guardbanding, create a table from the example in this manual, where the acceptance limits are
properly modified by your Guardbanding method.
Table 5. Calibration and Verification Steps for Volts dc (AUX Output)
Step
Product
Output
(OUTPUT VZ)
Product
Range (AUX
Output)
Product
Output (AUX
Output)
Product
Output Limits
1 1 V 120 mV 0 mV ±0.30 mV
2 -1 V 120 mV 120 mV ±0.34 mV
3 1 V 120 mV -120 mV ±0.34 mV
4 -1 V 1.2 V 0.121 V ±0.34 mV
5 1 V 1.2 V -0.121 V ±0.34 mV
6 -1 V 1.2 V 1.2 V ±0.66 mV
7 1 V 1.2 V -1.2 V ±0.66 mV
8 -1 V 7 V 1.21 V ±0.66 mV
9 1 V 7 V -1.21 V ±0.66 mV
10 -1 V 7 V 7 V ±2.40 mV
11 1 V 7 V -7 V ±2.40 mV
5560A 8588A
Calibration and Verification of the Product
Amps DC Calibration and Verification
Table 6 lists the required equipment.
To calibrate the Amps dc function (subsequent amps dc calibration and verification steps, see Table 7):
1. Set the 8588A as follows: Volts dc, Range Auto, NPLC 50, Guard ON (external guard).
2. Make sure that the DUT is in STBY.
3. Connect a strap between the Guard and Ground terminals of the DUT.
4. Complete an internal DC Zero Calibration on the Product.
5. Calculate the shunt resistance in Ω from the calibration records and/or regression analysis for all
shunts listed in Table 7.
6. Record the shunt resistance in the Shunt_R Ω column in Table 7.
7. Connect the 8588A for V dc measurement with the low thermal cable to Fluke 742A-1k SENSE See
Figure 5.
Table 6. Required Equipment for Amps DC
Equipment Description Manufacture/Model/PN Quantity
Digital Multimeter Fluke Calibration 8588A 1
±(0 μA to 100 μA) Fluke 742A-1k Resistance Standard 1
±(1 mA to 1.2 mA) Fluke A40B-1mA Current Shunt 1
±(10 mA to 12 mA) Fluke A40B-10mA Current Shunt 1
±(100 mA to 120 mA) Fluke A40B-100mA Current Shunt 1
±(1 A to 1.2 A) Fluke A40B-1A Current Shunt 1
±3 A Fluke A40B-5A Current Shunt 1
±10 A Fluke A40B-10A Current Shunt 1
±(12 A to 20 A) Fluke A40B-20A Current Shunt 1
±30 A Fluke A40B-50A Current Shunt 1
Type N (M) to dual banana (M) E-Z-Hook PN 9415 1
Type N (F) to Type N (F) adapter Various 1
LC Male to LC Male adapter A40B-ADAPT/LC 1
LC Female to N Male inter-series adapter A40B-ADAPT/LCN 1
N to 4 mm double banana connector A40B-LEAD/4mm 1

<!-- llm_chunk_end id=service_chunk_0003 -->

<!-- llm_chunk_start id=service_chunk_0004 source=service_manual_5560a source_line_start=721 source_line_end=980 retrieval_priority=normal -->

## service_chunk_0004: 6. Record the shunt resistance in the Shunt_R Ω column in Table 7.

6. Record the shunt resistance in the Shunt_R Ω column in Table 7.
7. Connect the 8588A for V dc measurement with the low thermal cable to Fluke 742A-1k SENSE See
Figure 5.
Table 6. Required Equipment for Amps DC
Equipment Description Manufacture/Model/PN Quantity
Digital Multimeter Fluke Calibration 8588A 1
±(0 μA to 100 μA) Fluke 742A-1k Resistance Standard 1
±(1 mA to 1.2 mA) Fluke A40B-1mA Current Shunt 1
±(10 mA to 12 mA) Fluke A40B-10mA Current Shunt 1
±(100 mA to 120 mA) Fluke A40B-100mA Current Shunt 1
±(1 A to 1.2 A) Fluke A40B-1A Current Shunt 1
±3 A Fluke A40B-5A Current Shunt 1
±10 A Fluke A40B-10A Current Shunt 1
±(12 A to 20 A) Fluke A40B-20A Current Shunt 1
±30 A Fluke A40B-50A Current Shunt 1
Type N (M) to dual banana (M) E-Z-Hook PN 9415 1
Type N (F) to Type N (F) adapter Various 1
LC Male to LC Male adapter A40B-ADAPT/LC 1
LC Female to N Male inter-series adapter A40B-ADAPT/LCN 1
N to 4 mm double banana connector A40B-LEAD/4mm 1
DBL BANANA N (M) RG58C/U (≈ 16 in) (Fluke PN 900394) 5790-8026 1
Test Lead Banana to Banana 24 in Pomona 1368-A-24 1
Low Thermal Cables Fluke 5730-7003 1
Figure 5. Amps DC with 742A-1k - Meter Zero
8. On the 8588A, push ZERO, and then ZERO FUNC. Allow the zero function to finish.
9. Connect the test equipment as shown in Figure 6.
10. Output from the DUT/Measure with the meter and record the 8588A measured values in the DMM
Reading on Shunt Output [V] column. Complete all steps for the present connection (Table 7,
steps 1 to 20). Refer to the Product manual how to set and use range lock on bottom of range
outputs.
11. Set the Product to STBY.
12. Move the red lead connected to the Product V AUX to the 30 A terminal.
13. Complete the subsequent steps for this connection (Table 7, 21, and 22). See the Product manual
for how to set and use range lock on bottom of range outputs.
Figure 6. Amps DC with742A-1k
742A-1k Resistance Standard
CURRENT SENSEHI HI
LO LONOMINAL VALUE = 1 KΩ
TEMPERATURE RANGE: 18 °C TO 28 °CMAXIMUM VOLTAGE = 10 VDCMAXIMUM CURRENT = 0.01 A ‘
CHASSISGROUND
742A-1k
8588A
742A-1k Resistance Standard
CURRENT SENSEHI HI
LO LONOMINAL VALUE = 1 KΩ
TEMPERATURE RANGE: 18 °C TO 28 °CMAXIMUM VOLTAGE = 10 VDCMAXIMUM CURRENT = 0.01 A ‘
CHASSISGROUND
5560A 8588A
742A-1k
Calibration and Verification of the Product
14. Connect the test equipment as shown in Figure 7.
15. Toggle the power switch of the A40B-1mA shunt to ON. Continue only if power light illuminates and
the BATT LOW is off.
16. With no current applied from the Product to the Fluke A40B-1mA shunt, proceed with the zero
meter function. On the 8588A, push ZERO, and then ZERO FUNC. Allow the zero function to finish.
17. Start with Table 7, step 23. Set the output from the DUT/Measure with the meter and record the
8588A measured value in the DMM Reading on Shunt Output [V] column. Complete all steps for
the present connection (Table 7, steps 23 to 26). Refer to the Product manual for how to set/use
range lock on bottom of range outputs.
Figure 7. Amps DC with A40B-1mA
18. Set the Product to STBY. Disconnect the shunt. Toggle the power switch of the A40B-1mA shunt to
OFF.
19. Connect the test equipment as shown in Figure 8.
20. With no current applied from the Product to the Fluke A40B-10mA shunt, proceed with the zero
meter function. On the 8588A, push ZERO, and then ZERO FUNC. Allow the zero function to finish.
21. Start with Table 7, step 27 and output from the DUT/Measure with the meter and record the 8588A
measured value in the DMM Reading on Shunt Output [V] column. Complete all steps for the
present connection (Table 7, steps 27 to 30). Refer to the Product manual for how to set and use
range lock on bottom of range outputs.
A40B-1mA
INPUTOUTPUT
5560A 8588A
A40B-1mA
Figure 8. Amps DC with A40B-10mA
22. Set the Product to STBY. Disconnect the shunt. Connect the test equipment as shown in Figure 9.
23. With no current applied from the Product to the Fluke A40B-100mA shunt, proceed with the zero
meter function. On the 8588A, push ZERO, and then ZERO FUNC. Allow the zero function to finish.
24. Start with Table 7, step 31. Set the output from the DUT/Measure with the meter and record the
8588A measured value in the DMM Reading on Shunt Output [V] column. Complete all steps for
the present connection (Table 7, steps 31 to 34). Refer to the Product manual for how to set/use
range lock on bottom of range outputs.
Figure 9. Amps DC with A40B-100mA
A40B-10mA
INPUTOUTPUT
5560A 8588A
A40B-10mA
5560A 8588A
A40B-100mA
Calibration and Verification of the Product
25. Set the Product to STBY. Disconnect the shunt. Connect the test equipment as shown in Figure 10.
26. With no current applied from the Product to the Fluke A40B-1A shunt, proceed with the zero meter
function. On the 8588A, push ZERO, and then ZERO FUNC. Allow the zero function to finish.
27. Start with Table 7, step 35. Set the output from the DUT and wait 30 seconds for the reading to
settle. Measure with the meter and record the 8588A measurement in the DMM Reading on Shunt
Output [V] column. Complete all steps for the present connection (Table 7, steps 35 to 38). Refer
to the Product manual for how to set and use range lock on the bottom of range outputs.
28. Set the Product to STBY.
29. Move the red lead connected to the Product V AUX to the 30 A terminal.
30. Complete the subsequent Table 7, steps 39 and 40 for this connection.
Figure 10. Amps DC with A40B-1A
31. Set the Product to STBY. Disconnect the shunt. Connect the test equipment as shown in Figure 11.
32. With no current applied from the Product to the Fluke A40B-5A shunt, proceed with the meter zero
function. On the 8588A Push INPUT, and then ZERO FUNC. Allow the zero function to finish.
33. Start with Table 7, step 41. Set the output from the DUT and wait 30 seconds the reading to settle.
Measure with the meter and record the 8588A measured value in the DMM Reading on Shunt
Output [V] column. Complete both steps for the present connection (Table 7, steps 41 and 42).
34. Set the Product to STBY.
5560A 8588A
A40B-1A
INPUT OUTPUT
Figure 11. Amps DC with A40B-5A
35. Set the Product to STBY. Disconnect the shunt. Connect the test equipment as shown in Figure 12.
36. With no current applied from the Product to the Fluke A40B-10A shunt, proceed with the meter zero
function. On the 8588A, push ZERO, and then ZERO FUNC. Allow th zero function to finish.
37. Start with Table 7, step 43. Set the output from the DUT, wait 2 minutes for settling and measure
with the meter and record the 8588A measurement in the DMM Reading on Shunt Output [V]
column. Complete both steps for the present connection (Table 7, steps 43 and 44). Refer to the
Product manual for how to set/use range lock on bottom of range outputs.
Figure 12. Amps DC with A40B-10A
38. Set the Product to STBY. Disconnect the shunt. Connect the test equipment as shown in Figure 13.
5560A 8588A
INPUT
A40B-5A
OUTPUT
5560A 8588A
INPUT
A40B-10A
OUTPUT
Calibration and Verification of the Product
39. With no current applied from the Product to the Fluke A40B-20A shunt, proceed with the meter zero
function. On the 8588A, push ZERO, and then ZERO FUNC. Allow the zero function to finish.
40. Start with Table 7, step 45. Set the output from the DUT and wait 3 minutes for settling. Measure
with the meter and record the 8588A measured value in the DMM Reading on Shunt Output [V]
column. Complete the steps for the present connection (Table 7, steps 45 to 50). Refer to the
Product manual how to set and use range lock on bottom of range outputs.
Figure 13. Amps DC with A40B-20A
41. Set the Product to STBY. Disconnect the shunt. Connect the test equipment as shown in Figure 14.
42. With no current applied from the Product to the Fluke A40B-50A shunt, proceed with the meter zero
function. On the 8588A, push ZERO, and then ZERO FUNC. Allow the zero function to finish.
43. Start with Table 7, step 51. Set the output from the DUT and wait 3 minutes for settling. Measure
with the meter and record the 8588A measured in the DMM Reading on Shunt Output [V]
column. Complete both steps for the present connection (Table 7, steps 51 and 52). Refer to the
Product manual how to set/use range lock on bottom of range outputs.
INPUT
A40B-20A
OUTPUT
5560A 8588A
INPUT
A40B-20A
OUTPUT
Figure 14. Amps DC with A40B-50A
44. For all A dc steps, calculate the output with the formula below. Use the appropriate conversion to
convert from base units to units for the specific evaluation step.
45. With the entire table populated, evaluate each step for compliance to limits. To apply
Guardbanding, create a table from the example in this manual, where the acceptance limits are
properly modified by your Guardbanding method.
Table 7. Calibration and Verification Steps for Amps DC
Step ProductRangeProductOutput Shunt Shunt_R[Ω]
DMM
Reading
on Shunt
Output
[V]
Calculated
Product
Output
Limits
1 120 μA 0 μA Fluke 742A-1k ±6.0 nA
2 120 μA -0.0001 μA Fluke 742A-1k ±6.0 nA
3 120 μA 10 μA Fluke 742A-1k ±7.0 nA
4 120 μA -10 μA Fluke 742A-1k ±7.0 nA
5 120 μA 100 μA Fluke 742A-1k ±16.0 nA
6 120 μA -100 μA Fluke 742A-1k ±16.0 nA
7 1.2 mA 0 mA Fluke 742A-1k ±15.0 nA
8 1.2 mA -0.000001 mA Fluke 742A-1k ±15.0 nA
5560A 8588A
INPUT
A40B-50A
OUTPUT
Calculated Product Output = DMM Reading on Shunt output [V]
Shunt_R []
Calibration and Verification of the Product
Step ProductRangeProductOutput Shunt Shunt_R[Ω]
DMM
Reading
on Shunt
Output
[V]
Calculated
Product
Output
Limits
9 1.2 mA 0.1 mA Fluke 742A-1k ±23.0 nA
10 1.2 mA -0.1 mA Fluke 742A-1k ±23.0 nA
23 1.2 mA 1 mA Fluke A40B-1mA ±95.0 nA
24 1.2 mA -1 mA Fluke A40B-1mA ±95.0 nA
11 12 mA 0 mA Fluke 742A-1k ±0.08 μA
12 12 mA -0.00001 mA Fluke 742A-1k ±0.08 μA
25 12 mA 1 mA Fluke A40B-1mA ±0.16 μA
26 12 mA -1 mA Fluke A40B-1mA ±0.16 μA
27 12 mA 10 mA Fluke A40B-10mA ±0.88 μA
28 12 mA -10 mA Fluke A40B-10mA ±0.88 μA
13 120 mA 0 mA Fluke 742A-1k ±0.80 μA
14 120 mA -0.0001 mA Fluke 742A-1k ±0.80 μA
29 120 mA 10 mA Fluke A40B-10mA ±2 μA
30 120 mA -10 mA Fluke A40B-10mA ±2 μA
31 120 mA 100 mA Fluke A40B-100mA ±9 μA
32 120 mA -100 mA Fluke A40B-100mA ±9 μA
15 1.2 A 0 A Fluke 742A-1k ±10 μA
16 1.2 A -0.000001 A Fluke 742A-1k ±10 μA
33 1.2 A 0.1 A Fluke A40B-100mA ±23 μA
34 1.2 A -0.1 A Fluke A40B-100mA ±23 μA
35 1.2 A 1 A Fluke A40B-1A ±140 μA
36 1.2 A -1 A Fluke A40B-1A ±140 μA
17 3.1 A 0 A Fluke 742A-1k ±150 μA
18 3.1 A -0.00001 A Fluke 742A-1k ±150 μA
37 3.1 A 1 A Fluke A40B-1A ±390 μA
38 3.1 A -1 A Fluke A40B-1A ±390 μA
Table 7. Calibration and Verification Steps for Amps DC (cont.)
Resistance Calibration and Verification
The verification points for resistance are selected based on knowledge about the hardware and the
electronic circuits in the Product. The resistance section uses:
• Different measurement modes. For resistance up to and including 100 kΩ the measurements are
performed in four-wire mode (4W). The rest of the measurements are performed in two-wire mode
(2W).
• Different measurement methods are used: Direct and Transfer from resistance standards (whenever
the TUR is low).
• Different resistance modes. Because of Product compliance (Operating Characteristics) certain
steps require the Fluke Calibration 8588A to be used in Low Current Mode (LoI) to reduce the
current into the Product.
For all resistance steps: Toggle the meter to the Volts dc function prior to putting the Product in operate
mode. Toggle the meter to the resistance function and range as instructed in the section below after
the Product is in operate. Failure to follow this sequence results in compliance-limits error on the
Product.
Step ProductRangeProductOutput Shunt Shunt_R[Ω]
DMM
Reading
on Shunt
Output
[V]
Calculated
Product
Output
Limits
41 3.1 A 3.1 A Fluke A40B-5A ±0.894 mA
42 3.1 A -3.1 A Fluke A40B-5A ±0.894 mA
19 12 A 0 A Fluke 742A-1k ±0.250 mA
20 12 A -0.00001 A Fluke 742A-1k ±0.250 mA
39 12 A 1 A Fluke A40B-1A ±490 μA
40 12 A -1 A Fluke A40B-1A ±490 μA
43 12 A 10 A Fluke A40B-10A ±2.650 mA
44 12 A -10 A Fluke A40B-10A ± 2.650 mA
45 12 A 12 A Fluke A40B-20A ± 3.13 mA
46 12 A -12 A Fluke A40B-20A ± 3.13 mA
21 30.2 A 0 A Fluke 742A-1k ± 0.50 mA
22 30.2 A -0.0001 A Fluke 742A-1k ± 0.50 mA
47 30.2 A 12.1 A Fluke A40B-20A ± 10.2 mA
48 30.2 A -12.1 A Fluke A40B-20A ±10.2 mA
49 30.2 A 20 A Fluke A40B-20A ±16.5 mA
50 30.2 A -20 A Fluke A40B-20A ±16.5 mA

<!-- llm_chunk_end id=service_chunk_0004 -->

<!-- llm_chunk_start id=service_chunk_0005 source=service_manual_5560a source_line_start=961 source_line_end=1220 retrieval_priority=normal -->

## service_chunk_0005: Calculated

Calculated
Product
Output
Limits
41 3.1 A 3.1 A Fluke A40B-5A ±0.894 mA
42 3.1 A -3.1 A Fluke A40B-5A ±0.894 mA
19 12 A 0 A Fluke 742A-1k ±0.250 mA
20 12 A -0.00001 A Fluke 742A-1k ±0.250 mA
39 12 A 1 A Fluke A40B-1A ±490 μA
40 12 A -1 A Fluke A40B-1A ±490 μA
43 12 A 10 A Fluke A40B-10A ±2.650 mA
44 12 A -10 A Fluke A40B-10A ± 2.650 mA
45 12 A 12 A Fluke A40B-20A ± 3.13 mA
46 12 A -12 A Fluke A40B-20A ± 3.13 mA
21 30.2 A 0 A Fluke 742A-1k ± 0.50 mA
22 30.2 A -0.0001 A Fluke 742A-1k ± 0.50 mA
47 30.2 A 12.1 A Fluke A40B-20A ± 10.2 mA
48 30.2 A -12.1 A Fluke A40B-20A ±10.2 mA
49 30.2 A 20 A Fluke A40B-20A ±16.5 mA
50 30.2 A -20 A Fluke A40B-20A ±16.5 mA
51 30.2 A 30 A Fluke A40B-50A ±24.5 mA
52 30.2 A -30 A Fluke A40B-50A ±24.5 mA
Table 7. Calibration and Verification Steps for Amps DC (cont.)
Calibration and Verification of the Product
Table 8 lists the required equipment.
The instructions in this section and the measurement sequence is structured to use common settings,
modes, and methods to simplify the calibration function.
To calibrate the Resistance function:
1. Make sure that the DUT is in STBY.
2. Set the 8588A as follows: Resistance 4Wire, LoI OFF, Range (as per Table 10), NPLC 50, Guard
OFF (external guard light ring off). Set the meter to DC Voltage temporarily to prevent compliance
limit errors on the Product.
3. Connect a strap between the Guard and Ground terminals of the DUT.
4. Connect the test equipment as shown in Figure 15.
5. Start with step 1 in Table 10. Set the output from the DUT 4W Resistance. Measure with the meter
and record the 8588A measured value in the DMM Measurement on Product column in Table 10.
Change the meter range for each step. Complete all steps for the present connection and meter
setup (Table 10, steps 1 to 14).
Figure 15. Resistance 4W with 8588A
Table 8. Required Equipment for Resistance
Equipment Description Manufacture/Model/PN Quantity
Digital Multimeter Fluke Calibration 8588A 1
Resistance Standard Fluke 742A-100k 1
Resistance Standard Fluke 742A-1M 1
Resistance Standard Fluke 742A-10M 1
Resistance Standard MI 9331G/100 M 1
Resistance Standard MI 9331G/1 G 1
Low Thermal Cables Fluke Calibration 5730A-7003 1
Double banana RG58 cable Pomona Model 2BC-24 and 2BC-36 1
BNC (F) to Type N (M) Pasternack PN PE9002 2
BNC (F) To Single Banana Plug Pomona Model 1894 1
Resistance Standard. Fluke 742-10k 1
5560A 8588A
6. Set the Product to STBY.
7. Connect the 8588A to Fluke 742A-100k for 4-Wire measurement.
8. Set the 8588A as follows: Resistance 4Wire, LoI OFF, Range (as per Table 10), NPLC 50, Guard
OFF (external guard light ring off).
9. Record the following measurements in step 15 of Table 10.
10. Measure with the meter and record the 8588A measured value in the DMM Measurement on
Transfer Resistor column in Table 10.
11. Disconnect the 8588A from the resistor standard and connect the cables to the Product for 4W
measurement. Set the meter temporarily to the Volts dc Function.
12. Set the Product to output 100 kΩ. Set meter to the Resistance function. Measure with the meter
and record the 8588A measured value in the DMM Measurement on Product column in Table 10.
13. Set the Product to STBY.
14. Set the 8588A as follows: Resistance 4Wire, LoI ON, Range (as per Table 10.), NPLC 50, Guard
OFF (external guard light ring off).
15. Record the following measurements in Table 10, step 16.
16. Measure with the meter and record the 8588A measured value in the DMM Measurement on
Transfer Resistor column in Table 10.
17. Connect the 8588A to the Product for 2-Wire measurement. Connect the cable between the meter
and DUT guard terminals.
18. Set the 8588A as follows: Resistance 2Wire, LoI ON, Range Auto, NPLC 50, Guard OFF (external
guard light ring off). Set temporarily to the Volts dc Function.
19. Set the Product to output 121 kΩ. Set the meter to the Resistance function. Measure with the meter
and record the 8588A measured value in the DMM Measurement on Product column in Table 10.
20. Set the Product to STBY.
21. Connect the 8588A to Fluke 742A-1M for 2-Wire measurement.
22. Measure with the meter and record the 8588A measured value in the DMM Measurement on
Transfer Resistor column in Table 10.
23. Disconnect the 8588A from the resistor standard and connect the cables to the Product for 2-W
measurement.
24. Set the Product to output 1 MΩ. Measure with the meter and record the 8588A measured value in
the DMM Measurement on Product column in Table 10, step 17.
25. Set the Product to STBY.
26. Complete Table 10, steps 18 to 22 and follow the same sequence for 2W, where the meter
measures a resistor following by the Product measurement. For all steps, connect the cable
between meter and resistor guard terminals.
27. The subsequent section (Table 10, steps 23 to 26) uses characterization and linearization of the
8588A 1 GΩ range at 100 MΩ and 1 GΩ.
28. Input the values for both standards in the Transfer Value column in Table 9.
29. Set the 8588A as follows: Resistance 2Wire, LoI OFF, Range 1 G, NPLC 50, Guard OFF (external
guard light ring off).
Calibration and Verification of the Product
30. Connect the 8588A to 100 MΩ standard for 2-Wire measurement. Use appropriate adapters at the
resistor standard to accommodate the connection.
31. Measure with the meter and record the 8588A measured value in the DMM Measurement on
Transfer Resistor column in Table 9, step 1.
32. Connect the 8588A to 1 GΩ standard for 2-Wire measurement. Use appropriate adapters at the
resistor standard to accommodate the connection.
33. Measure with the meter and record the 8588A measured value in the DMM Measurement on
Transfer Resistor column in Table 9, step 5.
Build the following formulas in Excel to calculate the Linear error of the meter at each point for
Table 9, steps 2 to 5.
Meter error at 0.1 GΩ:
Meter error at 1 GΩ:
Calculate the Meter error (Linear Interpolation) with this formula:
where X0 =0.1 and X1=1 and X is the value from the Product Output column in Table 9 for each step.
34. Connect the existing setup used for high resistance to the Product for 2-W measurements and
complete Table 10, steps 23 to 26.
Table 9. 8588A 1G W Range Characterization
Step 8588ARangeProductOutputTransferResistor Transfer Value
DMM
Measurement
on Transfer
Resistor
Meter Error
(Linear Error)
DMMErr_ppm
1 1.2 GΩ 0.1 GΩ MI 9331G/100 M GΩ GΩ N/A
2 1.2 GΩ 0.3 GΩ N/A N/A N/A μΩ/Ω
3 1.2 GΩ 0.4 GΩ N/A N/A N/A μΩ/Ω
4 1.2 GΩ 0.64 GΩ N/A N/A N/A μΩ/Ω
5 1.2 GΩ 1 GΩ MI 9331G/1 G GΩ GΩ μΩ/Ω
Y 0 = (DMM meas-0.1GW -0.1GΩRvalue)
0.1GΩRvalue
106 []
Y 1 = ( DMM meas-1GΩ-1GΩRvalue)
1GΩRvalue
106 [m/]
Y = Y 0 (X1 -X)+Y1 (X-X0)
X1 -X0
35. Connect the Product, the system 5730A, and the 8588A as shown on Figure 16.
36. Disconnect the V-Guard to Ground strap on the 5730A. The DUT strap should still be connected.
37. Set the 8588A as follows: Resistance 2Wire, LoI OFF, Range (as per Table 10), NPLC 50, Guard
OFF (external guard light ring off).
Figure 16. Resistance 4W with Low Current with 5730A as Current Source
38. Input the value of the 742A-10k resistor into the Transfer Resistor column in Table 10, steps 23
and 24 in Ω.
39. Starting with step 23, output the resistance value from the Product.
40. Measure the voltage across the SENSE terminals with the 8588A and record in the DMM
Measurement on Transfer Resistor column of Table 10 in V.
41. Move the connection to the Product SENSE terminals and measure the voltage across the SENSE
terminals with the 8588A and record in the DMM Measurement on Product column of Table 10 in
V.
42. Output the resistance value for step 24 from the Product.
43. Measure the Product SENSE terminals voltage across the SENSE terminals with the 8588A and
record in the DMMPROD column of Table 10 in V.
44. Return the connection as in Figure 16.
45. Measure the voltage across the 742A-10k SENSE terminals with the 8588A and record in step 24
in the DMMSTD column of Table 10 in V.
46. Calculate the Product Output as follows:
For steps 1 through 14: Product Output = DMM PROD
For steps 15 through 22: Product Output = DMM PROD - (DMM STD -R STD)
For steps 23 through 26: Product Output = DMM PROD * (1 - DMMErr *10 -6)
742A-10k Resistance Standard
CURRENT SENSEHI HI
LO LONOMINAL VALUE = 10 KΩ
TEMPERATURE RANGE: 18 °C TO 28 °CMAXIMUM VOLTAGE = 30 VDCMAXIMUM CURRENT = 3 mA ‘
CHASSISGROUND
10 VDCMAX5730A
742A-10k
8588A
5560A
Calibration and Verification of the Product
For steps 27 through 28:
47. With the entire table populated, evaluate each step for compliance to limits. To apply
Guardbanding, create a table from the example in this manual, where the acceptance limits are
properly modified by your Guardbanding method.
Table 10. Calibration and Verification Steps for Resistance
Step ProductRangeProductOutputDMM Mode/MethodTransferResistorTransferValue
DMM
Measure-
ment on
Transfer
Resistor
DMM
Measure-
ment on
Product
Calculated
Product
Output
Limits
1 12 Ω 0 Ω Normal 10 Ω /Direct N/A N/A N/A Ω Ω ±1.0 mΩ
2 12 Ω 1 Ω Normal 10 Ω /Direct N/A N/A N/A Ω Ω ±1.0 mΩ
3 12 Ω 10 Ω Normal 10 Ω /Direct N/A N/A N/A Ω Ω ±1.2 mΩ
4 120 Ω 12.1 Ω Normal 10 Ω /Direct N/A N/A N/A Ω Ω ±1.3 mΩ
5 120 Ω 100 Ω Normal 100 Ω /Direct N/A N/A N/A Ω Ω ±3.2 mΩ
6 1.2 kΩ 0.121 kΩ Normal 100 Ω /Direct N/A N/A N/A kΩ kΩ ±4.7 mΩ
7 1.2 kΩ 1 kΩ Normal 1 kΩ /Direct N/A N/A N/A kΩ kΩ ±24.0 mΩ
8 12 kΩ 1.21 kΩ Normal 1 kΩ /Direct N/A N/A N/A kΩ kΩ ±46.6 mΩ
9 12 kΩ 1.9 kΩ Normal 1 kΩ /Direct N/A N/A N/A kΩ kΩ ±61.8 mΩ
10 12 kΩ 3 kΩ Normal 10 kΩ /Direct N/A N/A N/A kΩ kΩ ±86.0 mΩ
11 12 kΩ 5 kΩ Normal 10 kΩ /Direct N/A N/A N/A kΩ kΩ ±130 mΩ
12 12 kΩ 10 kΩ Normal 10 kΩ /Direct N/A N/A N/A kΩ kΩ ±240 mΩ
13 12 kΩ 12 kΩ Normal 10 kΩ /Direct N/A N/A N/A kΩ kΩ ±284 mΩ
14 120 kΩ 12.1 kΩ Normal 10 kΩ /Direct N/A N/A N/A kΩ kΩ ±466 mΩ
15 120 kΩ 100 kΩ Normal 100 kΩ/ Transfer
Fluke
742A-
100k
kΩ kΩ kΩ kΩ ±2.4 Ω
Product Output = RSTD * DMM PROD
DMM STD
Step ProductRangeProductOutputDMM Mode/MethodTransferResistorTransferValue
DMM
Measure-
ment on
Transfer
Resistor
DMM
Measure-
ment on
Product
Calculated
Product
Output
Limits
16 1.2 MΩ 0.121 MΩ LoI 100 kΩ/Transfer
Fluke
742A-
100k
kΩ kΩ kΩ kΩ ±4.7 Ω
17 1.2 MΩ 1 MΩ Normal 1 MΩ /Transfer
Fluke
742A-
1M
MΩ MΩ MΩ MΩ ±24.0 Ω
18 12 MΩ 1.21 MΩ LoI 1 MΩ /Transfer
Fluke
742A-
1M
MΩ MΩ MΩ MΩ ±63.9 Ω
19 12 MΩ 10 MΩ Normal 10 MΩ/ Transfer
Fluke
742A-
10M
MΩ MΩ MΩ MΩ ±310.0 Ω
20 120 MΩ 12.1 MΩ Normal 10 MΩ/ Transfer
Fluke
742A-
10M
MΩ MΩ MΩ MΩ ±7.10 kΩ
21 120 MΩ 100 MΩ Normal 100MΩ / Transfer
MI
9331G/
100 M
MΩ MΩ MΩ MΩ ±40.5 kΩ
22 1.2 GΩ 0.121 GΩ Normal 100MΩ / Transfer
MI
9331G/
100 M
MΩ MΩ MΩ GΩ ±0.57 MΩ
23 1.2 GΩ 0.3 GΩ Normal 1 GΩ /Transfer N/A
Table 9,
Meter
error
μΩ/Ω GΩ GΩ ±1.27 MΩ
24 1.2 GΩ 0.4 GΩ Normal 1 GΩ /Transfer N/A

<!-- llm_chunk_end id=service_chunk_0005 -->

<!-- llm_chunk_start id=service_chunk_0006 source=service_manual_5560a source_line_start=1201 source_line_end=1460 retrieval_priority=normal -->

## service_chunk_0006: Fluke

Fluke
742A-
10M
MΩ MΩ MΩ MΩ ±7.10 kΩ
21 120 MΩ 100 MΩ Normal 100MΩ / Transfer
MI
9331G/
100 M
MΩ MΩ MΩ MΩ ±40.5 kΩ
22 1.2 GΩ 0.121 GΩ Normal 100MΩ / Transfer
MI
9331G/
100 M
MΩ MΩ MΩ GΩ ±0.57 MΩ
23 1.2 GΩ 0.3 GΩ Normal 1 GΩ /Transfer N/A
Table 9,
Meter
error
μΩ/Ω GΩ GΩ ±1.27 MΩ
24 1.2 GΩ 0.4 GΩ Normal 1 GΩ /Transfer N/A
Table 9,
Meter
error
μΩ/Ω GΩ GΩ ±1.66 MΩ
25 1.2 GΩ 0.64 GΩ Normal 1 GΩ /Transfer N/A
Table 9,
Meter
error
μΩ/Ω GΩ GΩ ±2.6 MΩ
26 1.2 GΩ 1 GΩ Normal 1 GΩ /Transfer
MI
9331G/
1 G
Table 9,
Meter
error
μΩ/Ω GΩ GΩ ±4.0 MΩ
27 12 Ω 0 Ω Ext. currentsource 100 μA N/A N/A N/A ±40.0 mΩ
28 120 Ω 100 Ω Ext. currentsource 100 μA N/A N/A N/A ±42.2 mΩ
Table 10. Calibration and Verification Steps for Resistance (cont.)
Calibration and Verification of the Product
Volts AC Calibration and Verification (OUTPUT VZ)
Table 11 lists the required equipment.
The volts ac calibration uses two methods. For frequencies ≤10 Hz low frequency DMM (Fluke 8588A)
is used. For frequencies >10 Hz the calibration is accomplished with Fluke 5790B AC Measurement
Standard.
1. Set the 8588A as follows: Volts ac, Range Auto, Band Wideband, Coupling: DC 10MΩ, Guard ON
(external guard).
2. Make sure that the DUT is in STBY.
3. Connect a strap between the guard and ground terminals of the DUT.
4. Complete an internal dc zero calibration on the Product.
5. Connect the 8588A to the Product as shown in Figure 17.
Figure 17. Low frequency Volts AC Calibration
6. Start with step 1 in Table 12. Set the Product to Operate. Make a measurement with the meter and
record in the Calculated Product Output column.
7. Continue with step 2.
8. Complete all steps for low frequency (Table 12, 1 to 39).
9. Set the Product to STBY.
Table 11. Required Equipment Volts AC Main Output
Equipment Description Manufacture/Model/PN Quantity
AC Measurement Standard Fluke 5790B 1
Digital Multimeter Fluke 8588A 1
Double banana RG58 cable Pomona Model 2BC-24 1
Single banana to single banana lead Various 1
5560A 8588A
10. Disconnect the present setup.
11. Connect the Product to Fluke 5790B as shown in Figure 18.
Figure 18. Volts AC Calibration
12. Starting with step 40, make a measurement with the 5790B. Record the measurement in the
Product Output column of Table 12.
13. Continue with the rest of the steps for this connection (Table 12, all steps).
14. With the entire table populated, evaluate each step for compliance to limits. To apply
Guardbanding, create a table from the example in this manual, where the acceptance limits are
properly modified by your Guardbanding method.
Table 12. Calibration and Verification steps for Volts AC
Step Product Range Product Output Product Frequency
Calculated
Product
Output
Limits
1 12 mV 1 mV 3 Hz ±9.00 μV
2 12 mV 1 mV 5 Hz ±7.70 μV
3 12 mV 1 mV 10 Hz ±6.12 μV
40 12 mV 1 mV 1 kHz ±6.12 μV
41 12 mV 1 mV 20 kHz ±6.12 μV
42 12 mV 1 mV 50 kHz ±6.30 μV
43 12 mV 1 mV 100 kHz ±16.2 μV
44 12 mV 1 mV 300 kHz ±36.4 μV
45 12 mV 1 mV 500 kHz ±36.4 μV
+/- 3% (1 year) 83 days since ca2/06/15 10:52am
SetSetReferenceReferenceSe
Me
Auto Range 2.2 V
Pk-Pk StatisticsCurrentShunt
Input 2
5560A 5590B
Calibration and Verification of the Product
Step Product Range Product Output Product Frequency
Calculated
Product
Output
Limits
4 12 mV 10 mV 3 Hz ±27.0 μV
5 12 mV 10 mV 5 Hz ±14.0 μV
6 12 mV 10 mV 10 Hz ±7.2 μV
46 12 mV 10 mV 1 kHz ±7.2 μV
47 12 mV 10 mV 20 kHz ±7.2 μV
48 12 mV 10 mV 50 kHz ±9.0 μV
49 12 mV 10 mV 100 kHz ±27 μV
50 12 mV 10 mV 300 kHz ±94 μV
51 12 mV 10 mV 500 kHz ±94 μV
7 120 mV 12.1 mV 3 Hz ±31 μV
8 120 mV 12.1 mV 5 Hz ±15 μV
9 120 mV 12.1 mV 10 Hz ±7.4 μV
52 120 mV 12.1 mV 1 kHz ±7.4 μV
53 120 mV 12.1 mV 20 kHz ±7.4 μV
54 120 mV 12.1 mV 50 kHz ±11 μV
55 120 mV 12.1 mV 100 kHz ±28 μV
56 120 mV 12.1 mV 300 kHz ±49 μV
57 120 mV 12.1 mV 500 kHz ±49 μV
10 120 mV 100 mV 3 Hz ±207 μV
11 120 mV 100 mV 5 Hz ±77 μV
12 120 mV 100 mV 10 Hz ±18 μV
58 120 mV 100 mV 1 kHz ±18 μV
59 120 mV 100 mV 20 kHz ±18 μV
60 120 mV 100 mV 50 kHz ±36 μV
61 120 mV 100 mV 100 kHz ±84 μV
62 120 mV 100 mV 300 kHz ±190 μV
63 120 mV 100 mV 500 kHz ±190 μV
13 1.2 V 0.121 V 3 Hz ±317 μV
14 1.2 V 0.121 V 5 Hz ±155 μV
Table 12. Calibration and Verification steps for Volts AC (cont.)
Step Product Range Product Output Product Frequency
Calculated
Product
Output
Limits
15 1.2 V 0.121 V 10 Hz ±74 μV
64 1.2 V 0.121 V 1 kHz ±74 μV
65 1.2 V 0.121 V 20 kHz ±74 μV
66 1.2 V 0.121 V 50 kHz ±43 μV
67 1.2 V 0.121 V 100 kHz ±108 μV
68 1.2 V 0.121 V 300 kHz ±264 μV
69 1.2 V 0.121 V 500 kHz ±264 μV
16 1.2 V 1 V 3 Hz ±2.08 mV
17 1.2 V 1 V 5 Hz ±0.77 mV
18 1.2 V 1 V 10 Hz ±0.18 mV
70 1.2 V 1 V 40.01 Hz ±0.12 mV
71 1.2 V 1 V 1 kHz ±0.12 mV
72 1.2 V 1 V 20 kHz ±0.12 mV
73 1.2 V 1 V 50 kHz ±0.25 mV
74 1.2 V 1 V 100 kHz ±0.60 mV
75 1.2 V 1 V 300 kHz ±1.60 mV
76 1.2 V 1 V 500 kHz ±1.60 mV
19 12 V 1.21 V 3 Hz ±3.17 mV
20 12 V 1.21 V 5 Hz ±1.60 mV
21 12 V 1.21 V 10 Hz ±0.49 mV
77 12 V 1.21 V 1 kHz ±0.19 mV
78 12 V 1.21 V 20 kHz ±0.19 mV
79 12 V 1.21 V 50 kHz ±0.34 mV
80 12 V 1.21 V 100 kHz ±0.80 mV
81 12 V 1.21 V 300 kHz ±2.54 mV
82 12 V 1.21 V 500 kHz ±2.54 mV
22 12 V 10 V 3 Hz ±20.75 mV
23 12 V 10 V 5 Hz ±7.75 mV
24 12 V 10 V 10 Hz ±1.50 mV
Table 12. Calibration and Verification steps for Volts AC (cont.)
Calibration and Verification of the Product
Step Product Range Product Output Product Frequency
Calculated
Product
Output
Limits
83 12 V 10 V 1 kHz ±1.20 mV
84 12 V 10 V 20 kHz ±1.20 mV
85 12 V 10 V 50 kHz ±2.45 mV
86 12 V 10 V 100 kHz ±5.73 mV
87 12 V 10 V 300 kHz ±16.6 mV
88 12 V 10 V 500 kHz ±16.6 mV
25 120 V 12.1 V 3 Hz ±31.7 mV
26 120 V 12.1 V 5 Hz ±16.0 mV
27 120 V 12.1 V 10 Hz ±4.89 mV
89 120 V 12.1 V 1 kHz ±1.89 mV
90 120 V 12.1 V 20 kHz ±1.89 mV
91 120 V 12.1 V 50 kHz ±3.40 mV
92 120 V 12.1 V 100 kHz ±8.03 mV
93 [1] 120 V 12.1 V 300 kHz ±39.36 mV
28 120 V 100 V 3 Hz ±208 mV
29 120 V 100 V 5 Hz ±78 mV
30 120 V 100 V 10 Hz ±15.00 mV
94 120 V 100 V 40.01 Hz ±12.00 mV
95 120 V 100 V 1 kHz ±12.00 mV
96 120 V 100 V 20 kHz ±12.00 mV
97 120 V 100 V 50 kHz ±25 mV
98 120 V 100 V 100 kHz ±57 mV
99 [1] 120 V 70 V 300 kHz ±132 mV
31 330 V 121 V 3 Hz ±317 mV
32 330 V 121 V 5 Hz ±160 mV
33 330 V 121 V 10 Hz ±22 mV
100 330 V 121 V 1 kHz ±22 mV
Table 12. Calibration and Verification steps for Volts AC (cont.)
Step Product Range Product Output Product Frequency
Calculated
Product
Output
Limits
101 330 V 121 V 10 kHz ±22 mV
102 330 V 121 V 10.01 kHz ±22 mV
103 330 V 121 V 20 kHz ±22 mV
104 330 V 121 V 50 kHz ±37 mV
105 330 V 121 V 100 kHz ±158 mV
34 330 V 330 V 3 Hz ±735 mV
35 330 V 330 V 5 Hz ±306 mV
36 330 V 330 V 10 Hz ±46 mV
106 330 V 330 V 1 kHz ±46 mV
107 330 V 330 V 20 kHz ±46 mV
108 330 V 330 V 50 kHz ±87 mV
109 330 V 330 V 100 kHz ±409 mV
37 1020 V 331 V 3 Hz ±737 mV
38 1020 V 331 V 5 Hz ±307 mV
39 1020 V 331 V 10 Hz ±118 mV
110 1020 V 331 V 1 kHz ±118 mV
111 1020 V 331 V 10 kHz ±118 mV
112 1020 V 1000 V 40 Hz ±195 mV
113 1020 V 1000 V 1 kHz ±195 mV
114 1020 V 1020 V 10 kHz ±197 mV
[1] 5560A Only
Table 12. Calibration and Verification steps for Volts AC (cont.)
Calibration and Verification of the Product
AC Power. Volts AC Calibration and Verification (OUTPUT VZ) (5530A, 5550A and
5560A)
This section only applies to devices with Firmware 4.0 or later.
1. Before you make any connection changes, set the Product to STBY.
2. Connect the Product to 5790B as shown in Figure 19. Note the added copper wire shoring on the
terminals of the Product: SENSE VZ LO to SENSE VZ 30 A to OUTPUT VZ VI AUX. Use 16 AWG/
1.3 mm minimum size.
3. Starting with step 1 in Table 13, the setup of the Product is: Volts AC as fundamental, Current AC
set to 3rd harmonic, phase set to 0 degrees.
4. Set the Product to the first step in Table 13 and make the measurement with the 5790B. Record the
measurement in the Product Output column of the table.
5. Do the rest of the steps in the table for this connection.
6. With the table fully populated, evaluate each step for compliance to limits. To apply Guardbanding,
create a table from the example in this manual where the acceptance limits are properly modified
by your Guardbanding method.
Figure 19. Connections with Jumpers
+/- 3% (1 year) 83 days since ca2/06/15 10:52am
SetSetReferenceReferenceSe
Me
Auto Range 2.2 V
Pk-Pk StatisticsCurrentShunt
Input 2
Volts AC Calibration and Verification (AUX Output) (5530A, 5550A, and 5560A)
Table 14 lists the required equipment.
To proceed with volts ac out of the Sense VZ LO/Output VI AUX proceed as follows:
1. Connect the Product to Fluke 5790B as shown in Figure 20.
2. Connect a strap between the guard and ground terminals of the DUT.
Table 13. Calibration and Verification steps for AC Power - Volts AC
Step Product Output ProductFrequency Product Phase Product Output
90D
Specification

<!-- llm_chunk_end id=service_chunk_0006 -->

<!-- llm_chunk_start id=service_chunk_0007 source=service_manual_5560a source_line_start=1441 source_line_end=1700 retrieval_priority=normal -->

## service_chunk_0007: 5. Do the rest of the steps in the table for this connection.

5. Do the rest of the steps in the table for this connection.
6. With the table fully populated, evaluate each step for compliance to limits. To apply Guardbanding,
create a table from the example in this manual where the acceptance limits are properly modified
by your Guardbanding method.
Figure 19. Connections with Jumpers
+/- 3% (1 year) 83 days since ca2/06/15 10:52am
SetSetReferenceReferenceSe
Me
Auto Range 2.2 V
Pk-Pk StatisticsCurrentShunt
Input 2
Volts AC Calibration and Verification (AUX Output) (5530A, 5550A, and 5560A)
Table 14 lists the required equipment.
To proceed with volts ac out of the Sense VZ LO/Output VI AUX proceed as follows:
1. Connect the Product to Fluke 5790B as shown in Figure 20.
2. Connect a strap between the guard and ground terminals of the DUT.
Table 13. Calibration and Verification steps for AC Power - Volts AC
Step Product Output ProductFrequency Product Phase Product Output
90D
Specification
Limits
1 0.120001 V/3.1 A 333 Hz 0 ° ±29.8 μV
2 1.20001 V/12 A 333 Hz 0 ° ±238 μV
3 1.20001 V/1.2 A 1666 Hz 0 ° ±238 μV
4 1.20001 V/1.2 A 3333 Hz 0 ° ±238 μV
5 1.20001 V/0.333 A 10000 Hz 0 ° ±238 μV
6 12.0001 V/12 A 333 Hz 0 ° ±2.38 mV
7 12.0001 V/1.2 A 1666 Hz 0 ° ±2.38 mV
8 12.0001 V/1.2 A 3333 Hz 0 ° ±2.38 mV
9 12.0001 V/0.333 A 10000 Hz 0 ° ±2.38 mV
10 120.001 V/12 A 333 Hz 0 ° ±29.8 mV
11 120.001 V/1.2 A 1666 Hz 0 ° ±29.8 mV
12 120.001 V/1.2 A 3333 Hz 0 ° ±30 mV
13 330.001 V/12 A 333 Hz 0 ° ±198 mV
Table 14. Required Equipment Volts AC from the AUX Output
Equipment Description Manufacture/Model/PN Quantity
AC Measurement Standard Fluke 5790B 1
Test Lead Banana to Banana 24 in Pomona Model 1368-A-24 1
Single banana to single banana lead Various 1
Calibration and Verification of the Product
Figure 20. Volts AC Out of the SENSE VZ LO/OUTPUT VI AUX Calibration Adjustment
3. Set the 5790B for Input 2, Auto range, High resolution ON, GUARD ON.
4. Start with step 1 in Table 15. Set the DUT to 1 V for the main output and Product output setting V
and Hz in Table 15. Make a measurement with the 5790B. Record the measurement in the
Product Output column of Table 15.
5. Continue with the rest of the steps for this connection (Table 15, steps 41 to 12). The main output to
remain set to 1 V for all steps.
6. With the entire table populated, evaluate each step for compliance to limits. To apply
Guardbanding, create a table from the example in this manual where the acceptance limits are
properly modified by your Guardbanding method.
Table 15. Calibration and Verification steps for Volts AC Out of the AUX Output
Step Product Output(OUTPUT VZ)Product Output(SENSE Output)ProductFrequency Product Output Limits
1 1 V 120 mV 45 Hz ±0.372 mV
2 1 V 120 mV 65 Hz ±0.372 mV
3 1 V 1.2 V 45 Hz ±1.02 mV
4 1 V 1.2 V 400 Hz ±1.02 mV
5 1 V 1.2 V 1 kHz ±1.02 mV
6 1 V 1.2 V 5 kHz ±1.79 mV
7 1 V 5 V 45 Hz ±3.30 mV
8 1 V 5 V 400 Hz ±3.30 mV
9 1 V 5 V 1 kHz ±3.30 mV
10 1 V 5 V 5 kHz ±6.4 mV
11 1 V 5 V 10 kHz ±12.4 mV
12 1 V 3.3 V 30 kHz ±100 mV
+/- 3% (1 year) 83 days since ca2/06/15 10:52am
SetSetReferenceReferenceSe
Me
Auto Range 2.2 V
Pk-Pk StatisticsCurrentShunt
Input 2
5560A 5790B
ACV ACV. Volts AC Calibration and Verification (AUX Output) (5530A, 5550A and
5560A)
This section only applies to devices with Firmware 4.0 or later.
1. Set the Product is set to STBY before you make any connection changes.
2. Connect the Product to Fluke 5790B as shown in Figure 20.
3. The setup of the Product is: AUX Volts as fundamental, AC Voltage out of OUTPUT VZ set to 3rd
harmonic, phase set to 0 degrees. Starting at step 1 of Table 16, make a measurement with the
5790B. Record the measurement in the Product Output column of the table.
4. Continue with the rest of the steps in the table for this connection.
5. After you have gone through each step of the table, evaluate each step for compliance to limits. To
apply Guardbanding, create a table from the example in this manual, where the acceptance limits
are properly modified by your Guardbanding method.
Amps AC Calibration and Verification
Table 17 lists the required equipment.
Table 16. Calibration and Verification steps for ACV ACV - Volts AC (Aux Output)
Step Product Output ProductFrequencyProductPhase Product Output
90D
Specification
Limits
1 1020 V/0.12001 V 166 Hz 0 ° ±0.67 mV
2 500 V/0.12001 V 333 Hz 0 ° ±0.67 mV
3 250 V/1.2001 V 3333 Hz 0 ° ±2.14 mV
4 120 V/1.2001 V 10000 Hz 0 ° ±3.58 mV
Table 17. Required Equipment for Amps AC
Equipment Description Manufacture/Model/PN Quantity
Digital Multimeter Fluke 8588A 1
(1 mA to 1.2 mA) Fluke A40B-1mA Current Shunt 1
(10 mA to 12 mA) Fluke A40B-10mA Current Shunt 1
(100 mA to 120 mA) Fluke A40B-100mA Current Shunt 1
(1 A to 1.2 A) Fluke A40B-1A Current Shunt 1
3.1 A, 3.11 A Fluke A40B-5A Current Shunt 1
10 A Fluke A40B-10A Current Shunt 1
(12.1 A to 20 A) Fluke A40B-20A Current Shunt 1
30 A Fluke A40B-50A Current Shunt 1
Calibration and Verification of the Product
The amps ac calibration and verification uses two methods. For frequencies ≤10 Hz, use a low-
frequency Fluke Calibration 8588A meter to monitor the output of Fluke A40B series shunts. For
frequencies >10 Hz the calibration and verification is accomplished with the Fluke Calibration 5790B
AC Measurement Standard monitoring the output of the Fluke A40B series shunts.
To calibrate the amps ac function:
1. Set the 8588A as follows: Volts ac, Range Auto, Wide Bandwidth, Coupling: DC 10 MΩ, Guard ON
(external guard).
2. Make sure that the DUT is in STBY.
3. Connect a strap between the Guard and Ground terminals of the DUT.
4. Complete an internal dc zero calibration on the Product.
5. Connect the 8588A to the Product as shown in Figure 21.
6. Make sure that the DUT is in STBY.
7. Calculate the shunt resistance in Ω from calibration records and/or regression analysis for all
shunts listed in Table 18. Use the A40B series instruction manual for guidance for how to calculate
shunt ac resistance for every point in the calibration record.
8. Record the shunt resistance for each step in Ω in the Shunt_R column in Table 18.
9. Toggle the power switch of the A40B-1 mA shunt to ON. Continue only if the power light is
illuminated and the BATT LOW is off.
10. Start with step 1. Set the output from the DUT. Measure with the 8588A and record in the DMM
Reading on Shunt Output [V] column of Table 18.
11. Continue with step 2, Table 18.
12. Complete Table 18, steps 1 to 5.
Equipment Description Manufacture/Model/PN Quantity
Type N (M) to dual banana (M) E-Z-Hook PN 9415 1
Type N (F) to Type N (F) adapter Various 1
LC Male to LC Male adapter A40B-ADAPT/LC 1
LC Female to N Male inter-series adapter A40B-ADAPT/LCN 1
N to 4 mm double banana connector A40B-LEAD/4mm 1
DBL BANANA N (M) RG58C/U (≈ 16 in) (Fluke PN 900394) 5790-8026 1
Table 17. Required Equipment for Amps AC (cont.)
Figure 21. Amps AC with A40B-1mA
13. Disconnect the shunt output cable from the 8588A and connect it to the 5790B Input 2.
14. Set the 5790B for Input 2, Auto range, High resolution ON, EXT GUARD.
15. Connect heavy gauge guard cable between the DUT and the 5790B.
16. From step 6, Table 18, set the output from the DUT/Measure with the 5790B and record the 5790B
measured in the DMM Reading on Shunt Output [V] column. Complete Table 18, steps 6 to 30.
17. Set the Product to STBY.
18. Toggle the power switch of the A40B-1mA shunt to OFF.
19. Connect the test equipment as shown in Figure 22.
Figure 22. Amps AC with A40B-10mA
A40B-1mA
INPUTOUTPUT
5560A 8588A
A40B-10mA
INPUTOUTPUT
5560A 8588A
Calibration and Verification of the Product
20. From step 31, Table 18, output from the DUT/Measure with the meter and record the 8588A
measurement in the DMM Reading on Shunt Output [V] column.
21. Complete Table 18, steps 31 and 32.
22. Disconnect the shunt output cable from the 8588A and connect to the 5790B Input 2.
23. Set the 5790B for Input 2, Auto range, High resolution ON, GUARD ON.
24. Connect a heavy gauge guard cable between the DUT and the 5790B.
25. From Table 18, step 33, output from the DUT/Measure with the 5790B and record the 5790B
measurement in the DMM Reading on Shunt Output [V] column. Complete Table 18, steps 33 to
42.
26. Set the Product to STBY.
27. Connect the test equipment as shown in Figure 23.
Figure 23. Amps AC with A40B-100mA
28. From step 43, Table 18, set the output from the DUT/Measure with the meter and record the 8588A
measurement in the DMM Reading on Shunt Output [V] column.
29. Complete Table 18, steps 43 and 44.
30. Disconnect the shunt output cable from the 8588A and connect to the 5790B Input 2.
31. Set the 5790B for Input 2, Auto range, High resolution ON, GUARD ON.
32. Connect a heavy gauge guard cable between the DUT and the 5790B.
33. From Table 18, step 45, output from the DUT/Measure with the 5790B and record the 5790B
measurement in the DMM Reading on Shunt Output [V] column. Complete Table 18, steps 45 to
54.
34. Set the Product to STBY.
35. Connect the test equipment as shown in Figure 24.
A40B-100mA
OUTPUT
5560A 8588A
Figure 24. Amps AC with A40B-1A
36. From Table 18, step 55, set the output from the DUT and wait 30 seconds for the output to settle.
Measure with the meter and record the 8588A measurement in the DMM Reading on Shunt
Output [V] column.
37. Complete Table 18, step 55 and 56.
38. Disconnect the shunt output cable from the 8588A and connect to the 5790B Input 2.
39. Set the 5790B for Input 2, Auto range, High resolution ON, EXT GUARD.
40. Connect heavy gauge guard cable between the DUT and the 5790B.
41. From step 57, Table 18, output from the DUT/Measure with the 5790B and record the 5790B
measurement in the DMM Reading on Shunt Output [V] column. Complete Table 18, steps 57 to
65.
42. Set the Product to STBY.
43. Connect the test equipment as shown in Figure 25.
44. From step 66, Table 18, output from the DUT and wait 1 minute for the output to settle. Measure
with the meter and record the 8588A measurement in the DMM Reading on Shunt Output [V]
column.
45. Disconnect the shunt output cable from the 8588A and connect to the 5790B Input 2.
46. Set the 5790B for Input 2, Auto range, High resolution ON, EXT GUARD.
47. Connect heavy gauge guard cable between the DUT and the 5790B.
48. From step 67, Table 18, output from the DUT and Measure with the 5790B. Record the 5790B
measurement in the DMM Reading on Shunt Output [V] column. Complete Table 18, steps 67 to
70.
49. Set the Product to STBY.
A40B-1A
OUTPUT
5560A 8588A
Calibration and Verification of the Product
Figure 25. Amps AC with A40B-5A
50. Move the red lead connected to the Product VI AUX to the 30 A terminal.
51. Move the connection of the shunt output to the 8588A.
52. From step 71, Table 18, output from the DUT and measure with the meter. Record the 8588A
measurement in the DMM Reading on Shunt Output [V] column.
53. Disconnect the shunt output cable from the 8588A and connect to the 5790B Input 2.
54. Set the 5790B for Input 2, Auto range, High resolution ON, GUARD ON.
55. Connect heavy gauge guard cable between the DUT and the 5790B.
56. From step 72, Table 18, output from the DUT and measure with the 5790B and record the
measurement in the DMM Reading on Shunt Output [V] column. Complete Table 18, steps 72 to
75.
57. Set the Product to STBY.
58. Connect the test equipment as shown in Figure 26.
Figure 26. Amps AC with A40B-10A
A40B-5A
INPUT OUTPUT
5560A 8588A
A40B-10A
INPUT OUTPUT
5560A 8588A
59. From step 76, Table 18, output from the DUT, wait 3 minutes for the output to settle. Measure with
the meter and record the 8588A measurement in the DMM Reading on Shunt Output [V] column.
60. Disconnect the shunt output cable from the 8588A and connect to the 5790B Input 2.
61. Set the 5790B for Input 2, Auto range, High resolution ON, EXT GUARD.
62. Connect the heavy gauge guard cable between the DUT and the 5790B.
63. From step 77, Table 18, output from the DUT and measure with the 5790B. Record the 5790B
measurement in the DMM Reading on Shunt Output [V] column. Complete Table 18, steps 77 to
80.
64. Set the Product to STBY.
65. Connect the test equipment as shown in Figure 27.
Figure 27. Amps AC with A40B-20A
66. From step 81, Table 18, output from the DUT and wait 3 minutes for the output to settle. Measure
with the meter and record the 8588A measurement in the DMM Reading on Shunt Output [V]
column.
67. Continue with and complete step 85.
68. Disconnect the shunt output cable from the 8588A and connect to the 5790B Input 2.
69. Set the 5790B for Input 2, Auto range, High resolution ON, EXT GUARD.
70. Connect heavy gauge guard cable between the DUT and the 5790B.
71. From step 82, Table 18, output from the DUT and measure with the 5790B. Record the 5790B
measurement in the DMM Reading on Shunt Output [V] column. Complete Table 18, steps 82 to
88.
72. Set the Product to STBY.
73. Connect the test equipment as shown in Figure 28.
A40B-20A
INPUT OUTPUT
5560A 8588A
Calibration and Verification of the Product
Figure 28. Amps AC with A40B-50A
74. From step 89, Table 18, output from the DUT and wait 3 minutes for the output to settle. Measure
with the meter and record the 8588A measurement in the DMM Reading on Shunt Output [V]
column.
75. After step 89 is complete, disconnect the shunt output cable from the 8588A and connect to the
5790B Input 2.
76. Set the 5790B for Input 2, Auto range, High resolution ON, GUARD ON.

<!-- llm_chunk_end id=service_chunk_0007 -->

<!-- llm_chunk_start id=service_chunk_0008 source=service_manual_5560a source_line_start=1681 source_line_end=1940 retrieval_priority=normal -->

## service_chunk_0008: 67. Continue with and complete step 85.

67. Continue with and complete step 85.
68. Disconnect the shunt output cable from the 8588A and connect to the 5790B Input 2.
69. Set the 5790B for Input 2, Auto range, High resolution ON, EXT GUARD.
70. Connect heavy gauge guard cable between the DUT and the 5790B.
71. From step 82, Table 18, output from the DUT and measure with the 5790B. Record the 5790B
measurement in the DMM Reading on Shunt Output [V] column. Complete Table 18, steps 82 to
88.
72. Set the Product to STBY.
73. Connect the test equipment as shown in Figure 28.
A40B-20A
INPUT OUTPUT
5560A 8588A
Calibration and Verification of the Product
Figure 28. Amps AC with A40B-50A
74. From step 89, Table 18, output from the DUT and wait 3 minutes for the output to settle. Measure
with the meter and record the 8588A measurement in the DMM Reading on Shunt Output [V]
column.
75. After step 89 is complete, disconnect the shunt output cable from the 8588A and connect to the
5790B Input 2.
76. Set the 5790B for Input 2, Auto range, High resolution ON, GUARD ON.
77. Connect heavy gauge guard cable between the DUT and the 5790B.
78. From step 90, Table 18, output from the DUT and measure with the 5790B. Record the 5790B
measurement in the DMM Reading on Shunt Output [V] column. Complete Table 18, steps 90 to
92.
79. Set the Product to STBY.
80. For all steps, calculate the Product output with the formula below. Use the appropriate conversion
to convert from base units to units for the specific evaluation step.
81. With the entire table populated, evaluate each step for compliance to limits. To apply
Guardbanding, create a table from the example in this manual where the acceptance limits are the
properly modified by your Guardbanding method.
A40B-50A
INPUT OUTPUT
5560A 8588A
Calculated Product Output = DMM Reading on Shunt output [V]
Shunt_R []
Table 18. Calibration and Verification Steps for Amps AC
Step ProductRangeProductOutputProductFrequency Shunt Shunt_R[Ω]
DMM
Reading on
Shunt
Output [V]
Calculated
Product
Output
Limits
1 120 μA 10 μA 3 Hz Fluke A40B-1mA ±12.0 nA
6 120 μA 10 μA 45 Hz Fluke A40B-1mA ±12.0 nA
7 120 μA 10 μA 1 kHz Fluke A40B-1mA ±12.0 nA
8 120 μA 10 μA 5 kHz Fluke A40B-1mA ±12.0 nA
9 120 μA 10 μA 10 kHz Fluke A40B-1mA ±52.0 nA
10 120 μA 10 μA 30 kHz Fluke A40B-1mA ±1040.0 nA
2 120 μA 100 μA 3 Hz Fluke A40B-1mA ±30.0 nA
11 120 μA 100 μA 45 Hz Fluke A40B-1mA ±30.0 nA
12 120 μA 100 μA 1 kHz Fluke A40B-1mA ±30.0 nA
13 120 μA 100 μA 5 kHz Fluke A40B-1mA ±30.0 nA
14 120 μA 100 μA 10 kHz Fluke A40B-1mA ±160.0 nA
15 120 μA 100 μA 30 kHz Fluke A40B-1mA ±1400 nA
3 1.2 mA 0.121 mA 3 Hz Fluke A40B-1mA ±124 nA
16 1.2 mA 0.121 mA 45 Hz Fluke A40B-1mA ±124 nA
17 1.2 mA 0.121 mA 1 kHz Fluke A40B-1mA ±124 nA
18 1.2 mA 0.121 mA 5 kHz Fluke A40B-1mA ±124 nA
19 1.2 mA 0.121 mA 10 kHz Fluke A40B-1mA ±245 nA
20 1.2 mA 0.121 mA 30 kHz Fluke A40B-1mA ±5484 nA
Calibration and Verification of the Product
Step ProductRangeProductOutputProductFrequency Shunt Shunt_R[Ω]
DMM
Reading on
Shunt
Output [V]
Calculated
Product
Output
Limits
4 1.2 mA 1 mA 3 Hz Fluke A40B-1mA ±300 nA
21 1.2 mA 1 mA 45 Hz Fluke A40B-1mA ±300 nA
22 1.2 mA 1 mA 1 kHz Fluke A40B-1mA ±300 nA
23 1.2 mA 1 mA 5 kHz Fluke A40B-1mA ±300 nA
24 1.2 mA 1 mA 10 kHz Fluke A40B-1mA ±1300 nA
25 1.2 mA 1 mA 30 kHz Fluke A40B-1mA ±9.00 μA
5 12 mA 1.21 mA 3 Hz Fluke A40B-1mA ±1.24 μA
26 12 mA 1.21 mA 45 Hz Fluke A40B-1mA ±1.24 μA
27 12 mA 1.21 mA 1 kHz Fluke A40B-1mA ±1.24 μA
28 12 mA 1.21 mA 5 kHz Fluke A40B-1mA ±1.24 μA
29 12 mA 1.21 mA 10 kHz Fluke A40B-1mA ±2.45 μA
30 12 mA 1.21 mA 30 kHz Fluke A40B-1mA ±14.84 μA
31 12 mA 10 mA 3 Hz Fluke A40B-10mA ±3.00 μA
33 12 mA 10 mA 45 Hz Fluke A40B-10mA ±3.00 μA
34 12 mA 10 mA 1 kHz Fluke A40B-10mA ±3.00 μA
35 12 mA 10 mA 5 kHz Fluke A40B-10mA ±3.00 μA
36 12 mA 10 mA 10 kHz Fluke A40B-10mA ±13.00 μA
37 12 mA 10 mA 30 kHz Fluke A40B-10mA ±50 μA
32 120 mA 12.1 mA 3 Hz Fluke A40B-10mA ±12 μA
Table 18. Calibration and Verification Steps for Amps AC (cont.)
Step ProductRangeProductOutputProductFrequency Shunt Shunt_R[Ω]
DMM
Reading on
Shunt
Output [V]
Calculated
Product
Output
Limits
38 120 mA 12.1 mA 45 Hz Fluke A40B-10mA ±6 μA
39 120 mA 12.1 mA 1 kHz Fluke A40B-10mA ±6 μA
40 120 mA 12.1 mA 5 kHz Fluke A40B-10mA ±10 μA
41 120 mA 12.1 mA 10 kHz Fluke A40B-10mA ±25 μA
42 120 mA 12.1 mA 30 kHz Fluke A40B-10mA ±148 μA
43 120 mA 100 mA 3 Hz Fluke A40B-100mA ±30 μA
45 120 mA 100 mA 45 Hz Fluke A40B-100mA ±17 μA
46 120 mA 100 mA 1 kHz Fluke A40B-100mA ±17 μA
47 120 mA 100 mA 5 kHz Fluke A40B-100mA ±28 μA
48 120 mA 100 mA 10 kHz Fluke A40B-100mA ±130 μA
49 120 mA 100 mA 30 kHz Fluke A40B-100mA ±500 μA
44 1.2 A 0.121 A 3 Hz Fluke A40B-100mA ±0.12 mA
50 1.2 A 0.121 A 45 Hz Fluke A40B-100mA ±0.07 mA
51 1.2 A 0.121 A 1 kHz Fluke A40B-100mA ±0.07 mA
52 1.2 A 0.121 A 5 kHz Fluke A40B-100mA ±0.10 mA
53 1.2 A 0.121 A 10 kHz Fluke A40B-100mA ±0.54 mA
54 1.2 A 0.121 A 30 kHz Fluke A40B-100mA ±0.78 mA
55 1.2 A 1 A 3 Hz Fluke A40B-1A ±0.30 mA
57 1.2 A 1 A 45 Hz Fluke A40B-1A ±0.25 mA
58 1.2 A 1 A 1 kHz Fluke A40B-1A ±0.25 mA
Table 18. Calibration and Verification Steps for Amps AC (cont.)
Calibration and Verification of the Product
Step ProductRangeProductOutputProductFrequency Shunt Shunt_R[Ω]
DMM
Reading on
Shunt
Output [V]
Calculated
Product
Output
Limits
59 1.2 A 1 A 5 kHz Fluke A40B-1A ±0.28 mA
60 1.2 A 1 A 10 kHz Fluke A40B-1A ±2.30 mA
61 1.2 A 1 A 30 kHz Fluke A40B-1A ±4.30 mA
56 3.1 A 1.21 A 3 Hz Fluke A40B-1A ±0.86 mA
62 3.1 A 1.21 A 45 Hz Fluke A40B-1A ±0.59 mA
63 3.1 A 1.21 A 1 kHz Fluke A40B-1A ±0.59 mA
64 3.1 A 1.21 A 5 kHz Fluke A40B-1A ±0.66 mA
65 3.1 A 1.21 A 10 kHz Fluke A40B-1A ±2.92 mA
66 3.1 A 3.1 A 3 Hz Fluke A40B-5A ±1.43 mA
67 3.1 A 3.1 A 45 Hz Fluke A40B-5A ±1.04 mA
68 3.1 A 3.1 A 1 kHz Fluke A40B-5A ±1.04 mA
69 3.1 A 3.1 A 5 kHz Fluke A40B-5A ±1.23 mA
70 3.1 A 3.1 A 10 kHz Fluke A40B-5A ±6.70 mA
71 12 A 3.11 A 3 Hz Fluke A40B-5A ±1.93 mA
72 12 A 3.11 A 45 Hz Fluke A40B-5A ±1.25 mA
73 12 A 3.11 A 1 kHz Fluke A40B-5A ±1.25 mA
74 12 A 3.11 A 5 kHz Fluke A40B-5A ±1.73 mA
75 12 A 3.11 A 10 kHz Fluke A40B-5A ±7.22 mA
76 12 A 10 A 3 Hz Fluke A40B-10A ±4.00 mA
77 12 A 10 A 45 Hz Fluke A40B-10A ±2.90 mA
78 12 A 10 A 1 kHz Fluke A40B-10A ±2.90 mA
79 12 A 10 A 5 kHz Fluke A40B-10A ±3.80 mA
80 12 A 10 A 10 kHz Fluke A40B-10A ±21.0 mA
81 30.2 A 12.1 A 3 Hz Fluke A40B-20A ±20 mA
82 30.2 A 12.1 A 45 Hz Fluke A40B-20A ±15 mA
83 30.2 A 12.1 A 1 kHz Fluke A40B-20A ±15 mA
84 30.2 A 12.1 A 5 kHz Fluke A40B-20A ±56 mA
85 30.2 A 20 A 3 Hz Fluke A40B-20A ±26 mA
86 30.2 A 20 A 45 Hz Fluke A40B-20A ±19 mA
87 30.2 A 20 A 1 kHz Fluke A40B-20A ±19 mA
Table 18. Calibration and Verification Steps for Amps AC (cont.)
AC Power. Amps AC Calibration and Verification (5530A, 5550A and 5560A)
This section applies to devices with Firmware 4.0 or later.
1. Set the Product to STBY before you make any connection changes.
2. Connect the test equipment as shown in Figure 29.
3. Calculate the shunt resistance in Ω from calibration records and/or regression analysis for all
shunts listed in Table 19. Use the A40B series Users Manual for guidance to calculate shunt ac
resistance for every point in the calibration record.
4. Record the shunt resistance for each step in Ω in the Shunt_R column in Table 19.
Figure 29. ACP - Amps AC with A40B-10 mA
Step ProductRangeProductOutputProductFrequency Shunt Shunt_R[Ω]
DMM
Reading on
Shunt
Output [V]
Calculated
Product
Output
Limits
88 30.2 A 20 A 5 kHz Fluke A40B-20A ±88 mA
89 30.2 A 30 A 3 Hz Fluke A40B-50A ±34 mA
90 30.2 A 30 A 45 Hz Fluke A40B-50A ±25 mA
91 30.2 A 30 A 1 kHz Fluke A40B-50A ±25 mA
92 30.2 A 30 A 5 kHz Fluke A40B-50A ±128 mA
Table 18. Calibration and Verification Steps for Amps AC (cont.)
+/- 3% (1 year) 83 days since ca2/06/15 10:52am
SetSetReferenceReferenceSe
Me
Auto Range 2.2 V
Pk-Pk StatisticsCurrentShunt
Input 2
A40B-1mA
INPUTOUTPUT
5560A
A40B-10mA
5790B
Calibration and Verification of the Product
The setup of the Product is: AC Current as fundamental, AC Voltage set to 3rd harmonic, phase set
to 0 degrees.
5. Set the 5790B for Input 2, Auto range, High resolution ON, GUARD ON.
6. Connect a heavy gauge guard cable between the DUT and the 5790B.
7. Set the Product to the first step in Table 19, make a measurement with the 5790B. Record the
measurement in the DMM Reading on Shunt Output [V] column of the table.
8. Complete steps 2 to 4 of the table.
9. Set the Product to STBY.
10. Connect the test equipment as in Figure 30.
Figure 30. ACP - Amps AC with A40B-100mA
11. Connect a heavy gauge guard cable between the DUT and the 5790B.
12. Set the Product stimulus per step 5 in Table 19, make a measurement with the 5790B. Record the
measurement in the DMM Reading on Shunt Output [V] column of the table.
13. Complete Table 19, steps 6 to 8.
14. Set the Product to STBY.
15. Connect the test equipment as shown in Figure 31.
+/- 3% (1 year) 83 days since ca2/06/15 10:52am
SetSetReferenceReferenceSe
Me
Auto Range 2.2 V
Pk-Pk StatisticsCurrentShunt
Input 2
5560A
A40B-100mA
Output
5790B
Figure 31. ACP - Amps AC with A40B-1A
16. Set the Product stimulus per step 9 in Table 19, make a measurement with the 5790B. Record the
measurement in the DMM Reading on Shunt Output [V] column of Table 19.
17. Set the Product to STBY.
18. Connect the test equipment as shown in Figure 32.
Figure 32. ACP-Amps AC with A40B-5A
19. Set the Product stimulus per step 10 in Table 19 and make a measurement with the 5790B. Record
the measurement in the DMM Reading on Shunt Output [V] column of the table.
20. Set the Product to STBY.
21. Connect the test equipment as shown in Figure 33.
+/- 3% (1 year) 83 days since ca2/06/15 10:52am
SetSetReferenceReferenceSe
Me
Auto Range 2.2 V
Pk-Pk StatisticsCurrentShunt
Input 2
5560A
A40B-1A
Output
5790B
A40B-5A
Input Output
8588A5560A
Calibration and Verification of the Product
Figure 33. ACP -Amps AC with A40B-20A
22. Set the Product stimulus per step 11 in Table 19 and make a measurement with the 5790B. Record
the measurement in the DMM Reading on Shunt Output [V] column of the table.
23. Set the Product to STBY.
24. For all steps, calculate the Product output with the formula below. Use the appropriate conversion
to convert from base units to units for the specific evaluation step.
25. With the entire table populated, evaluate each step for compliance to limits. To apply
Guardbanding, create a table from the example in this manual, where the acceptance limits are
properly modified by your Guardbanding method.
26. Set the Product to STBY.

<!-- llm_chunk_end id=service_chunk_0008 -->

<!-- llm_chunk_start id=service_chunk_0009 source=service_manual_5560a source_line_start=1921 source_line_end=2180 retrieval_priority=normal -->

## service_chunk_0009: Pk-Pk StatisticsCurrentShunt

Pk-Pk StatisticsCurrentShunt
Input 2
5560A
A40B-1A
Output
5790B
A40B-5A
Input Output
8588A5560A
Calibration and Verification of the Product
Figure 33. ACP -Amps AC with A40B-20A
22. Set the Product stimulus per step 11 in Table 19 and make a measurement with the 5790B. Record
the measurement in the DMM Reading on Shunt Output [V] column of the table.
23. Set the Product to STBY.
24. For all steps, calculate the Product output with the formula below. Use the appropriate conversion
to convert from base units to units for the specific evaluation step.
25. With the entire table populated, evaluate each step for compliance to limits. To apply
Guardbanding, create a table from the example in this manual, where the acceptance limits are
properly modified by your Guardbanding method.
26. Set the Product to STBY.
Table 19. Calibration and Verification steps for AC Power - Amps AC
Step ProductOutputProductFrequencyProductPhase Shunt Shunt_R[Ω]
DMM
Reading on
Shunt
Output [V]
Calculated
Product
Output
90D
Specifi-
cation
Limits
1 1020 V/0.012001 A 333 Hz 0 ° FlukeA40B-10mA ±11 μA
2 500 V/0.012001 A 1666 Hz 0 ° FlukeA40B-10mA ±11 μA
3 250 V/0.012001 A 3333 Hz 0 ° FlukeA40B-10mA ±18 μA
5560A
A40B-20A
Input Output
8588A
Calculated Product Output = DMM Reading on Shunt output [V]
Shunt_R []
Capacitance Calibration and Verification
Table 20 lists the required equipment.
To calibrate the Capacitance function for values <1 mF:
1. Remove the Guard Ground strap on the Product.
2. Set the LCR meter for Cp Mode, Level 1V, Freq 1 kHz, Speed Slow.
Step ProductOutputProductFrequencyProductPhase Shunt Shunt_R[Ω]
DMM
Reading on
Shunt
Output [V]
Calculated
Product
Output
90D
Specifi-
cation
Limits
4 120 V/0.012001 A 10000 Hz 0 ° FlukeA40B-10mA ±34 μA
5 1020 V/0.12001 A 333 Hz 0 °
Fluke
A40B-
100mA
±0.12 mA
6 500 V/0.12001 A 1666 Hz 0 °
Fluke
A40B-
100mA
±0.12 mA
7 250 V/0.12001 A 3333 Hz 0 °
Fluke
A40B-
100mA
±0.18 mA
8 120 V/0.12001 A 10000 Hz 0 °
Fluke
A40B-
100mA
±0.84 mA
9 1020 V/1.20001 A 333 Hz 0 ° FlukeA40B-1A ±0.89 mA
10 1020 V/3.11 A 333 Hz 0 ° FlukeA40B-5A ±4.75 mA
11 1020 V/12.0001 A 333 Hz 0° FlukeA40B-20A ± 23 mA
Table 20. Required Equipment for Capacitance
Equipment Description Manufacture/Model/PN Quantity
Digital Multimeter Fluke 8588A 1
LCR Meter Hioki IM3533 1
Calibrator (precision current source) Fluke 5730A 1
BNC (M) to BNC (M) 4W lead set for LCR Various 1
Low Thermal Cables 5730A-7003 2
BNC (F) to BNC (M) Y Adapter Pomona Model 6700 2
BNC (F) To Single Banana Plug Pomona Model 1894 2
Table 19. Calibration and Verification steps for AC Power - Amps AC (cont.)
Calibration and Verification of the Product
3. Complete the OPEN/SHORT compensation of the LCR meter and lead set for two-wire
measurement that includes the Y adapter and single banana plugs. Do not connect a strap
between the Guard and Ground terminals of the DUT for this function.
4. Connect the LCR meter to the Product for two wire capacitance measurements.
5. From step 1, Table 21, set the LCR meter for the recommended frequency (the Product can be
verified at frequencies other than specified, but the measured output varies within the specifications
as a function of the frequency).
6. Select Cp mode.
7. Output from the Product. Measure with the LCR meter and record in Table 21.
8. When completed, disconnect the current setup.
The Product can source capacitance values larger than what most RCL meters can measure. To do
capacitance verification on outputs >120 μF, a dc current from a precision current source and a high-
speed sampling digital multimeter is necessary.
Table 21. Calibration and Verification Steps for Capacitance with LCR Meter
Step Product Range Product Output Test Frequency Calculated Product Output Limits
1 1.2 nF 0.2 nF 1000 Hz ±4.2 pF
2 1.2 nF 1 nF 1000 Hz ±3.1 pF
3 12 nF 1.21 nF 1000 Hz ±6.3 pF
4 12 nF 10 nF 1000 Hz ±16 pF
5 120 nF 12.1 nF 610 Hz ±45 pF
6 120 nF 20 nF 610 Hz ±54 pF
7 120 nF 30 nF 610 Hz ±66 pF
8 120 nF 50 nF 610 Hz ±90 pF
9 120 nF 100 nF 610 Hz ±150 pF
10 120 nF 120 nF 610 Hz ±174 pF
11 1.2 μF 0.121 μF 100 Hz ±445 pF
12 1.2 μF 1 μF 100 Hz ±1.50 nF
13 12 μF 1.21 μF 80 Hz ±4.45 nF
14 12 μF 10 μF 80 Hz ±15.0 nF
15 120 μF 12.1 μF 20 Hz ±41 nF
16 120 μF 100 μF 20 Hz ±155 nF
17 1.2 mF 0.121 mF 5 Hz ±516 nF
Capacitance is the product of an applied current and the ratio of the charge time to the charge voltage.
A measurement procedure for capacitance is to apply a known current across the capacitor and then
measure the voltage change for a known time interval. Fluke Calibration recommended to implement
the following in computer-controlled routine for consistency of results and timely sequence execution.
To proceed with this calibration and verification:
9. Connect the precision current source, the sampling DMM (8588A) and the Product as shown in
Figure 34.
10. Set the 8588A as follows:
• Reset meter
• Set Initiate Layer to Continuous OFF
• Volts dc
• Range 1 V (10 V for C ≥1.21 mF)
• Aperture 1 ms
• Coupling dc
• Filter ON 100 kHz
• Turn Calculate Statistics to ON
• Select TRIG SETUP and set the Trigger Layer parameters:
Trigger Event Timer
Trigger Timer 5 s
Trigger Count 2
Trigger Delay: 0 s
Delay 0
11. Set the Product to output the first point of Table 22. Set to Operate.
12. Set the current source calibrate to the DC current value in the table for each step.
13. Set to Operate and as soon as the stable LED for the current source is on, trigger the meter.
14. After the meter acquires the data (in 5 seconds), set the current source to STBY.
15. Retrieve the MIN and MAX readings from the meter acquired statistics system. Calculate (MAX -
MIN) and record in Table 22 in the DMM Measurement column.
16. Continue with these steps and use the same routine. The meter setup does not have to be set
again except for the statistics system. Clear the statistics between each step.
C = I *
t
v
Calibration and Verification of the Product
Figure 34. Capacitance Charge Connection
The Calculated Product Output is calculated with this formula:
17. Use the appropriate conversion to convert from base units to units for the specific evaluation step.
18. With the entire table populated, evaluate each step for compliance to limits. To apply
Guardbanding, create a table from the example in this manual, where the acceptance limits are
properly modified by your Guardbanding method.
Table 22. Calibration and Verification Steps for Capacitance Using Charge Method
Step ProductRangeProductOutputTestCurrentDMMMeasurement [V]CalculatedProduct Output Limits
18 1.2 mF 1 mF 90 μA ±2.5 μF
19 12 mF 1.21 mF 219.9 μA ±5.7 μF
20 12 mF 10 mF 2.199 mA ±25 μF
21 120 mF 12.1 mF 5.5 mA ±84 μF
22 120 mF 100 mF 45 mA ±480 μF
5730A
5560A
8588A
Calculated Product Output = Test_current * 
v
Inductance Calibration and Verification (5550A and 5560A)
Table 23 lists the required equipment.
To calibrate the Inductance function:
1. Remove the Guard Ground strap on the Product.
2. Set the LCR meter for Ls Mode, Level 1V, Freq 1 kHz, Speed Slow.
3. Complete OPEN/SHORT compensation of the LCR meter and lead set including the banana to bnc
plugs. Do not connect a strap between the Guard and Ground terminals of the DUT for this
function.
4. Connect the LCR meter to the Product for four-wire inductance measurements.
5. Starting at step 1, Table 24, set the LCR meter for the recommended frequency (the Product can
be verified at frequencies other than the specified, but the measured output varies within the
specifications as a function of the frequency).
6. Select Ls mode.
7. Output each value from the Product. Measure with the LCR meter and record in Table 24.
Table 23. Required Equipment for Inductance
Equipment Description Manufacture/Model/PN Quantity
LCR Meter Hioki IM3533 1
BNC (M) to BNC (M) 4W lead set for LCR Various 1
BNC (F) To Single Banana Plug Pomona Model 1894 4
Table 24. Calibration and Verification Steps for Inductance with LCR Meter
Step Product Range Product Output Test Frequency Calculated Product Output Limits
1 120 μH 15 μH 1000 Hz ±227 nH
2 120 μH 100 μH 1000 Hz ±380 nH
3 1.2 mH 121 μH 1000 Hz ±1.13 μH
4 1.2 mH 1 mH 1000 Hz ±2.1 μH
5 12 mH 1.21 mH 110 Hz ±11.3 μH
6 12 mH 2 mH 110 Hz ±12.2 μH
7 12 mH 3 mH 110 Hz ±13.3 μH
8 12 mH 5 mH 110 Hz ±15.5 μH
9 12 mH 10 mH 110 Hz ±21.0 μH
10 12 mH 12 mH 110 Hz ±23.2 μH
11 120 mH 12.1 mH 100 Hz ±113 μH
12 120 mH 100 mH 100 Hz ±210 μH
13 1.2 H 0.121 H 10 Hz ±1157 μH
14 1.2 H 1 H 10 Hz ±2.3 mH
Calibration and Verification of the Product
8. When completed, disconnect the present setup.
9. Use the appropriate conversion to convert from base units to units for the specific evaluation step.
10. With the entire table populated, evaluate each step for compliance to limits. To apply
Guardbanding, create a table from the example in this manual, where the acceptance limits are
properly modified by your Guardbanding method.
Thermocouple Calibration and Verification
Table 25 lists the required equipment.
The thermocouple function is calibrated for source and measure. The thermocouple function relies on
internal sensing to offset the error caused by the temperature at the thermocouple port. Only one
measurement of an actual thermocouple is required to verify the performance of the temperature
sensing at the thermocouple port. The rest of the measurement verifies the linearity of the
thermocouple function.
To calibrate the Thermocouple Measure function including the temperature compensation:
1. Connect a strap between the Guard and Ground terminals of the DUT.
2. Connect a characterized Type J thermocouple to the Product thermocouple port.
3. Set the Product for tc Type J measure.
4. Set the temperature compensation to internal.
5. Immerse the characterized thermocouple in a lag bath together with the thermistor probe monitored
by a thermometer system.
6. Both the thermocouple and probe must be immersed to the same depth and be in close proximity.
7. Obtain calibration data for the characterized thermocouple and record its error in the Type J tc
Error column of Table 26.
Step Product Range Product Output Test Frequency Calculated Product Output Limits
15 12 H 1.21 H 3 Hz ±12.2 mH
16 12 H 10 H 3 Hz ±28.0 mH
17 120 H 12.1 H 2 Hz ±126.6 mH
18 120 H 100 H 2 Hz ±320 mH
Table 25. Required Equipment for Thermocouple
Equipment Description Manufacture/Model/PN Quantity
Calibrator (precision voltage source) Fluke 5730A 1
Digital Multimeter Fluke 8588A 1
Thermometer Fluke 1504 1
Thermistor probe Fluke 5610-9-B 1
Type J thermocouple Omega TJ36-ICIN-18U-8-SMPW-M 1
Dewar flask with cap Various 1
Type B copper mini-plug with copper wire Various 1
Table 24. Calibration and Verification Steps for Inductance with LCR Meter (cont.)
8. Take a measurement with the Product and record in the Product Measurement column of
Table 26.
9. Take a measurement with the thermometer system and record in the Thermometer Measurement
column of Table 26.
10. Calculate the Product input error as follows:
To calibrate the Thermocouple Measure Function linearity with temperature compensation OFF:
1. Connect a strap between the Guard and Ground terminals of the DUT.
2. Connect a copper thermocouple mini plug with a twisted pair copper wire to the Product
thermocouple port.

<!-- llm_chunk_end id=service_chunk_0009 -->

<!-- llm_chunk_start id=service_chunk_0010 source=service_manual_5560a source_line_start=2161 source_line_end=2420 retrieval_priority=normal -->

## service_chunk_0010: 18 120 H 100 H 2 Hz ±320 mH

18 120 H 100 H 2 Hz ±320 mH
Table 25. Required Equipment for Thermocouple
Equipment Description Manufacture/Model/PN Quantity
Calibrator (precision voltage source) Fluke 5730A 1
Digital Multimeter Fluke 8588A 1
Thermometer Fluke 1504 1
Thermistor probe Fluke 5610-9-B 1
Type J thermocouple Omega TJ36-ICIN-18U-8-SMPW-M 1
Dewar flask with cap Various 1
Type B copper mini-plug with copper wire Various 1
Table 24. Calibration and Verification Steps for Inductance with LCR Meter (cont.)
8. Take a measurement with the Product and record in the Product Measurement column of
Table 26.
9. Take a measurement with the thermometer system and record in the Thermometer Measurement
column of Table 26.
10. Calculate the Product input error as follows:
To calibrate the Thermocouple Measure Function linearity with temperature compensation OFF:
1. Connect a strap between the Guard and Ground terminals of the DUT.
2. Connect a copper thermocouple mini plug with a twisted pair copper wire to the Product
thermocouple port.
3. Connect the twisted pair to the Fluke 5730A OUTPT HI/LO. Observe correct polarity.
4. Disconnect the V-Guard to Ground strap on the 5730A.
5. Set the Product for tc 10 μV/°C measure.
6. Set the temperature compensation to external and 0 °C.
7. Starting with step 1,Table 27, source the voltage from the 5730A (external voltage source output
equivalent).
8. Wait for the DUT to settle and then record the temperature measurement in the Product
Measurement column of Table 27.
9. Calculate the Product input error as follows:
Table 26. Type J Thermocouple Calibration and Verification
Step
Product
Measurement on
Type J tc [°C]
Type J tc Error
from Calibration
[°C]
Thermometer
Measurement of Lag
Bath [°C]
Calculated
Product Input
Error [°C]
Limits
1 ±0.09 °C
Product Input error = Prod meas - tcerror - Thermometer meas
Product Input error [V] = Prodmeas_°C * (10 * 10-6) - 5730Aoutput
Calibration and Verification of the Product
To calibrate the Thermocouple Source function linearity with temperature compensation OFF:
1. Connect a strap between the Guard and Ground terminals of the DUT.
2. Connect a copper thermocouple mini plug with twisted pair copper wire to Fluke 8588A INPUT HI/
LO (observe proper polarity). Short the thermocouple mini plug under the VI AUX binding post of
the 5560A.
3. Set the 8588A as follows: Volts dc, Range 100 mV, NPLC 50, Guard ON (external guard).
4. Push ZERO, and then ZERO FUNC. Allow the zero range to finish.
5. Connect the copper mini plug to the Product thermocouple port.
6. Set the Product for tc 10 μV/°C source.
7. Set the temperature compensation to external and 0°C.
8. Start with step 1, Table 28, source the temperature from the Product (Product Temperature output
setting).
9. Measure with the 8588A and record in the DMM Measurement on Product column of Table 27.
10. Continue with the remainder of the steps in Table 28.
11. Calculate the Product input error as follows:
Table 27. 10 μV/°C Measure Thermocouple Calibration and Verification
Step Temp Amplitude Func-tion Step
Temp-
erature
Set Point
External
Voltage
Source
Output
Equivalent
Product
Measure-
ment
Calc-
ulated
Product
Input
Error [V]
Limits
1 0 °C 0 mV Meas 1 0 °C 0 mV ±1.60 μV
2 1000 °C 10 mV Meas 2 1000 °C 10 mV ±1.80 μV
3 -1000 °C -10 mV Meas 3 -1000 °C -10 mV ±1.80 μV
4 5000 °C 50 mV Meas 2 5000 °C 50 mV ±2.60 μV
5 -5000 °C -50 mV Meas 3 -5000 °C -50 mV ±2.60 μV
6 10000 °C 100 mV Meas 2 10000 °C 100 mV ±3.60 μV
7 -10000 °C -100 mV Meas 3 -10000 °C -100 mV ±3.60 μV
8 30000 °C 300 mV Meas 4 30000 °C 300 mV ±15.0 μV
9 -30000 °C -300 mV Meas 5 -30000 °C -300 mV ±15.0 μV
Product Input error = DMMmeas_°C - Prodoutput (V)
12. With all steps in the table populated, evaluate each step for compliance to limits. To apply
Guardbanding, create a table from the example in this manual, where the acceptance limits are
properly modified by your Guardbanding method.
Phase Calibration and Verification (5530A, 5550A, and 5560A)
Table 29 lists the required equipment.
The phase function is calibrated for dual output voltage as well as when voltage/current are sourced
out of the Product.
Dual voltage output is straightforward - the Product OUTPUT VZ is connected to the phase meter
REFERENCE INPUT and the Product AUX Output is connected to the phase meter SIGNAL INPUT.
Table 28. 10 μV/°C Source Thermocouple Calibration and Verification
Step Product TemperatureOutput settingProduct OutputEquivalentDMM Measurementon Product
Calculated
Product Output
Error [°C]
Limits
1 0 °C 0 mV ±1.00 μV
2 1000 °C 10 mV ±1.16 μV
3 -1000 °C -10 mV ±1.16 μV
4 5000 °C 50 mV ±1.80 μV
5 -5000 °C -50 mV ±1.80 μV
6 10000 °C 100 mV ±2.60 μV
7 -10000 °C -100 mV ±2.60 μV
Table 29. Required Equipment for Phase
Equipment Description Manufacture/Model/PN Quantity
Phase meter Clarke-hess 6000A 1
100 mA Fluke A40B-100mA Current Shunt 1
3 A Fluke A40B-5A Current Shunt 1
(10 A, 12 A and 20 A) Fluke A40B-20A Current Shunt 1
Type N (M) to dual banana (M) E-Z-Hook PN 9415 1
Type N (F) to Type N (F) adapter Various 1
N to 4 mm double banana connector A40B-LEAD/4mm 1
DBL BANANA N (M) RG58C/U (≈ 16") (Fluke PN 900394) 5790-8026 1
BNC (M) to Binding Posts Pomona Model 1296 1
Double banana RG58 cable Pomona Model 2BC-24 and 2BC-36 2
Calibration and Verification of the Product
To calibrate dual output V/V:
1. Connect the phase meter REFERENCE INPUT to the Product OUTPUT VZ HI/LO with the double
banana RG58 cable and BNC (M) to the binding post adapter.
2. Connect the phase meter SIGNAL INPUT to the Product SENSE VZ LO/VI AUX with the double
banana RG58 cable and BNC (M) to the binding post adapter. Use the same length cables for both.
3. Start with step 1, Table 30, source the specified phase with specific signal and frequency
parameters from the Product.
4. Measure with the phase meter and record in the Measured Product Output column.
5. Continue with the remainder of the steps in Table 30.
Voltage/Current output requires the placement of a current shunt between the Product and the phase
meter SIGNAL INPUT.
WCaution
Failure to connect a shunt may result in phase meter damage.
To calibrate dual output V/I:
1. Connect phase meter REFERENCE INPUT to the Product OUTPUT VZ HI/LO with the double
banana RG58 cable and the BNC (M) to the binding post adapter.
2. Connect the phase meter SIGNAL INPUT to the A40B-100mA shunt output with the appropriate
cable and adapters.
3. Connect the shunt input to the Product SENSE VZ LO/VI AUX with the A40B-LEAD/4mm. Use the
cable with such a length that the total length of shunt and cable is approximately the length of the
cables used for the REFERENCE INPUT.
4. Populate Table 31 with the Shunt Phase Error. Obtain the phase error from the A40B specifications
or phase calibration and verification process.
5. Starting with step 8, Table 31, source the specified phase with the specific signal and frequency
parameters from the Product.
Table 30. Phase Calibration and Verification Record for V/V
Step Product Output Product Frequency Product Phase Measured Product Output Limits
1 10 V/5 V 65 Hz 0° ±0.10 °
2 10 V/5 V 65 Hz 30° ±0.10 °
3 10 V/5 V 65 Hz 45° ±0.10 °
4 10 V/5 V 65 Hz 60° ±0.10 °
5 10 V/5 V 65 Hz 90° ±0.10 °
6 10 V/5 V 65 Hz 180° ±0.10 °
7 10 V/5 V 65 Hz 270° ±0.10 °
6. Measure with the phase meter and record in the Measured Product Output column.
7. Continue with the remainder of the steps in Table 31.
8. Complete Table 31, steps 8 to 19 for 100 mA.
9. Set the Product to STBY.
10. Replace the 100 mA shunt with the 5 A shunt. For current >3.1 A connect the shunt input to SENSE
VZ LO/30 A.
11. Complete Table 31, steps 20 and 21.
12. Set the Product to STBY.
13. Replace the 5 A shunt with the 20 A shunt.
14. Complete the remainder of the steps in Table 31.
15. Set the Product to STBY when finished.
16. Calculate the Product output as follows:
17. With all steps in the table populated, evaluate each step for compliance to limits. To apply
Guardbanding, create a table from the example in this manual, where the acceptance limits are
properly modified by your Guardbanding method.
Table 31. Phase Calibration and Verification Record for V/I
Step Product Output ProductFrequencyProductPhase
Shunt
Phase
Error
Measured
Product
Output
Calculated
Product
Output
Limits
8 10 V/0.1 A 65 Hz 0° ±0.10 °
9 10 V/0.1 A 65 Hz 30° ±0.10 °
10 10 V/0.1 A 65 Hz 45° ±0.10 °
11 10 V/0.1 A 65 Hz 60° ±0.10 °
12 10 V/0.1 A 65 Hz 90° ±0.10 °
13 10 V/0.1 A 65 Hz 180° ±0.10 °
14 10 V/0.1 A 65 Hz 270° ±0.10 °
15 10 V/0.1 A 400 Hz 90° ±0.25 °
16 10 V/0.1 A 1000 Hz 90° ±0.50 °
17 10 V/0.1 A 5000 Hz 90° ±2.5 °
18 10 V/0.1 A 10000 Hz 90° ±5.0 °
19 10 V/0.1 A 30000 Hz 90° ±10 °
20 10 V/3.11 A 65 Hz 0° ±0.10 °
21 10 V/3.11 A 400 Hz 0° ±0.25 °
22 1 V/12.1 A 65 Hz 180° ±0.10 °
23 10 V/12.1 A 65 Hz 30° ±0.10 °
Product Product Output = PhaseMeter meas - ShuntPhaseerror
Calibration and Verification of the Product
Frequency Calibration and Verification
Table 32 lists the required equipment.
To calibrate the Frequency function:
1. Set the frequency counter as follows: Frequency Input A, Gate time of 1s, Trigger on positive slope,
AC Coupled, 1 M Ohm Input Impedance, Amplitude 3 V.
2. Connect the frequency counter Input A to the Product OUTPUT VZ HI/LO with the BNC cables and
adapters.
3. Set the Product to the Frequency/Amplitude in Table 33. Set to operate. Measure with the
frequency counter and record the counter measured values in the Product Output Measured by
Counter column.
4. Evaluate for compliance to limits. If Guardbanding is to be applied create a table from the example
in this manual, where the acceptance limits are properly modified by your Guardbanding method.
Step Product Output ProductFrequencyProductPhase
Shunt
Phase
Error
Measured
Product
Output
Calculated
Product
Output
Limits
24 1.21 V/20 A 65 Hz 0° ±0.10 °
25 10 V/20 A 400 Hz 90° ±0.25 °
26 250 V/0.1 A 65 Hz 90° ±0.10 °
27 250 V/0.1 A 10000 Hz 0° ±5.00 °
28 250 V/0.1 A 30000 Hz 45° ±10.00 °
Table 32. Required Equipment for Frequency
Equipment Description Manufacture/Model/PN Quantity
Frequency Counter Tektronix FCA3100 (Option MS or HS) 1
BNC (F) To Single Banana Plug Pomona Model 1894 1
BNC (M) To BNC (M) cable Various 1
Table 33. Frequency Calibration and Verification
Step ProductFrequency Product Amplitude Product Output Measured by Counter Limits
1 1000000 Hz 3 V ±7.5 Hz
Table 31. Phase Calibration and Verification Record for V/I (cont.)
Adjustment
The Product mainframe has no internal hardware adjustments. The display prompts you through the
entire calibration adjustment routine. Calibration adjustment occurs in these major steps:
1. The Product sources specific output values and you measure the outputs using traceable
measuring instruments of higher accuracy. The Product automatically programs the outputs and
prompts you to make external connections to appropriate measurement instruments.
2. At each measure and enter step, you can push the OPTIONS, and BACK UP STEP softkeys to
redo a step, or SKIP STEP to skip over a step.
3. You enter the measured results either manually through the front panel keypad or remotely with an
external terminal or computer.
Note
There are automatic steps that the Product uses. No operator action is necessary for those
steps.
4. The Product computes a software correction factor and stores it in volatile memory.
5. When the calibration adjustment process is complete, you are prompted to either store all the
correction factors in nonvolatile memory or discard them and start over. All the routine calibration
adjustment steps are available from the front panel interface as well as the remote interface (IEEE-

<!-- llm_chunk_end id=service_chunk_0010 -->

<!-- llm_chunk_start id=service_chunk_0011 source=service_manual_5560a source_line_start=2401 source_line_end=2660 retrieval_priority=normal -->

## service_chunk_0011: Step ProductFrequency Product Amplitude Product Output Measured by Counter Limit

Step ProductFrequency Product Amplitude Product Output Measured by Counter Limits
1 1000000 Hz 3 V ±7.5 Hz
Table 31. Phase Calibration and Verification Record for V/I (cont.)
Adjustment
The Product mainframe has no internal hardware adjustments. The display prompts you through the
entire calibration adjustment routine. Calibration adjustment occurs in these major steps:
1. The Product sources specific output values and you measure the outputs using traceable
measuring instruments of higher accuracy. The Product automatically programs the outputs and
prompts you to make external connections to appropriate measurement instruments.
2. At each measure and enter step, you can push the OPTIONS, and BACK UP STEP softkeys to
redo a step, or SKIP STEP to skip over a step.
3. You enter the measured results either manually through the front panel keypad or remotely with an
external terminal or computer.
Note
There are automatic steps that the Product uses. No operator action is necessary for those
steps.
4. The Product computes a software correction factor and stores it in volatile memory.
5. When the calibration adjustment process is complete, you are prompted to either store all the
correction factors in nonvolatile memory or discard them and start over. All the routine calibration
adjustment steps are available from the front panel interface as well as the remote interface (IEEE-
488 or serial). Remote commands for calibration adjustment are described in the 5560A/5550A/
5540A/5530A Remote Programmers Manual located at www.fluke.com.
Start the Adjustment
To begin Product calibration adjustment:
1. Tap Setup on the touch screen
2. Tap Secured under the 55x0A Adjustment where, depending on the device being adjusted, the
model is 5560A, 5550A, 5540A, or 5530A.
3. The Product is protected with security passcode.To unprotect the Product, see Calibration Security
Passcode in the Operators Manual.
4. After the Product is unprotected, the calibration adjustment procedure sequence shows:
DCV * ACV * Frequency * DCI * DCV DCV 1 * ACI * ACV ACV1 * Resistance
Capacitance * Inductance 1 * TC_source * TC_meas
Note
DCV DCV (V dc out of the secondary output) and ACV ACV (V ac out of the secondary output)
are not available on the 5540A. Inductance is not available on the 5540A and 5530A.
To begin a calibration adjustment, tap Continue. The firmware of the device proceeds with the first
section of the calibration adjust sequence.
Adjustment
Volts DC Adjustment (OUTPUT VZ)
The Product begins the adjust with internal steps.Complete a Vdc Zero on the Fluke Calibration 8588A.
Put a 4-wire short (Fluke PN 2540973) across the HI and LO input and sense terminals.
1. Set the 8588A as follows: Volts dc, Range Auto, NPLC 50, Guard ON (external guard).
2. Push ZERO, and then ZERO FUNC. Allow the zero function to finish.
3. Connect a strap between the Guard and Ground terminals of the DUT.
4. When the Product shows a connect prompt, connect the 8588A for vdc measurement with a low
thermal cable. Table 4 is a list of equipment required. Make the connection and tap Continue.
5. When the Product shows an instruction to set the Product to Operate, push J.
6. Measure with the meter and input the value on the touch screen in the Enter Measured Value field.
Note that the Product only accepts values in base units.
7. Continue to follow the on-screen instructions OPERATE/Measure/Input Value until all steps in the
function are complete.
8. When a section is complete, the Product highlights the subsequent section.
Volts AC Adjustment (OUTPUT VZ)
The Product begins the adjustment with internal steps. The volts ac calibration adjustment uses two
methods. For frequencies ≤10 Hz, a low frequency DMM (Fluke Calibration 8588A) is used. For
frequencies >10 Hz, use the Fluke Calibration 5790B AC Measurement Standard.
1. Set the 8588A as follows: Volts ac, Range Auto, Bandwidth Wide, Coupling: DC 10 MΩ, Guard ON
(external guard)
2. Set the 5790B for Input 2, Auto range, High resolution ON, EXT GUARD.
3. When the Product shows a connect prompt, tap Continue.
4. At this time, the Product shows the amplitude/frequency.
a. For steps with frequency ≤10 Hz, connect the 8588A for v ac measurement as per Figure 17.
b. For steps with frequency >10 Hz connect the 5790B for Vac measurement as per Figure 18.
5. Push J.
6. Measure with the meter and input the value on the touch screen in the Enter Measured Value field.
Note that the Product only accepts values in base units.
7. Continue to follow the on-screen instructions (OPERATE/Measure/Input Value) until all steps in the
function are complete. Alternate meters based on frequency of the step as for 4 a and b above.
8. When a section is complete, the Product highlights the subsequent section.
Frequency Adjustment (OUTPUT VZ)
The frequency calibration adjustment requires a frequency counter - see Table 32 for the
recommended model/requirements.
1. When the Product shows a connect prompt, connect the frequency counter Input A to the Product
OUTPUT VZ HI/LO with the BNC cables and adapters
2. Set the frequency counter as follows: Frequency Input A, Gate time of 1s, Trigger on positive slope,
AC Coupled, 1 MΩ Input Impedance, Amplitude 3 V.
3. For each step in this function, set to OPERATE when prompted.
4. Measure with the frequency counter and input the counter measured value with the touch display
interface.
5. Continue with all steps for this function as in step 3 and 4.
6. When a section is complete, the Product highlights the subsequent section.
Amps DC Adjustment
The Product begins the adjustment with internal steps. Once these internal steps complete, the
Product prompts the connection of the VI Aux terminals to a current DMM. This procedure is a
simplified method that does not produce the greatest TUR (Test Uncertainty Ratio). Advanced
calibration laboratories can use modified methods to improve TUR. Alternatively, you can use the
meter with shunts as in the calibration verification section. To proceed with the meter in amps dc mode.
To use the high-accuracy mode (shunts with a meter), you must determine and connect the shunt
model for each step. Failure to connect the appropriate shunt may result in shunt damage.
1. Set the 8588A as follows: Amps dc, Range Auto, NPLC 50, Guard ON (external guard).
2. When the Product shows a connect prompt, connect the 8588A for Idc measurement with a heavy
gauge low thermal cable. Make the connection and tap Continue.
3. When the Product shows an instruction to set the Product to Operate, push J.
4. Measure with the meter and input the value on the touch screen into the Enter Measured Value
field. Note that the Product only accepts values in base units.
5. Continue to follow the instructions on screen for OPERATE/Measure/Input Value and/or switching
to the high current output via OUTPUT LO/SENSE 30 terminals until all steps in the function are
complete.
6. When a section is complete, the Product highlights the subsequent section.
Volts DC (DCV DCV) Adjustment (Secondary Output) (5530A, 5550A, and 5560A)
The Product begins the adjustment with internal steps. Complete a Vdc Zero on the Fluke Calibration
8588A - put a 4-wire short (Fluke PN 2540973) across the HI and LO input and sense terminals.
1. Set the 8588A as follows: Volts dc, Range Auto, NPLC 50, Guard ON (external guard).
2. Push INPUT, and then ZERO FUNC. Allow the zero function to finish.
3. When the Product shows a connect prompt, connect the 8588A for vdc measurement to the
Product as instructed on the display with low-thermal cable.
4. When the Product shows an instruction to set the Product in Operate, push J.
Adjustment
5. Measure with the meter and input the value on the touch screen in the Enter Measured Value field.
Note that the Product only accepts values in base units. Example: a measurement output shows as
100.00000 mV, but the Product expects the value to be input in V.
6. Continue to follow the instructions on screen OPERATE/Measure/Input Value until all steps in the
function are complete.
7. When a section is complete, the Product highlights the subsequent section.
Amps AC Adjustment
The Product prompts for the connection of VI Aux terminals to a current DMM. This procedure is a
simplified method that does not produce the greatest TUR (Test Uncertainty Ratio). Advanced
calibration laboratories can use modified methods to improve TUR. Alternatively, one can use the
meter with shunts as in the calibration verification section. To proceed, put the meter into amps ac
mode. To use the high-accuracy mode (shunts with a meter), you must determine and connect the
shunt model for each step. Failure to connect appropriate shunt may result in shunt damage.
1. Set the 8588A as follows: Amps ac, Range Auto, NPLC 50, Guard ON (external guard).
2. When the Product shows a connect prompt, connect the 8588A for Iac measurement with heavy-
gauge low-thermal cable. Tap Continue after the connection is made.
3. When the Product shows an instruction to set the Product in Operate, push J.
4. Measure with the meter and input the value on the touch screen in the Enter Measured Value field.
Note that the Product only accepts values in base units. Example: a measurement output is shown
as 12.100 mA, but the Product expects the value to be input in A.
5. Continue to follow the on-screen instructions for OPERATE/Measure/Input Value and/or switching
to the high-current output via OUTPUT LO/SENSE 30 terminals until all steps in the function are
complete.
6. When a section is complete, the Product highlights the subsequent section.
Volts AC (ACV ACV) Adjustment (Secondary Output) (5530A, 5550A, and 5560A)
Use the Fluke Calibration 5790B AC Measurement Standard to accomplish the volts ac calibration
adjustment.
1. Set the 5790B for Input 2, Auto range, High resolution ON, EXT GUARD.
2. When the Product shows a connect prompt, tap Continue.
3. Push J to set the Product to operate.
4. Measure with the meter and input the value on the touch screen in the Enter Measured Value field.
Note that the Product only accepts values in base units. Example: a measurement output is shown
as 12.0000 mV, but the Product expects the value to be input in V.
5. Continue to follow the on-screen instructions OPERATE/Measure/Input Value until all steps in the
function are complete. Alternate meters based on frequency of the step as for 4 a and b.
6. When a section is complete, the Product highlights the subsequent section.
Resistance Adjustment
The Product begins the adjustment with internal steps.
Once the internal steps complete, the Product prompts for the connection of a DMM configured for
resistance measurements.
1. Connect the meter to the Product for four-wire measurement.
2. Observe the Product calibration adjust value - this drives the required meter range.
3. Set the 8588A as follows: Four Wire Resistance, Range *, NPLC 50, LoI OFF, Guard ON (external
guard).
4. Temporarily set the 8588A as follows: Volts dc. These prevents tripping the calibrator to STBY,
when the calibrator is set to OPERATE.
5. When the Product shows an instruction to set the Product in Operate, push J.
6. Change the 8588A to the resistance function - all previous setups are preserved.
7. Measure with the meter and input the value on the touch screen in the Enter Measured Value
field.
8. Continue to follow on-screen instructions for OPERATE/Measure/Input Value until all steps in the
function are complete. Note that the subsequent steps require the meter to be in LoI mode (LoI
ON): 121 kΩ, 1.21 MΩ.
9. When a section is complete, the Product highlights the subsequent section.
Capacitance Adjustment
The Product begins the adjustment with a prompt to input the ambient temperature - use the laboratory
temperature at the time of the adjustment.
After the ambient temperature entry, the Product requests an LCR meter connection. Do not connect
the LCR meter to the DUT at this time.
To proceed:
1. Set the LCR meter for Cp Mode, Level 1V, Freq 1 kHz, Speed Slow.
2. Complete ZERO/SHORT compensation of the LCR meter and the lead set for two-wire
measurement when the two-wire setup, including the Y adapter and single banana plugs, is
connected.
3. Do not connect a strap (remove strap) between the Guard and Ground terminals of the DUT for this
function.
4. Connect the LCR meter to the Product for two-wire capacitance measurements.
5. Tap Continue to go to the first adjustment point.
6. For each step, refer to Table 34 for test frequency setup.
Adjustment
Table 34. Adjustment Steps for Capacitance with LCR Meter
Step Product Output Test Frequency
1 0.2 nF 1000 Hz
2 1 nF 1000 Hz
3 1.21 nF 1000 Hz
4 10 nF 1000 Hz
5 12.1 nF 610 Hz
6 20 nF 610 Hz
7 30 nF 610 Hz
8 50 nF 610 Hz
9 100 nF 610 Hz
10 120 nF 610 Hz
11 0.121 μF 100 Hz
12 1 μF 100 Hz
13 1.21 μF 80 Hz
14 10 μF 80 Hz
15 12.1 μF 20 Hz
16 100 μF 20 Hz
17 0.121 mF 5 Hz
18 1 mF 5 Hz
19 1.21 mF 2 Hz
20 10 mF 2 Hz
21 12.1 mF 1 Hz
22 100 mF 1 Hz
7. Set the LCR meter test frequency.
8. Push J to set the Product to Operate.
9. After the LCR meter measurement settles, input the measurement in the Enter Measurement Value
window on the Product.
10. Complete Table 34, steps 6 to 9 until you complete all points in the sequence.
11. Alternatively, Table 34, steps 18 to 22 can be measured with the charge method - follow the
instructions in the calibration verification section.
12. When a section is complete, the Product highlights the subsequent section.
Inductance Adjustment
The Product begins with a prompt to connect an LCR meter. Do not connect the LCR meter to the DUT
at this time. Proceed as follows.
1. Set the LCR meter for Ls Mode, Level 1 V, Freq 1 kHz, Speed Slow.
2. Complete ZERO/SHORT compensation of the LCR meter and the lead set for four-wire
measurement when the single banana plugs are connected. Do not connect a strap (remove strap)
between the Guard and Ground terminals of the DUT for this function.
3. Connect the LCR meter to the Product for four-wire inductance measurements.
4. For each step, refer to Table 35 for the test frequency setup.
Table 35. Adjustment Steps for Inductance with LCR Meter
Step Product Output Test Frequency
1 15 μH 1000 Hz
2 100 μH 1000 Hz
3 121 μH 1000 Hz
4 1 mH 1000 Hz
5 1.21 mH 110 Hz
6 2 mH 110 Hz
7 3 mH 110 Hz
8 5 mH 110 Hz
9 10 mH 110 Hz
10 12 mH 110 Hz
11 12.1 mH 100 Hz
12 100 mH 100 Hz
13 0.121 H 10 Hz
Adjustment
5. Push J to set the Product to Operate.
6. After the LCR meter measurement settles, input the measurement in the Enter Measurement Value
window on the Product display.
7. Continue with Table 35, steps 5 to 8 until you complete all points in the sequence.
8. When a section is complete, the Product highlights the subsequent section.
TC Source Adjustment
The Product begins the adjustment with internal steps. While internal steps are in progress, continue
as follows:
1. Set the 8588A as follows: Volts dc, Range Auto, NPLC 50, Guard OFF (internal guard).
2. Connect Type B copper mini-plug with copper wire to the meter for vdc measurements. Short the
plug at the VI AUX terminal of the Product. Allow 3 minutes for thermal dissipation.
3. Push ZERO, and then ZERO FUNC. Allow the zero function to finish.
4. When the Product shows a connect prompt, connect the 8588A for vdc measurement to the
Product TC INPUT/OUTPUT as instructed on the display with the mini-plug.
5. When the Product shows an instruction to set the Product in Operate, push J.
6. Measure with the meter and input the value on the touch screen in the Enter Measured Value field.
Note that the Product only accepts values in base units. Example: a measurement output shows as
60.00000 mV, but the Product expects the value to be input in V.
7. Follow the on-screen instructions for OPERATE/Measure/Input Value until all steps in the function
are complete.
8. When a section is complete, the Product highlights the subsequent section.
Step Product Output Test Frequency
14 1 H 10 Hz
15 1.21 H 3 Hz
16 10 H 3 Hz

<!-- llm_chunk_end id=service_chunk_0011 -->

<!-- llm_chunk_start id=service_chunk_0012 source=service_manual_5560a source_line_start=2641 source_line_end=2900 retrieval_priority=normal -->

## service_chunk_0012: TC Source Adjustment

TC Source Adjustment
The Product begins the adjustment with internal steps. While internal steps are in progress, continue
as follows:
1. Set the 8588A as follows: Volts dc, Range Auto, NPLC 50, Guard OFF (internal guard).
2. Connect Type B copper mini-plug with copper wire to the meter for vdc measurements. Short the
plug at the VI AUX terminal of the Product. Allow 3 minutes for thermal dissipation.
3. Push ZERO, and then ZERO FUNC. Allow the zero function to finish.
4. When the Product shows a connect prompt, connect the 8588A for vdc measurement to the
Product TC INPUT/OUTPUT as instructed on the display with the mini-plug.
5. When the Product shows an instruction to set the Product in Operate, push J.
6. Measure with the meter and input the value on the touch screen in the Enter Measured Value field.
Note that the Product only accepts values in base units. Example: a measurement output shows as
60.00000 mV, but the Product expects the value to be input in V.
7. Follow the on-screen instructions for OPERATE/Measure/Input Value until all steps in the function
are complete.
8. When a section is complete, the Product highlights the subsequent section.
Step Product Output Test Frequency
14 1 H 10 Hz
15 1.21 H 3 Hz
16 10 H 3 Hz
17 12.1 H 2 Hz
18 100 H 2 Hz
Table 35. Adjustment Steps for Inductance with LCR Meter (cont.)
TC Measure Adjustment
The Product begins the adjustment with a prompt to connect to a vdc calibrator.
1. Connect the Type B copper mini-plug with copper wire between a calibrator and the Product TC
INPUT/OUTPUT. Allow 3 minutes for thermal dissipation.
2. Tap Continue.
3. Follow the on-screen instructions to apply the specific amplitude to the Product.
4. Wait for the calibrator to settle and tap Continue.
5. Follow the on-screen instructions until all steps that require calibrator output are complete.
6. When prompted, connect a characterized Type J thermocouple to the Product.
7. The characterized thermocouple should be immersed in a lag bath together with the thermistor
probe monitored by a thermometer (thermometer system).
8. Both the thermocouple and the probe have to be immersed to the same depth and be in close
proximity.
9. Obtain calibration data for the characterized thermocouple Type J in error from nominal near
ambient - tcerror.
10. Take a measurement with the thermometer system - Thermometermeas.
11. Calculate the Thermometry System output as:
Standard temperature = Thermometermeas - tc error
12. When prompted by the Product, input the calculated standard temperature. The display prompts for
Abort or Save. Tap Save.
This concludes the calibration adjustment of the Product.
Oscilloscope Calibration Option (600M, 1G, and 2G) Calibration,
Verification, and Adjustment
This section documents the calibration, verification, and adjustment procedures of the Oscilloscope
Calibration Option (scope option). Scope options are available for the 5560A, 5550A, and 5540A.
When you use the recommended equipment, these procedures supply traceable results for all scope
option functions. The necessary equipment and minimum specifications are shown in Table 36.
Fluke recommends that you send your Product to Fluke for calibration, verification, and adjustment.
See Contact Fluke Calibration. However, these procedures allow you to adjust the calibration and
verify the scope option at your site if necessary. Read through all procedures before you do them to
make sure you have the necessary resources.
Hardware adjustments made after repair, at the factory, or designated Fluke service centers, are
supplied in this manual.
Required Equipment for Calibration, Verification, and Adjustment
Table 36 summarizes the required equipment used for the calibration adjustment and verification tests
of the scope option. Individual lists of required equipment are included at the start of each test. The
equipment and methods in this manual are simplified to make it possible to calibrate the Product
without advanced metrological techniques and can result in low-test uncertainty ratios.
Oscilloscope Calibration Option (600M, 1G, and 2G) Calibration, Verification, and Adjustment
Scope Option Calibration and Verification
DC Voltage Calibration and Verification
This procedure uses:
• Fluke 8588A Reference Multimeter
• BNC(f) to Double Banana adapter
• BNC(m-f) Feed-Thru Termination 50 Ω
• Output Scope card cable supplied with the scope option
Initial setup:
Set the Product to Scope dc voltage (Function Menu > Scope > DCV).
Table 36. Required Equipment for Scope Option
Equipment Description Manufacture/Model Application
AC Measurement Standard -
50 MHz Wideband option Fluke 5790B/5
Leveled Sine Amplitude, Leveled Sine
Flatness Low Frequency
Calibrator Fluke 5560A/2G Measure ResistanceLeveled Sine Reflection Coefficient
Reference Multimeter Fluke 8588A V dc, V ac and Waveform Generator
RF Bridge Keysight 86205A Leveled Sine Reflection Coefficient
E-Series Power Sensor Keysight E9304A Leveled Sine FlatnessLeveled Sine Reflection Coefficient
EPM Series Power Meter Keysight N1913B Leveled Sine FlatnessLeveled Sine Reflection Coefficient
Arbitrary Function Generator Tektronix AFG1022 Leveled Sine Reflection Coefficient
Mixed Signal Oscilloscope Tektronix MSO64B
Edge Rise Time
Pulse width
Time Marker Period
Type N (M) to Type N (M) adapter CentricRF – C5552 Leveled Sine Reflection Coefficient
Type N (M) to BNC (F) adapter CentricRF – C5032 Leveled Sine FlatnessLeveled Sine Reflection Coefficient
Type N (F) to BNC (F) adapter CentricRF – C5003 Leveled Sine Flatness
BNC (F) to dual banana plug
adapter Pomona – 1269
V dc, V ac and Waveform Generator
Measure resistance
Shorting Cap for BNC (F) Pasternack – PE6012 Leveled Sine Reflection Coefficient
BNC (M-F) 50 Ω Feed-Thru
termination CentricRF – CFT508 V dc, V ac and Waveform Generator
DC Voltage Signal into 1 MΩ Calibration and Verification
1. Make the connections shown in Figure 35.
Figure 35. Equipment Connections for Scope Option DCV, ACV and Edge Adjustment – into
1 M Ohm
2. Make sure the Calibrator is set to 1 MΩ.
3. Set the 8588A to DCV, front input, 60.00 PLC and Zin = 1 MΩ.
4. Set the Calibrator SCOPE output to the voltages in Table 37.
5. Push Jon the Calibrator. Let the 8588A measurement become stable.
6. Record the 8588A measurement for each voltage in Table 37.
7. Compare the result to the Tolerance ±(V dc) column in Table 37.
Table 37. DC Voltage Calibration and Verification at 1 MΩ
Calibrator Output 8588A Measurement(V dc) Tolerance ±(V dc)
0 mV 4.000E-05 V
-0.001 mV 4.000E-05 V
5 mV 4.250E-05 V
-5 mV 4.250E-05 V
5.1 mV 4.255E-05 V
-5.1 mV 4.255E-05 V
20 mV 5.000E-05 V
-20 mV 5.000E-05 V
21 mV 5.050E-05 V
-21 mV 5.050E-05 V
50 mV 6.500E-05 V
Scope Card Cable
comes with DUT
Oscilloscope Calibration Option (600M, 1G, and 2G) Calibration, Verification, and Adjustment
Calibrator Output 8588A Measurement(V dc) Tolerance ±(V dc)
-50 mV 6.500E-05 V
51 mV 6.550E-05 V
-51 mV 6.550E-05 V
200 mV 1.400E-04 V
-200 mV 1.400E-04 V
201 mV 1.405E-04 V
-201 mV 1.405E-04 V
500 mV 2.900E-04 V
-500 mV 2.900E-04 V
501 mV 2.905E-04 V
-501 mV 2.905E-04 V
6.6 V 3.340E-03 V
-6.6 V 3.340E-03 V
6.7 V 3.390E-03 V
-6.7 V 3.390E-03 V
9.5 V 4.790E-03 V
-9.5 V 4.790E-03 V
12 V 6.040E-03 V
-12 V 6.040E-03 V
12.1 V 6.090E-03 V
-12.1 V 6.090E-03 V
65 V 3.254E-02 V
-65 V 3.254E-02 V
120 V 6.004E-02 V
-120 V 6.004E-02 V
Table 37. DC Voltage Calibration and Verification at 1 MΩ (cont.)
DC Voltage Signal into 50 Ω Calibration and Verification
1. Make the connections shown in Figure 36.
Figure 36. Equipment Connections Scope Option DCV, ACV and Edge Adjustment – into
50 Ohm
2. Set the Calibrator to 50 Ω.
3. Set the 8588A to DCV, Front input, 60.00 PLC and Zin = 1 MΩ.
4. Set the Calibrator SCOPE output to the voltages in Table 38.
5. Push J on the Calibrator. Let the 8588A measurement become stable.
6. Record the 8588A measurement for each voltage in Table 38.
7. Compare the result to the Tolerance ±(V dc) column.
Table 38. 10 DC Voltage Calibration and Verification into 50 Ω
Calibrator Output Fluke 8588A Measurement(V dc) Tolerance ±(V dc)
0 mV 4.000E-05 V
-0.001 mV 4.000E-05 V
5 mV 5.250E-05 V
-5 mV 5.250E-05 V
5.1 mV 5.275E-05 V
-5.1 mV 5.275E-05 V
20 mV 9.000E-05 V
-20 mV 9.000E-05 V
21 mV 9.250E-05 V
-21 mV 9.250E-05 V
50 mV 1.650E-04 V
Scope Card Cable
comes with DUT
BNC (M-F) 50 Ω
Feed-Thru termination
Oscilloscope Calibration Option (600M, 1G, and 2G) Calibration, Verification, and Adjustment
AC Voltage Amplitude Calibration and Verification
This procedure uses:
• Fluke 8588A Reference Multimeter
• BNC(f) to Double Banana adapter
• BNC(m-f) Feed-Thru Termination 50 Ω
• Output Scope Card cable supplied with the scope option
Initial Setup:
Set the Product to Scope ac voltage (Function Menu > Scope > ACV).
AC Voltage Signal into 1 MΩ Calibration and Verification
1. Make the connections shown in Figure 35.
2. Make sure the Calibrator is set to 1 MΩ.
8588A settings:
• Function: Digitize
• Input > Terminal > Front
• Coupling, Zin: DC, 1 MΩ
• Measure Setup > Low pass filter: 3 MHz
• Measure Setup > Range: base on AC voltage adjust point
Calibrator Output Fluke 8588A Measurement(V dc) Tolerance ±(V dc)
-50 mV 1.650E-04 V
51 mV 1.675E-04 V
-51 mV 1.675E-04 V
200 mV 5.400E-04 V
-200 mV 5.400E-04 V
201 mV 5.425E-04 V
-201 mV 5.425E-04 V
500 mV 1.290E-03 V
-500 mV 1.290E-03 V
501 mV 1.293E-03 V
-501 mV 1.293E-03 V
6.6 V 1.654E-02 V
-6.6 V 1.654E-02 V
Table 38. 10 DC Voltage Calibration and Verification into 50 Ω (cont.)
• Measure Setup > Aperture: calculated by the this equation:
Sample Rate = 100 * Adjust Frequency
(If Sample Rate > 5000000.0, use 5000000.0)
Aperture = (1 / Sample Rate) - 0.0000002
• Trigger Setup > Triggers/Arm (Count): calculated with this equation:
TriggerCount = 100 * (SampleRate / Adjust Frequency)
3. Set the Calibrator SCOPE output to the voltages in Table 39.
4. Push J on the Calibrator.
5. On the 8588A, push the TRIG softkey to collect data from the waveform. Export the digitized data
to the external device. Reference the 8588A Operators Manual Digitize Menu function for
information to extract the data.
To process the data, separate the data into two groups:
• Top level: MEDIAN of all readings >90% of reference level
• Base level: MEDIAN of all readings <10% of reference level
The measurement value is calculated as:
median of Top line – median of base line
6. Record the 8588A measurement for each voltage in Table 39.
7. Compare the results to those in the Tolerance ±(V dc) column.
Table 39. AC Voltage Calibration and Verification into 1 MΩ
Calibrator Output Fluke 8588AAperture SetupFluke 8588ATrigger Setup
Fluke 8588A
Measurement
(V ac)
Tolerance ±(V ac)
-1 mV 1 kHz 0.0000098 s 10000 4.100E-05 V
1 mV 1 kHz 0.0000098 s 10000 4.100E-05 V
-2 mV 1 kHz 0.0000098 s 10000 4.200E-05 V
2 mV 1 kHz 0.0000098 s 10000 4.200E-05 V
-2.01 mV 1 kHz 0.0000098 s 10000 4.201E-05 V
2.01 mV 1 kHz 0.0000098 s 10000 4.201E-05 V
-5 mV 1 kHz 0.0000098 s 10000 4.500E-05 V
5 mV 1 kHz 0.0000098 s 10000 4.500E-05 V
-5.1 mV 1 kHz 0.0000098 s 10000 4.510E-05 V
5.1 mV 1 kHz 0.0000098 s 10000 4.510E-05 V
-20 mV 1 kHz 0.0000098 s 10000 6.000E-05 V
20 mV 1 kHz 0.0000098 s 10000 6.000E-05 V
-21 mV 1 kHz 0.0000098 s 10000 6.100E-05 V
Oscilloscope Calibration Option (600M, 1G, and 2G) Calibration, Verification, and Adjustment
Calibrator Output Fluke 8588AAperture SetupFluke 8588ATrigger Setup
Fluke 8588A
Measurement
(V ac)
Tolerance ±(V ac)
21 mV 1 kHz 0.0000098 s 10000 6.100E-05 V
-50 mV 1 kHz 0.0000098 s 10000 9.000E-05 V
50 mV 1 kHz 0.0000098 s 10000 9.000E-05 V
-51 mV 1 kHz 0.0000098 s 10000 9.100E-05 V
51 mV 1 kHz 0.0000098 s 10000 9.100E-05 V
-200 mV 1 kHz 0.0000098 s 10000 2.400E-04 V
200 mV 1 kHz 0.0000098 s 10000 2.400E-04 V

<!-- llm_chunk_end id=service_chunk_0012 -->

<!-- llm_chunk_start id=service_chunk_0013 source=service_manual_5560a source_line_start=2881 source_line_end=3140 retrieval_priority=normal -->

## service_chunk_0013: -5 mV 1 kHz 0.0000098 s 10000 4.500E-05 V

-5 mV 1 kHz 0.0000098 s 10000 4.500E-05 V
5 mV 1 kHz 0.0000098 s 10000 4.500E-05 V
-5.1 mV 1 kHz 0.0000098 s 10000 4.510E-05 V
5.1 mV 1 kHz 0.0000098 s 10000 4.510E-05 V
-20 mV 1 kHz 0.0000098 s 10000 6.000E-05 V
20 mV 1 kHz 0.0000098 s 10000 6.000E-05 V
-21 mV 1 kHz 0.0000098 s 10000 6.100E-05 V
Oscilloscope Calibration Option (600M, 1G, and 2G) Calibration, Verification, and Adjustment
Calibrator Output Fluke 8588AAperture SetupFluke 8588ATrigger Setup
Fluke 8588A
Measurement
(V ac)
Tolerance ±(V ac)
21 mV 1 kHz 0.0000098 s 10000 6.100E-05 V
-50 mV 1 kHz 0.0000098 s 10000 9.000E-05 V
50 mV 1 kHz 0.0000098 s 10000 9.000E-05 V
-51 mV 1 kHz 0.0000098 s 10000 9.100E-05 V
51 mV 1 kHz 0.0000098 s 10000 9.100E-05 V
-200 mV 1 kHz 0.0000098 s 10000 2.400E-04 V
200 mV 1 kHz 0.0000098 s 10000 2.400E-04 V
-201 mV 1 kHz 0.0000098 s 10000 2.410E-04 V
201 mV 1 kHz 0.0000098 s 10000 2.410E-04 V
-500 mV 1 kHz 0.0000098 s 10000 5.400E-04 V
500 mV 1 kHz 0.0000098 s 10000 5.400E-04 V
-501 mV 1 kHz 0.0000098 s 10000 5.410E-04 V
501 mV 1 kHz 0.0000098 s 10000 5.410E-04 V
-2 V 1 kHz 0.0000098 s 10000 2.040E-03 V
2 V 1 kHz 0.0000098 s 10000 2.040E-03 V
-2.01 V 40.01 Hz 0.0002498 s 10000 2.050E-03 V
2.01 V 40.01 Hz 0.0002498 s 10000 2.050E-03 V
-2.01 V 1 kHz 0.0000098 s 10000 2.050E-03 V
2.01 V 1 kHz 0.0000098 s 10000 2.050E-03 V
-2.01 V 10 kHz 0.0000008 s 10000 5.065E-03 V
2.01 V 10 kHz 0.0000008 s 10000 5.065E-03 V
-6.6 V 40.01 Hz 0.0002498 s 10000 6.640E-03 V
6.6 V 40.01 Hz 0.0002498 s 10000 6.640E-03 V
-6.6 V 1 kHz 0.0000098 s 10000 6.640E-03 V
6.6 V 1 kHz 0.0000098 s 10000 6.640E-03 V
-6.6 V 10 kHz 0.0000008 s 10000 1.654E-02 V
6.6 V 10 kHz 0.0000008 s 10000 1.654E-02 V
-6.7 V 40.01 Hz 0.0002498 s 10000 6.740E-03 V
Table 39. AC Voltage Calibration and Verification into 1 MΩ (cont.)
Calibrator Output Fluke 8588AAperture SetupFluke 8588ATrigger Setup
Fluke 8588A
Measurement
(V ac)
Tolerance ±(V ac)
6.7 V 40.01 Hz 0.0002498 s 10000 6.740E-03 V
-6.7 V 1 kHz 0.0000098 s 10000 6.740E-03 V
6.7 V 1 kHz 0.0000098 s 10000 6.740E-03 V
-6.7 V 10 kHz 0.0000008 s 10000 1.679E-02 V
6.7 V 10 kHz 0.0000008 s 10000 1.679E-02 V
-15 V 40.01 Hz 0.0002498 s 10000 1.504E-02 V
15 V 40.01 Hz 0.0002498 s 10000 1.504E-02 V
-15 V 1 kHz 0.0000098 s 10000 1.504E-02 V
15 V 1 kHz 0.0000098 s 10000 1.504E-02 V
-15 V 10 kHz 0.0000008 s 10000 3.754E-02 V
15 V 10 kHz 0.0000008 s 10000 3.754E-02 V
-15.1 V 40.01 Hz 0.0002498 s 10000 1.514E-02 V
15.1 V 40.01 Hz 0.0002498 s 10000 1.514E-02 V
-15.1 V 1 kHz 0.0000098 s 10000 1.514E-02 V
15.1 V 1 kHz 0.0000098 s 10000 1.514E-02 V
-15.1 V 10 kHz 0.0000008 s 10000 3.779E-02 V
15.1 V 10 kHz 0.0000008 s 10000 3.779E-02 V
-120 V 40.01 Hz 0.0002498 s 10000 1.200E-01 V
120 V 40.01 Hz 0.0002498 s 10000 1.200E-01 V
-120 V 1 kHz 0.0000098 s 10000 1.200E-01 V
120 V 1 kHz 0.0000098 s 10000 1.200E-01 V
-120 V 10 kHz 0.0000008 s 10000 3.000E-01 V
120 V 10 kHz 0.0000008 s 10000 3.000E-01 V
Table 39. AC Voltage Calibration and Verification into 1 MΩ (cont.)
Oscilloscope Calibration Option (600M, 1G, and 2G) Calibration, Verification, and Adjustment
AC Voltage Signal into 50 Ω Calibration and Verification
1. Make the connections shown in Figure 36.
2. Make sure the Product is set to 50 Ω.
8588A settings:
• Function: Digitize
• Input > Terminal > Front
• Coupling, Zin: DC, 1 MΩ
• Measure Setup > Low pass filter: 3 MHz
• Measure Setup > Range: base on ac voltage adjust point
• Measure Setup > Aperture: calculated with this equation:
Sample Rate = 100 * Adjust Frequency
(If Sample Rate > 5000000.0, use 5000000.0)
Aperture = (1 / Sample Rate) - 0.0000002
• Trigger Setup > Triggers/Arm (Count): calculated with this equation:
Trigger Count = 100 * (Sample Rate / Adjust Frequency)
3. Set the Calibrator SCOPE output to the voltages in Table 40.
4. Push J on the Calibrator.
5. On 8588A Reference Multimeter, push TRIG softkey to collect data from the waveform. Export the
digitized data to the external device. Reference the 8588A Operators Manual Digitize Menu
function for information to extract the data.
To process the data, separate the data into two groups:
• Top level: MEDIAN of all readings >90% of reference level
• Base level: MEDIAN of all readings <10% of reference level
The measurement value is calculated as:
median of Top line – median of Base line
6. Record the 8588A measurement for each voltage in Table 40.
7. Compare the results to those in the Tolerance ±(V ac) column.
Table 40. AC Voltage Calibration and Verification into 50 Ω
Calibrator Output Fluke 8588AAperture SetupFluke 8588ATrigger Setup
Fluke 8588A
Measurement
(V ac)
Tolerance
±(V ac)
-1 mV 1 kHz 0.0000098 s 10000 4.250E-05 V
1 mV 1 kHz 0.0000098 s 10000 4.250E-05 V
-2 mV 1 kHz 0.0000098 s 10000 4.500E-05 V
2 mV 1 kHz 0.0000098 s 10000 4.500E-05 V
-2.01 mV 1 kHz 0.0000098 s 10000 4.503E-05 V
2.01 mV 1 kHz 0.0000098 s 10000 4.503E-05 V
-5 mV 1 kHz 0.0000098 s 10000 5.250E-05 V
5 mV 1 kHz 0.0000098 s 10000 5.250E-05 V
-5.1 mV 1 kHz 0.0000098 s 10000 5.275E-05 V
5.1 mV 1 kHz 0.0000098 s 10000 5.275E-05 V
-20 mV 1 kHz 0.0000098 s 10000 9.000E-05 V
20 mV 1 kHz 0.0000098 s 10000 9.000E-05 V
-21 mV 1 kHz 0.0000098 s 10000 9.250E-05 V
21 mV 1 kHz 0.0000098 s 10000 9.250E-05 V
-50 mV 1 kHz 0.0000098 s 10000 1.650E-04 V
50 mV 1 kHz 0.0000098 s 10000 1.650E-04 V
-51 mV 1 kHz 0.0000098 s 10000 1.675E-04 V
51 mV 1 kHz 0.0000098 s 10000 1.675E-04 V
-200 mV 1 kHz 0.0000098 s 10000 5.400E-04 V
200 mV 1 kHz 0.0000098 s 10000 5.400E-04 V
-201 mV 1 kHz 0.0000098 s 10000 5.425E-04 V
201 mV 1 kHz 0.0000098 s 10000 5.425E-04 V
-500 mV 1 kHz 0.0000098 s 10000 1.290E-03 V
500 mV 1 kHz 0.0000098 s 10000 1.290E-03 V
-501 mV 1 kHz 0.0000098 s 10000 1.293E-03 V
501 mV 1 kHz 0.0000098 s 10000 1.293E-03 V
-2 V 1 kHz 0.0000098 s 10000 5.040E-03 V
2 V 1 kHz 0.0000098 s 10000 5.040E-03 V
-2.01 V 40.01 Hz 0.0002498 s 10000 5.065E-03 V
Oscilloscope Calibration Option (600M, 1G, and 2G) Calibration, Verification, and Adjustment
Waveform Generator Calibration and Verification
This procedure uses:
• Fluke 8588A Reference Multimeter
• BNC(f) to Double Banana adapter
• BNC(m-f) Feed-Thru Termination 50 Ω
• Output Scope Card cable supplied with the scope option
Initial Setup:
Set the Product to the Scope Waveform Generator function (Function Menu > Scope > Waveform
Generator).
Calibration and Verification Signal into 1 MΩ
1. Make the connections shown in Figure 35.
2. Make sure the Calibrator is set to 1 MΩ.
8588A settings:
• Function: Digitize
• Input > Terminal > Front
• Coupling, Zin: DC, 1 MΩ
• Measure Setup > Low pass filter: 3 MHz
• Measure Setup > Range: base on ac voltage adjust point
• Measure Setup > Aperture: calculated with this equation:
Calibrator Output Fluke 8588AAperture SetupFluke 8588ATrigger Setup
Fluke 8588A
Measurement
(V ac)
Tolerance
±(V ac)
2.01 V 40.01 Hz 0.0002498 s 10000 5.065E-03 V
-2.01 V 1 kHz 0.0000098 s 10000 5.065E-03 V
2.01 V 1 kHz 0.0000098 s 10000 5.065E-03 V
-2.01 V 10 kHz 0.0000008 s 10000 5.065E-03 V
2.01 V 10 kHz 0.0000008 s 10000 5.065E-03 V
-6.6 V 40.01 Hz 0.0002498 s 10000 1.654E-02 V
6.6 V 40.01 Hz 0.0002498 s 10000 1.654E-02 V
-6.6 V 1 kHz 0.0000098 s 10000 1.654E-02 V
6.6 V 1 kHz 0.0000098 s 10000 1.654E-02 V
-6.6 V 10 kHz 0.0000008 s 10000 1.654E-02 V
6.6 V 10 kHz 0.0000008 s 10000 1.654E-02 V
Table 40. AC Voltage Calibration and Verification into 50 Ω (cont.)
Sample Rate = 100 * Adjust Frequency
(If Sample Rate > 5000000.0, use 5000000.0)
Aperture = (1 / Sample Rate) - 0.0000002
• Trigger Setup > Triggers/Arm (Count): calculated with this equation:
TriggerCount = 100 * (SampleRate / Adjust Frequency)
3. Set the Calibrator SCOPE voltage output and waveform as shown in Table 41.
4. Push Jon the Calibrator.
5. On 8588A Reference Multimeter, push TRIG softkey to collect data from the waveform. Export the
digitized data to the external device. Reference the 8588A Operators Manual Digitize Menu
function for information to extract the data.
To process the data, separate the data into two groups:
• Top level: MEDIAN of all readings > 90% of reference level
• Base level: MEDIAN of all readings < 10% of reference level
The measurement value is calculated as:
median of Top line – median of Base line
6. Record the 8588A measurement for each voltage in Table 41.
7. Compare the results to those in the Tolerance ± V column.
Table 41. Waveform Generator Calibration and Verification - into 1 MΩ
Output
Waveform
Fluke 8588A
Aperture Setup
Fluke 8588A
Trigger Setup
Fluke 8588A
Measurement
(V)
Tolerance
± V
1 mV 1 kHz SQUARE 0.0000098 s 10000 1.300E-04 V
2 mV 1 kHz SQUARE 0.0000098 s 10000 1.600E-04 V
2.01 mV 1 kHz SQUARE 0.0000098 s 10000 1.603E-04 V
5 mV 1 kHz SQUARE 0.0000098 s 10000 2.500E-04 V
5.1 mV 1 kHz SQUARE 0.0000098 s 10000 2.530E-04 V
20 mV 1 kHz SQUARE 0.0000098 s 10000 7.000E-04 V
21 mV 1 kHz SQUARE 0.0000098 s 10000 7.300E-04 V
50 mV 1 kHz SQUARE 0.0000098 s 10000 1.600E-03 V
51 mV 1 kHz SQUARE 0.0000098 s 10000 1.630E-03 V
200 mV 1 kHz SQUARE 0.0000098 s 10000 6.100E-03 V
201 mV 1 kHz SQUARE 0.0000098 s 10000 6.130E-03 V
500 mV 1 kHz SQUARE 0.0000098 s 10000 1.510E-02 V
501 mV 1 kHz SQUARE 0.0000098 s 10000 1.513E-02 V
2 V 1 kHz SQUARE 0.0000098 s 10000 6.010E-02 V
Oscilloscope Calibration Option (600M, 1G, and 2G) Calibration, Verification, and Adjustment
Output
Waveform
Fluke 8588A
Aperture Setup
Fluke 8588A
Trigger Setup
Fluke 8588A
Measurement
(V)
Tolerance
± V
2.01 V 1 kHz SQUARE 0.0000098 s 10000 6.040E-02 V
6.6 V 1 kHz SQUARE 0.0000098 s 10000 1.981E-01 V
6.7 V 1 kHz SQUARE 0.0000098 s 10000 2.011E-01 V
15 V 1 kHz SQUARE 0.0000098 s 10000 4.501E-01 V
15.1 V 1 kHz SQUARE 0.0000098 s 10000 4.531E-01 V
120 V 1 kHz SQUARE 0.0000098 s 10000 3.600E+00 V
1 mV 10 kHz SINE 0.0000008 s 10000 1.300E-04 V
2 mV 10 kHz SINE 0.0000008 s 10000 1.600E-04 V
2.01 mV 10 kHz SINE 0.0000008 s 10000 1.603E-04 V
5 mV 10 kHz SINE 0.0000008 s 10000 2.500E-04 V
5.1 mV 10 kHz SINE 0.0000008 s 10000 2.530E-04 V
20 mV 10 kHz SINE 0.0000008 s 10000 7.000E-04 V
21 mV 10 kHz SINE 0.0000008 s 10000 7.300E-04 V
50 mV 10 kHz SINE 0.0000008 s 10000 1.600E-03 V
51 mV 10 kHz SINE 0.0000008 s 10000 1.630E-03 V
200 mV 10 kHz SINE 0.0000008 s 10000 6.100E-03 V
201 mV 10 kHz SINE 0.0000008 s 10000 6.130E-03 V
500 mV 10 kHz SINE 0.0000008 s 10000 1.510E-02 V
501 mV 10 kHz SINE 0.0000008 s 10000 1.513E-02 V
6.6 V 10 kHz SINE 0.0000008 s 10000 1.981E-01 V
6.7 V 10 kHz SINE 0.0000008 s 10000 2.011E-01 V
15 V 10 kHz SINE 0.0000008 s 10000 4.501E-01 V
15.1 V 10 kHz SINE 0.0000008 s 10000 4.531E-01 V
120 V 10 kHz SINE 0.0000008 s 10000 3.600E+00 V
Table 41. Waveform Generator Calibration and Verification - into 1 MΩ (cont.)
Calibration and Verification Signal into 50 Ω
1. Make the connections shown in Figure 36.
2. Make sure the Calibrator is set to 50 Ω.
8588A settings:
• Function: Digitize
• Input > Terminal > Front
• Coupling, Zin: DC, 1 MΩ

<!-- llm_chunk_end id=service_chunk_0013 -->

<!-- llm_chunk_start id=service_chunk_0014 source=service_manual_5560a source_line_start=3121 source_line_end=3380 retrieval_priority=normal -->

## service_chunk_0014: 21 mV 10 kHz SINE 0.0000008 s 10000 7.300E-04 V

21 mV 10 kHz SINE 0.0000008 s 10000 7.300E-04 V
50 mV 10 kHz SINE 0.0000008 s 10000 1.600E-03 V
51 mV 10 kHz SINE 0.0000008 s 10000 1.630E-03 V
200 mV 10 kHz SINE 0.0000008 s 10000 6.100E-03 V
201 mV 10 kHz SINE 0.0000008 s 10000 6.130E-03 V
500 mV 10 kHz SINE 0.0000008 s 10000 1.510E-02 V
501 mV 10 kHz SINE 0.0000008 s 10000 1.513E-02 V
6.6 V 10 kHz SINE 0.0000008 s 10000 1.981E-01 V
6.7 V 10 kHz SINE 0.0000008 s 10000 2.011E-01 V
15 V 10 kHz SINE 0.0000008 s 10000 4.501E-01 V
15.1 V 10 kHz SINE 0.0000008 s 10000 4.531E-01 V
120 V 10 kHz SINE 0.0000008 s 10000 3.600E+00 V
Table 41. Waveform Generator Calibration and Verification - into 1 MΩ (cont.)
Calibration and Verification Signal into 50 Ω
1. Make the connections shown in Figure 36.
2. Make sure the Calibrator is set to 50 Ω.
8588A settings:
• Function: Digitize
• Input > Terminal > Front
• Coupling, Zin: DC, 1 MΩ
• Measure Setup > Low pass filter: 3 MHz
• Measure Setup > Range: base on AC voltage adjust point
• Measure Setup > Aperture: calculated by the following equation
• Sample Rate = 100 * Adjust Frequency
• (If Sample Rate > 5000000.0, use 5000000.0)
• Aperture = (1 / Sample Rate) - 0.0000002
• Trigger Setup > Triggers/Arm (Count): calculated with the following equation:
• Trigger Count = 100 * (Sample Rate / Adjust Frequency)
3. Set the Calibrator SCOPE output to the voltage in Table 42.
4. Push J on the Calibrator.
5. On 8588A Reference Multimeter, push TRIG softkey to collect data from the waveform. Export the
digitized data to the external device. Reference the 8588A Operators Manual Digitize Menu
function for information to extract the data.
To process this data, separate the data into two groups:
• Top level: MEDIAN of all readings > 90% of reference level
• Base level: MEDIAN of all readings < 10% of reference level
The measurement value is calculated as:
median of Top line – median of Base line
6. Record the 8588A measurement for each voltage in Table 42.
7. Compare the results to those in the Tolerance ±(V) column.
Table 42. Waveform Generator Calibration and Verification - into 50 Ω
Output
Waveform
Fluke 8588A
Aperture
Setup
Fluke 8588A
Trigger Setup
Fluke 8588A
Measurement
(V)
Tolerance
±(V)
1 mV 1 kHz SQUARE 0.0000098 s 10000 1.300E-04 V
2 mV 1 kHz SQUARE 0.0000098 s 10000 1.600E-04 V
2.01 mV 1 kHz SQUARE 0.0000098 s 10000 1.603E-04 V
5 mV 1 kHz SQUARE 0.0000098 s 10000 2.500E-04 V
Oscilloscope Calibration Option (600M, 1G, and 2G) Calibration, Verification, and Adjustment
Output
Waveform
Fluke 8588A
Aperture
Setup
Fluke 8588A
Trigger Setup
Fluke 8588A
Measurement
(V)
Tolerance
±(V)
5.1 mV 1 kHz SQUARE 0.0000098 s 10000 2.530E-04 V
20 mV 1 kHz SQUARE 0.0000098 s 10000 7.000E-04 V
21 mV 1 kHz SQUARE 0.0000098 s 10000 7.300E-04 V
50 mV 1 kHz SQUARE 0.0000098 s 10000 1.600E-03 V
51 mV 1 kHz SQUARE 0.0000098 s 10000 1.630E-03 V
200 mV 1 kHz SQUARE 0.0000098 s 10000 6.100E-03 V
201 mV 1 kHz SQUARE 0.0000098 s 10000 6.130E-03 V
500 mV 1 kHz SQUARE 0.0000098 s 10000 1.510E-02 V
501 mV 1 kHz SQUARE 0.0000098 s 10000 1.513E-02 V
2 V 1 kHz SQUARE 0.0000098 s 10000 6.010E-02 V
2.01 V 1 kHz SQUARE 0.0000098 s 10000 6.040E-02 V
6.6 V 1 kHz SQUARE 0.0000098 s 10000 1.981E-01 V
1 mV 10 kHz SINE 0.0000008 s 10000 1.300E-04 V
2 mV 10 kHz SINE 0.0000008 s 10000 1.600E-04 V
2.01 mV 10 kHz SINE 0.0000008 s 10000 1.603E-04 V
5 mV 10 kHz SINE 0.0000008 s 10000 2.500E-04 V
5.1 mV 10 kHz SINE 0.0000008 s 10000 2.530E-04 V
20 mV 10 kHz SINE 0.0000008 s 10000 7.000E-04 V
21 mV 10 kHz SINE 0.0000008 s 10000 7.300E-04 V
50 mV 10 kHz SINE 0.0000008 s 10000 1.600E-03 V
51 mV 10 kHz SINE 0.0000008 s 10000 1.630E-03 V
200 mV 10 kHz SINE 0.0000008 s 10000 6.100E-03 V
201 mV 10 kHz SINE 0.0000008 s 10000 6.130E-03 V
500 mV 10 kHz SINE 0.0000008 s 10000 1.510E-02 V
501 mV 10 kHz SINE 0.0000008 s 10000 1.513E-02 V
2 V 10 kHz SINE 0.0000008 s 10000 6.010E-02 V
2.01 V 10 kHz SINE 0.0000008 s 10000 6.040E-02 V
6.6 V 10 kHz SINE 0.0000008 s 10000 1.981E-01 V
Table 42. Waveform Generator Calibration and Verification - into 50 Ω (cont.)
Leveled Sine Amplitude Calibration and Verification
This procedure uses:
• Fluke 5790B AC Measurement Standard - Wideband
• Output Scope Card cable supplied with the scope option
Initial setup
Set the Calibrator to (Function Menu > Scope > Leveled Sine).
Leveled Sign Amplitude Calibration and Verification
1. Connect the Output N-type terminal to a 5790B Wideband configured as shown in Figure 37. Note
that this same configuration is used in Leveled Sine Amplitude Calibration and Verification and
Leveled Sine Wave Adjustment.
Figure 37. 5790B to Calibrator Connections
2. Set the Calibrator to 1 MΩ.
3. Set the 5790B to Wideband measurements with the ranges shown in Table 43.
4. Set the Product SCOPE output to the voltages shown in Table 43.
5. Push J on the Product. Let the 5790B measurement become stable.
6. Record the 5790B Wideband measurement for each voltage in Table 43.
Note
Make sure to convert the 5790B Wideband reading in Table 43 from Vrms to Vpp.
7. Compare the results to those in the Tolerance ±(Vpp) column of Table 43.
+/- 3% (1 year) 83 days since calibration2/06/15 10:52am
SetReference
Input 2
V1.000010.00004 kHz
Auto Range 22 V
SetupMenuPeak-to-Peak StatisticsCurrentShunt Reset
EX TRIGTRIG
INPUT 1 WIDEBAND GUARDINPUT 2
22 mV 220 mV 22 V2.2 V 220 V2.2 mV70 mV 700 mV 70 V7 V 700 V7 mV
1 kV
AUX5790B STD
DUT
Vpp = Vrms X 2 √2
Oscilloscope Calibration Option (600M, 1G, and 2G) Calibration, Verification, and Adjustment
Leveled Sine Flatness relative to 50 kHz Calibration and Verification
Leveled Sine Wave Flatness calibration and verification is divided into two frequency bands: 50 kHz to
50 MHz (Low frequency) and >50 MHz to 2 GHz (High frequency). The equipment setups are different
for each band. Leveled Sine Wave flatness is measured relative to 50 kHz. This is a direct
measurement in the low frequency band. You must do a transfer measurement at 50 MHz in the high
frequency band to calculate a flatness relative to 50 kHz.
Equipment Setup for Low Frequency Flatness:
• Fluke 5790B AC Measurement Standard with Wideband option
• BNC(f) to Type N(m) adapter
• Output Scope Card cable supplied with the scope option
Initial setup:
1. Use the connections shown in Figure 37.
2. Set the 5790B to Wideband, EXTRIG OFF and HIRES ON.
Equipment setup for High Frequency Flatness:
• Fluke 5790B AC Measurement Standard with Wideband option
• BNC(f) to Type N(m) adapter
• Keysight N1913B Power meter
• Keysight E9304A Power sensor
• BNC(f) to Type N(f) adapter
• Output Scope Card cable supplied with the scope option
Table 43. Leveled Sine Amplitude Calibration and Verification
Calibrator Output Fluke 5790B WidebandRange Setup
Fluke 5790B Wideband
Measurement
(Vpp)
Tolerance ±(Vpp)
5 mV 50 kHz 2.2 mV 4.000E-04 V
20 mV 50 kHz 7 mV 7.000E-04 V
20.1 mV 50 kHz 7 mV 7.020E-04 V
50 mV 50 kHz 22 mV 1.300E-03 V
50.1 mV 50 kHz 22 mV 1.302E-03 V
200 mV 50 kHz 70 mV 4.300E-03 V
201 mV 50 kHz 70 mV 4.320E-03 V
500 mV 50 kHz 220 mV 1.030E-02 V
501 mV 50 kHz 220 mV 1.032E-02 V
2 V 50 kHz 700 mV 4.030E-02 V
2.01 V 50 kHz 700 mV 4.050E-02 V
5.5 V 50 kHz 2.2 V 1.103E-01 V
Initial setup:
1. Connect the Keysight N1913B Power Meter to the Keysight E9304A Power Sensor, see Figure 44.
To learn more about how to connect these two instruments, refer to the operator manuals of the
instruments.
2. Zero and self-calibrate the power meter with the power sensor. Refer to the Keysight N1913B
operator manual to learn more.
3. Connect the power meter and power sensor combination, see Figure 38.
Figure 38. Calibrator and Keysight Power Meter and Power Sensor Connections
The Keysight N1913B Power Meter must be configured with:
• Reference relative to 50 MHz
• AVER:COUN 256
• Turn off Relative for Chan A
• WATTS
Low Frequency Leveled Sine Flatness Calibration and Verification
This procedure gives an example of a low frequency flatness test with a 5 mV Calibrator output. Use
the same procedure for other amplitudes. Compare the results with the flatness specification shown in
Table 44.
1. Set the Calibrator to output of 5 mV at 50 kHz.
2. Push J on the Product.
3. Allow the 5790B Wideband measurement to become stable. The 5790B shows approximately
1.77 mV rms.
4. Record the 5790B Wideband measurement in column A of Table 44 for the test voltages in all
rows.
5. Set the Calibrator to the test frequencies listed Table 44. Allow the 5790B Wideband measurement
to become stable.
6. Record the 5790B Wideband measurement in column B of Table 44.
7. Repeat Table 44, steps 5 and 6 for all the frequencies shown in the table for 5 mV applied.
Continue until you complete columns A and B.
Scope Card Cable
Comes with DUT
Power Meter STD
Type N (F) to BNC (F) Adapter E9034A Power Sensor
DUT
Oscilloscope Calibration Option (600M, 1G, and 2G) Calibration, Verification, and Adjustment
8. After both columns A and B are filled for all rows of the table, push L on the Calibrator.
9. Use the recorded values in columns A and B to calculate and record the value in column C for all
rows with this formula:
10. Compare column C to the specifications shown in the last column.
Table 44. Low Frequency Leveled Sine Flatness Relative to 50 kHz Calibration and Verification
Calibrator Output A50 kHz B C Tolerance ±(%)
5 mV Applied
100 kHz 3.50 %
200 kHz 3.50 %
500 kHz 3.50 %
1 MHz 3.50 %
2 MHz 3.50 %
5 MHz 3.50 %
10 MHz 3.50 %
20 MHz 5.00 %
49.99 MHz 5.00 %
50 MHz 5.00 %
16 mV Applied
50 MHz 3.63 %
16.1 mV Applied
50 MHz 3.62 %
Calibrator Output A50 kHz B C Tolerance ±(%)
20 mV Applied
100 kHz 2.00 %
200 kHz 2.00 %
500 kHz 2.00 %
1 MHz 2.00 %
2 MHz 2.00 %
5 MHz 2.00 %
Column C = 100 * Column B - Column AColumn A
10 MHz 2.00 %
20 MHz 3.50 %
49.99 MHz 3.50 %
20.1 mV Applied
100 kHz 2.00 %
200 kHz 2.00 %
500 kHz 2.00 %
1 MHz 2.00 %
2 MHz 2.00 %
5 MHz 2.00 %
10 MHz 2.00 %
20 MHz 3.50 %
49.99 MHz 3.50 %
50 mV Applied
100 kHz 1.70 %
200 kHz 1.70 %
500 kHz 1.70 %
1 MHz 1.70 %
2 MHz 1.70 %
5 MHz 1.70 %
10 MHz 1.70 %
20 MHz 3.20 %
49.99 MHz 3.20 %
50 MHz 3.20 %
Calibrator Output A50 kHz B C Tolerance ±(%)
50.1 mV Applied

<!-- llm_chunk_end id=service_chunk_0014 -->

<!-- llm_chunk_start id=service_chunk_0015 source=service_manual_5560a source_line_start=3361 source_line_end=3620 retrieval_priority=normal -->

## service_chunk_0015: 500 kHz 2.00 %

500 kHz 2.00 %
1 MHz 2.00 %
2 MHz 2.00 %
5 MHz 2.00 %
10 MHz 2.00 %
20 MHz 3.50 %
49.99 MHz 3.50 %
50 mV Applied
100 kHz 1.70 %
200 kHz 1.70 %
500 kHz 1.70 %
1 MHz 1.70 %
2 MHz 1.70 %
5 MHz 1.70 %
10 MHz 1.70 %
20 MHz 3.20 %
49.99 MHz 3.20 %
50 MHz 3.20 %
Calibrator Output A50 kHz B C Tolerance ±(%)
50.1 mV Applied
100 kHz 1.70 %
200 kHz 1.70 %
500 kHz 1.70 %
1 MHz 1.70 %
2 MHz 1.70 %
5 MHz 1.70 %
Table 44. Low Frequency Leveled Sine Flatness Relative to 50 kHz Calibration and Verification (cont.)
Oscilloscope Calibration Option (600M, 1G, and 2G) Calibration, Verification, and Adjustment
10 MHz 1.70 %
20 MHz 3.20 %
49.99 MHz 3.20 %
50 MHz 3.20 %
160 mV Applied
50 MHz 3.06 %
161 mV Applied
50 MHz 3.06 %
200 mV Applied
100 kHz 1.55 %
200 kHz 1.55 %
500 kHz 1.55 %
1 MHz 1.55 %
2 MHz 1.55 %
5 MHz 1.55 %
10 MHz 1.55 %
20 MHz 3.05 %
49.99 MHz 3.05 %
201 mV Applied
100 kHz 1.55 %
200 kHz 1.55 %
500 kHz 1.55 %
1 MHz 1.55 %
2 MHz 1.55 %
Calibrator Output A50 kHz B C Tolerance ±(%)
5 MHz 1.55 %
10 MHz 1.55 %
20 MHz 3.05 %
49.99 MHz 3.05 %
500 mV Applied
100 kHz 1.52 %
200 kHz 1.52 %
Table 44. Low Frequency Leveled Sine Flatness Relative to 50 kHz Calibration and Verification (cont.)
500 kHz 1.52 %
1 MHz 1.52 %
2 MHz 1.52 %
5 MHz 1.52 %
10 MHz 1.52 %
20 MHz 3.02 %
49.99 MHz 3.02 %
50 MHz 3.02 %
501 mV Applied
100 kHz 1.52 %
200 kHz 1.52 %
500 kHz 1.52 %
1 MHz 1.52 %
2 MHz 1.52 %
5 MHz 1.52 %
10 MHz 1.52 %
20 MHz 3.02 %
49.99 MHz 3.02 %
50 MHz 3.02 %
1.6 V Applied
50 MHz 3.01 %
1.61 V Applied
50 MHz 3.01 %
Calibrator Output A50 kHz B C Tolerance ±(%)
2 V Applied
100 kHz 1.51 %
200 kHz 1.51 %
500 kHz 1.51 %
1 MHz 1.51 %
2 MHz 1.51 %
5 MHz 1.51 %
10 MHz 1.51 %
Table 44. Low Frequency Leveled Sine Flatness Relative to 50 kHz Calibration and Verification (cont.)
Oscilloscope Calibration Option (600M, 1G, and 2G) Calibration, Verification, and Adjustment
High Frequency Leveled Sine Flatness Calibration and Verification
This procedure is an example of a high frequency flatness test with a 5 mV Calibrator output. Use the
same procedure for other amplitudes. Compare the results with the flatness specification shown in
Table 45.
To collect Reference values at 50 kHz and 50 MHz with 5790B Wideband:
1. Connect equipment as shown in Figure 37.
2. Set the Calibrator to output of 5 mV at 50 kHz.
3. Push J on the Product and allow the 5790B Wideband measurement become stable. The
5790B displays approximately 1.77 mV rms.
4. Record the 5790B Wideband measurement in column A of Table 45 for the test voltage.
5. Set the Calibrator to output of 5 mV at 50 MHz.
20 MHz 3.01 %
49.99 MHz 3.01 %
2.01 V Applied
100 kHz 1.50 %
200 kHz 1.50 %
500 kHz 1.50 %
1 MHz 1.50 %
2 MHz 1.50 %
5 MHz 1.50 %
10 MHz 1.50 %
20 MHz 3.00 %
49.99 MHz 3.00 %
5.5 V Applied
100 kHz 1.50 %
200 kHz 1.50 %
500 kHz 1.50 %
1 MHz 1.50 %
2 MHz 1.50 %
5 MHz 1.50 %
10 MHz 1.50 %
20 MHz 3.00 %
49.99 MHz 3.00 %
50 MHz 3.00 %
Table 44. Low Frequency Leveled Sine Flatness Relative to 50 kHz Calibration and Verification (cont.)
6. Push J on the Product. Allow the 5790B Wideband measurement stabilize. The 5790B
displays approximately 1.77 mV rms.
7. Record the 5790B Wideband measurement in column B of Table 45 for the test voltage.
8. Use the formula below to take the recorded values in columns A and B to calculate and record the
value in column C for all rows.
To collect reference values at 50 MHz with the Power Meter and Power Sensor:
1. Connect equipment as shown in Figure 44.
2. Set the Calibrator to output of 5 mV at 50 MHz.
3. Push J on the Product and allow the power meter measurement to become stable. The
power meter measurement is approximately 0.0000627 mW.
4. Record power meter measurement in column D of Table 45 for the test voltage (all rows.)
To collect values at test frequency:
1. Set the Calibrator to output of 5 mV at test frequency.
2. Push J on the Product and allow the power meter measurement to become stable.
3. Record power meter measurement in column E of Table 45 for the test voltage (all rows).
4. Repeat Table 45, steps 1 and 3 for all the frequencies shown in Table 45 for 5 mV applied.
Continue until you have completed column E.
5. After all columns A, B, C, D and E are filled for all rows of the table, push Eon the Calibrator.
6. Use the formula below to take the recorded values in columns C, D and E to calculate and record
the value in column F for all rows:
7. Compare column F to the specifications shown in the last column.
Column C = 100 * Column B - Column AColumn A
Column F = Column E - Column D2 + Column C
Oscilloscope Calibration Option (600M, 1G, and 2G) Calibration, Verification, and Adjustment
Table 45. High Frequency Leveled Sine Flatness Relative to 50 kHz Calibration and Verification
Output [1],[2]
From 5790B WB From Power Meter andPower Sensor
F Tolerance±(%)A
50 kHz
(V rms)
B
50 MHz
(V rms)
C
(%)
D
50 MHz
(%)
E
(%)
5 mV Applied
74.99 MHz 5.00 %
75 MHz 5.00 %
137.49 MHz 5.00 %
137.5 MHz 5.00 %
274.99 MHz 5.00 %
275 MHz 5.00 %
549.99 MHz 5.00 %
550 MHz 5.00 %
600 MHz 5.00 %
600.01 MHz 6.00 %
1 GHz 6.00 %
1.1 GHz 6.00 %
1.10001 GHz 7.00 %
1.49999 GHz 7.00 %
1.5 GHz 7.00 %
2.1 GHz 7.00 %
10 mV Applied
600.01 MHz 5.00 %
1 GHz 5.00 %
1.1 GHz 5.00 %
1.10001 GHz 6.00 %
1.49999 GHz 6.00 %
1.5 GHz 6.00 %
2.1 GHz 6.00 %
10.1 mV Applied
600.01 MHz 4.99 %
1 GHz 4.99 %
Output [1],[2]
From 5790B WB From Power Meter andPower Sensor
F Tolerance±(%)A
50 kHz
(V rms)
B
50 MHz
(V rms)
C
(%)
D
50 MHz
(%)
E
(%)
1.1 GHz 4.99 %
1.10001 GHz 5.99 %
1.49999 GHz 5.99 %
1.5 GHz 5.99 %
2.1 GHz 5.99 %
16 mV Applied
74.99 MHz 3.63 %
75 MHz 3.63 %
137.49 MHz 3.63 %
137.5 MHz 3.63 %
274.99 MHz 3.63 %
275 MHz 3.63 %
549.99 MHz 3.63 %
550 MHz 3.63 %
600 MHz 3.63 %
16.1 mV Applied
74.99 MHz 3.62 %
75 MHz 3.62 %
137.49 MHz 3.62 %
137.5 MHz 3.62 %
274.99 MHz 3.62 %
275 MHz 3.62 %
549.99 MHz 3.62 %
550 MHz 3.62 %
600 MHz 3.62 %
30 mV Applied
600.01 MHz 4.33 %
1 GHz 4.33 %
1.1 GHz 4.33 %
Table 45. High Frequency Leveled Sine Flatness Relative to 50 kHz Calibration and Verification (cont.)
Oscilloscope Calibration Option (600M, 1G, and 2G) Calibration, Verification, and Adjustment
Output [1],[2]
From 5790B WB From Power Meter andPower Sensor
F Tolerance±(%)A
50 kHz
(V rms)
B
50 MHz
(V rms)
C
(%)
D
50 MHz
(%)
E
(%)
1.10001 GHz 5.33 %

<!-- llm_chunk_end id=service_chunk_0015 -->

<!-- llm_chunk_start id=service_chunk_0016 source=service_manual_5560a source_line_start=3601 source_line_end=3860 retrieval_priority=normal -->

## service_chunk_0016: 1 GHz 4.33 %

1 GHz 4.33 %
1.1 GHz 4.33 %
Table 45. High Frequency Leveled Sine Flatness Relative to 50 kHz Calibration and Verification (cont.)
Oscilloscope Calibration Option (600M, 1G, and 2G) Calibration, Verification, and Adjustment
Output [1],[2]
From 5790B WB From Power Meter andPower Sensor
F Tolerance±(%)A
50 kHz
(V rms)
B
50 MHz
(V rms)
C
(%)
D
50 MHz
(%)
E
(%)
1.10001 GHz 5.33 %
1.49999 GHz 5.33 %
1.5 GHz 5.33 %
2.1 GHz 5.33 %
30.1 mV Applied
600.01 MHz 4.33 %
1 GHz 4.33 %
1.1 GHz 4.33 %
1.10001 GHz 5.33 %
1.49999 GHz 5.33 %
1.5 GHz 5.33 %
2.1 GHz 5.33 %
50 mV Applied
74.99 MHz 3.20 %
75 MHz 3.20 %
137.49 MHz 3.20 %
137.5 MHz 3.20 %
274.99 MHz 3.20 %
275 MHz 3.20 %
549.99 MHz 3.20 %
550 MHz 3.20 %
600 MHz 3.20 %
50.1 mV Applied
74.99 MHz 3.20 %
75 MHz 3.20 %
137.49 MHz 3.20 %
137.5 MHz 3.20 %
274.99 MHz 3.20 %
Table 45. High Frequency Leveled Sine Flatness Relative to 50 kHz Calibration and Verification (cont.)
Output [1],[2]
From 5790B WB From Power Meter andPower Sensor
F Tolerance±(%)A
50 kHz
(V rms)
B
50 MHz
(V rms)
C
(%)
D
50 MHz
(%)
E
(%)
275 MHz 3.20 %
549.99 MHz 3.20 %
550 MHz 3.20 %
600 MHz 3.20 %
100 mV Applied
600.01 MHz 4.10 %
1 GHz 4.10 %
1.1 GHz 4.10 %
1.10001 GHz 5.10 %
1.49999 GHz 5.10 %
1.5 GHz 5.10 %
2.1 GHz 5.10 %
101 mV Applied
600.01 MHz 4.10 %
1 GHz 4.10 %
1.1 GHz 4.10 %
1.10001 GHz 5.10 %
1.49999 GHz 5.10 %
1.5 GHz 5.10 %
2.1 GHz 5.10 %
160 mV Applied
74.99 MHz 3.06 %
75 MHz 3.06 %
137.49 MHz 3.06 %
137.5 MHz 3.06 %
274.99 MHz 3.06 %
275 MHz 3.06 %
Table 45. High Frequency Leveled Sine Flatness Relative to 50 kHz Calibration and Verification (cont.)
Oscilloscope Calibration Option (600M, 1G, and 2G) Calibration, Verification, and Adjustment
Output [1],[2]
From 5790B WB From Power Meter andPower Sensor
F Tolerance±(%)A
50 kHz
(V rms)
B
50 MHz
(V rms)
C
(%)
D
50 MHz
(%)
E
(%)
549.99 MHz 3.06 %
550 MHz 3.06 %
600 MHz 3.06 %
161 mV Applied
74.99 MHz 3.06 %
75 MHz 3.06 %
137.49 MHz 3.06 %
137.5 MHz 3.06 %
274.99 MHz 3.06 %
275 MHz 3.06 %
549.99 MHz 3.06 %
550 MHz 3.06 %
600 MHz 3.06 %
300 mV Applied
600.01 MHz 4.03 %
1 GHz 4.03 %
1.1 GHz 4.03 %
1.10001 GHz 5.03 %
1.49999 GHz 5.03 %
1.5 GHz 5.03 %
2.1 GHz 5.03 %
Table 45. High Frequency Leveled Sine Flatness Relative to 50 kHz Calibration and Verification (cont.)
301 mV Applied
600.01 MHz 4.03 %
1 GHz 4.03 %
1.1 GHz 4.03 %
1.10001 GHz 5.03 %
1.49999 GHz 5.03 %
1.5 GHz 5.03 %
2.1 GHz 5.03 %
Output [1],[2]
From 5790B WB From Power Meter andPower Sensor
F Tolerance±(%)A
50 kHz
(V rms)
B
50 MHz
(V rms)
C
(%)
D
50 MHz
(%)
E
(%)
500 mV Applied
74.99 MHz 3.02 %
75 MHz 3.02 %
137.49 MHz 3.02 %
137.5 MHz 3.02 %
274.99 MHz 3.02 %
275 MHz 3.02 %
549.99 MHz 3.02 %
550 MHz 3.02 %
600 MHz 3.02 %
501 mV Applied
74.99 MHz 3.02 %
75 MHz 3.02 %
137.49 MHz 3.02 %
137.5 MHz 3.02 %
274.99 MHz 3.02 %
275 MHz 3.02 %
549.99 MHz 3.02 %
550 MHz 3.02 %
600 MHz 3.02 %
Table 45. High Frequency Leveled Sine Flatness Relative to 50 kHz Calibration and Verification (cont.)
Oscilloscope Calibration Option (600M, 1G, and 2G) Calibration, Verification, and Adjustment
1 V Applied
600.01 MHz 4.01 %
1 GHz 4.01 %
1.1 GHz 4.01 %
1.10001 GHz 5.01 %
1.49999 GHz 5.01 %
1.5 GHz 5.01 %
2.1 GHz 5.01 %
Output [1],[2]
From 5790B WB From Power Meter andPower Sensor
F Tolerance±(%)A
50 kHz
(V rms)
B
50 MHz
(V rms)
C
(%)
D
50 MHz
(%)
E
(%)
1.01 V Applied
600.01 MHz 4.01 %
1 GHz 4.01 %
1.1 GHz 4.01 %
1.10001 GHz 5.01 %
1.49999 GHz 5.01 %
1.5 GHz 5.01 %
2.1 GHz 5.01 %
1.6 V Applied
74.99 MHz 3.01 %
75 MHz 3.01 %
137.49 MHz 3.01 %
137.5 MHz 3.01 %
274.99 MHz 3.01 %
275 MHz 3.01 %
549.99 MHz 3.01 %
550 MHz 3.01 %
600 MHz 3.01 %
1.61 V Applied
74.99 MHz 3.01 %
75 MHz 3.01 %
Table 45. High Frequency Leveled Sine Flatness Relative to 50 kHz Calibration and Verification (cont.)
137.49 MHz 3.01 %
137.5 MHz 3.01 %
274.99 MHz 3.01 %
275 MHz 3.01 %
549.99 MHz 3.01 %
550 MHz 3.01 %
600 MHz 3.01 %
Output [1],[2]
From 5790B WB From Power Meter andPower Sensor
F Tolerance±(%)A
50 kHz
(V rms)
B
50 MHz
(V rms)
C
(%)
D
50 MHz
(%)
E
(%)
3.5 V Applied
600.01 MHz 4.00 %
1 GHz 4.00 %
1.1 GHz 4.00 %
1.10001 GHz 5.00 %
1.49999 GHz 5.00 %
1.5 GHz 5.00 %
2.1 GHz 5.00 %
5.5 V Applied
74.99 MHz 3.00 %
75 MHz 3.00 %
137.49 MHz 3.00 %
137.5 MHz 3.00 %
274.99 MHz 3.00 %
275 MHz 3.00 %
549.99 MHz 3.00 %
550 MHz 3.00 %
600 MHz 3.00 %
[1] 600 MHz - 1.1 GHz verification points only applicable for the 1G and 2G options.

<!-- llm_chunk_end id=service_chunk_0016 -->

<!-- llm_chunk_start id=service_chunk_0017 source=service_manual_5560a source_line_start=3841 source_line_end=4100 retrieval_priority=normal -->

## service_chunk_0017: (%)

(%)
3.5 V Applied
600.01 MHz 4.00 %
1 GHz 4.00 %
1.1 GHz 4.00 %
1.10001 GHz 5.00 %
1.49999 GHz 5.00 %
1.5 GHz 5.00 %
2.1 GHz 5.00 %
5.5 V Applied
74.99 MHz 3.00 %
75 MHz 3.00 %
137.49 MHz 3.00 %
137.5 MHz 3.00 %
274.99 MHz 3.00 %
275 MHz 3.00 %
549.99 MHz 3.00 %
550 MHz 3.00 %
600 MHz 3.00 %
[1] 600 MHz - 1.1 GHz verification points only applicable for the 1G and 2G options.
[2] 1.10001 GHz - 2.1 GHz verification points only applicable for the 2G option.
Table 45. High Frequency Leveled Sine Flatness Relative to 50 kHz Calibration and Verification (cont.)
Oscilloscope Calibration Option (600M, 1G, and 2G) Calibration, Verification, and Adjustment
Leveled Sine Reflection Coefficient Calibration and Verification
This procedure uses:
• Fluke 5560A Multi-Product Calibrator (scope option required)
• Tektronix AFG1022 Arbitrary Function Generator
• Keysight 86205A Directional Bridge
• Keysight N1913B Power meter
• Keysight E9304A Power sensor
• BNC(f) to Type N(m) adapter
• Type N(m) to Type N(m) adapter
• Shorting cap for BNC(f)
• Output Scope Card cable supplied with the scope option
Initial setup:
Set the Calibrator (DUT) to Scope, Leveled Sine (Function Menu > Scope > Leveled Sine). Ensure
both have REFCLOCK Set to External.
Tektronix AFG1022 set up:
Connect the 10 MHz IN located in the back of the DUT and the 5560A standard to Out1 and Out2 of
the Tektronix AFG1022, see Figure 39.
Figure 39. Tektronix AFG1022 Initial Connections
Tektronix AFG1022 Out1 and Out2 settings:
• Waveform: Square
• Frequ: 10 MHz
• Voltage Offset: 2.5
• Voltage amplitude: 5.0
Arbitrary Function Generator
DUT 5560A/2G STD
Collect OPEN and SHORT Values
See Figure 40 for connections:
1. Connect the SCOPE connector of the Product to the Directional Bridge with the Type N(m) to Type
N(m) adapter.
2. Connect the Power Meter and Power Sensor to the Directional Bridge.
3. Connect Type N(m) to BNC(f) to the third port of Directional Bridge.
Figure 40. Leveled Sine Reflection Coefficient - OPEN Connections
Power Meter settings:
• Frequency: 5 MHz
• SENSE1:FREQ 5MHz
• SENSE1:AVERAGE 0
• SENSE1:AVERAGE:COUNT:AUTO 0
• SENSE1:AVERAGE:SDETECT 0
• SENSE1:MRATE FAST
• UNIT:POWER DBM
• INIT:CONT ON
4. Set the Calibrator SCOPE standard output to the voltage shown in column A in Table 46.
5. Set the Power Meter range to the range shown in column B in Table 46.
6. Push Jon the Calibrator standard. Let the power meter measurement become stable.
7. Record the Power meter measurement (converted to Vpp) into column C of Table 46.
8. With the same connections used in Figure 40, add a shorting cap to the connect Type N(m) to
BNC(f) connected to the third port of the Directional Bridge. See Figure 41. Let the power meter
measurement become stable.
9. Repeat step 4 through 6 above. Let the power meter measurement become stable.
Type N (M) to BNC (F)
Leave
this
open
Type N (M) to Type N (M)
Direct Connection
5560A
STD
Power
Meter
STD
Power Sensor Cable
Directional
Bridge
Oscilloscope Calibration Option (600M, 1G, and 2G) Calibration, Verification, and Adjustment
Figure 41. Leveled Sine Reflection Coefficient - SHORT Connections
10. Record the Power meter measurement into column D of Table 46.
11. After all columns C and D are filled, push L on the Calibrator Standard.
12. Repeat these steps until columns C and D are complete.
13. Use the formula below and take the recorded values in column C and D to calculate and record
Z_Max in column E of Table 46.
Leveled Sine Reflection Coefficient Calibration and Verification Process
1. Remove the shorting cap to the connect Type N(m) to BNC(f) connected to the third port of
Directional Bridge.
2. Use the scope card cable to connect to the scope connector of the Calibrator, see Figure 42.
Figure 42. Leveled Sine Reflection Coefficient Calibration and Verification Connections
3. Set the Out1 of Arbitrary Function Generator to SOURCE1:FREQ to the value shown in column F
of Table 46. Use this formula to calculate the value for a test point:
Shorting Cap
for BNC (F)
Directional
Bridge
Column E = Column C + Column D2
4. Set the Calibrator SCOPE standard output to the voltage shown in column A in Table 46.
5. Set the Power Meter range to the range shown in column B in Table 46.
6. Set the Calibrator SCOPE output to the voltage shown in Calibrator Output in Table 46.
7. Push J on the Calibrator Standard.
8. Push J on the Calibrator. Let the power meter measurement become stable.
9. Export the Power meter measurement data to the external device and apply 15 reading moving
average filter.
Record V_Max (Vpp) of filtered data into column G of Table 46.
Record V_Min (Vpp) of filtered data into column H of Table 46.
10. After columns G and H are filled for a row of the table, push L on the Calibrator standard and
the Calibrator.
11. Use the recorded values in columns G and H to calculate and record the value in column I with this
formula:
12. Use the recorded values in columns E and I to calculate and record the value in column J with this
formula:
13. Compare column J to the specifications shown in the last column.
14. Repeat step all steps for all test points listed in Table 46.
Table 46. Leveled Sine Reflection Coefficient Calibration and Verification
Output
A B C D E F G H I
J Tolerance±5560A Std
Ampl (V)
Power
Meter
Range
(Open) (Short) Z_Max AFG1022Out1 Freq (Hz) V_Max V_Min Z_DUT
2.01 V
5 MHz
3.015 V
5 MHz RANGE 1 10000002.0000 0.048
2.01 V
10 MHz
3.015 V
10 MHz RANGE 1 10000001.0000 0.048
2.01 V
20 MHz
3.015 V
20 MHz RANGE 1 10000000.5000 0.091
2.01 V
49.99
MHz
3.015 V
49.99
MHz
RANGE 1 10000000.2000 0.091
Freq = 10E6 + 10E6 * = 1Test Frequency
Column I = Column G - Column H2
Column J = Column IColumn E
Oscilloscope Calibration Option (600M, 1G, and 2G) Calibration, Verification, and Adjustment
Output
A B C D E F G H I
J Tolerance±5560A Std
Ampl (V)
Power
Meter
Range
(Open) (Short) Z_Max AFG1022Out1 Freq (Hz) V_Max V_Min Z_DUT
1.61 V 50
MHz
2.415 V
50 MHz RANGE 1 10000000.2000 0.091
1.61 V
74.99
MHz
2.415 V
74.99
MHz
RANGE 1 10000000.1334 0.091
1.61 V
75 MHz
2.415 V
75 MHz RANGE 1 10000000.1333 0.091
1.61 V
137.49
MHz
2.415 V
137.49
MHz
RANGE 1 10000000.0727 0.091
1.61 V
137.5
MHz
2.415 V
137.5
MHz
RANGE 1 10000000.0727 0.091
1.61 V
274.99
MHz
2.415 V
274.99
MHz
RANGE 1 10000000.0364 0.091
1.61 V
275 MHz
2.415 V
275 MHz RANGE 1 10000000.0364 0.091
1.61 V
549.99
MHz
2.415 V
549.99
MHz
RANGE 1 10000000.0182 0.091
1.61 V
550 MHz
2.415 V
550 MHz RANGE 1 10000000.0182 0.091
1.61 V
600 MHz
2.415 V
600 MHz RANGE 1 10000000.0167 0.107
1.01 V
600.01
MHz
1.515 V
600.01
MHz
RANGE 1 10000000.0167 0.111
1.01 V 1
GHz
1.515V 1
GHz RANGE 1 10000000.0100 0.111
1.01 V 1.1
GHz
1.515 V
1.1 GHz RANGE 1 10000000.0091 0.111
1.01 V
1.10001
GHz
1.515 V
1.10001
GHz
RANGE 1 10000000.0091 0.149
Table 46. Leveled Sine Reflection Coefficient Calibration and Verification (cont.)
Output
A B C D E F G H I
J Tolerance±5560A Std
Ampl (V)
Power
Meter
Range
(Open) (Short) Z_Max AFG1022Out1 Freq (Hz) V_Max V_Min Z_DUT
1.01 V
1.49999
GHz
1.51 5V
1.49999
GHz
RANGE 1 10000000.0067 0.149
1.01 V 1.5
GHz
1.515V
1.5 GHz RANGE 1 10000000.0067 0.149
1.01 V 2

<!-- llm_chunk_end id=service_chunk_0017 -->

<!-- llm_chunk_start id=service_chunk_0018 source=service_manual_5560a source_line_start=4081 source_line_end=4340 retrieval_priority=normal -->

## service_chunk_0018: Output

Output
A B C D E F G H I
J Tolerance±5560A Std
Ampl (V)
Power
Meter
Range
(Open) (Short) Z_Max AFG1022Out1 Freq (Hz) V_Max V_Min Z_DUT
1.01 V
1.49999
GHz
1.51 5V
1.49999
GHz
RANGE 1 10000000.0067 0.149
1.01 V 1.5
GHz
1.515V
1.5 GHz RANGE 1 10000000.0067 0.149
1.01 V 2
GHz
1.515 V
2 GHz RANGE 1 10000000.0050 0.149
1.01 V 2.1
GHz
1.515 V
2.1 GHz RANGE 1 10000000.0048 0.167
5 V
5 MHz
0.833V
5 MHz RANGE 1 10000002.0000 0.048
5 V
10 MHz
0.833 V
10 MHz RANGE 1 10000001.0000 0.048
5 V 20
MHz
0.833 V
20 MHz RANGE 1 10000000.5000 0.091
5 V
49.99
MHz
0.833 V
49.99
MHz
RANGE 1 10000000.2000 0.091
5 V
50 MHz
0.833 V
50 MHz RANGE 1 10000000.2000 0.091
5 V
74.99
MHz
0.833 V
74.99
MHz
RANGE 1 10000000.1334 0.091
5 V 75
MHz
0.833 V
75 MHz RANGE 1 10000000.1333 0.091
5 V
137.49
MHz
0.833 V
137.49
MHz
RANGE 1 10000000.0727 0.091
5 V
137.5
MHz
0.833 V
137.5
MHz
RANGE 1 10000000.0727 0.091
5 V
274.99
MHz
0.833 V
274.99
MHz
RANGE 1 10000000.0364 0.091
5 V 275
MHz
0.833 V
275 MHz RANGE 1 10000000.0364 0.091
5 V
549.99
MHz
0.833 V
549.99
MHz
RANGE 1 10000000.0182 0.091
5 V
550 MHz
0.833 V
550 MHz RANGE 1 10000000.0182 0.091
5 V
600 MHz
0.833 V
600 MHz RANGE 1 10000000.0167 0.107
3.5 V
600.01
MHz
0.583 V
600.01
MHz
RANGE 1 10000000.0167 0.111
Table 46. Leveled Sine Reflection Coefficient Calibration and Verification (cont.)
Oscilloscope Calibration Option (600M, 1G, and 2G) Calibration, Verification, and Adjustment
Edge Rise Time Calibration and Verification
This verification tests the rise time of the Edge function (Function Menu > Scope > Edge).
This procedure uses
• Tektronix MSO64B Oscilloscope
• Output Scope Card cable supplied with the scope option
Edge Rise Time Calibration and Verification Process
1. Connect the output cable to the SCOPE connector on the Calibrator.
2. Connect the other end of the output cable to channel 1 of the oscilloscope. See Figure 43.
Figure 43. Time Base Measurement Connection
Output
A B C D E F G H I
J Tolerance±5560A Std
Ampl (V)
Power
Meter
Range
(Open) (Short) Z_Max AFG1022Out1 Freq (Hz) V_Max V_Min Z_DUT
3.5 V
1 GHz
0.583 V
1 GHz RANGE 1 10000000.0100 0.111
3.5 V
1.1 GHz
0.583 V
1.1 GHz RANGE 1 10000000.0091 0.111
3.5 V
1.10001
GHz
0.583 V
1.10001
GHz
RANGE 1 10000000.0091 0.149
3.5 V
1.49999
GHz
0.583 V
1.49999
GHz
RANGE 1 10000000.0067 0.149
3.5 V
1.5 GHz
0.583 V
1.5 GHz RANGE 1 10000000.0067 0.149
3.5 V
2 GHz
0.583V
2 GHz RANGE 1 10000000.0050 0.149
3.5 V
2.1 GHz
0.583 V
2.1 GHz RANGE 1 10000000.0048 0.167
Table 46. Leveled Sine Reflection Coefficient Calibration and Verification (cont.)
Channel 1
3. Push the DEFAULT SETUP button to reset to default and then set the oscilloscope to:
• Acquire mode: Average
• Number of averages: 500
• Measure: Risetime
• Horizontal scale: 500 ps/div
• Set the Calibrator output to test points list in Table 47.
4. Push J on the Product.
5. Change the scale of the oscilloscope to see full wave.
6. Adjust the main time base position and vertical offset until the edge signal is in the center of the
oscilloscope display. Record the rise time measurement for the test point in Table 47. The
measured edge rise time must be less than the time shown in last column of Table 47.
Table 47. Edge Rise Time Calibration and Verification
Calibrator Output Tektronix MSO64BMeasurement Tolerance (ps)
5 mV 100 kHz ≤175
10 mV 100 kHz ≤175
25 mV 100 kHz ≤175
50 mV 100 kHz ≤175
60 mV 100 kHz ≤175
80 mV 100 kHz ≤175
100 mV 100 kHz ≤175
200 mV 100 kHz ≤175
250 mV 100 kHz ≤175
300 mV 100 kHz ≤175
500 mV 100 kHz ≤175
600 mV 100 kHz ≤175
1 V 100 kHz ≤175
2.5 V 100 kHz ≤175
Oscilloscope Calibration Option (600M, 1G, and 2G) Calibration, Verification, and Adjustment
Pulse Width Calibration and Verification
This procedure uses
• Tektronix MSO64B Oscilloscope
• Output Scope Card cable supplied with the scope option
Initial setup:
Set the Calibrator to Function > Scope > Pulse.
Pulse Width Calibration and Verification Process
1. Connect the output cable to the SCOPE connector on the Calibrator.
2. Connect the other end of the output cable to channel 1 of the oscilloscope, see Figure 43.
3. Push the DEFAULT SETUP button to reset to default and then set the oscilloscope to:
• Acquire mode: Average
• Number of averages: 128
• Measure: Pulse Width
• Horizontal scale: 250 ns/div
4. Set the Calibrator output to period shown in Table 48.
5. Set the voltage to 2.5 V.
6. Push J on the Product. Let the oscilloscope measurement become stable.
7. Change the oscilloscope to see full wave.
8. Adjust the main time base position and vertical offset until the pulse signal is in the center of the
oscilloscope display.
9. Record the width measurement for the test point in Table 48.
10. Compare the width measurement to the value in the Tolerance ±(ns) column of Table 48.
Time Marker Period Calibration and Verification
This procedure uses:
• Tektronix MSO64B Oscilloscope
• Output Scope Card cable supplied with the scope option
Initial setup:
Set the Calibrator to (Function Menu > Scope > Edge).
Table 48. Pulse Width Calibration and Verification
Calibrator Output Tektronix MSO64BMeasurement Tolerance ±(ns)
250 ns 2.00
Time Marker Period Calibration and Verification Process
1. Connect the output cable to the SCOPE connector on the Calibrator. Connect the other end of the
output cable to Channel 1 of the oscilloscope. See Figure 43.
2. Push the DEFAULT SETUP button to reset to default and then set the oscilloscope to:
• Acquire mode: Average
• Number of averages: 128
• Measure: Risetime
• Horizontal scale: 250 ns/div
• Set the Calibrator output to test points list in Table 49.
3. Push J on the Product.
4. Change the scale of the oscilloscope to see full wave.
5. Adjust the main time base position and vertical offset until the pulse signal is in the center of the
oscilloscope display.
6. Record the width measurement for the test point in Table 49.
7. Compare the width measurement to the value in the Tolerance ±(s) column of the Table 49.
Measure Resistance Calibration and Verification
This procedure uses
• Fluke 5560A Multi-Product Calibrator
• BNC(f) to Double Banana adapter
• Output Scope Card cable supplied with the scope option
Initial setup:
Set the Calibrator to Function > Scope > Resistance.
Table 49. Time Marker Period Calibration and Verification
Calibrator Output Tektronix MSO64BMeasurement Tolerance ±(s)
20 ns 5.00E-14
2 s 5.00E-06
Oscilloscope Calibration Option (600M, 1G, and 2G) Calibration, Verification, and Adjustment
Measure Resistance Calibration and Verification Process
1. Connect the SCOPE connector of the Calibrator to the 5560A, see Figure 45.
2. Set the 5560A to:
• Function: Single Output > Resistance
• Guard: INTERNAL
• Comp: OFF
3. Set the 5560A to the resistance value shown in Table 50 and Push J. Let the Calibrator
measurement become stable.
4. Record the measurement for each test point in Table 50.
5. Compare the result to the Tolerance ±(Ω) column.
Measure Capacitance Calibration and Verification

<!-- llm_chunk_end id=service_chunk_0018 -->

<!-- llm_chunk_start id=service_chunk_0019 source=service_manual_5560a source_line_start=4321 source_line_end=4580 retrieval_priority=normal -->

## service_chunk_0019: • BNC(f) to Double Banana adapter

• BNC(f) to Double Banana adapter
• Output Scope Card cable supplied with the scope option
Initial setup:
Set the Calibrator to Function > Scope > Resistance.
Table 49. Time Marker Period Calibration and Verification
Calibrator Output Tektronix MSO64BMeasurement Tolerance ±(s)
20 ns 5.00E-14
2 s 5.00E-06
Oscilloscope Calibration Option (600M, 1G, and 2G) Calibration, Verification, and Adjustment
Measure Resistance Calibration and Verification Process
1. Connect the SCOPE connector of the Calibrator to the 5560A, see Figure 45.
2. Set the 5560A to:
• Function: Single Output > Resistance
• Guard: INTERNAL
• Comp: OFF
3. Set the 5560A to the resistance value shown in Table 50 and Push J. Let the Calibrator
measurement become stable.
4. Record the measurement for each test point in Table 50.
5. Compare the result to the Tolerance ±(Ω) column.
Measure Capacitance Calibration and Verification
The verification procedure for the Measure Capacitance mode is a capacitance measurement of a
known capacitance value and then comparing the capacitance measurement to the value of the
capacitance.
This procedure uses:
• Adapter and capacitors to make 5 pF, 29 pF and 49 pF nominal values at the end of a BNC(f)
connector.
• Output Scope Card cable supplied with the scope option.
Initial setup:
Set the Calibrator to Function > Scope > Capacitance.
Measure Capacitance Calibration and Verification Process
1. Connect one end of the output cable to the SCOPE connector of the Calibrator. Do not connect
anything to the other end of this cable.
2. Let the Calibrator measurement become stable and then tap the Offset ZERO button on the
display to zero the capacitance measurement.
3. Connect the other end of the cable to the capacitance shown in Table 51. Let the Calibrator
measurement become stable.
4. Record the measurement for each test point in Table 51.
Table 50. Measure Resistance Calibration and Verification
Fluke 5560A Output Calibrator Measurement Tolerance ±(Ω)
40 Ω 0.040
50 Ω 0.050
60 Ω 0.060
0.6 MΩ 600
1 MΩ 1000
1.5 MΩ 1500
5. Compare the measured capacitance value to the actual capacitance and the value in the
Tolerance ±(pF) column of the Table 51.
Scope Option Adjustment Setup
The Calibrator Mainframe must be fully calibrated before you do the scope option calibration
adjustment.
You must adjust the calibration of the DCV function first. The ACV function depends on the DCV
function.
The Product must complete a warm-up period (a minimum of two times the period the Product was
turned off, or a maximum of 30 minutes), and the scope option must be on for a minimum of 5 minutes
before you begin calibration adjustment. This lets internal components become thermally stable.
Scope option calibration is adjusted from the front panel.
Note
Access to the Adjustment mode requires a passcode. The default passcode is set to the serial
number of the DUT. Enter the serial number and push E. For more passcode
information, see the Operators Manual available at www.fluke.com.
To start Scope Option Adjustment mode, use Setup > Scope Adjustment to open the scope
adjustment menu.
• All equipment used for calibration adjustment must be calibrated, certified traceable (if traceability is
kept), and operated in their specified operation environment.
• For best accuracy, make sure the equipment has sufficient time to warm up before you start
adjustment. Refer to the operation manual for each piece of equipment.
• Before you start these procedures, read the complete procedures to make sure you have the
resources to do them.
• The Product starts calibration with the dc voltage (DCV) mode. Select Continue and follow
instructions on the display.
Scope Option Adjustment
The Voltage, Edge, and Wave Generator modes have square wave voltages that must be calibrated or
verified. Program the 8588A Reference Multimeter from the front panel or through the remote interface
to make these measurements.
Table 51. Measure Capacitance Calibration and Verification
Nominal Capacitance
Value
Measurement
Actual Capacitance
Value Tolerance ±(pF)
5 pF 0.75
29 pF 1.95
49 pF 2.95
Oscilloscope Calibration Option (600M, 1G, and 2G) Calibration, Verification, and Adjustment
Before Scope Option Adjustment
To obtain reference levels for leveled sine at 50 kHz and 50 MHz to use them further in the procedure:
1. Connect the Output N-type terminal to a 5790B Wideband configured to measure ac voltage. See
Figure 37.
5790B settings:
• External trigger OFF
• HIRES ON
• Range: As shown in the 5790B Wideband Range Setup column of Table 52.
2. Set the Calibrator output to voltages shown in the Calibrator Output (V) column of Table 52 at
50 kHz.
3. Push J on the Calibrator. Let the 5790B measurement become stable.
4. Record the 5790B measurement into column A of Table 52.
5. Push L on the Calibrator.
6. Set the Calibrator output to voltage shown in the Calibrator Output column of Table 52 at 50 MHz.
7. Push J on the Calibrator. Let the 5790B measurement become stable.
8. Record the 5790B measurement for each voltage into column B of Table 52.
9. Push L on the Calibrator.
10. Repeat Table 52, steps 2 to 10 and fill each row of the table.
For column C in Table 52:
1. Connect the Keysight N1913B Power Meter to the Keysight E9304A Power Sensor, see Figure 44.
Refer to their operator manuals for connections.
2. Zero and self-calibrate the power meter with the power sensor. Refer to the Keysight N1913B
operator manual.
3. Power Meter settings:
a. Turn off relative for channel 1.
b. Set channel 1 to measure power, display dBm, auto range, and average 256.
4. For each row of Table 52, connect the Output N-type terminal to a Precision Power Meter
configured to measure ac voltage and tap Continue on the display. See Figure 44.
5. Set the Calibrator output to voltages shown in the Calibrator Output (V) column of Table 37 at
50 MHz.
6. Push J on the Calibrator. Let the 5790B measurement become stable.
7. Convert the reading from dBm to V RMS and record into column C of Table 52.
8. Push L on the Calibrator.
9. Repeat Table 52, steps 5 through 7 and fill each row of the table.
Figure 44. The Keysight N1913B Power Meter and Keysight E9304A Power Sensor
Connections
Table 52. Adjustment Points for Leveled Sine Wave - Before
Calibrator Output
(V)
5790B Wideband
Range Setup
A
at 50 kHz
B
at 50 MHz
N1913B Setup C
at 50 MHzRange Count
0.005 2.2 mV LP 32
0.01 2.2 mV LP 32
0.0101 2.2 mV LP 16
0.016 2.2 mV LP 16
0.01601 2.2 mV LP 8
0.02 22 mV LP 4
0.0201 22 mV LP 4
0.03 22 mV LP 4
0.0301 22 mV LP 4
0.05 22 mV LP 4
0.0501 22 mV LP 4
0.1 70 mV LP 4
0.101 70 mV LP 4
0.16 70 mV LP 4
0.1601 70 mV LP 4
0.2 220 mV LP 4
0.201 220 mV HP 32
0.3 220 mV HP 32
0.301 220 mV HP 32
0.5 220 mV HP 32
0.501 220 mV HP 16
1 700 mV HP 8
Direct Connection
N1913B Power Meter E9034A Power Sensor
Oscilloscope Calibration Option (600M, 1G, and 2G) Calibration, Verification, and Adjustment
DC Voltage Adjustment
This procedure uses:
• Fluke 8588A Reference Multimeter
• BNC(f) to Double Banana adapter
• BNC(m-f) Feed-Thru Termination 50 Ω
• Output Scope Card cable supplied with the scope option
The Product prompts for 1 MOhm and 10 Ohm input impedances. See Figure 35 and Figure 36 for
equipment connections.
DCV highlights with the Calibrator in Scope Adjustment mode.
To adjust dc voltage:
1. Make the connections shown in Figure 35.
8588A settings:
• Function: DC Voltage
• Input > Terminal > Front
• Measure Setup > Manual > Edit PLC: 60.00 PLC
• Z in > 1 MΩ
2. Tap Continue on the display.
3. Push J on the Calibrator. Let the 8588A voltage measurement become stable. Type in the
measurement with the Calibrator keypad and push E.
Note
The Calibrator shows a message if the typed value is higher or lower than the limits of the
value. If this occurs, examine the connections and carefully re-type the measurement with the
correct unit (for example, mV, V). Repair may be necessary if the warning continues.
4. Repeat step 3 until the Calibrator shows the next connection with 50 Ω input impedance and tap
Continue on the display.
Calibrator Output
(V)
5790B Wideband
Range Setup
A
at 50 kHz
B
at 50 MHz
N1913B Setup C
at 50 MHzRange Count
1.01 700 mV HP 4
1.6 700 mV HP 4
1.601 700 mV HP 4
2 2.2 V HP 4
2.01 2.2 V HP 4
3.5 2.2 V HP 4
5.5 2.2 V HP 4
Table 52. Adjustment Points for Leveled Sine Wave - Before (cont.)
5. Connect the SCOPE connector of the Calibrator to the 8588A input HI and LO as shown in
Figure 36.
6. Repeat step 3 until the Calibrator display prompts to adjust ac voltage.
AC Voltage Adjustment
For equipment and setup, see DC Voltage Adjustment.
To adjust ac voltage:
When the Calibrator is in Scope Adjustment mode and ACV is highlighted:
1. Make the connections shown in Figure 35.
8588A settings:
• Function: Digitize
• Input > Terminal > Front
• Coupling, Zin: DC, 1 MΩ
• Measure Setup > Low pass filter: 3 MHz
• Measure Setup > Range: base on ac voltage adjust point
• Measure Setup > Aperture: <Aperture value> which is shown in the 8588A Aperture Setup
column of Table 53. This aperture value was calculated based on adjust frequency with this
formula:
Sample Rate = 100 * Adjust Frequency
(If Sample Rate > 5000000.0, use 5000000.0)
Aperture = (1 / Sample Rate) - 0.0000002
• Trigger Setup > Triggers/Arm (Count): 10000
2. Tap Continue on the display.
3. Push J.
4. On the 8588A, push the TRIG softkey to collect data from the waveform. Export the digitized data
to the external device. Reference the 8588A Operators Manual Digitize Menu function for
information to extract the data.
5. Process the data.
Separate the data into two groups:
• Top level: MEDIAN of all readings >90% of reference level
• Base level: MEDIAN of all readings <10 % of reference level
The processed value is calculated as:
median of Top line – median of Base line.
6. Type in the processed value from step 5 with the Calibrator keypad and push E.
Note
The Calibrator shows a message if the typed value is higher or lower than the limits of the
value. If this occurs, examine the setup and carefully re-type in the measurement with the
correct unit (for example, mV, V). Repair may be necessary if the warning continues.
Oscilloscope Calibration Option (600M, 1G, and 2G) Calibration, Verification, and Adjustment
7. Repeat step 3 though 6 until the Calibrator shows the next connection with 50 Ω input impedance.
8. Connect the SCOPE connector of the Calibrator to the 8588A input HI and LO as shown in
Figure 36.
8588A settings:
Measure Setup > Aperture: <Aperture value> which is shown in the 8588A Aperture Setup column
of Table 54. This aperture value was calculated based on adjust frequency with this formula:
Sample Rate = 100 * Adjust Frequency (If Sample Rate > 5000000.0, use 5000000.0) Aperture =
(1 / Sample Rate) - 0.0000002 • Trigger Setup > Triggers/Arm (Count): 10000
9. Tap Continue on the display.
10. Repeat Table 54, steps 3 to 6 until the Calibrator prompts to adjust Edge.
Table 53. Sequential Adjustment Points and 8588A Aperture Setup for AC Voltage - 1 M Ohm
Calibrator Output
(V)
ADJ Freq
(Hz) 8588A Aperture Setup 8588A Trigger Setup
-0.001 40 0.0002498 s 10000
-0.002 40 0.0002498 s 10000
0.001 40 0.0002498 s 10000
0.002 40 0.0002498 s 10000
-0.002001 40 0.0002498 s 10000
-0.005 40 0.0002498 s 10000
0.002001 40 0.0002498 s 10000
0.005 40 0.0002498 s 10000

<!-- llm_chunk_end id=service_chunk_0019 -->

<!-- llm_chunk_start id=service_chunk_0020 source=service_manual_5560a source_line_start=4561 source_line_end=4820 retrieval_priority=normal -->

## service_chunk_0020: 8588A settings:

8588A settings:
Measure Setup > Aperture: <Aperture value> which is shown in the 8588A Aperture Setup column
of Table 54. This aperture value was calculated based on adjust frequency with this formula:
Sample Rate = 100 * Adjust Frequency (If Sample Rate > 5000000.0, use 5000000.0) Aperture =
(1 / Sample Rate) - 0.0000002 • Trigger Setup > Triggers/Arm (Count): 10000
9. Tap Continue on the display.
10. Repeat Table 54, steps 3 to 6 until the Calibrator prompts to adjust Edge.
Table 53. Sequential Adjustment Points and 8588A Aperture Setup for AC Voltage - 1 M Ohm
Calibrator Output
(V)
ADJ Freq
(Hz) 8588A Aperture Setup 8588A Trigger Setup
-0.001 40 0.0002498 s 10000
-0.002 40 0.0002498 s 10000
0.001 40 0.0002498 s 10000
0.002 40 0.0002498 s 10000
-0.002001 40 0.0002498 s 10000
-0.005 40 0.0002498 s 10000
0.002001 40 0.0002498 s 10000
0.005 40 0.0002498 s 10000
-0.005001 40 0.0002498 s 10000
-0.02 40 0.0002498 s 10000
0.005001 40 0.0002498 s 10000
0.02 40 0.0002498 s 10000
-0.020001 40 0.0002498 s 10000
-0.05 40 0.0002498 s 10000
0.020001 40 0.0002498 s 10000
0.05 40 0.0002498 s 10000
-0.05001 40 0.0002498 s 10000
-0.2 40 0.0002498 s 10000
0.05001 40 0.0002498 s 10000
0.2 40 0.0002498 s 10000
-0.20001 40 0.0002498 s 10000
Calibrator Output
(V)
ADJ Freq
(Hz) 8588A Aperture Setup 8588A Trigger Setup
-0.5 40 0.0002498 s 10000
0.20001 40 0.0002498 s 10000
0.5 40 0.0002498 s 10000
-0.5001 40 0.0002498 s 10000
-2 40 0.0002498 s 10000
0.5001 40 0.0002498 s 10000
2 40 0.0002498 s 10000
-2.0001 40 0.0002498 s 10000
-6.6 40 0.0002498 s 10000
2.0001 40 0.0002498 s 10000
6.6 40 0.0002498 s 10000
-6.601 40 0.0002498 s 10000
-15 40 0.0002498 s 10000
6.601 40 0.0002498 s 10000
15 40 0.0002498 s 10000
-15.01 40 0.0002498 s 10000
-120 40 0.0002498 s 10000
15.01 40 0.0002498 s 10000
120 40 0.0002498 s 10000
6.6 500 0.0000198 s 10000
6.6 5000 0.0000018 s 10000
6.6 10000 0.0000008 s 10000
15 500 0.0000198 s 10000
15 5000 0.0000018 s 10000
15 10000 0.0000008 s 10000
120 500 0.0000198 s 10000
120 5000 0.0000018 s 10000
120 10000 0.0000008 s 10000
Table 53. Sequential Adjustment Points and 8588A Aperture Setup for AC Voltage - 1 M Ohm
Oscilloscope Calibration Option (600M, 1G, and 2G) Calibration, Verification, and Adjustment
Table 54. Sequential Adjustment Points and 8588A Aperture setup for AC Voltage - into 50 Ohm
Calibrator Output
(V)
ADJ Freq
(Hz) 8588A Aperture Setup 8588A Trigger Setup
-0.001 40 0.0002498 s 10000
-0.002 40 0.0002498 s 10000
0.001 40 0.0002498 s 10000
0.002 40 0.0002498 s 10000
-0.002001 40 0.0002498 s 10000
-0.005 40 0.0002498 s 10000
0.002001 40 0.0002498 s 10000
0.005 40 0.0002498 s 10000
-0.005001 40 0.0002498 s 10000
-0.02 40 0.0002498 s 10000
0.005001 40 0.0002498 s 10000
0.02 40 0.0002498 s 10000
-0.020001 40 0.0002498 s 10000
-0.05 40 0.0002498 s 10000
0.020001 40 0.0002498 s 10000
0.05 40 0.0002498 s 10000
-0.05001 40 0.0002498 s 10000
-0.2 40 0.0002498 s 10000
0.05001 40 0.0002498 s 10000
0.2 40 0.0002498 s 10000
-0.20001 40 0.0002498 s 10000
-0.5 40 0.0002498 s 10000
0.20001 40 0.0002498 s 10000
0.5 40 0.0002498 s 10000
-0.5001 40 0.0002498 s 10000
-2 40 0.0002498 s 10000
0.5001 40 0.0002498 s 10000
2 40 0.0002498 s 10000
-2.0001 40 0.0002498 s 10000
-6.6 40 0.0002498 s 10000
2.0001 40 0.0002498 s 10000
6.6 40 0.0002498 s 10000
Edge Measurement Adjustment
To adjust Edge:
When the Calibrator is in Scope Adjustment mode and Edge is highlighted:
1. Connect the SCOPE connector of the Calibrator to the 8588A input HI and LO as shown in
Figure 35.
8588A settings:
• Function: Digitize
• Input > Terminal > Front
• Coupling, Zin: DC, 1 MΩ
• Measure Setup > Low pass filter: 3 MHz
• Measure Setup > Range: base on ac voltage adjust point
• Measure Setup > Aperture: <Aperture value> which is shown in the Fluke 8588A Aperture
Setup column of Table 55. This Aperture value was calculated based on adjust frequency with
this formula:
Sample Rate = 100 * Adjust Frequency
(If Sample Rate > 5000000.0, use 5000000.0)
Aperture = (1 / Sample Rate) - 0.0000002
• Trigger Setup > Triggers/Arm (Count): 10000
2. Tap Continue on the display.
3. Push J.
4. On the 8588A, push the TRIG softkey to collect data of the waveform. Export the digitized data to
the external device. Reference the 8588A Operators Manual Digitize Menu function for information
to extract the data.
5. Process the data:
Separate the data into two groups:
• Top level: MEDIAN of all readings > 90% of reference level
• Base level: MEDIAN of all readings < 10% of reference level
The processed value is calculated as:
median of Top line – median of Base line.
6. Type in the processed value from step 4 with the Calibrator keypad and push E.
Note
The Calibrator shows a message if the typed value is higher or lower than the limits of the
value. If this occurs, examine the setup and carefully re-type the measurement with the correct
unit (for example, mV, V). Repair may be necessary if the warning continues.
7. Repeat Table 55, steps 3 through 5 until the Calibrator prompts to adjust Leveled Sine.
Oscilloscope Calibration Option (600M, 1G, and 2G) Calibration, Verification, and Adjustment
Leveled Sine Wave Adjustment
This procedure uses:
• Fluke 5790B Wideband
• Keysight N1913B Power Meter or equivalent
• Keysight E9304A Power Sensor or equivalent
• Type_N(f) to BNC(f) adapter
• Output Scope Card cable supplied with the scope option
Leveled Sine Wave LOW Frequency Adjustment
When Calibrator is in Scope Adjustment mode and Leveled Sine is highlighted:
1. Setup the 5790B Wideband with External trigger OFF and HIRES ON and range as shown in
Table 56.
2. Connect the Output N-type terminal to the 5790B Wideband configured to measure ac voltage and
push Continue on the display. See Figure 37.
3. Push J.
4. Type in the measured output in volts RMS with the Calibrator keypad and push E.
Table 55. Sequential Adjustment Points and 8588A Aperture Setup for Edge
Calibrator Output
(V)
ADJ Freq
(Hz) 8588A Aperture Setup 8588A Trigger Setup
0.005 1000 0.0000098 s 10000
0.01 1000 0.0000098 s 10000
0.025 1000 0.0000098 s 10000
0.05 1000 0.0000098 s 10000
0.06 1000 0.0000098 s 10000
0.08 1000 0.0000098 s 10000
0.1 1000 0.0000098 s 10000
0.2 1000 0.0000098 s 10000
0.25 1000 0.0000098 s 10000
0.3 1000 0.0000098 s 10000
0.5 1000 0.0000098 s 10000
0.6 1000 0.0000098 s 10000
1 1000 0.0000098 s 10000
2.5 1000 0.0000098 s 10000
Note
The Calibrator shows a message if the typed value is higher or lower than the limits of the
value. If this occurs, examine the setup and carefully re-type the measurement with the correct
unit (for example, mV, V). Repair may be necessary if the warning continues.
5. Repeat step 3 and 4 until the Calibrator prompts to adjust leveled sine mid frequency.
Table 56. Sequential Adjustment Points for Leveled Sine LO Points Setup
Calibrator Output 5790B Wideband
Range Setup(V) (Hz)
0.005 50000 2.2 mV
0.02 50000 22 mV
0.02 20000000 22 mV
0.02 49900000 22 mV
0.0201 50000 22 mV
0.05 50000 22 mV
0.05 20000000 22 mV
0.05 49900000 22 mV
0.0501 50000 22 mV
0.2 50000 220 mV
0.2 20000000 220 mV
0.2 49900000 220 mV
0.201 50000 220 mV
0.5 50000 220 mV
0.5 20000000 220 mV
0.5 49900000 220 mV
0.501 50000 220 mV
2 50000 2.2 V
2 20000000 2.2 V
2 49900000 2.2 V
2.01 50000 2.2 V
5.5 50000 2.2 V
5.5 20000000 2.2 V
5.5 49900000 2.2 V
Oscilloscope Calibration Option (600M, 1G, and 2G) Calibration, Verification, and Adjustment
Leveled Sine Wave MID Frequency and HIGH Frequency Adjustment
To adjust the calibration leveled sine wave MID and HIGH frequencies:
1. Connect the Keysight N1913B Power Meter to the Keysight E9304A Power Sensor, see
Figure 44.To learn how to connect these two instruments, refer to their operator manuals.
2. Zero and self-calibrate the power meter with the power sensor. Refer to the Keysight N1913B
operator manual.
Power Meter settings:
• Turn off relative for channel 1
• Set channel 1 to measure power, display dBm, auto range, and average 256.
3. Connect the Output N-type terminal to a Precision Power Meter configured to measure ac voltage
and tap Continue on the display. See Figure 44.
4. Push J.
5. Type in the measured output in volts RMS with the Calibrator keypad and push E.
Note
For frequency of 50 MHz, type in the measured output collected in column B of Table 52.
For frequency >50 MHz, calculate the V rms values with this formula:
Value Enter = Value from Power Meter + column B of Table 52 - column C of Table 52.
Note
Ensure all values are converted to V rms.
Note
The Calibrator shows a message if the typed value is higher or lower than the limits of the
value. If this occurs, examine the setup and carefully re-type the measurement with the correct
unit (for example, mV, V). Repair may be necessary if the warning continues.
6. Repeat step 4 and 5 until the Calibrator prompts to adjust Resistance.
Table 57. Sequential Adjustment Points and 5790B or Power Meter Setup for Leveled Sine MID
Calibrator Output 5790B Wideband
Range Setup
N1913B Setup
(V) (Hz) Range Count
0.005 50E+6 2.2 mV
0.016 50E+6 2.2 mV
0.016 300E+6 LP 16
0.016 600E+6 LP 16
0.005 75E+6 LP 32
0.005 137E+6 LP 32
0.016 75E+6 LP 16
0.016 137E+6 LP 16
0.01601 50E+6 2.2 mV
Calibrator Output 5790B Wideband
Range Setup
N1913B Setup
(V) (Hz) Range Count
0.05 50E+6 22 mV
0.05 300E+6 LP 4
0.05 600E+6 LP 4
0.01601 75E+6 LP 8
0.01601 137E+6 LP 8
0.05 75E+6 LP 4
0.05 137E+6 LP 4
0.0501 50E+6 22 mV
0.16 50E+6 70 mV
0.16 300E+6 LP 4
0.16 600E+6 LP 4

<!-- llm_chunk_end id=service_chunk_0020 -->

<!-- llm_chunk_start id=service_chunk_0021 source=service_manual_5560a source_line_start=4801 source_line_end=5060 retrieval_priority=normal -->

## service_chunk_0021: 0.005 75E+6 LP 32

0.005 75E+6 LP 32
0.005 137E+6 LP 32
0.016 75E+6 LP 16
0.016 137E+6 LP 16
0.01601 50E+6 2.2 mV
Calibrator Output 5790B Wideband
Range Setup
N1913B Setup
(V) (Hz) Range Count
0.05 50E+6 22 mV
0.05 300E+6 LP 4
0.05 600E+6 LP 4
0.01601 75E+6 LP 8
0.01601 137E+6 LP 8
0.05 75E+6 LP 4
0.05 137E+6 LP 4
0.0501 50E+6 22 mV
0.16 50E+6 70 mV
0.16 300E+6 LP 4
0.16 600E+6 LP 4
0.0501 75E+6 LP 4
0.0501 137E+6 LP 4
0.16 75E+6 LP 4
0.16 137E+6 LP 4
0.1601 50E+6 70 mV
0.5 50E+6 220 mV
0.5 300E+6 HP 32
0.5 600E+6 HP 32
0.1601 75E+6 LP 4
0.1601 137E+6 LP 4
0.5 75E+6 HP 32
0.5 137E+6 HP 32
0.501 50E+6 220 mV
1.6 50E+6 700 mV
1.6 300E+6 HP 4
1.6 600E+6 HP 4
0.501 75E+6 HP 16
0.501 137E+6 HP 16
1.6 75E+6 HP 4
Table 57. Sequential Adjustment Points and 5790B or Power Meter Setup for Leveled Sine MID
Oscilloscope Calibration Option (600M, 1G, and 2G) Calibration, Verification, and Adjustment
Calibrator Output 5790B Wideband
Range Setup
N1913B Setup
(V) (Hz) Range Count
1.6 137E+6 HP 4
1.601 50E+6 700 mV
5.5 50E+6 2.2 V
5.5 300E+6 HP 4
5.5 600E+6 HP 4
1.601 75E+6 HP 4
1.601 137E+6 HP 4
5.5 75E+6 HP 4
5.5 137E+6 HP 4
Table 58. Sequential Adjustment Points and Power Meter set up for Leveled Sine HIGH
Calibrator Output N1913B Setup
(V) (Hz) [1], [2] Range Count
0.005 601E+6 LP 32
0.01 601E+6 LP 32
0.01 2E+9 LP 32
0.01 2E+9 LP 32
0.0101 601E+6 LP 16
0.03 601E+6 LP 4
0.03 2E+9 LP 4
0.03 2E+9 LP 4
0.0301 601E+6 LP 4
0.1 601E+6 LP 4
0.1 2E+9 LP 4
0.1 2E+9 LP 4
0.101 601E+6 LP 4
Table 57. Sequential Adjustment Points and 5790B or Power Meter Setup for Leveled Sine MID
Resistance Adjustment
The Product adjusts the calibration of Measure Resistance mode (Function > Scope > Resistance)
with resistors of known values. Use the Calibrator keypad to enter the actual resistance values as the
Calibrator measures those values.
The resistors must make a solid connection to a BNC(f) to make a connection to the end of the output
cable supplied with the scope option. You must know the resistance values at this BNC(f) connector.
This procedure uses:
• Resistors of known values and Fluke 5560A Calibrator Main Frame Source Resistance
• Adapter to connect resistors to the BNC(f) connector (Fluke recommends Pomona 1269)
Calibrator Output N1913B Setup
(V) (Hz) [1], [2] Range Count
0.3 601E+6 HP 32
0.3 2E+9 HP 32
0.3 2E+9 HP 32
0.301 601E+6 HP 32
1 601E+6 HP 8
1 2E+9 HP 8
1 2E+9 HP 8
1.01 601E+6 HP 4
3.5 601E+6 HP 4
3.5 2E+9 HP 4
3.5 2E+9 HP 4
[1] 601E+6 adjustment points only applicable for the 1G option.
[2] 2E+9 adjustment points only applicable for the 2G option.
Table 58. Sequential Adjustment Points and Power Meter set up for Leveled Sine HIGH (cont.)
Oscilloscope Calibration Option (600M, 1G, and 2G) Calibration, Verification, and Adjustment
When the Calibrator is in Scope Adjustment mode and Resistance is highlighted:
1. Make the connections shown in Figure 45:
Figure 45. Resistance Calibration Adjustment Connections
5560A Calibrator settings:
• Function setting: Function > Single Output > Resistance
• Guard: INTERNAL
• Comp: OFF
• Output: 40 Ω.
2. Push J.
3. Tap the Continue button on the display.
4. Tap the Continue button on the display again and use the Calibrator keypad to enter the actual
Measured value of 40 Ω (40.00 Ω).
5. Push E. Wait for the DUT to measure the value and prompt you for the next value.
5560A settings:
• Function setting: Function > Single Output > Resistance
• Guard: INTERNAL
• Comp: OFF
• Output: 60 Ω.
6. Push J.
7. Tap the Continue button on the display.
8. Tap the Continue button on the display again and use the Calibrator keypad to enter the actual
Measured value of 60 Ω (60.00 Ω).
9. Push E. Wait for the DUT to measure the value and prompt you for the next value.
5560A settings: Observe banana plug is in OPPOSITE polarity.
Observe Banana Plug is in
OPPOSITE POLARITY
Scope Card Cable
comes with DUT
5560A
DUT
• Function setting: Function > Single Output > Resistance
• Guard: INTERNAL
• Comp: OFF
• Output: 1 MΩ
• Output Scope card cable supplied with the scope option
10. Push J.
11. Tap the Continue button on the display.
12. Tap the Continue button on the display again and use the Calibrator keypad to enter the actual
Measured value of 1 MΩ (1 MΩ).
13. Push E. Wait for the DUT to measure the value.
14. Push the Save button on the display to store the adjustment results.
Maintenance
Most common maintenance steps for the Product are found in the Operators Manual.
Product Disposal
Dispose of the Product in a professional and environmentally sound manner:
• Delete personal data on the Product before disposal.
• Remove batteries that are not integrated into the electrical system before disposal and dispose of
batteries separately.
• If this Product has an integral battery, put the entire Product in the electrical waste.
Scope Option Maintenance
Maintenance procedures of diagnostic remote commands for the scope option are not available to
users. If the scope option is not installed or is not connected to internal power, when you tap the Scope
button, the display indicates that the option is not installed.
If the message shows with an installed scope option, you must send the Calibrator to Fluke for repair.
To purchase a scope option, see your Fluke sales representative.See Contact Fluke Calibration.
Replaceable Parts
The Product has limited user-replaceable parts available. Due to design, there are hazards associated
with repair and replacement of parts internal to the chassis. Service down to a Printed Circuit Assembly
(PCA) level should only be performed by a Fluke Calibration Authorized Service Center.
Units found to be unable to adjust within specification or exhibit error codes during diagnostics indicate
that the Product will require service and should be returned to a Fluke Calibration Authorized Service
Center for troubleshooting and repair.
Use the items in Table 59 to identify some of the parts in Figure 46. Note that not all parts are shown in
the figure. Electronic components can be ordered directly from Fluke Calibration and its authorized
representatives with the Fluke part number. See Contact Fluke Calibration.
Replaceable Parts
Table 59. Replaceable Parts
Item Sequence Description
Fluke
Calibration
Part Number
Quantity
14 5080A-8006,HANDLE,4U 3468705 4
15 5560A-2011,TERMINAL BLOCK 4844092 1
16 5560A-2010,FRONT PANEL,PLASTIC 4844089 1
17 (not shown) 5560A-2702,ENCODER MODULE 4937780 1
18 5560A-8003,TERMINAL DECAL 4844160 1
19 5560A-2701-01,BINDING POST- RED 4884440 4
20 5560A-2701-02,BINDING POST- BLACK 4884457 2
21 5560A-2701-04,BINDING POST- GREEN 4884478 1
22 5560A-2701-03,BINDING POST- BLUE 4884469 1
23 CONNECTOR,ADAPTER,C0AXIAL,N(F),SMA(F),BULKHEAD MOUNT,BULK 1279066 1
24 5560A-2012,LIGHT RING COVER 4844108 1
25 5560A-8008,KEYPAD 4937744 1
26 5560A-8009,ENCODER WHEEL 4937842 1
27 5560A-8010,DISPLAY 4937863 1
28 5730A-2012,KNOB,ENCODER 4219600 1
29 5560A-8002,USB/LOWER DECAL 4844151 1
31 (not shown) FUSE,.25X1.25,5A,250V,SLOW 109215 1
32 POWER ENTRY MODULE,6A,250V,FILTER,FUSE,DPSTSWITCH,FLANGE MT,.187TABS,SHIELDED 4355075 1
33 FILTER,LINE,5A/250V,CHASSIS MOUNT,.250 SPADETERMINALS,64X34MM 5276811 1
34 (not shown) 5440A-8198-01,BINDING POST,STUD,PLATED 102707 1
35 (not shown) WASHER LOCK INTRNL STL .267ID 110817 1
36 (not shown) NUT,HEX,JAM,1/4-28,7/16IN,5/32IN H,BRASS 5569321 1
37 (not shown) 5440A-8197-01,BINDING HEAD,PLATED 102889 1
38 (not shown) 5560A-6501,POWER TRANSFORMER 4944989 1
39 (not shown) 5520A-3013,SHIM,TRANSFORMER 625985 1
40 (not shown) SCREW,HK M4-0.7X8MM,STEEL,PLAIN,LOW HEADSOCKET CAP SCREW,W/SELF LOCKING PATCH 3472154 21
43 (not shown) 5560A-8007,NUT, #10, LOW THERMAL 4859582 16
Item Sequence Description
Fluke
Calibration
Part Number
Quantity
44 (not shown) WASHER,LOCK,EXT TOOTH,#10 SCREW,.204INID,.395IN OD,.018IN THK,PHOS BRONZE 4884555 8
45 (not shown) WASHER,FLAT,#10 X.5IN OD,.04IN THK,GRADE C-110,COPPER 4884543 8
46 (not shown) CABLE ASSEMBLY,USB 2.0,USB A(M) TO USB MINI-B(M),SHIELDED,EXTRA-FLEX,12.00 L 3346686 1
48 (not shown) 5730A-4401,INLET HARNESS 4308875 1
49 (not shown) 5730A-4402,INLET WIRE 4308882 1
50 (not shown) 5730A-4403,INLET WIRE 4308894 1
51 (not shown) 5730A-4404,GROUND WIRE 4308907 1
5 (not shown) 5730A-4405,GROUND WIRE 4308918 1
53 (not shown) CABLE ACCESSORY,CABLEACCESS,TIE,4.00L,.10W,.75 DIA 172080 3
54 (not shown) 5560A-2003,FAN BRACKET 4844014 1
55 5560A-2002,GUARD BOX COVER 4844006 1
56 5560A-2008,FRONT PANEL 4844061 1
57 5560A-2004,REAR PANEL 4844023 1
58 5560A-2005,TOP COVER 4844038 1
59 5560A-2006,BOTTOM COVER 4844045 1
60 5560A-2009,FRONT COVER, GUARD BOX 4844077 1
61 (not shown) 5560A-2023,FRONT LCD MOUNT 4937726 1
62 5560A-2001,CHASSIS 4843996 1
63 (not shown) 5560A-8016,LCD CUSHION, BACK 4966029 1
64 (not shown) CONNECTOR ACC,CONNACC,COAX,BNC,LOCKWASHER 622743 2
65 (not shown) CONNECTOR ACC,CONN ACC,COAX,BNC,NUT 622719 2
66 (not shown) 57LFC-4402,TRANSFORMER GROUND CABLE 2095956 1
67 (not shown) WASHER FLAT.219 ID.506 OD.061 THK STEEL ZINC-CHROMATE 2565513 4
68 (not shown) SCREW,MODIFIED 660933 4
69 NUT HEX ELASTIC STOP STL 10-32.375 944350 4
70 (not shown) SCREW,6-32 X 1/4IN,PAN HEAD,PHILLIPS,STEEL,ZINCPL,PATCH LOCK 152140 4
Table 59. Replaceable Parts (cont.)
Replaceable Parts
Item Sequence Description
Fluke
Calibration
Part Number
Quantity
71 SCREW,M4-0.7X6MM,PHILLIPS,PANHEAD,STEEL,ZINC PLATED,W/SELF LOCKING PATCH 3472262 26
72 (not shown) SCREW,M3X0.5,8MM,PAN,PHILLIP,STEEL,ZN-CHROMATE,ROHS COMPL. 2803610 19
73 (not shown) SCREW,4-14,.375,PAN,PHILLIPS,STEEL,ZINC-ROHSCLEAR,THREAD FORM 448456 9
74 CONNECTOR,CONN,COAX,BNC(F),CABLE 412858 1
75 (not shown) SCREW,M2 X 0.4,3MM,PAN.PHILLIPS,STEEL,ZINC-CHROMATE 2568619 2
76 SCREW,M3-0.5 X 8MM,PHILLIPS FLAT HEAD,DIN965,STEEL,ZINC PL,W/SELF LOCKING PATCH 3472058 23
77 5560A-2014,TCOUPLE LEVER 4844124 2
78 (not shown) 5560A-2015,TCOUPLE COVER 4844136 1
80 5700A-2043-01,BOTTOM FOOT, MOLDED, GRAY #7 868786 4
81 (not shown) SPRING,COMPRESSION,0.24IN OD,1.75IN L,0.02INWIRE,1.5LB/IN,MUSIC WIRE 5272855 2
82 (not shown) 5520A-2026,TRANSFORMER COVER, PAINTED 647138 1
83 (not shown) 5560A-8015,DISPLAY CABLE SHIELD/BRACKET 4962599 1
87 5522A-8002,RETAINER, ANALOG TOPCOVER 3472691 2
89 (not shown) NUT,HEX,K-LOCK,6-32,.140IN THK,5/16IN AF,EXTTOOTH LOCK WASHER,STEEL 152819 2
90 (not shown) 5560A-2501,FAN ASSEMBLY 4937839 1
91 (not shown) TAPE,TAPE,FOAM,VINYL,.500,.125 330449 1.666
92 (not shown) SCREW,M3-0.5 X 10MM L,SOCKET HEAD CAPSCREW,STEEL,ZINC,PATCH LOCK 4603503 4
SCREW,M3X0.5,6MM,PAN
HEAD,PHILLIPS,STEEL,ZINC-CHROMATE,S-L NYLON
PATCH
3783203 25
94 WT-630564,TILT STAND 2650711 2
95 (not shown) 5560A-8012,LCD CUSHION 4937759 1
97 (not shown) SPRING,BELLEVILLE,FOR 1/4IN BOLT,.258 ID,.563OD,.043 THK,.068 H,STEEL,ZINC CLR 5194811 4
98 (not shown) FOAM PAD,URETHANE,.250 IN X.375 IN X .062 INTHK,ADHESIVE 2567386 6
Table 59. Replaceable Parts (cont.)

<!-- llm_chunk_end id=service_chunk_0021 -->

<!-- llm_chunk_start id=service_chunk_0022 source=service_manual_5560a source_line_start=5041 source_line_end=5085 retrieval_priority=normal -->

## service_chunk_0022: 77 5560A-2014,TCOUPLE LEVER 4844124 2

77 5560A-2014,TCOUPLE LEVER 4844124 2
78 (not shown) 5560A-2015,TCOUPLE COVER 4844136 1
80 5700A-2043-01,BOTTOM FOOT, MOLDED, GRAY #7 868786 4
81 (not shown) SPRING,COMPRESSION,0.24IN OD,1.75IN L,0.02INWIRE,1.5LB/IN,MUSIC WIRE 5272855 2
82 (not shown) 5520A-2026,TRANSFORMER COVER, PAINTED 647138 1
83 (not shown) 5560A-8015,DISPLAY CABLE SHIELD/BRACKET 4962599 1
87 5522A-8002,RETAINER, ANALOG TOPCOVER 3472691 2
89 (not shown) NUT,HEX,K-LOCK,6-32,.140IN THK,5/16IN AF,EXTTOOTH LOCK WASHER,STEEL 152819 2
90 (not shown) 5560A-2501,FAN ASSEMBLY 4937839 1
91 (not shown) TAPE,TAPE,FOAM,VINYL,.500,.125 330449 1.666
92 (not shown) SCREW,M3-0.5 X 10MM L,SOCKET HEAD CAPSCREW,STEEL,ZINC,PATCH LOCK 4603503 4
SCREW,M3X0.5,6MM,PAN
HEAD,PHILLIPS,STEEL,ZINC-CHROMATE,S-L NYLON
PATCH
3783203 25
94 WT-630564,TILT STAND 2650711 2
95 (not shown) 5560A-8012,LCD CUSHION 4937759 1
97 (not shown) SPRING,BELLEVILLE,FOR 1/4IN BOLT,.258 ID,.563OD,.043 THK,.068 H,STEEL,ZINC CLR 5194811 4
98 (not shown) FOAM PAD,URETHANE,.250 IN X.375 IN X .062 INTHK,ADHESIVE 2567386 6
Table 59. Replaceable Parts (cont.)
Item Sequence Description
Fluke
Calibration
Part Number
Quantity
99 5560A-2027,XFRMR BRACE 5334517 1
100 5560A-2028,BRACE INSULATOR PLATE 5334521 1
101 (not
shown)
MAGNETIC MATERIAL,ROUND CABLE EMI
SUPPRESSOR,265OHMS@100MHZ,12.7MM
CABLE,30X40MM
5383876 1
103 WASHER,SHOULDER,.118 ID,.250 OD,.070 L,NYLON 485417 4
104 (not
shown)
CONNECTOR,COAXIAL,BNC(M),DUST CAP,2
GHZ,BULK (5530A) 6075391 1
105 (not
shown)
CONNECTOR,COAXIAL,DUST CAP,FEMALE,TYPE N
(5530A) 6075475 1
Table 59. Replaceable Parts (cont.)
Replaceable Parts
Figure 46. Replacement Parts

<!-- llm_chunk_end id=service_chunk_0022 -->

