# Fluke 5560A/5550A/5540A/5530A Operators Manual — LLM/PyMeasure optimized

---
title: "Fluke 5560A/5550A/5540A/5530A Operators Manual — LLM/PyMeasure optimized"
source_file: "operators_guide.md"
vendor: "fluke"
model: "5560A"
class_name: "Fluke5560A"
instrument_type: "multifunction precision calibrator / precision source calibrator"
workflow_step: 03
source_role: "operator safety and operation planning"
command_inventory_created: false
command_syntax_authority: "programming_guide.md"
generated_on: "2026-05-07"
local_artifact: true
upstream_pr: false
---

# LLM_AGENT_CONTRACT

This file is for LLM/RAG planning of safe hardware tests and operator safety procedures for the Fluke 5560A/5550A/5540A/5530A calibrator family.

## Mandatory rules for LLM/Codex agents:

1. Treat the calibrator as safety-critical hardware.
2. Do **not** enable output automatically in generated hardware tests.
3. Do **not** tell an operator to connect or disconnect DUT leads while output may be active.
4. Do **not** treat front-panel procedures as remote commands.
5. Do **not** invent SCPI or remote command syntax from the Operators Manual.
6. Use the Remote Programmers Manual / Programming Guide as the authoritative source for command syntax.
7. Use this Operators Manual for safety, operator workflows, fixture requirements, model/option constraints, warm-up, remote-port setup, and error interpretation.
8. Use the Service Manual for service/calibration-risk boundaries and qualified-service-only procedures.
9. Mark OCR/conversion ambiguity as `needs-verification` before using it in code, metrology, or safety-critical procedures.

# DOCUMENT ROLE IN PYMEASURE WORKFLOW

| File | Role | Not allowed |
|---|---|---|
| operators_guide.md | Operator safety, user workflows, DUT connections, remote-port setup, safe hardware-test policy, model/option constraints, error-code meaning. | Full remote-command inventory or exact command syntax. |
| operators_manual_llm.md | LLM/RAG planning aid for safety and operator workflow. | Driver implementation by itself. |
| programming_guide.md | Authoritative source for remote command syntax, parameters, responses, status registers, command/query forms, and error-query commands. | Physical fixture instructions unless stated there. |
| service_manual.md | Service risk, calibration/adjustment risk, internal-service boundaries, verification prerequisites. | Inventing remote commands or routine operator procedures. |

# QUICK FACTS FOR RETRIEVAL

| Field | Value |
|---|---|
| Instrument family | Fluke 5560A / 5550A / 5540A / 5530A Calibrators |
| Instrument type | Multifunction precision calibrator / precision source calibrator |
| Manual type | Operators Manual |
| Revision | August 2022 Rev. 3, 3/25 |
| Remote interfaces | IEEE-488/GPIB, RS-232, USBTMC, Ethernet/LAN/Telnet |
| Local operation | Front panel, touchscreen, keypad, softkeys, function menus |
| Remote operation authority | Remote Programmers Manual / Programming Guide |
| Warm-up requirement | At least 30 minutes after power-on; after short power-off, warm up at least twice the off-time, max 30 minutes |
| Power-up/reset default | 0 mV dc, Standby, 120 mV range; volatile values return to most recent defaults |
| Safe operator state | Standby / output inactive at terminals; reset removes output and returns to power-up default |
| Safety class | Line-powered instrument requiring protective earth grounding |

# SAFETY SUMMARY FOR DRIVER AND HARDWARE TEST PLANNING

| Topic | Risk | PyMeasure implication | Hardware-test policy | Source evidence |
|---|---|---|---|---|
| Operate mode | Terminals can carry hazardous voltage/current. | Keep output activation as explicit methods or tightly controlled APIs; never enable by side effect. | `operator-confirmed-only` | Section 4, row 1 |
| Standby mode | Output value is inactive at selected terminals, but accidental Operate is still possible. | Use as final state but do not rely on it as permission to rewire without operator verification. | `roundtrip-safe` for final-state checks | Section 4, row 2 |
| Reset / abort-to-default | Returns to 0 mV dc, Standby, 120 mV range. | Useful as safe recovery state if Programming Guide exposes a remote equivalent. | `roundtrip-safe` or `protocol-only` depending command | Section 4, row 3 |
| DUT connection changes | Manual warns not to connect/disconnect with voltage present. | Hardware tests must not require wiring changes while test is running. | `operator-confirmed-only` | Section 4, row 4 |
| High voltage | Hazardous voltage indicator for >30 Vrms or 42 V peak. | Add explicit safety gates for any output above these thresholds. | `operator-confirmed-only` | Section 4, row 5 |
| High current | VI AUX and 30A terminal selection depends on current level. | Current output tests need fixture/load and terminal-policy notes. | `operator-confirmed-only` | Section 4, row 6 |
| Simulated power | Up to 30.9 kW, not available on 5540A. | Do not run automatically; model-gate API. | `never` for broad tests | Section 4, row 7 |
| Guard/earth | Only one earth-to-LO tie point should exist; external guard changes internal guard connection. | Do not auto-change guard in broad hardware tests without fixture declaration. | `operator-confirmed-only` | Section 4, row 8 |
| Calibration passcode | Protects NVM calibration constants and clock/date changes. | Do not expose as routine workflow; protocol-test only unless explicitly scoped. | `protocol-only` / `never` | Section 4, row 9, Section 12 |
| Restore default calibration | Deletes calibration constants and requires full calibration. | Do not implement/run without explicit project decision. | `never` | Section 4, row 10, Section 12 |
| Firmware update | Uses USB host / maintenance workflow. | Not part of normal PyMeasure driver. | `never` | Section 4, row 11 |
| Covers/fuses/repair | Covers removed exposes hazardous voltages; service by approved technician. | Do not generate repair procedures as normal test guidance. | `never` | Section 4, row 12 |

