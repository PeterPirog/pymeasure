---
title: "Fluke 5560A/5550A/5540A/5530A Operators Manual — LLM/PyMeasure optimized"
source_file: "Operators_manual_5560A.md"
source_manual: "5560A/5550A/5540A/5530A Calibrator Operators Manual"
source_revision: "August 2022 Rev. 3, 3/25"
vendor: "fluke"
model: "5560A"
instrument_family: ["Fluke 5560A", "Fluke 5550A", "Fluke 5540A", "Fluke 5530A"]
instrument_type: "multifunction precision calibrator / precision source calibrator"
optimized_for: ["LLM retrieval", "GPT Codex", "PyMeasure driver planning", "safe hardware tests", "operator workflow"]
generated_on: "2026-05-06"
local_artifact: true
upstream_pr: false
---

# Fluke 5560A/5550A/5540A/5530A Operators Manual — LLM/PyMeasure optimized

## 0. LLM_AGENT_CONTRACT

Use this file as an operator-level, safety, fixture, remote-port, model-option, and hardware-test policy reference for PyMeasure driver planning.

Mandatory rules for LLM/Codex agents:

1. Treat the calibrator as safety-critical hardware.
2. Do **not** enable output automatically in generated hardware tests.
3. Do **not** tell an operator to connect or disconnect DUT leads while output may be active.
4. Do **not** treat front-panel procedures as remote commands.
5. Do **not** invent SCPI or remote command syntax from the Operators Manual.
6. Use the Remote Programmers Manual / Programming Guide as the authoritative source for command syntax.
7. Use this Operators Manual for safety, operator workflows, fixture requirements, model/option constraints, warm-up, remote-port setup, and error interpretation.
8. Use the Service Manual for service/calibration-risk boundaries and qualified-service-only procedures.
9. Mark OCR/conversion ambiguity as `needs-verification` before using it in code, metrology, or safety-critical procedures.

## 1. Document role in the PyMeasure workflow

| Source | Use for PyMeasure | Do not use for |
|---|---|---|
| Operators Manual | Operator safety, user workflows, DUT connections, remote-port setup, safe hardware-test policy, model/option constraints, error-code meaning. | Full remote-command inventory or exact command syntax. |
| Programming Guide | Remote command syntax, parameters, responses, status registers, command/query forms, and error-query commands. | Physical fixture instructions unless stated there. |
| Service Manual | Service risk, calibration/adjustment risk, internal-service boundaries, verification prerequisites. | Inventing remote commands or routine operator procedures. |

## 2. Quick facts for retrieval

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

## 3. Output capability summary

| Function area | Capability / limitation | PyMeasure implication |
|---|---|---|
| DC voltage | 0 V to ±1020 V | Hazardous output; never enable automatically in broad hardware tests. |
| DC current | 0 A to ±30.2 A | Hazardous output; fixture/load dependent. |
| AC voltage | 1 mV to 1020 V | Hazardous output; RMS representation for non-scope sine wave functions. |
| AC current | 10 µA to 30.2 A | Hazardous output; current terminal/range matters. |
| AC waveforms | Sine wave and square wave | Waveform affects RMS vs p-p representation and offset/duty behavior. |
| Resistance | Short circuit to 1200 MΩ | Synthetic impedance; wiring and compensation matter. |
| Capacitance | 220 pF to 120 mF | Synthetic impedance; fixture and lead effects matter. |
| Inductance | 12 µH to 120 H | Not available on 5540A and 5530A. |
| RTD simulation | 10 RTD types | Type and temperature scale dependent. |
| Thermocouple simulation | 17 thermocouple types | Requires matching TC wire/connectors and reference-junction handling. |
| Simulated power | Up to 30.9 kW | Not available on 5540A; operator-confirmed only. |
| Scope options | Scope calibration functions when option installed | Option-gated APIs and hardware tests. |

## 4. Safety summary for driver and hardware-test planning

| Topic | Risk | PyMeasure implication | Hardware-test policy |
|---|---|---|---|
| Operate mode | Terminals can carry hazardous voltage/current. | Keep output activation as explicit methods or tightly controlled APIs; never enable by side effect. | `operator-confirmed-only` |
| Standby mode | Output value is inactive at selected terminals, but accidental Operate is still possible. | Use as final state but do not rely on it as permission to rewire without operator verification. | `roundtrip-safe` for final-state checks |
| Reset / abort-to-default | Returns to 0 mV dc, Standby, 120 mV range. | Useful as safe recovery state if Programming Guide exposes a remote equivalent. | `roundtrip-safe` or `protocol-only` depending command |
| DUT connection changes | Manual warns not to connect/disconnect with voltage present. | Hardware tests must not require wiring changes while test is running. | `operator-confirmed-only` |
| High voltage | Hazardous voltage indicator for >30 Vrms or 42 V peak. | Add explicit safety gates for any output above these thresholds. | `operator-confirmed-only` |
| High current | VI AUX and 30A terminal selection depends on current level. | Current output tests need fixture/load and terminal-policy notes. | `operator-confirmed-only` |
| Simulated power | Up to 30.9 kW, not available on 5540A. | Do not run automatically; model-gate API. | `never` for broad tests |
| Guard/earth | Only one earth-to-LO tie point should exist; external guard changes internal guard connection. | Do not auto-change guard in broad hardware tests without fixture declaration. | `operator-confirmed-only` |
| Calibration passcode | Protects NVM calibration constants and clock/date changes. | Do not expose as routine workflow; protocol-test only unless explicitly scoped. | `protocol-only` / `never` |
| Restore default calibration | Deletes calibration constants and requires full calibration. | Do not implement/run without explicit project decision. | `never` |
| Firmware update | Uses USB host / maintenance workflow. | Not part of normal PyMeasure driver. | `never` |
| Covers/fuses/repair | Covers removed exposes hazardous voltages; service by approved technician. | Do not generate repair procedures as normal test guidance. | `never` |

## 5. Remote operation and interface summary

### IEEE-488/GPIB

- The rear-panel GPIB port is a fully programmable parallel interface bus.
- It meets IEEE-488.1 and supplemental IEEE-488.2 behavior.
- Under controller control, the product operates as a talker/listener.
- The Operators Manual refers to the Remote Programmers Manual for the command set.
- Product defaults list GPIB enabled as true and GPIB address as `4`.

### RS-232

- The rear-panel RS-232 port is used for serial remote control.
- Product defaults list RS-232 enabled as true.
- Product defaults list baud rate `9600`, data bits `8`, stop bits `1`, parity `none`, flow control `XON/XOFF`, EOL `CR/LF`, and interface `Terminal`.
- Remote-port setup options include data bits 8/7, stop bits 1/2, flow control None/RTS-CTS/XON-XOFF, parity None/Even/Odd, baud rates 9600/19200/38400/57600/115200, EOL CR/LF/CR/LF, and Terminal/Computer mode.

### USBTMC

- The rear-panel USB 2.0 type B port is a programmable USBTMC interface meeting USBTMC-USB488 and supplemental IEEE-488.2 behavior.
- The Operators Manual gives the VISA resource pattern: `USB0::0x0F7E::0x800A::[serial number]::INSTR`.
- Vendor ID: `0x0F7E`.
- Product ID: `0x800A`.
- USBTMC is enabled by default.

### Ethernet / Telnet

- The rear-panel 10/100/1000BASE-T Ethernet port supports remote control.
- The Operators Manual describes command entry from a telnet session.
- Product defaults list Telnet enabled as true and Telnet port `3490`.
- Product defaults list Telnet EOL `CR/LF`, interface `Terminal`, DHCP on, netmask `255.255.255.0`, and placeholder IP/MAC/gateway values.
- Remote-port setup provides DHCP, static IP, gateway, subnet mask, current IP, gateway, MAC address, port, EOL, remote interface mode, network-security address range, and restore defaults.

## 6. Remote port setup facts

| Interface | Setting | Values/defaults from Operators Manual | PyMeasure implication | Notes |
|---|---|---|---|---|
| USBTMC | VISA resource | `USB0::0x0F7E::0x800A::[serial number]::INSTR` | Useful for examples and hardware test docs. | Serial number can be obtained from rear panel, Setup > About, or `*IDN?` through another interface. |
| USBTMC | Enabled default | true | Hardware tests can use VISA USBTMC if available. | Use Programming Guide for exact command behavior. |
| GPIB | Address | default `4` | Hardware tests should accept `--device-address`; do not hard-code. | Some lab setups may differ. |
| GPIB | Enabled default | true | Supports standard PyVISA usage. | IEEE-488.1/488.2 context supports likely `SCPIMixin`. |
| RS-232 | Baud rates | 9600, 19200, 38400, 57600, 115200 | Add connection examples only; no fixed default in driver unless aligned with repo style. | Default: 9600. |
| RS-232 | Data bits | 8 or 7 | User-overridable connection settings. | Default: 8. |
| RS-232 | Stop bits | 1 or 2 | User-overridable connection settings. | Default: 1. |
| RS-232 | Flow control | None, RTS/CTS, XON/XOFF | User-overridable connection settings. | Default: XON/XOFF. |
| RS-232 | Parity | None, Even, Odd | User-overridable connection settings. | Default: none. |
| RS-232 | EOL | CR/LF, CR, LF | Hardware tests must use configured terminator. | Default: CR/LF. |
| Ethernet/Telnet | Port | default `3490` | TCPIP/Telnet examples can use this port. | Confirm with actual instrument setup. |
| Ethernet/Telnet | EOL | CR/LF, CR, LF | Hardware tests must match configured EOL. | Default: CR/LF. |
| Ethernet/Telnet | DHCP/static | DHCP On by default; static IP fields available | Do not assume IP; user supplies VISA/TCP address. | Security address range exists. |

## 7. Operate / Standby / Reset behavior

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

## 8. DUT connection and fixture constraints

| Function area | Required physical setup | Risk | Hardware-test policy | Notes |
|---|---|---|---|---|
| Voltage output | OUTPUT HI/LO, optional sense terminals | Hazardous voltage at high levels | `operator-confirmed-only` | External sense only for specified ranges/functions. |
| Current ≤3.1 A | VI AUX and OUTPUT LO / Sense LO depending function | High current, wiring and terminal selection risk | `operator-confirmed-only` | Terminal choice affects safe setup. |
| Current >3.1 A | 30A terminal and OUTPUT/SENSE LO | High current | `operator-confirmed-only` | Requires appropriate load/shunt and cables. |
| Resistance | OUTPUT terminals, compensation setting | Synthetic impedance; wiring polarity matters | `operator-confirmed-only` | 2-wire/4-wire/Comp OFF must match DUT. |
| Capacitance | OUTPUT terminals; stray capacitance nulling may be needed | Fixture-dependent | `operator-confirmed-only` | Do not auto-test without fixture. |
| Inductance | OUTPUT terminals; not 5540A/5530A | Fixture-dependent, option/model dependent | `operator-confirmed-only` | Model-gate before API/tests. |
| RTD source | Three-terminal connection recommended for RTD meters | Lead-resistance errors | `operator-confirmed-only` | Identical lead resistances may be required. |
| TC source | TC connector with matching thermocouple wire/connectors | Thermal EMF / incorrect TC type | `operator-confirmed-only` | Avoid heating connector with fingers. |
| TC measure | TC connector and reference-junction handling | Measurement validity depends on physical setup | `operator-confirmed-only` | Open TC Detect can affect parallel measurements. |
| Guard/Earth | Single ground tie point; external guard for grounded DUT LO | Ground loops, safety ground errors | `operator-confirmed-only` | Do not defeat protective earth. |
| Scope outputs | SCOPE OUT and TRIG connectors when option installed | Option-dependent output | `operator-confirmed-only` | Scope options must be installed and detected. |
| Overload tests | 50 Ω oscilloscope input and power-rating confirmation | Can damage DUT | `never` for broad tests | Operator-confirmed fixture only. |

## 9. Output function map for PyMeasure planning

| Function group | Operator function | Availability | Main risks | PyMeasure planning note |
|---|---|---|---|---|
| Single Output | DCV | All models | Up to ±1020 V | Configure value while standby; activation separate. |
| Single Output | ACV | All models | Up to 1020 V, frequency/waveform/offset constraints | Needs waveform, frequency, offset, duty-cycle modeling. |
| Single Output | DCI | All models | Up to ±30.2 A, terminal change at high current | Terminal/range constraints; external load required. |
| Single Output | ACI | All models | Up to 30.2 A, waveform/coil/52120A options | Fixture-dependent. |
| Single Output | Resistance | All models | Synthetic impedance and wiring compensation | Model compensation settings carefully. |
| Single Output | Capacitance | All models | Stray capacitance and fixture dependency | Parser not likely, but test policy strict. |
| Single Output | Inductance | 5560A/5550A only | Not available on 5540A/5530A | Model-gate API and tests. |
| Single Output | RTD Source | All models | RTD type and temperature-scale constraints | Values depend on selected RTD type. |
| Single Output | TC Source | All models | TC wire and reference-junction constraints | Type, scale, offset, RJ handling. |
| Measure | TC Measure | All models | Physical temperature/TC setup | Query/measurement candidates only if Programming Guide confirms. |
| Dual Output | DC Power | Not available on 5540A | Voltage + current simultaneous output | Operator-confirmed only. |
| Dual Output | AC Power | Not available on 5540A | Simulated power and phase/DPF | Operator-confirmed only. |
| Dual Output | DCV DCV | Not available on 5540A | Dual voltage; AUX limits | Model-gate and terminal notes. |
| Dual Output | ACV ACV | Not available on 5540A | Dual waveform/phase; AUX limits | Model-gate and waveform constraints. |
| Scope | Scope DCV | Scope option required | Scope output, 50 Ω/1 MΩ impedance | Option-gated. |
| Scope | Scope ACV | Scope option required | Scope waveform/trigger/impedance | Option-gated. |
| Scope | Edge | Scope option required | Pulse response output | Operator-confirmed only. |
| Scope | Leveled Sine | Scope option required | Bandwidth test signal | Operator-confirmed only. |
| Scope | Marker | Scope option required | Timing marker output | Option/waveform-frequency dependent. |
| Scope | Waveform Generator | Scope option required | Signal generator output | Do not use for oscilloscope level/bandwidth accuracy checks. |
| Scope | Video | Scope option required | Video trigger output | Format/field constraints. |
| Scope | Pulse | Scope option required | Pulse amplitude/period constraints | Option-gated. |
| Scope | Measure Resistance | Scope option required | Automatically enters Operate | Never broad auto-test. |
| Scope | Measure Capacitance | Scope option required | Automatically enters Operate | Never broad auto-test. |
| Scope | Overload DC | Scope option required | Applies power into 50 Ω input | Never broad auto-test. |
| Scope | Overload AC | Scope option required | Applies AC power into 50 Ω input | Never broad auto-test. |