# REMOTE OPERATION AND INTERFACE SUMMARY

| Interface | Confirmed? | Setup facts | Termination/EOL | Remote/local notes | Source evidence | Notes |
|---|---|---|---|---|---|---|
| IEEE-488/GPIB | yes | Fully programmable parallel interface bus meeting IEEE-488.1 and supplemental IEEE-488.2 behavior; GPIB enabled by default, address `4`. | LF with EOI asserted. | Under controller control, operates as talker/listener. Operators Manual refers to Programming Guide for command set. | Section 5, paragraph 1-3 | IEEE-488.1/488.2 context supports likely `SCPIMixin`. |
| RS-232 | yes | Rear-panel serial port for serial remote control; RS-232 enabled by default. Baud `9600`, data bits `8`, stop bits `1`, parity `none`, flow control `XON/XOFF`, EOL `CR/LF`, interface `Terminal`. | Configurable: CR/LF, CR, LF. Default: CR/LF. | Remote-port setup options include data bits 8/7, stop bits 1/2, flow control None/RTS-CTS/XON-XOFF, parity None/Even/Odd, baud rates 9600/19200/38400/57600/115200. | Section 5, paragraph 4-6 | Serial remote has no SRQ capability. |
| USBTMC | yes | Rear-panel USB 2.0 type B port; meets USBTMC-USB488 and supplemental IEEE-488.2 behavior. VISA resource: `USB0::0x0F7E::0x800A::[serial number]::INSTR`. | Not specified. | Vendor ID: `0x0F7E`. Product ID: `0x800A`. USBTMC enabled by default. | Section 5, paragraph 7-9 | Use Programming Guide for exact command behavior. |
| Ethernet / Telnet | yes | Rear-panel 10/100/1000BASE-T Ethernet port supports remote control; Telnet session command entry. Telnet enabled by default, port `3490`. EOL `CR/LF`, interface `Terminal`, DHCP on, netmask `255.255.255.0`. | Configurable: CR/LF, CR, LF. Default: CR/LF. | Remote-port setup provides DHCP, static IP, gateway, subnet mask, current IP, gateway, MAC address, port, EOL, remote interface mode, network-security address range, and restore defaults. | Section 5, paragraph 10-12 | Do not assume IP; user supplies VISA/TCP address. |

# REMOTE PORT SETUP FACTS

| Interface | Setting | Values/defaults from manual | PyMeasure implication | Source evidence | Notes |
|---|---|---|---|---|---|
| USBTMC | VISA resource | `USB0::0x0F7E::0x800A::[serial number]::INSTR` | Useful for examples and hardware test docs. | Section 5, paragraph 9 | Serial number can be obtained from rear panel, Setup > About, or `*IDN?` through another interface. |
| USBTMC | Enabled default | true | Hardware tests can use VISA USBTMC if available. | Section 5, paragraph 11 | Use Programming Guide for exact command behavior. |
| GPIB | Address | default `4` | Hardware tests should accept `--device-address`; do not hard-code. | Section 5, paragraph 4 | Some lab setups may differ. |
| GPIB | Enabled default | true | Supports standard PyVISA usage. | Section 5, paragraph 2 | IEEE-488.1/488.2 context supports likely `SCPIMixin`. |
| RS-232 | Baud rates | 9600, 19200, 38400, 57600, 115200 | Add connection examples only; no fixed default in driver unless aligned with repo style. | Section 5, paragraph 6 | Default: 9600. |
| RS-232 | Data bits | 8 or 7 | User-overridable connection settings. | Section 5, paragraph 6 | Default: 8. |
| RS-232 | Stop bits | 1 or 2 | User-overridable connection settings. | Section 5, paragraph 6 | Default: 1. |
| RS-232 | Flow control | None, RTS/CTS, XON/XOFF | User-overridable connection settings. | Section 5, paragraph 6 | Default: XON/XOFF. |
| RS-232 | Parity | None, Even, Odd | User-overridable connection settings. | Section 5, paragraph 6 | Default: none. |
| RS-232 | EOL | CR/LF, CR, LF | Hardware tests must use configured terminator. | Section 5, paragraph 6 | Default: CR/LF. |
| Ethernet/Telnet | Port | default `3490` | TCPIP/Telnet examples can use this port. | Section 5, paragraph 12 | Confirm with actual instrument setup. |
| Ethernet/Telnet | EOL | CR/LF, CR, LF | Hardware tests must match configured EOL. | Section 5, paragraph 12 | Default: CR/LF. |
| Ethernet/Telnet | DHCP/static | DHCP On by default; static IP fields available | Do not assume IP; user supplies VISA/TCP address. | Section 5, paragraph 12 | Security address range exists. |

# OPERATE / STANDBY / RESET BEHAVIOR

- In Operate mode, the output value and function shown on the display are active at the selected terminals.
- In Standby mode, the displayed output value and function are inactive at the selected terminals.
- Reset returns the calibrator to the power-up state: `0 mV dc`, `Standby`, `120 mV range`, with volatile values set to their most recent default values.
- The instrument automatically enters Standby when reset is pushed, when a voltage above 30 Vrms or 42 V peak is selected after a lower voltage, when functions change, when current output location changes between AUX and 30 A, when overload or reverse-power is detected, or when the function screen is obscured by menus.

PyMeasure policy:

- Output activation commands must be explicit and not triggered by setting a value.
- Broad hardware tests must not activate output automatically.
- Hardware tests that configure outputs must use `try/finally` and leave the calibrator in safe final state.
- If the Programming Guide confirms `STBY`, use it as the preferred remote safe-final-state command.
- If the Programming Guide confirms `OPER`, mark it `operator-confirmed-only`.

**Output-enable or Operate actions must not be used in broad automated hardware tests. They require operator-confirmed-only policy unless a later human-approved test scope defines safe load, wiring, range, and final state.**

# DUT CONNECTION AND FIXTURE CONSTRAINTS

| Function area | Required physical setup | Risk | Hardware-test policy | Source evidence | Notes |
|---|---|---|---|---|---|
| Voltage output | OUTPUT HI/LO, optional sense terminals | Hazardous voltage at high levels | `operator-confirmed-only` | Section 8, row 1 | External sense only for specified ranges/functions. |
| Current ≤3.1 A | VI AUX and OUTPUT LO / Sense LO depending function | High current, wiring and terminal selection risk | `operator-confirmed-only` | Section 8, row 2 | Terminal choice affects safe setup. |
| Current >3.1 A | 30A terminal and OUTPUT/SENSE LO | High current | `operator-confirmed-only` | Section 8, row 3 | Requires appropriate load/shunt and cables. |
| Resistance | OUTPUT terminals, compensation setting | Synthetic impedance; wiring polarity matters | `operator-confirmed-only` | Section 8, row 4 | 2-wire/4-wire/Comp OFF must match DUT. |
| Capacitance | OUTPUT terminals; stray capacitance nulling may be needed | Fixture-dependent | `operator-confirmed-only` | Section 8, row 5 | Do not auto-test without fixture. |
| Inductance | OUTPUT terminals; not 5540A/5530A | Fixture-dependent, option/model dependent | `operator-confirmed-only` | Section 8, row 6 | Model-gate before API/tests. |
| RTD source | Three-terminal connection recommended for RTD meters | Lead-resistance errors | `operator-confirmed-only` | Section 8, row 7 | Identical lead resistances may be required. |
| TC source | TC connector with matching thermocouple wire/connectors | Thermal EMF / incorrect TC type | `operator-confirmed-only` | Section 8, row 8 | Avoid heating connector with fingers. |
| TC measure | TC connector and reference-junction handling | Measurement validity depends on physical setup | `operator-confirmed-only` | Section 8, row 9 | Open TC Detect can affect parallel measurements. |
| Guard/Earth | Single ground tie point; external guard for grounded DUT LO | Ground loops, safety ground errors | `operator-confirmed-only` | Section 8, row 10 | Do not defeat protective earth. |
| Scope outputs | SCOPE OUT and TRIG connectors when option installed | Option-dependent output | `operator-confirmed-only` | Section 8, row 11 | Scope options must be installed and detected. |
| Overload tests | 50 Ω oscilloscope input and power-rating confirmation | Can damage DUT | `never` for broad tests | Section 8, row 12 | Operator-confirmed fixture only. |

# OUTPUT / INPUT FUNCTION MAP FOR PYMEASURE PLANNING

| Function group | Operator function | Availability | Main risks | PyMeasure planning note | Source evidence |
|---|---|---|---|---|---|
| Single Output | DCV | All models | Up to ±1020 V | Configure value while standby; activation separate. | Section 9, row 1 |
| Single Output | ACV | All models | Up to 1020 V, frequency/waveform/offset constraints | Needs waveform, frequency, offset, duty-cycle modeling. | Section 9, row 2 |
| Single Output | DCI | All models | Up to ±30.2 A, terminal change at high current | Terminal/range constraints; external load required. | Section 9, row 3 |
| Single Output | ACI | All models | Up to 30.2 A, waveform/coil/52120A options | Fixture-dependent. | Section 9, row 4 |
| Single Output | Resistance | All models | Synthetic impedance and wiring compensation | Model compensation settings carefully. | Section 9, row 5 |
| Single Output | Capacitance | All models | Stray capacitance and fixture dependency | Parser not likely, but test policy strict. | Section 9, row 6 |
| Single Output | Inductance | 5560A/5550A only | Not available on 5540A/5530A | Model-gate API and tests. | Section 9, row 7 |
| Single Output | RTD Source | All models | RTD type and temperature-scale constraints | Values depend on selected RTD type. | Section 9, row 8 |
| Single Output | TC Source | All models | TC wire and reference-junction constraints | Type, scale, offset, RJ handling. | Section 9, row 9 |
| Measure | TC Measure | All models | Physical temperature/TC setup | Query/measurement candidates only if Programming Guide confirms. | Section 9, row 10 |
| Dual Output | DC Power | Not available on 5540A | Voltage + current simultaneous output | Operator-confirmed only. | Section 9, row 11 |
| Dual Output | AC Power | Not available on 5540A | Simulated power and phase/DPF | Operator-confirmed only. | Section 9, row 12 |
| Dual Output | DCV DCV | Not available on 5540A | Dual voltage; AUX limits | Model-gate and terminal notes. | Section 9, row 13 |
| Dual Output | ACV ACV | Not available on 5540A | Dual waveform/phase; AUX limits | Model-gate and waveform constraints. | Section 9, row 14 |
| Scope | Scope DCV | Scope option required | Scope output, 50 Ω/1 MΩ impedance | Option-gated. | Section 9, row 15 |
| Scope | Scope ACV | Scope option required | Scope waveform/trigger/impedance | Option-gated. | Section 9, row 16 |
| Scope | Edge | Scope option required | Pulse response output | Operator-confirmed only. | Section 9, row 17 |
| Scope | Leveled Sine | Scope option required | Bandwidth test signal | Operator-confirmed only. | Section 9, row 18 |
| Scope | Marker | Scope option required | Timing marker output | Option/waveform-frequency dependent. | Section 9, row 19 |
| Scope | Waveform Generator | Scope option required | Signal generator output | Do not use for oscilloscope level/bandwidth accuracy checks. | Section 9, row 20 |
| Scope | Video | Scope option required | Video trigger output | Format/field constraints. | Section 9, row 21 |
| Scope | Pulse | Scope option required | Pulse amplitude/period constraints | Option-gated. | Section 9, row 22 |
| Scope | Measure Resistance | Scope option required | Automatically enters Operate | Never broad auto-test. | Section 9, row 23 |
| Scope | Measure Capacitance | Scope option required | Automatically enters Operate | Never broad auto-test. | Section 9, row 24 |
| Scope | Overload DC | Scope option required | Applies power into 50 Ω input | Never broad auto-test. | Section 9, row 25 |
| Scope | Overload AC | Scope option required | Applies AC power into 50 Ω input | Never broad auto-test. | Section 9, row 26 |