## 10. Model and option dependencies

| Model or option | Feature impact | PyMeasure implication | Hardware-test implication | Source context |
|---|---|---|---|---|
| 5560A | Full family capability in examples unless otherwise noted | Main target class; can share family driver if model checks added | Still require option detection for scope/52120A | Operators Manual family scope |
| 5550A | Same family; some option differences possible | Consider family parameterization | Check `*IDN?` and options before tests | Operators Manual family scope |
| 5540A | Dual output and simulated power not available; inductance not available | Gate dual-output, power, and inductance APIs | Skip unsupported hardware tests | Function menu notes and output capability notes |
| 5530A | Inductance not available; family capability subset | Gate inductance API | Skip unsupported hardware tests | Output capability notes |
| 52120A amplifier | Extends current output; up to three amplifiers, high-current use | Separate feature flag / external-fixture API | Operator-confirmed only | 52120A section |
| Scope options | Scope menu active only when installed | Option-gated subsystem | Skip if option absent | Scope options section |
| 600M option | 600 MHz oscilloscope calibration option available for 5560A/5550A/5540A | Option detection needed | Operator-confirmed only | Options/accessories section |
| 1G option | 1.1 GHz option available for 5560A/5550A | Option detection needed | Operator-confirmed only | Options/accessories section |
| 2G option | 2.2 GHz option for 5560A | Option detection needed | Operator-confirmed only | Options/accessories section |

## 11. Warm-up, zeroing, and metrology prerequisites

| Requirement | Condition | Driver implication | Hardware-test policy |
|---|---|---|---|
| Warm-up after power-on | At least 30 minutes | Hardware tests that assert metrology behavior should report warm-up state or skip unless operator confirms. | `operator-confirmed-only` |
| Warm-up after power cycling | At least twice the off-time, max 30 minutes | Do not assume immediate metrology-grade operation after reconnect. | `operator-confirmed-only` |
| Zero adjustment | Required every 14 days or after ambient temperature changes by more than 5 °C | Do not run automatically; provide explicit method only if Programming Guide confirms command. | `protocol-only` / `operator-confirmed-only` |
| Specifications | UI can display specification information if enabled | Documentation note; not driver validation unless ranges from Programming Guide are confirmed. | `query-only` if readback exists |
| Ohms zero / impedance zero | Mentioned through setup/calibration context | Treat as maintenance/metrology procedure. | `operator-confirmed-only` |

## 12. Calibration security and persistent settings

| Topic | Risk | Remote-command reference? | PyMeasure implication | Hardware-test policy |
|---|---|---|---|---|
| Calibration security passcode | Protects calibration constants and date/time changes | `CAL_SECURE` mentioned; confirm syntax in Programming Guide | Do not expose as ordinary workflow | `protocol-only` / `never` |
| Calibration passcode change | Losing passcode requires Fluke service | `CAL_PASSCODE` mentioned; confirm syntax in Programming Guide | Do not automate in tests | `never` |
| Restore default calibration | Deletes calibration constants; full calibration required afterward | Front-panel menu topic, not command syntax | Do not implement/run without explicit project decision | `never` |
| Restore default setup/factory defaults | Persistent setup changes | front-panel menu topic | Avoid in hardware tests | `never` |
| Output limits | Saved in nonvolatile memory | command syntax from Programming Guide only | Hardware tests should not alter persistent limits broadly | `protocol-only` unless explicitly scoped |
| Date/time changes | Product must be unlocked | command syntax from Programming Guide only | Avoid in generic driver tests | `never` |
| Report string / PUD string | Persistent data | command syntax from Programming Guide only | Avoid in broad tests | `protocol-only` |

## 13. Error-code knowledge base