# MODEL AND OPTION DEPENDENCIES

| Model or option | Feature impact | PyMeasure implication | Hardware-test implication | Source evidence | Notes |
|---|---|---|---|---|---|
| 5560A | Full family capability in examples unless otherwise noted | Main target class; can share family driver if model checks added | Still require option detection for scope/52120A | Section 10, row 1 | Operators Manual family scope |
| 5550A | Same family; some option differences possible | Consider family parameterization | Check `*IDN?` and options before tests | Section 10, row 2 | Operators Manual family scope |
| 5540A | Dual output and simulated power not available; inductance not available | Gate dual-output, power, and inductance APIs | Skip unsupported hardware tests | Section 10, row 3 | Function menu notes and output capability notes |
| 5530A | Inductance not available; family capability subset | Gate inductance API | Skip unsupported hardware tests | Section 10, row 4 | Output capability notes |
| 52120A amplifier | Extends current output; up to three amplifiers, high-current use | Separate feature flag / external-fixture API | Operator-confirmed only | Section 10, row 5 | 52120A section |
| Scope options | Scope menu active only when installed | Option-gated subsystem | Skip if option absent | Section 10, row 6 | Scope options section |
| 600M option | 600 MHz oscilloscope calibration option available for 5560A/5550A/5540A | Option detection needed | Operator-confirmed only | Section 10, row 7 | Options/accessories section |
| 1G option | 1.1 GHz option available for 5560A/5550A | Option detection needed | Operator-confirmed only | Section 10, row 8 | Options/accessories section |
| 2G option | 2.2 GHz option for 5560A | Option detection needed | Operator-confirmed only | Section 10, row 9 | Options/accessories section |

# WARM-UP, ZEROING, AND METROLOGY PREREQUISITES

| Requirement | Condition | Driver implication | Hardware-test policy | Source evidence |
|---|---|---|---|---|
| Warm-up after power-on | At least 30 minutes | Hardware tests that assert metrology behavior should report warm-up state or skip unless operator confirms. | `operator-confirmed-only` | Section 11, row 1 |
| Warm-up after power cycling | At least twice the off-time, max 30 minutes | Do not assume immediate metrology-grade operation after reconnect. | `operator-confirmed-only` | Section 11, row 2 |
| Zero adjustment | Required every 14 days or after ambient temperature changes by more than 5 °C | Do not run automatically; provide explicit method only if Programming Guide confirms command. | `protocol-only` / `operator-confirmed-only` | Section 11, row 3 |
| Specifications | UI can display specification information if enabled | Documentation note; not driver validation unless ranges from Programming Guide are confirmed. | `query-only` if readback exists | Section 11, row 4 |
| Ohms zero / impedance zero | Mentioned through setup/calibration context | Treat as maintenance/metrology procedure. | `operator-confirmed-only` | Section 11, row 5 |

# PERSISTENT SETTINGS / CALIBRATION SECURITY

| Topic | Risk | Command-like reference? | PyMeasure implication | Hardware-test policy | Source evidence |
|---|---|---|---|---|---|
| Calibration security passcode | Protects calibration constants and date/time changes | `CAL_SECURE` | Do not expose as ordinary workflow | `protocol-only` / `never` | Section 12, row 1, Section 16 |
| Calibration passcode change | Losing passcode requires Fluke service | `CAL_PASSCODE` | Do not automate in tests | `never` | Section 12, row 2, Section 16 |
| Restore default calibration | Deletes calibration constants; full calibration required afterward | front-panel menu topic | Do not implement/run without explicit project decision | `never` | Section 12, row 3 |
| Restore default setup/factory defaults | Persistent setup changes | front-panel menu topic | Avoid in hardware tests | `never` | Section 12, row 4 |
| Output limits | Saved in nonvolatile memory | command syntax from Programming Guide only | Hardware tests should not alter persistent limits broadly | `protocol-only` unless explicitly scoped | Section 12, row 5 |
| Date/time changes | Product must be unlocked | command syntax from Programming Guide only | Avoid in generic driver tests | `never` | Section 12, row 6 |
| Report string / PUD string | Persistent data | command syntax from Programming Guide only | Avoid in broad tests | `protocol-only` | Section 12, row 7 |

# ERROR-CODE KNOWLEDGE BASE

| Code | Message | Category | PyMeasure implication | Suggested handling | Source evidence |
|---|---|---|---|---|---|
| `0` | No error | `no-error` | Normal end-of-queue / no fault condition. | Drain error queue at end of tests. | Section 13, row 1 |
| `-440` | 488.2 query after indefinite response | `ieee-488-protocol` | Check query sequencing, reads after queries, and interface-specific timing. | Drain error queue, retry. | Section 13, row 2 |
| `-430` | 488.2 I/O deadlock | `ieee-488-protocol` | Check query sequencing, reads after queries, and interface-specific timing. | Drain error queue, retry. | Section 13, row 3 |
| `-420` | 488.2 unterminated command | `ieee-488-protocol` | Check query sequencing, reads after queries, and interface-specific timing. | Drain error queue, retry. | Section 13, row 4 |
| `-410` | 488.2 interrupted query | `ieee-488-protocol` | Check query sequencing, reads after queries, and interface-specific timing. | Drain error queue, retry. | Section 13, row 5 |
| `-377` | LAN address: port combination unavailable | `interface-communication` | Check VISA resource, interface setup, EOL, timeout, and selected remote interface. | Verify network configuration. | Section 13, row 6 |
| `-376` | Command only allowed on synchronous interface | `interface-communication` | Check VISA resource, interface setup, EOL, timeout, and selected remote interface. | Verify interface type. | Section 13, row 7 |
| `-375` | Command only allowed on asynchronous interface | `interface-communication` | Check VISA resource, interface setup, EOL, timeout, and selected remote interface. | Verify interface type. | Section 13, row 8 |
| `-374` | GPIB/488.1 unspecified error | `ieee-488-protocol` | Check query sequencing, reads after queries, and interface-specific timing. | Drain error queue, retry. | Section 13, row 9 |
| `-373` | GPIB/488.1 write operation timeout | `ieee-488-protocol` | Check query sequencing, reads after queries, and interface-specific timing. | Drain error queue, retry. | Section 13, row 10 |
| `-372` | GPIB/488.1 read/write operation aborted | `ieee-488-protocol` | Check query sequencing, reads after queries, and interface-specific timing. | Drain error queue, retry. | Section 13, row 11 |
| `-371` | GPIB/488.1 board address error | `ieee-488-protocol` | Check query sequencing, reads after queries, and interface-specific timing. | Drain error queue, retry. | Section 13, row 12 |
| `-370` | GPIB/488.1 system call has failed | `ieee-488-protocol` | Check query sequencing, reads after queries, and interface-specific timing. | Drain error queue, retry. | Section 13, row 13 |
| `-369` | LAN port encountered error while reading data | `interface-communication` | Check VISA resource, interface setup, EOL, timeout, and selected remote interface. | Verify network configuration. | Section 13, row 14 |
| `-368` | Fatal error occurred while accessing the LAN port | `interface-communication` | Check VISA resource, interface setup, EOL, timeout, and selected remote interface. | Verify network configuration. | Section 13, row 15 |
| `-367` | USB-TMC encountered error while reading data | `interface-communication` | Check VISA resource, interface setup, EOL, timeout, and selected remote interface. | Verify USB connection. | Section 13, row 16 |
| `-366` | GPIB/488.1 encountered error while reading data | `ieee-488-protocol` | Check query sequencing, reads after queries, and interface-specific timing. | Drain error queue, retry. | Section 13, row 17 |
| `-365` | Fatal error occurred while accessing the serial port | `interface-communication` | Check VISA resource, interface setup, EOL, timeout, and selected remote interface. | Verify serial connection. | Section 13, row 18 |
| `-363` | Input Buffer Overrun | `syntax-parameter` | Check command spelling, parameter count, units, type conversion, validator, and mapping. | Validate command format. | Section 13, row 19 |
| `-361` | RS-232 framing/parity/overrun error detected | `interface-communication` | Check VISA resource, interface setup, EOL, timeout, and selected remote interface. | Verify serial settings. | Section 13, row 20 |
| `-350` | Too many errors | `syntax-parameter` | Check command spelling, parameter count, units, type conversion, validator, and mapping. | Drain error queue, retry. | Section 13, row 21 |
| `-302` | Command execution locked out | `syntax-parameter` | Check command spelling, parameter count, units, type conversion, validator, and mapping. | Validate command format. | Section 13, row 22 |
| `-301` | Restricted Command | `syntax-parameter` | Check command spelling, parameter count, units, type conversion, validator, and mapping. | Validate command format. | Section 13, row 23 |
| `-224` | Characters must be A-Z, 0-9, - or _ | `syntax-parameter` | Check command spelling, parameter count, units, type conversion, validator, and mapping. | Validate command format. | Section 13, row 24 |
| `-223` | Character string was more than limit | `syntax-parameter` | Check command spelling, parameter count, units, type conversion, validator, and mapping. | Validate command format. | Section 13, row 25 |
| `-222` | Illegal data value was entered | `syntax-parameter` | Check command spelling, parameter count, units, type conversion, validator, and mapping. | Validate command format. | Section 13, row 26 |
| `-193` | No entry in list to retrieve | `syntax-parameter` | Check command spelling, parameter count, units, type conversion, validator, and mapping. | Validate command format. | Section 13, row 27 |
| `-192` | Too many dimensions to be returned | `syntax-parameter` | Check command spelling, parameter count, units, type conversion, validator, and mapping. | Validate command format. | Section 13, row 28 |
| `-191` | Parameter type detection error | `syntax-parameter` | Check command spelling, parameter count, units, type conversion, validator, and mapping. | Validate command format. | Section 13, row 29 |
| `-190` | Parameter is not a boolean type | `syntax-parameter` | Check command spelling, parameter count, units, type conversion, validator, and mapping. | Validate command format. | Section 13, row 30 |
| `-157` | Unmatched bracket | `syntax-parameter` | Check command spelling, parameter count, units, type conversion, validator, and mapping. | Validate command format. | Section 13, row 31 |
| `-154` | String size is beyond limit | `syntax-parameter` | Check command spelling, parameter count, units, type conversion, validator, and mapping. | Validate command format. | Section 13, row 32 |
| `-153` | Parameter is not an unquoted string type | `syntax-parameter` | Check command spelling, parameter count, units, type conversion, validator, and mapping. | Validate command format. | Section 13, row 33 |
| `-152` | Parameter is not an quoted string type | `syntax-parameter` | Check command spelling, parameter count, units, type conversion, validator, and mapping. | Validate command format. | Section 13, row 34 |
| `-150` | Invalid string data | `syntax-parameter` | Check command spelling, parameter count, units, type conversion, validator, and mapping. | Validate command format. | Section 13, row 35 |
| `-140` | Parameter is not a character type | `syntax-parameter` | Check command spelling, parameter count, units, type conversion, validator, and mapping. | Validate command format. | Section 13, row 36 |
| `-138` | Too many suffixes in command header | `syntax-parameter` | Check command spelling, parameter count, units, type conversion, validator, and mapping. | Validate command format. | Section 13, row 37 |
| `-137` | Invalid suffix in command header | `syntax-parameter` | Check command spelling, parameter count, units, type conversion, validator, and mapping. | Validate command format. | Section 13, row 38 |
| `-130` | Suffix Error. Wrong units for parameter | `syntax-parameter` | Check command spelling, parameter count, units, type conversion, validator, and mapping. | Validate command format. | Section 13, row 39 |
| `-127` | Invalid dimensions in a channel list | `syntax-parameter` | Check command spelling, parameter count, units, type conversion, validator, and mapping. | Validate command format. | Section 13, row 40 |
| `-126` | Numeric value is real | `syntax-parameter` | Check command spelling, parameter count, units, type conversion, validator, and mapping. | Validate command format. | Section 13, row 41 |
| `-125` | Numeric value is negative | `syntax-parameter` | Check command spelling, parameter count, units, type conversion, validator, and mapping. | Validate command format. | Section 13, row 42 |
| `-124` | Numeric value overflowed its storage | `syntax-parameter` | Check command spelling, parameter count, units, type conversion, validator, and mapping. | Validate command format. | Section 13, row 43 |
| `-122` | Parameter is not a numeric type | `syntax-parameter` | Check command spelling, parameter count, units, type conversion, validator, and mapping. | Validate command format. | Section 13, row 44 |
| `-120` | Numeric value is invalid | `syntax-parameter` | Check command spelling, parameter count, units, type conversion, validator, and mapping. | Validate command format. | Section 13, row 45 |
| `-117` | Wrong type of parameter(s) | `syntax-parameter` | Check command spelling, parameter count, units, type conversion, validator, and mapping. | Validate command format. | Section 13, row 46 |
| `-115` | Missing or wrong number of parameters | `syntax-parameter` | Check command spelling, parameter count, units, type conversion, validator, and mapping. | Validate command format. | Section 13, row 47 |
| `-102` | Syntax error | `syntax-parameter` | Check command spelling, parameter count, units, type conversion, validator, and mapping. | Validate command format. | Section 13, row 48 |
| `1000` | Illegal Parameter | `syntax-parameter` | Check command spelling, parameter count, units, type conversion, validator, and mapping. | Validate command format. | Section 13, row 49 |
| `1001` | Failed to save data to non-volatile storage | `persistent-storage` | Avoid in generic hardware tests; may change nonvolatile state or depend on USB/storage. | Do not use in automated tests. | Section 13, row 50 |
| `1002` | Failed to read data from non-volatile storage | `persistent-storage` | Avoid in generic hardware tests; may change nonvolatile state or depend on USB/storage. | Do not use in automated tests. | Section 13, row 51 |
| `1003` | Remote Port Configuration Invalid | `interface-communication` | Check VISA resource, interface setup, EOL, timeout, and selected remote interface. | Verify remote configuration. | Section 13, row 52 |
| `1004` | Units Must Be The Same | `internal-unknown` | Drain error queue, record state, and require manual review if repeated. | Require manual review. | Section 13, row 53 |
| `1005` | Limit Too Small or Large | `range-limit-validation` | Improve PyMeasure validators and value maps using Programming Guide limits. | Use Programming Guide ranges. | Section 13, row 54 |
| `1006` | Cannot Get Range Data | `range-limit-validation` | Improve PyMeasure validators and value maps using Programming Guide limits. | Use Programming Guide ranges. | Section 13, row 55 |
| `1007` | Cannot Find Range | `range-limit-validation` | Improve PyMeasure validators and value maps using Programming Guide limits. | Use Programming Guide ranges. | Section 13, row 56 |
| `1008` | Cannot Send Sync Pulse | `internal-unknown` | Drain error queue, record state, and require manual review if repeated. | Require manual review. | Section 13, row 57 |
| `1009` | Writing PCA serial number failed | `interface-communication` | Check VISA resource, interface setup, EOL, timeout, and selected remote interface. | Verify hardware connection. | Section 13, row 58 |
| `1201` | Feature not available | `feature-unavailable` | Gate API by model/option/firmware and skip unsupported tests. | Check model/option before API. | Section 13, row 59 |
| `1202` | FAILED SELF-TEST [VALUE] - USE THE POWER BUTTON TO TURN THE INSTRUMENT OFF AND BACK ON] | `self-test-diagnostic` | Do not use in broad tests; may be long-running or require operator action. | Do not run automatically. | Section 13, row 60 |
| `1203` | Command presently unavailable (in response to TRG command when in some scope functions) | `internal-unknown` | Drain error queue, record state, and require manual review if repeated. | Require manual review. | Section 13, row 61 |
| `1300` | Cannot change the LAN settings now | `interface-communication` | Check VISA resource, interface setup, EOL, timeout, and selected remote interface. | Verify network configuration. | Section 13, row 62 |
| `1500`-`1519` | Various internal/USB/storage errors | `internal-unknown` / `persistent-storage` / `interface-communication` | Drain error queue, record state, and require manual review if repeated. | Require manual review. | Section 13, rows 63-78 |
| `1600`-`1601` | Invalid Time/Date settings | `syntax-parameter` | Avoid changing persistent time/date unless explicitly scoped. | Do not automate. | Section 13, rows 79-80 |
| `1700` | Cannot communicate with 52120 | `52120a-amplifier` | Requires external 52120A fixture; skip unless explicitly configured. | Skip unless 52120A connected. | Section 13, row 81 |
| `4001`-`4008` | Overvoltage/Overcurrent protection faults | `output-protection` | Immediately put instrument in safe final state; inspect wiring/load before retry. | Fail fast, safe state. | Section 13, rows 82-89 |
| `4009` | Scope Option PLL unlocked | `restricted-security` | Do not automate broadly; requires explicit operator/security decision. | Protocol-only. | Section 13, row 90 |
| `4100`-`4105` | Compliance/exceeding faults | `output-protection` / `range-limit-validation` | Immediately put instrument in safe final state; inspect wiring/load before retry. | Fail fast, safe state. | Section 13, rows 91-95 |
| `4200`-`4202` | Monitoring faults | `output-protection` / `internal-unknown` | Immediately put instrument in safe final state; inspect wiring/load before retry. | Fail fast, safe state. | Section 13, rows 96-98 |
| `4300`-`4305` | Zero Cal failures | `zero-adjustment` | Treat as explicit operator-confirmed maintenance/metrology procedure. | Protocol-only/operator-confirmed-only. | Section 13, rows 99-104 |
| `4404` | UNKNOWN HARDWARE FAULT | `self-test-diagnostic` | Do not use in broad tests; may be long-running or require operator action. | Do not run automatically. | Section 13, row 105 |
| `4405` | Integrator limit exceeded | `range-limit-validation` | Improve PyMeasure validators and value maps using Programming Guide limits. | Use Programming Guide ranges. | Section 13, row 106 |
| `4500`-`4509` | 52120/USB/LAN communication errors | `interface-communication` / `52120a-amplifier` | Check VISA resource, interface setup, EOL, timeout, and selected remote interface. | Verify connections. | Section 13, rows 107-115 |
| `5000`-`5010` | 52120A-related errors | `persistent-storage` / `52120a-amplifier` | Requires external 52120A fixture; skip unless explicitly configured. | Skip unless 52120A connected. | Section 13, rows 116-125 |
| `6001`-`6007` | Calibration constant errors | `internal-unknown` / `zero-adjustment` | Drain error queue, record state, and require manual review if repeated. | Require manual review. | Section 13, rows 126-132 |
| `7001`-`7029` | Range/frequency/command errors | `range-limit-validation` / `internal-unknown` | Improve PyMeasure validators and value maps using Programming Guide limits. | Use Programming Guide ranges. | Section 13, rows 133-151 |
| `7500`-`7545` | Function-specific range/command errors | `range-limit-validation` / `feature-unavailable` / `internal-unknown` | Improve PyMeasure validators and value maps using Programming Guide limits. | Use Programming Guide ranges. | Section 13, rows 152-188 |
| `7546`-`7602` | Additional function-specific errors | `range-limit-validation` / `output-protection` / `52120a-amplifier` | Improve PyMeasure validators and value maps using Programming Guide limits. | Use Programming Guide ranges. | Section 13, rows 189-207 |
| `8001`-`8013` | Warm-up and zero adjustment timing errors | `zero-adjustment` | Treat as explicit operator-confirmed maintenance/metrology procedure. | Protocol-only/operator-confirmed-only. | Section 13, rows 208-220 |
| `8101`-`8111` | Polynomial fit and matrix errors | `internal-unknown` / `syntax-parameter` | Drain error queue, record state, and require manual review if repeated. | Require manual review. | Section 13, rows 221-231 |
| `8201`-`8203` | USB stick read/write errors | `interface-communication` | Check VISA resource, interface setup, EOL, timeout, and selected remote interface. | Verify USB stick. | Section 13, rows 232-234 |
| `10001`-`10301` | JSON/RPC/serialization errors | `interface-communication` / `syntax-parameter` | Check VISA resource, interface setup, EOL, timeout, and selected remote interface. | Verify interface. | Section 13, rows 235-237 |
| `11001`-`11007` | Memory/passcode errors | `persistent-storage` / `restricted-security` | Avoid in generic hardware tests; may change nonvolatile state or depend on USB/storage. | Do not use in automated tests. | Section 13, rows 238-244 |
| `65535` | Unknown Error | `internal-unknown` | Drain error queue, record state, and require manual review if repeated. | Require manual review. | Section 13, row 245 |
| `65536` | Default Error | `self-test-diagnostic` | Do not use in broad tests; may be long-running or require operator action. | Do not run automatically. | Section 13, row 246 |