| Code | Message | Category | PyMeasure implication |
|---|---|---|---|
| `0` | No error | `no-error` | Normal end-of-queue / no fault condition. |
| `-440` | 488.2 query after indefinite response | `ieee-488-protocol` | Check query sequencing, reads after queries, and interface-specific timing. |
| `-430` | 488.2 I/O deadlock | `ieee-488-protocol` | Check query sequencing, reads after queries, and interface-specific timing. |
| `-420` | 488.2 unterminated command | `ieee-488-protocol` | Check query sequencing, reads after queries, and interface-specific timing. |
| `-410` | 488.2 interrupted query | `ieee-488-protocol` | Check query sequencing, reads after queries, and interface-specific timing. |
| `-377` | LAN address: port combination unavailable, choose another address or port | `interface-communication` | Check VISA resource, interface setup, EOL, timeout, and selected remote interface. |
| `-376` | Command only allowed on synchronous (for example, gpib/usb-tmc) interface type | `interface-communication` | Check VISA resource, interface setup, EOL, timeout, and selected remote interface. |
| `-375` | Command only allowed on asynchronous (for example, serial/telnet) interface type | `interface-communication` | Check VISA resource, interface setup, EOL, timeout, and selected remote interface. |
| `-374` | GPIB/488.1 unspecified error | `ieee-488-protocol` | Check query sequencing, reads after queries, and interface-specific timing. |
| `-373` | GPIB/488.1 write operation timeout | `ieee-488-protocol` | Check query sequencing, reads after queries, and interface-specific timing. |
| `-372` | GPIB/488.1 read/write operation aborted | `ieee-488-protocol` | Check query sequencing, reads after queries, and interface-specific timing. |
| `-371` | GPIB/488.1 board address error | `ieee-488-protocol` | Check query sequencing, reads after queries, and interface-specific timing. |
| `-370` | GPIB/488.1 system call has failed | `ieee-488-protocol` | Check query sequencing, reads after queries, and interface-specific timing. |
| `-369` | LAN port encountered error while reading data | `interface-communication` | Check VISA resource, interface setup, EOL, timeout, and selected remote interface. |
| `-368` | Fatal error occurred while accessing the LAN port | `interface-communication` | Check VISA resource, interface setup, EOL, timeout, and selected remote interface. |
| `-367` | USB-TMC encountered error while reading data | `interface-communication` | Check VISA resource, interface setup, EOL, timeout, and selected remote interface. |
| `-366` | GPIB/488.1 encountered error while reading data | `ieee-488-protocol` | Check query sequencing, reads after queries, and interface-specific timing. |
| `-365` | Fatal error occurred while accessing the serial port | `interface-communication` | Check VISA resource, interface setup, EOL, timeout, and selected remote interface. |
| `-363` | Input Buffer Overrun | `syntax-parameter` | Check command spelling, parameter count, units, type conversion, validator, and mapping. |
| `-361` | RS-232 framing/parity/overrun error detected | `interface-communication` | Check VISA resource, interface setup, EOL, timeout, and selected remote interface. |
| `-350` | Too many errors | `syntax-parameter` | Check command spelling, parameter count, units, type conversion, validator, and mapping. |
| `-302` | Command execution locked out | `syntax-parameter` | Check command spelling, parameter count, units, type conversion, validator, and mapping. |
| `-301` | Restricted Command | `syntax-parameter` | Check command spelling, parameter count, units, type conversion, validator, and mapping. |
| `-224` | Characters must be A-Z, 0-9, - or _ | `syntax-parameter` | Check command spelling, parameter count, units, type conversion, validator, and mapping. |
| `-223` | Character string was more than limit | `syntax-parameter` | Check command spelling, parameter count, units, type conversion, validator, and mapping. |
| `-222` | Illegal data value was entered | `syntax-parameter` | Check command spelling, parameter count, units, type conversion, validator, and mapping. |
| `-193` | No entry in list to retrieve | `syntax-parameter` | Check command spelling, parameter count, units, type conversion, validator, and mapping. |
| `-192` | Too many dimensions to be returned | `syntax-parameter` | Check command spelling, parameter count, units, type conversion, validator, and mapping. |
| `-191` | Parameter type detection error | `syntax-parameter` | Check command spelling, parameter count, units, type conversion, validator, and mapping. |
| `-190` | Parameter is not a boolean type | `syntax-parameter` | Check command spelling, parameter count, units, type conversion, validator, and mapping. |
| `-157` | Unmatched bracket | `syntax-parameter` | Check command spelling, parameter count, units, type conversion, validator, and mapping. |
| `-154` | String size is beyond limit | `syntax-parameter` | Check command spelling, parameter count, units, type conversion, validator, and mapping. |
| `-153` | Parameter is not an unquoted string type | `syntax-parameter` | Check command spelling, parameter count, units, type conversion, validator, and mapping. |
| `-152` | Parameter is not an quoted string type | `syntax-parameter` | Check command spelling, parameter count, units, type conversion, validator, and mapping. |
| `-150` | Invalid string data | `syntax-parameter` | Check command spelling, parameter count, units, type conversion, validator, and mapping. |
| `-140` | Parameter is not a character type | `syntax-parameter` | Check command spelling, parameter count, units, type conversion, validator, and mapping. |
| `-138` | Too many suffixes in command header | `syntax-parameter` | Check command spelling, parameter count, units, type conversion, validator, and mapping. |
| `-137` | Invalid suffix in command header | `syntax-parameter` | Check command spelling, parameter count, units, type conversion, validator, and mapping. |
| `-130` | Suffix Error. Wrong units for parameter | `syntax-parameter` | Check command spelling, parameter count, units, type conversion, validator, and mapping. |
| `-127` | Invalid dimensions in a channel list | `syntax-parameter` | Check command spelling, parameter count, units, type conversion, validator, and mapping. |
| `-126` | Numeric value is real | `syntax-parameter` | Check command spelling, parameter count, units, type conversion, validator, and mapping. |
| `-125` | Numeric value is negative | `syntax-parameter` | Check command spelling, parameter count, units, type conversion, validator, and mapping. |
| `-124` | Numeric value overflowed its storage | `syntax-parameter` | Check command spelling, parameter count, units, type conversion, validator, and mapping. |
| `-122` | Parameter is not a numeric type | `syntax-parameter` | Check command spelling, parameter count, units, type conversion, validator, and mapping. |
| `-120` | Numeric value is invalid | `syntax-parameter` | Check command spelling, parameter count, units, type conversion, validator, and mapping. |
| `-117` | Wrong type of parameter(s) | `syntax-parameter` | Check command spelling, parameter count, units, type conversion, validator, and mapping. |
| `-115` | Missing or wrong number of parameters | `syntax-parameter` | Check command spelling, parameter count, units, type conversion, validator, and mapping. |
| `-102` | Syntax error | `syntax-parameter` | Check command spelling, parameter count, units, type conversion, validator, and mapping. |
| `1000` | Illegal Parameter | `syntax-parameter` | Check command spelling, parameter count, units, type conversion, validator, and mapping. |
| `1001` | Failed to save data to non-volatile storage | `persistent-storage` | Avoid in generic hardware tests; may change nonvolatile state or depend on USB/storage. |
| `1002` | Failed to read data from non-volatile storage | `persistent-storage` | Avoid in generic hardware tests; may change nonvolatile state or depend on USB/storage. |
| `1003` | Remote Port Configuration Invalid | `interface-communication` | Check VISA resource, interface setup, EOL, timeout, and selected remote interface. |
| `1004` | Units Must Be The Same | `internal-unknown` | Drain error queue, record state, and require manual review if repeated. |
| `1005` | Limit Too Small or Large | `range-limit-validation` | Improve PyMeasure validators and value maps using Programming Guide limits. |
| `1006` | Cannot Get Range Data | `range-limit-validation` | Improve PyMeasure validators and value maps using Programming Guide limits. |
| `1007` | Cannot Find Range | `range-limit-validation` | Improve PyMeasure validators and value maps using Programming Guide limits. |
| `1008` | Cannot Send Sync Pulse | `internal-unknown` | Drain error queue, record state, and require manual review if repeated. |
| `1009` | Writing PCA serial number failed | `interface-communication` | Check VISA resource, interface setup, EOL, timeout, and selected remote interface. |
| `1201` | Feature not available | `feature-unavailable` | Gate API by model/option/firmware and skip unsupported tests. |
| `1202` | FAILED SELF-TEST [VALUE] - USE THE POWER BUTTON TO TURN THE INSTRUMENT OFF AND BACK ON] | `self-test-diagnostic` | Do not use in broad tests; may be long-running or require operator action. |
| `1203` | Command presently unavailable (in response to TRG command when in some scope functions [*TRG can be used in MEASR and MEASC]) | `internal-unknown` | Drain error queue, record state, and require manual review if repeated. |
| `1300` | Cannot change the LAN settings now | `interface-communication` | Check VISA resource, interface setup, EOL, timeout, and selected remote interface. |
| `1500` | Failed to set DAC to desired value | `internal-unknown` | Drain error queue, record state, and require manual review if repeated. |
| `1501` | Cannot change the monitor now | `internal-unknown` | Drain error queue, record state, and require manual review if repeated. |
| `1502` | Cannot find that cal constant | `internal-unknown` | Drain error queue, record state, and require manual review if repeated. |
| `1503` | Cannot save cal constant | `persistent-storage` | Avoid in generic hardware tests; may change nonvolatile state or depend on USB/storage. |
| `1504` | Cannot Store, Cal is Secured | `restricted-security` | Do not automate broadly; requires explicit operator/security decision. |
| `1506` | Cannot Change the Date While Instrument is Secured | `restricted-security` | Do not automate broadly; requires explicit operator/security decision. |
| `1507` | Continue command ignored | `internal-unknown` | Drain error queue, record state, and require manual review if repeated. |
| `1508` | Backup command ignored | `internal-unknown` | Drain error queue, record state, and require manual review if repeated. |
| `1509` | Cannot execute procedure backup request now | `internal-unknown` | Drain error queue, record state, and require manual review if repeated. |
| `1510` | Cannot execute procedure abort request now | `internal-unknown` | Drain error queue, record state, and require manual review if repeated. |
| `1511` | Cannot execute procedure start request now | `internal-unknown` | Drain error queue, record state, and require manual review if repeated. |
| `1512` | Cannot execute procedure step skip request now | `internal-unknown` | Drain error queue, record state, and require manual review if repeated. |
| `1513` | Cannot execute procedure section jump request now | `internal-unknown` | Drain error queue, record state, and require manual review if repeated. |
| `1514` | Cannot start diagnostics now | `self-test-diagnostic` | Do not use in broad tests; may be long-running or require operator action. |
| `1515` | Cannot Change the Temperature While Instrument is Secured | `restricted-security` | Do not automate broadly; requires explicit operator/security decision. |
| `1516` | Cannot Change the Report String While Instrument is Secured | `interface-communication` | Check VISA resource, interface setup, EOL, timeout, and selected remote interface. |
| `1517` | Cannot sync scope capacitance offset | `range-limit-validation` | Improve PyMeasure validators and value maps using Programming Guide limits. |
| `1518` | Retry command ignored | `internal-unknown` | Drain error queue, record state, and require manual review if repeated. |
| `1519` | Cannot execute retry request now | `internal-unknown` | Drain error queue, record state, and require manual review if repeated. |
| `1600` | Invalid Time or Time Setting | `syntax-parameter` | Check command spelling, parameter count, units, type conversion, validator, and mapping. |
| `1601` | Invalid Date or Date Setting | `syntax-parameter` | Check command spelling, parameter count, units, type conversion, validator, and mapping. |
| `1700` | Cannot communicate with 52120 | `52120a-amplifier` | Requires external 52120A fixture; skip unless explicitly configured. |
| `4001` | Overvoltage on the 12V amplifier | `output-protection` | Immediately put instrument in safe final state; inspect wiring/load before retry. |
| `4002` | Overvoltage on the millivolt output | `output-protection` | Immediately put instrument in safe final state; inspect wiring/load before retry. |
| `4003` | Power up, line power fault | `self-test-diagnostic` | Do not use in broad tests; may be long-running or require operator action. |
| `4004` | External clock failure | `clock-date-time` | Avoid changing persistent time/date unless explicitly scoped. |
| `4005` | Overcurrent on the 12V amplifier | `output-protection` | Immediately put instrument in safe final state; inspect wiring/load before retry. |
| `4006` | PLL unlocked, missing 10 MHz reference | `syntax-parameter` | Check command spelling, parameter count, units, type conversion, validator, and mapping. |
| `4007` | Excess output current or common mode voltage on the guard terminal | `output-protection` | Immediately put instrument in safe final state; inspect wiring/load before retry. |
| `4008` | Overvoltage or overcurrent condition | `output-protection` | Immediately put instrument in safe final state; inspect wiring/load before retry. |
| `4009` | Scope Option PLL unlocked | `restricted-security` | Do not automate broadly; requires explicit operator/security decision. |
| `4100` | Compliance voltage exceeded | `output-protection` | Immediately put instrument in safe final state; inspect wiring/load before retry. |
| `4101` | Specification exceeded | `internal-unknown` | Drain error queue, record state, and require manual review if repeated. |
| `4102` | Compliance current limit exceeded | `output-protection` | Immediately put instrument in safe final state; inspect wiring/load before retry. |
| `4103` | Output settling timed out | `output-protection` | Immediately put instrument in safe final state; inspect wiring/load before retry. |
| `4105` | Integrator limit exceeded | `range-limit-validation` | Improve PyMeasure validators and value maps using Programming Guide limits. |
| `4200` | Temperature monitoring has failed | `internal-unknown` | Drain error queue, record state, and require manual review if repeated. |
| `4201` | Compliance voltage monitoring has failed | `output-protection` | Immediately put instrument in safe final state; inspect wiring/load before retry. |
| `4202` | Compliance voltage above threshold | `output-protection` | Immediately put instrument in safe final state; inspect wiring/load before retry. |
| `4300` | Zero Cal nulling operation exceeded maximum attempts to converge | `zero-adjustment` | Treat as explicit operator-confirmed maintenance/metrology procedure. |
| `4301` | Zero Cal convergence write failed | `zero-adjustment` | Treat as explicit operator-confirmed maintenance/metrology procedure. |
| `4302` | Zero Cal failed to take measurement | `zero-adjustment` | Treat as explicit operator-confirmed maintenance/metrology procedure. |
| `4303` | Zero Cal no starting value provided | `zero-adjustment` | Treat as explicit operator-confirmed maintenance/metrology procedure. |
| `4304` | Zero Cal pre-checkpoint sequence failed | `zero-adjustment` | Treat as explicit operator-confirmed maintenance/metrology procedure. |
| `4305` | Zero Cal failed to take checkpoint measurement. | `zero-adjustment` | Treat as explicit operator-confirmed maintenance/metrology procedure. |
| `4404` | UNKNOWN HARDWARE FAULT - USE THE POWER BUTTON TO TURN THE INSTRUMENT OFF AND BACK ON | `self-test-diagnostic` | Do not use in broad tests; may be long-running or require operator action. |
| `4405` | Integrator limit exceeded | `range-limit-validation` | Improve PyMeasure validators and value maps using Programming Guide limits. |
| `4500` | Cannot open 52120 control port | `interface-communication` | Check VISA resource, interface setup, EOL, timeout, and selected remote interface. |
| `4501` | DAC counts out of range | `range-limit-validation` | Improve PyMeasure validators and value maps using Programming Guide limits. |
| `4502` | Out current limit has been exceeded | `range-limit-validation` | Improve PyMeasure validators and value maps using Programming Guide limits. |
| `4503` | External voltage detected on Output post | `output-protection` | Immediately put instrument in safe final state; inspect wiring/load before retry. |
| `4504` | External voltage detected on VI AUX post | `internal-unknown` | Drain error queue, record state, and require manual review if repeated. |
| `4505` | Thermocouple output voltage exceeds hardware limits | `output-protection` | Immediately put instrument in safe final state; inspect wiring/load before retry. |
| `4506` | Could not start LED test | `internal-unknown` | Drain error queue, record state, and require manual review if repeated. |
| `4507` | Json deserialization failed | `interface-communication` | Check VISA resource, interface setup, EOL, timeout, and selected remote interface. |
| `4508` | INGUARD NOT RESPONDING - USE THE POWER BUTTON TO TURN THE INSTRUMENT OFF AND BACK ON | `self-test-diagnostic` | Do not use in broad tests; may be long-running or require operator action. |
| `4509` | Inguard reported previous watchdog timeout [VALUE] | `interface-communication` | Check VISA resource, interface setup, EOL, timeout, and selected remote interface. |
| `5000` | Error while reading 52120A cal store | `persistent-storage` | Avoid in generic hardware tests; may change nonvolatile state or depend on USB/storage. |
| `5001` | Expected a 52120A but it was gone | `52120a-amplifier` | Requires external 52120A fixture; skip unless explicitly configured. |
| `5002` | 52120A cal store corrupted | `persistent-storage` | Avoid in generic hardware tests; may change nonvolatile state or depend on USB/storage. |
| `5003` | Value out of range of 52120A | `52120a-amplifier` | Requires external 52120A fixture; skip unless explicitly configured. |
| `5004` | Unknown error reported by 52120A | `interface-communication` | Check VISA resource, interface setup, EOL, timeout, and selected remote interface. |
| `5005` | 52120A added or removed | `52120a-amplifier` | Requires external 52120A fixture; skip unless explicitly configured. |
| `5006` | 52120A forcibly turned off | `52120a-amplifier` | Requires external 52120A fixture; skip unless explicitly configured. |
| `5007` | 52120A detected over compliance | `output-protection` | Immediately put instrument in safe final state; inspect wiring/load before retry. |
| `5008` | 52120A detected over range | `52120a-amplifier` | Requires external 52120A fixture; skip unless explicitly configured. |
| `5009` | 52120A detected over temperature | `52120a-amplifier` | Requires external 52120A fixture; skip unless explicitly configured. |
| `5010` | Maximum of three 52120A amplifiers supported, additional amplifiers ignored | `interface-communication` | Check VISA resource, interface setup, EOL, timeout, and selected remote interface. |
| `6001` | Cal constant does not exist | `internal-unknown` | Drain error queue, record state, and require manual review if repeated. |
| `6002` | Cal correction is missing an input value | `syntax-parameter` | Check command spelling, parameter count, units, type conversion, validator, and mapping. |
| `6003` | Attempted to divide by zero | `zero-adjustment` | Treat as explicit operator-confirmed maintenance/metrology procedure. |
| `6004` | Attempted to reverse an irreversible calculation | `internal-unknown` | Drain error queue, record state, and require manual review if repeated. |
| `6005` | Cal parameter does not exist | `syntax-parameter` | Check command spelling, parameter count, units, type conversion, validator, and mapping. |
| `6006` | Cal correction is value only | `internal-unknown` | Drain error queue, record state, and require manual review if repeated. |
| `6007` | Calculated corrector out of tolerance | `internal-unknown` | Drain error queue, record state, and require manual review if repeated. |
| `7001` | Frequency must be > 0.0 Hz | `range-limit-validation` | Improve PyMeasure validators and value maps using Programming Guide limits. |
| `7002` | Function does not permit a frequency below [VALUE] | `range-limit-validation` | Improve PyMeasure validators and value maps using Programming Guide limits. |
| `7003` | Cannot specify more than one frequency | `range-limit-validation` | Improve PyMeasure validators and value maps using Programming Guide limits. |
| `7004` | Cannot specify more than two magnitudes | `range-limit-validation` | Improve PyMeasure validators and value maps using Programming Guide limits. |
| `7005` | Units are required for multiple entries | `internal-unknown` | Drain error queue, record state, and require manual review if repeated. |
| `7006` | Not applicable | `feature-unavailable` | Gate API by model/option/firmware and skip unsupported tests. |
| `7007` | Cannot set Duty Cycle in this configuration | `range-limit-validation` | Improve PyMeasure validators and value maps using Programming Guide limits. |
| `7008` | Cannot set Offset in this configuration | `range-limit-validation` | Improve PyMeasure validators and value maps using Programming Guide limits. |
| `7009` | Range Lock disabled in this configuration | `range-limit-validation` | Improve PyMeasure validators and value maps using Programming Guide limits. |
| `7010` | Compensation not available for this function | `feature-unavailable` | Gate API by model/option/firmware and skip unsupported tests. |
| `7011` | Cannot enable compensation in this configuration | `internal-unknown` | Drain error queue, record state, and require manual review if repeated. |
| `7012` | Harmonic not available for this function | `feature-unavailable` | Gate API by model/option/firmware and skip unsupported tests. |
| `7013` | Fundamental not available for this function | `feature-unavailable` | Gate API by model/option/firmware and skip unsupported tests. |
| `7014` | Setting Range not available for this function | `persistent-storage` | Avoid in generic hardware tests; may change nonvolatile state or depend on USB/storage. |
| `7015` | Cannot change polarity for this function | `internal-unknown` | Drain error queue, record state, and require manual review if repeated. |
| `7016` | This value cannot be slewed | `internal-unknown` | Drain error queue, record state, and require manual review if repeated. |
| `7017` | Cannot change Phase for this function | `internal-unknown` | Drain error queue, record state, and require manual review if repeated. |
| `7018` | Validation of requested attributes failed | `internal-unknown` | Drain error queue, record state, and require manual review if repeated. |
| `7019` | Offset range not found | `range-limit-validation` | Improve PyMeasure validators and value maps using Programming Guide limits. |
| `7020` | Read only mode for calibration control | `internal-unknown` | Drain error queue, record state, and require manual review if repeated. |
| `7021` | Must be in read only mode to execute this command | `internal-unknown` | Drain error queue, record state, and require manual review if repeated. |
| `7022` | Cannot enter watts by itself | `internal-unknown` | Drain error queue, record state, and require manual review if repeated. |
| `7023` | Value not available | `feature-unavailable` | Gate API by model/option/firmware and skip unsupported tests. |
| `7024` | Harmonic not available for non-sine waveforms | `feature-unavailable` | Gate API by model/option/firmware and skip unsupported tests. |
| `7025` | TC offset can only be set while in TC Measurement function | `range-limit-validation` | Improve PyMeasure validators and value maps using Programming Guide limits. |
| `7026` | Temperature Scale can only be set while sourcing or measuring temperature | `internal-unknown` | Drain error queue, record state, and require manual review if repeated. |
| `7027` | RTD type can only be set while in RTD Source function | `internal-unknown` | Drain error queue, record state, and require manual review if repeated. |
| `7028` | TC type can only be set while in TC Source/Measure function | `internal-unknown` | Drain error queue, record state, and require manual review if repeated. |
| `7029` | Coupled command queue limit exceeded | `range-limit-validation` | Improve PyMeasure validators and value maps using Programming Guide limits. |
| `7500` | Cannot have magnitude above [VALUE] in function [FUNCTION] | `range-limit-validation` | Improve PyMeasure validators and value maps using Programming Guide limits. |
| `7501` | Cannot have magnitude below [VALUE] in function [FUNCTION] | `range-limit-validation` | Improve PyMeasure validators and value maps using Programming Guide limits. |
| `7502` | No appropriate range found in function | `range-limit-validation` | Improve PyMeasure validators and value maps using Programming Guide limits. |
| `7503` | Magnitude exceeds boundaries of selected range | `range-limit-validation` | Improve PyMeasure validators and value maps using Programming Guide limits. |
| `7504` | Incorrect units for selected function [FUNCTION] | `internal-unknown` | Drain error queue, record state, and require manual review if repeated. |
| `7505` | Invalid second range selected for function [FUNCTION] | `syntax-parameter` | Check command spelling, parameter count, units, type conversion, validator, and mapping. |
| `7506` | Current post/range mismatch for function [FUNCTION] | `range-limit-validation` | Improve PyMeasure validators and value maps using Programming Guide limits. |
| `7507` | Cannot have frequency above [VALUE] in this configuration | `range-limit-validation` | Improve PyMeasure validators and value maps using Programming Guide limits. |
| `7509` | Cannot have both Duty Cycle and DC Offset | `range-limit-validation` | Improve PyMeasure validators and value maps using Programming Guide limits. |
| `7510` | Duty Cycle must be between 1 and 99 | `range-limit-validation` | Improve PyMeasure validators and value maps using Programming Guide limits. |
| `7511` | Duty Cycle is only available with Square Wave | `range-limit-validation` | Improve PyMeasure validators and value maps using Programming Guide limits. |
| `7512` | Requested offset exceeds the maximum allowed for this output range and waveform | `output-protection` | Immediately put instrument in safe final state; inspect wiring/load before retry. |
| `7513` | Cannot accept non-coupled command while coupled-commands are queued | `internal-unknown` | Drain error queue, record state, and require manual review if repeated. |
| `7514` | External sense not available for this function | `feature-unavailable` | Gate API by model/option/firmware and skip unsupported tests. |
| `7515` | Harmonic must be greater than zero | `zero-adjustment` | Treat as explicit operator-confirmed maintenance/metrology procedure. |
| `7516` | Cannot enable 2 wire compensation below [VALUE] in function [FUNCTION] | `internal-unknown` | Drain error queue, record state, and require manual review if repeated. |
| `7517` | Thermocouple reference must be specified as a temperature | `internal-unknown` | Drain error queue, record state, and require manual review if repeated. |
| `7518` | Thermocouple offset must be specified as a temperature | `range-limit-validation` | Improve PyMeasure validators and value maps using Programming Guide limits. |
| `7519` | Cannot have reference below [VALUE] in function [FUNCTION] | `internal-unknown` | Drain error queue, record state, and require manual review if repeated. |
| `7520` | Cannot have reference above [VALUE] in function [FUNCTION] | `internal-unknown` | Drain error queue, record state, and require manual review if repeated. |
| `7521` | Thermocouple offset is limited to +/- [VALUE] | `range-limit-validation` | Improve PyMeasure validators and value maps using Programming Guide limits. |
| `7522` | Cannot use external sense on selected range | `range-limit-validation` | Improve PyMeasure validators and value maps using Programming Guide limits. |
| `7523` | Function not available | `feature-unavailable` | Gate API by model/option/firmware and skip unsupported tests. |
| `7524` | Line Marker can range from 1 through [VALUE] with the selected frame format in function [FUNCTION] | `range-limit-validation` | Improve PyMeasure validators and value maps using Programming Guide limits. |
| `7525` | Cannot enable external reference in this function | `internal-unknown` | Drain error queue, record state, and require manual review if repeated. |
| `7526` | Trigger Option not available with given primary magnitude | `feature-unavailable` | Gate API by model/option/firmware and skip unsupported tests. |
| `7527` | Cannot change Power Factor for this function | `internal-unknown` | Drain error queue, record state, and require manual review if repeated. |
| `7528` | Cannot change Phase Angle Sign for this function | `internal-unknown` | Drain error queue, record state, and require manual review if repeated. |
| `7529` | Cannot have magnitude above [VALUE] in function [FUNCTION] with waveform [WAVEFORM] | `range-limit-validation` | Improve PyMeasure validators and value maps using Programming Guide limits. |
| `7530` | The magnitude representation cannot be changed in this function | `range-limit-validation` | Improve PyMeasure validators and value maps using Programming Guide limits. |
| `7531` | Cannot set wave now | `internal-unknown` | Drain error queue, record state, and require manual review if repeated. |
| `7532` | Cannot enable 2 wire compensation above [VALUE] in function [FUNCTION] | `internal-unknown` | Drain error queue, record state, and require manual review if repeated. |
| `7533` | Watts requires AC Power and a sine waveform | `range-limit-validation` | Improve PyMeasure validators and value maps using Programming Guide limits. |
| `7534` | Power factor must be ≥-1.0 and ≤1.0 | `internal-unknown` | Drain error queue, record state, and require manual review if repeated. |
| `7535` | Cannot have magnitude between -1mV and 1mV in SACV | `range-limit-validation` | Improve PyMeasure validators and value maps using Programming Guide limits. |
| `7536` | Cannot have magnitude above [VALUE] in function [FUNCTION] with this impedance setting | `persistent-storage` | Avoid in generic hardware tests; may change nonvolatile state or depend on USB/storage. |
| `7537` | Cannot have magnitude below [VALUE] in function [FUNCTION] with this impedance setting | `persistent-storage` | Avoid in generic hardware tests; may change nonvolatile state or depend on USB/storage. |
| `7538` | Feature not available | `feature-unavailable` | Gate API by model/option/firmware and skip unsupported tests. |
| `7539` | Cannot set requested impedance value (in response to the OUT_IMP {Z50 / Z1M} command) | `internal-unknown` | Drain error queue, record state, and require manual review if repeated. |
| `7540` | Cannot have secondary magnitude in function [FUNCTION] | `range-limit-validation` | Improve PyMeasure validators and value maps using Programming Guide limits. |
| `7541` | Cannot have primary magnitude in function [FUNCTION] | `range-limit-validation` | Improve PyMeasure validators and value maps using Programming Guide limits. |
| `7542` | Cannot have frequency in function [FUNCTION] | `range-limit-validation` | Improve PyMeasure validators and value maps using Programming Guide limits. |
| `7543` | dBm only allowed in single sine ACV | `internal-unknown` | Drain error queue, record state, and require manual review if repeated. |
| `7544` | Requested waveform not available in this configuration | `feature-unavailable` | Gate API by model/option/firmware and skip unsupported tests. |
| `7545` | Offset cannot be greater than 50 % of the primary output in function [FUNCTION] | `output-protection` | Immediately put instrument in safe final state; inspect wiring/load before retry. |
| `7600` | Cannot use boost amplifier now | `52120a-amplifier` | Requires external 52120A fixture; skip unless explicitly configured. |
| `7601` | Cannot select boost amplifier post now | `52120a-amplifier` | Requires external 52120A fixture; skip unless explicitly configured. |
| `7602` | Can only output that current on the HIGH post | `output-protection` | Immediately put instrument in safe final state; inspect wiring/load before retry. |
| `7603` | Valid Pulse amplitudes are 2.5V, 1V, 250mV, 100mV, 25mV, 10mV | `internal-unknown` | Drain error queue, record state, and require manual review if repeated. |
| `7604` | Volts per division too low | `internal-unknown` | Drain error queue, record state, and require manual review if repeated. |
| `8001` | Power up was less than 30 minutes ago | `internal-unknown` | Drain error queue, record state, and require manual review if repeated. |
| `8002` | Zero adjustment is required every [VALUE] days | `zero-adjustment` | Treat as explicit operator-confirmed maintenance/metrology procedure. |
| `8003` | Ohms zero adjustment is required every [VALUE] hours | `zero-adjustment` | Treat as explicit operator-confirmed maintenance/metrology procedure. |
| `8012` | Zero adjustment is required every [VALUE] days | `zero-adjustment` | Treat as explicit operator-confirmed maintenance/metrology procedure. |
| `8013` | Ohms zero adjustment is required every [VALUE] hours | `zero-adjustment` | Treat as explicit operator-confirmed maintenance/metrology procedure. |
| `8101` | Size of X and Y should be the same for Polyfit | `internal-unknown` | Drain error queue, record state, and require manual review if repeated. |
| `8102` | Failed matrix reduction using Gauss-Jordan elimination | `internal-unknown` | Drain error queue, record state, and require manual review if repeated. |
| `8103` | Cannot read coefficients from the matrix | `internal-unknown` | Drain error queue, record state, and require manual review if repeated. |
| `8104` | Missing required input for calculation | `syntax-parameter` | Check command spelling, parameter count, units, type conversion, validator, and mapping. |
| `8106` | Failed to read matrix coefficients | `internal-unknown` | Drain error queue, record state, and require manual review if repeated. |
| `8107` | TC Measurement is invalid | `syntax-parameter` | Check command spelling, parameter count, units, type conversion, validator, and mapping. |
| `8108` | Lag bath input needs to be between -10 °C and 70 °C | `internal-unknown` | Drain error queue, record state, and require manual review if repeated. |
| `8109` | Entered value out of bounds | `range-limit-validation` | Improve PyMeasure validators and value maps using Programming Guide limits. |
| `8110` | Wrong unit for reference | `internal-unknown` | Drain error queue, record state, and require manual review if repeated. |
| `8111` | Cannot store cal constants during this step | `persistent-storage` | Avoid in generic hardware tests; may change nonvolatile state or depend on USB/storage. |
| `8201` | USB stick read failed | `interface-communication` | Check VISA resource, interface setup, EOL, timeout, and selected remote interface. |
| `8202` | USB stick write failed | `interface-communication` | Check VISA resource, interface setup, EOL, timeout, and selected remote interface. |
| `8203` | No data available | `internal-unknown` | Drain error queue, record state, and require manual review if repeated. |
| `10001` | Exception happened during json serialization | `interface-communication` | Check VISA resource, interface setup, EOL, timeout, and selected remote interface. |
| `10002` | Exception happened during RPC communication | `interface-communication` | Check VISA resource, interface setup, EOL, timeout, and selected remote interface. |
| `10003` | Unhandled exception: | `internal-unknown` | Drain error queue, record state, and require manual review if repeated. |
| `10101` | Memory allocation error: | `internal-unknown` | Drain error queue, record state, and require manual review if repeated. |
| `10201` | Unknown command: | `internal-unknown` | Drain error queue, record state, and require manual review if repeated. |
| `10301` | Unknown string Id: | `syntax-parameter` | Check command spelling, parameter count, units, type conversion, validator, and mapping. |
| `11001` | Duplicate Setting | `persistent-storage` | Avoid in generic hardware tests; may change nonvolatile state or depend on USB/storage. |
| `11002` | Setting not found | `persistent-storage` | Avoid in generic hardware tests; may change nonvolatile state or depend on USB/storage. |
| `11003` | Unable to read clock | `clock-date-time` | Avoid changing persistent time/date unless explicitly scoped. |
| `11004` | Unable to set clock | `clock-date-time` | Avoid changing persistent time/date unless explicitly scoped. |
| `11005` | Entered value is outside allowable limits | `range-limit-validation` | Improve PyMeasure validators and value maps using Programming Guide limits. |
| `11006` | Invalid password | `syntax-parameter` | Check command spelling, parameter count, units, type conversion, validator, and mapping. |
| `11007` | The passcode must be 1 to 8 digits in length | `restricted-security` | Do not automate broadly; requires explicit operator/security decision. |
| `65535` | Unknown Error | `internal-unknown` | Drain error queue, record state, and require manual review if repeated. |
| `65536` | Default Error | `self-test-diagnostic` | Do not use in broad tests; may be long-running or require operator action. |