# HARDWARE-TEST POLICY

| Test type | Allowed automatically? | Required preconditions | Required final state | Policy | Notes |
|---|---|---|---|---|---|
| Identity query | yes | Valid VISA address and remote interface configured | No state change | `query-only` | Use Programming Guide syntax, likely `*IDN?`. |
| Options query | yes | Valid VISA address | No state change | `query-only` | Use Programming Guide syntax. |
| Error queue query | yes | Valid VISA address | Queue drained or reported | `query-only` | Use Programming Guide error-query commands. |
| Remote port readback | cautious | Interface remains stable | No disruptive changes | `operator-confirmed-only` | Avoid changing port while connected. |
| Output configuration while standby | maybe | Operator confirms no DUT risk and output remains inactive | Standby | `output-off-only`; do not activate terminals. | |
| Low-voltage output | no broad auto-test | Load/DUT specified, operator confirms wiring | Standby/reset | `operator-confirmed-only` | Even low voltage can damage sensitive DUTs. |
| High-voltage output | no | Fixture, insulation, load, operator confirmation | Standby/reset | `operator-confirmed-only` | Hazard threshold >30 Vrms or 42 V peak. |
| High-current output | no | Correct terminal, load/shunt, current rating, operator confirmation | Standby/reset | `operator-confirmed-only` | Current output above 3.1 A uses 30A terminal. |
| Simulated power | no | Power-meter fixture and operator-confirmed procedure | Standby/reset | `never` for broad tests | Not available on 5540A; hazardous output. |
| Resistance/capacitance/inductance output | no broad auto-test | DUT fixture and compensation/wiring declared | Standby/reset | `operator-confirmed-only` | Inductance unavailable on 5540A/5530A. |
| RTD/TC output | no broad auto-test | Correct wire/type/reference junction | Standby/reset | `operator-confirmed-only` | Physical temperature setup matters. |
| TC measurement | no broad auto-test | TC fixture stable and type selected | No hazardous output | `operator-confirmed-only` | Open TC Detect may affect parallel measurements. |
| 52120A amplifier operation | no | External amplifier connected and configured | Standby/reset, amplifier safe | `operator-confirmed-only` | Up to three 52120A units; high-current risk. |
| Scope outputs | no broad auto-test | Scope option present, scope fixture connected | Standby/reset | `operator-confirmed-only` | Option dependent. |
| Scope overload tests | never broad auto-test | Explicit oscilloscope power-rating verification | Standby/reset | `never` | Can damage oscilloscope. |
| Calibration security | no | Authorized metrology/service procedure | Secured state | `protocol-only` / `never` | Passcode risk. |
| Zero adjustment | no broad auto-test | Warm-up complete, metrology procedure expected | Standby | `protocol-only` / `operator-confirmed-only` | Long-running/state-changing. |
| Restore defaults | no | Explicit operator/service decision | Known configured state | `never` | Can alter persistent settings or calibration constants. |
| Firmware update | no | Manual maintenance process | N/A | `never` | Not a PyMeasure driver feature. |