## 14. Hardware-test policy derived from Operators Manual

| Test type | Allowed automatically? | Required preconditions | Required final state | Notes |
|---|---:|---|---|---|
| Identity query | yes | Valid VISA address and remote interface configured | No state change | Use Programming Guide syntax, likely `*IDN?`. |
| Options query | yes | Valid VISA address | No state change | Use Programming Guide syntax. |
| Error queue query | yes | Valid VISA address | Queue drained or reported | Use Programming Guide error-query commands. |
| Remote port readback | cautious | Interface remains stable | No disruptive changes | Avoid changing port while connected. |
| Output configuration while standby | maybe | Operator confirms no DUT risk and output remains inactive | Standby | `output-off-only`; do not activate terminals. |
| Low-voltage output | no broad auto-test | Load/DUT specified, operator confirms wiring | Standby/reset | Even low voltage can damage sensitive DUTs. |
| High-voltage output | no | Fixture, insulation, load, operator confirmation | Standby/reset | Hazard threshold >30 Vrms or 42 V peak. |
| High-current output | no | Correct terminal, load/shunt, current rating, operator confirmation | Standby/reset | Current output above 3.1 A uses 30A terminal. |
| Simulated power | no | Power-meter fixture and operator-confirmed procedure | Standby/reset | Not available on 5540A; hazardous output. |
| Resistance/capacitance/inductance output | no broad auto-test | DUT fixture and compensation/wiring declared | Standby/reset | Inductance unavailable on 5540A/5530A. |
| RTD/TC output | no broad auto-test | Correct wire/type/reference junction | Standby/reset | Physical temperature setup matters. |
| TC measurement | no broad auto-test | TC fixture stable and type selected | No hazardous output | Open TC Detect may affect parallel measurements. |
| 52120A amplifier operation | no | External amplifier connected and configured | Standby/reset, amplifier safe | Up to three 52120A units; high-current risk. |
| Scope outputs | no broad auto-test | Scope option present, scope fixture connected | Standby/reset | Option dependent. |
| Scope overload tests | never broad auto-test | Explicit oscilloscope power-rating verification | Standby/reset | Can damage oscilloscope. |
| Calibration security | no | Authorized metrology/service procedure | Secured state | Passcode risk. |
| Zero adjustment | no broad auto-test | Warm-up complete, metrology procedure expected | Standby | Long-running/state-changing. |
| Restore defaults | no | Explicit operator/service decision | Known configured state | Can alter persistent settings or calibration constants. |
| Firmware update | no | Manual maintenance process | N/A | Not a PyMeasure driver feature. |