# COMMAND-LIKE REFERENCES REQUIRING PROGRAMMING GUIDE CONFIRMATION

These are tokens or command-like references encountered in the Operators Manual or needed as cross-references for later PyMeasure planning. Do not treat this section as command inventory.

| Token | Operators Manual context | Found in Programming Guide? | Decision | Notes |
|---|---|---|---|---|
| `CAL_SECURE` | mentioned literally in Operators Manual | yes | `confirmed-by-programming-guide` | Do not use Operators Manual as the syntax authority. |
| `CAL_PASSCODE` | mentioned literally in Operators Manual | yes | `confirmed-by-programming-guide` | Do not use Operators Manual as the syntax authority. |
| `*IDN?` | mentioned literally in Operators Manual | yes | `confirmed-by-programming-guide` | Do not use Operators Manual as the syntax authority. |
| `TRG` | mentioned literally in Operators Manual | yes | `confirmed-by-programming-guide` | Do not use Operators Manual as the syntax authority. |
| `*TRG` | mentioned literally in Operators Manual | yes | `confirmed-by-programming-guide` | Do not use Operators Manual as the syntax authority. |
| `OUT_IMP` | mentioned literally in Operators Manual | yes | `confirmed-by-programming-guide` | Do not use Operators Manual as the syntax authority. |
| `STBY` | operator concept or later safe-state/error-handling candidate; not literal in Operators Manual | yes | `confirmed-by-programming-guide` | Do not use Operators Manual as the syntax authority. |
| `OPER` | mentioned literally in Operators Manual | yes | `confirmed-by-programming-guide` | Do not use Operators Manual as the syntax authority. |
| `OUT` | mentioned literally in Operators Manual | yes | `confirmed-by-programming-guide` | Do not use Operators Manual as the syntax authority. |
| `ERR?` | operator concept or later safe-state/error-handling candidate; not literal in Operators Manual | yes | `confirmed-by-programming-guide` | Do not use Operators Manual as the syntax authority. |
| `FAULT?` | operator concept or later safe-state/error-handling candidate; not literal in Operators Manual | yes | `confirmed-by-programming-guide` | Do not use Operators Manual as the syntax authority. |
| `EXPLAIN?` | operator concept or later safe-state/error-handling candidate; not literal in Operators Manual | yes | `confirmed-by-programming-guide` | Do not use Operators Manual as the syntax authority. |

# PYMEASURE DESIGN IMPLICATIONS

- The instrument family supports IEEE-488.2 style remote control and SCPI/common-command behavior through the programming manual, so a future driver should likely use `SCPIMixin, Instrument` if the Programming Guide confirms the common command set.
- Do not use `includeSCPI=True`.
- Do not create `get_*` or `set_*` methods.
- Keep output configuration separate from output activation.
- Treat `OPER`/Operate behavior as hazardous and `operator-confirmed-only` for real hardware tests.
- Treat `STBY`/Standby as safe-final-state candidate if confirmed in the Programming Guide.
- Use `Instrument.control` only after command/query form, parameter values, validators, and mappings are verified in the Programming Guide.
- Use `Instrument.measurement` or explicit read methods for query-only status/identity/error responses.
- Use explicit methods for command-only actions, especially reset, standby, operate, zero, diagnostics, and self-test.
- Use model/option detection before exposing dual-output, inductance, 52120A, and scope-option behavior.
- High-risk commands should be protocol-tested only or operator-confirmed.
- Hardware tests must skip without a VISA address.
- Hardware tests must leave source/output disabled or in standby and must query the documented error queue afterward.

# DO-NOT-INFER LIST

- Do not infer command syntax from front-panel labels or procedure names.
- Do not infer query forms from natural-language descriptions.
- Do not infer output safety from low-level command names.
- Do not infer that a physical setup is safe without documented wiring and load.
- Do not infer model/option availability from one family member to another.
- Do not infer that service/calibration procedures are operator-safe.
- Do not treat command-like references as implemented API.

# OCR_AND_CONVERSION_NOTES

The source Markdown appears converted from a PDF and contains visible formatting artifacts: split table rows, repeated headings, page labels, broken special symbols, and front-panel key names represented as isolated characters. Critical values must be checked against the official manual before use in metrology, calibration, safety-critical code, or final PyMeasure documentation.

No obvious OCR artifacts detected in reviewed sections.
Some sections may still require verification during later prompts.
Safety-critical values must be checked against the official manual before real hardware tests.

# STEP 04 AND STEP 05 HANDOFF CHECKLIST

- Step 04 must use Service Manual for service/calibration-risk only.
- Step 04 must not infer operator-safe behavior from service procedures.
- Step 05 must use Programming Guide, not Operator Manual, for command inventory.
- Step 05 may use this file only for risk hints and hardware-test policy.
- Command-like references from this file must remain cross-references until confirmed.