## 15. Command-like references requiring Programming Guide confirmation

These are tokens or command-like references encountered in the Operators Manual or needed as cross-references for later PyMeasure planning. Do not treat this section as command inventory.

| Token | Operators Manual context | Found in Programming Guide? | Decision | Notes |
|---|---|---:|---|---|
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

## 16. PyMeasure design implications

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

## 17. RAG navigation map

| User/Codex intent | Use this section | PyMeasure implication |
|---|---|---|
| Identify instrument family and capabilities | Quick facts, Output capability summary | Establish class scope and model family. |
| Plan remote connection examples | Remote operation and interface summary, Remote port setup facts | Create safe documentation and hardware-test CLI examples. |
| Decide safe hardware-test policy | Safety summary, Operate/Standby behavior, Hardware-test policy | Avoid hazardous broad tests. |
| Understand physical wiring requirements | DUT connection and fixture constraints | Require operator-confirmed fixture for output tests. |
| Plan output subsystem API | Output function map | Split configure vs activate. |
| Handle model/option dependencies | Model and option dependencies | Gate features and skip tests. |
| Interpret errors | Error-code knowledge base | Improve exception messages and test diagnostics. |
| Handle calibration/security concerns | Calibration security and persistent settings | Do not automate sensitive state changes. |
| Plan warm-up/zero metrology state | Warm-up, zeroing, metrology prerequisites | Avoid asserting accuracy without preconditions. |
| Check command references | Command-like references | Confirm in Programming Guide before use. |

## 18. OCR and conversion notes

The source Markdown appears converted from a PDF and contains visible formatting artifacts: split table rows, repeated headings, page labels, broken special symbols, and front-panel key names represented as isolated characters. Critical values must be checked against the official manual before use in metrology, calibration, safety-critical code, or final PyMeasure documentation.

## 19. Local artifact policy

This file is for local PyMeasure driver planning only. It should not be included in the final upstream PyMeasure pull request. Keep it under `assets/<vendor>/<model>/` or equivalent local workspace storage.
