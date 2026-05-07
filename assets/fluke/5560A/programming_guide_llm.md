---
title: "Fluke 5560A/5550A/5540A/5530A - Programming Guide LLM Planning Aid"
source_file: "assets/fluke/5560A/programming_guide.md"
vendor: fluke
model: "5560A"
class_name: Fluke5560A
instrument_type: "multifunction precision calibrator / precision source calibrator"
workflow_step: 02
full_command_inventory_created: false
complete_command_extraction_deferred_to: "Prompt 05 commands.txt"
generated_on: "2026-05-07"
local_artifact: true
upstream_pr: false
---

# LLM_AGENT_CONTRACT

- Use this file for retrieval and planning only.
- Use the Programming Guide (`programming_guide.md`) as the source for command syntax.
- Do not use this file as a full command inventory.
- Full command inventory must be produced in Prompt 05.
- Do not implement code from this file alone.
- Do not run hardware tests from this file alone.

# DOCUMENT ROLE IN WORKFLOW

| File | Role | Not allowed |
|---|---|---|
| programming_guide.md | authoritative source for remote command syntax | unsafe direct hardware execution |
| programming_guide_llm.md | LLM/RAG planning aid | complete command inventory |
| commands.txt | complete command inventory from Prompt 05 | invented commands |
| command_coverage.md | API/test/status mapping | command syntax not in commands.txt |

# DOCUMENT MAP

This section identifies likely source regions in `programming_guide.md` for major topic areas, using source evidence (headings, table names, or nearby text). Stable line numbers are not verified; use heading search instead.

| Region | Source evidence | Content type |
|---|---|---|
| Table of contents / high-level overview | "Command index by function" | Top-level command grouping |
| Command summary tables | "Table 20. Common Commands" through "Table 28. Thermocouple (TC) Measurement Command" | Summary descriptions per command |
| Detailed command reference | "Atomic command reference" with per-command subsections (e.g., `### OUT {#out}`) | Full syntax, parameters, responses, examples |
| Status/event registers | "Check Product Status", "Table 16. Status Register Summary", "Table 17. Status Byte Register (STB) and Service Request Enable (SRE)", "Table 18. Event Status Register (ESR) and Event Status Enable (ESE)", "Table 19. Bit Assignments for the ISR, ISCEs, and ISCR" | Register maps, bit definitions, read/write commands |
| Error handling | "Error Queue", "ERR?", "FAULT?", "EXPLAIN?", "# Error code reference" | Queue behavior, error codes, explanations |
| Data formats / terminators | "Parameter Syntax Rules", "Table 13. Units Accepted in Parameters and Used in Responses", "Table 14. Terminator Characters", "Table 15. Response Data Types" | Units, terminators, block data, response types |
| Remote interface setup | "Remote Operations", "Set up the IEEE-488 Port", "Set up the USBTMC Port", "Set up the RS-232 Port", "Set up and Connect the Ethernet Interface" | Interface configuration and constraints |
| Safety warnings | "XW Warning" under "Remote Operations" | Safety-critical statements |
| Program examples | "Remote Program Examples", "Guidelines for Programming the Calibrator" | Compound commands, synchronization, SRQ handling |

# REMOTE INTERFACE NOTES

| Interface | Confirmed? | Setup facts | Termination/EOL | SRQ/status notes | Source evidence | Notes |
|---|---:|---|---|---|---|---|
| IEEE-488/GPIB | Yes | Max 15 devices; cable length max 20 m (2 m * devices); supports SH1, AH1, T6, L4, SR1, RL1, DC1, DT1 | Response: ASCII LF with EOI asserted. Command: any char with EOI, or LF. | Full SRQ via bus control line; serial poll supported; RQS bit in STB | "Set up the IEEE-488 Port", "Table 1", "Table 14" | Interface messages (REN, GTL, LLO, etc.) are not sent as literal data commands |
| USBTMC | Yes | Requires NI-VISA drivers; USBTMC-488 adds Interrupt IN endpoint for SRQ | Same as IEEE-488 (uses bulk endpoints) | SRQ via Interrupt IN endpoint; serial poll via control endpoint; RQS bit auto-communicated | "USBTMC Interface", "USBTMC Communication Overview", "Table 14" | Resource string format documented: `USB0::0x0F7E::0x800A::[serial number]::INSTR` |
| RS-232 | Yes | Rear-panel DB-9 DTE; null-modem cable; max 15 m; defaults: 9600, 8N1, Ctrl-S/Ctrl-Q flow control | Command: CR, LF, or CRLF. Response: configurable EOL (CR/LF/CRLF) via SP_SET / EOLSTR | No SRQ line/capability; status registers still operate; SRQ emulated via SRQSTR string | "RS-232 Serial Interface", "Table 2", "Table 14", "Exceptions for Serial and Ethernet Remote Control" | Ctrl-C acts as DCL/SDC; Ctrl-T as GET; Ctrl-P as SPE/SPD |
| Ethernet/Telnet | Yes | TCP socket; default port 3490; one client at a time; DHCP enabled by default | Same as RS-232 (shares behavior) | No SRQ line; same RS-232 emulation via SRQSTR | "Ethernet Interface", "Configure the General Network Socket Port", "Table 14" | LAN server rejects additional connections while one client is connected |

# REMOTE COMMUNICATION FORMAT NOTES

- **Command termination:**
  - IEEE-488: LF, or any ASCII character with EOI asserted.
  - RS-232/Ethernet: CR, LF, or CRLF.
- **Response termination:**
  - IEEE-488: ASCII LF with EOI control line held high.
  - RS-232/Ethernet: EOL character programmed per port (CR, LF, or CRLF).
- **EOI:** Used on IEEE-488 to mark end of response message; also used with ATN for polling.
- **ASCII:** All commands and responses are ASCII-based. Lower-case or upper-case accepted for commands and units.
- **Incoming character processing:**
  - Most significant data bit (DIO8) ignored.
  - All data taken as 7-bit ASCII.
  - ASCII characters < 32 (Space) discarded, except LF (10), CR (13), and characters within `*PUD` argument.
- **Compound commands:** Semicolon (`;`) separates commands in a single line.
- **Coupled commands:** Can interfere when combined in a compound command; order-independent among themselves, but `*WAI` between them decouples them.
- **Overlapped commands:** Begin execution but may complete later; `*WAI`, `*OPC`, `*OPC?` required for synchronization.
- **Numeric formats:** Up to 15 significant digits, exponents in range ±1.0E±20.
- **Parameter separation:** Comma-separated when more than one parameter.
- **Expressions:** Not valid as parameters (e.g., `4+2*13` is rejected).
- **Binary Block Data:** Two forms per IEEE-488.2:
  - Indefinite Length: `#0` followed by data bytes, terminated by LF with EOI (or CR/LF for RS-232/Ethernet).
  - Definite Length: `#n<nn digits><data bytes>` where `n` is number of digits in the byte-count field.
- **Response Data Types (Table 15):** Integer, Floating (up to 15 sig figs, ±E20), String (including quote delimiters), CRD (keyword response), IAD (Indefinite ASCII, must be last query in message), Binary Block Data (e.g., `*PUD?`).
- **Output queue:** Up to 800 characters; MAV bit set when data available.
- **Error queue:** Up to 16 entries; first 15 errors kept; 16th entry is overflow error. Cleared on power-off or `*CLS`.
- **Input buffer:** Up to 350 bytes (FIFO). IEEE-488 holds off with NRFD when full. RS-232 issues XOFF at 80% full, XON at <40% full (or RTS equivalent).

# COMMAND NOTATION GUIDE

- Command names are documented in backticks in the source (e.g., `` `OUT` ``).
- Query commands end with `?` and return data.
- Common commands begin with `*` (e.g., `*RST`, `*IDN?`).
- Parameters are space-separated from the command; one space required after command if parameters exist. Extra spaces/tabs between parameters are optional and allowed for clarity.
- Units may be upper or lower case.
- Parameter lists use commas to separate multiple parameters.
- Optional parameters are documented in the detailed command reference with "(optional)" labels.
- Response types are labeled in the source as Integer, Floating, String, CRD, IAD, or Binary Block Data.
- Command classifications in the source include: sequential, overlapped, coupled, RS-232/Ethernet-only, IEEE-488-only.
- Do not write `*IDN` as a set command. The source documents only `*IDN?` as a query.

# COMMAND EXTRACTION HINTS FOR PROMPT 05

This section is not the command inventory. Prompt 05 must re-read `programming_guide.md` and extract all commands into `commands.txt`.

| Source region | What to extract in Prompt 05 | Authority level | Risk of incompleteness | Notes |
|---|---|---|---|---|
| "Command index by function" (Common, Error Mode, External Connection, Oscilloscope, Output, RS-232/Ethernet, Setup/Utility, Status, TC Measurement, Adjustment/Service) | All command names (set and query) | High | Low | Good starting list, but may miss commands not listed in the functional index |
| "Atomic command reference" per-command subsections | Full syntax, parameters, response format, examples, classifications (overlapped/coupled/sequential) | Highest | Low | This is the authoritative detailed reference; must be the primary extraction source |
| "Table 20" through "Table 28" | Command names and brief descriptions | High | Medium | Summary tables; some commands span multiple tables (e.g., `*TRG` appears in Common and Oscilloscope) |
| "Commands for RS-232/Ethernet Only" and "Commands for IEEE-488 Only" | Interface-specific commands and control characters | High | Low | Ensures interface-specific commands are not missed |
| "Error code reference" | Error codes | Low (for command inventory) | N/A | Error codes are not commands, but relevant for error handling implementation |

# DATA TRANSFER AND PARSER NOTES

| Topic | Fact from Programming Guide | Source evidence | Parser implication | needs-verification |
|---|---|---|---|---|
| ASCII responses | All responses are ASCII-based; 7-bit ASCII processing | "Incoming Character Processing" | Parser must handle ASCII text, discard control chars <32 except LF/CR | No |
| Binary block data | Indefinite (`#0...<LF/EOI>`) and Definite (`#n<digits><data>`) formats | "Parameter Syntax Rules" | Parser must detect `#` header and read exact byte count for definite length | No |
| Definite length blocks | `#n` where `n` is digit count of byte-count field; max response 64 chars for `*PUD?` | `*PUD?` description | Read `n` digits, convert to int, read that many bytes | No |
| Indefinite length blocks | `#0` then data until LF with EOI (or CR/LF for RS-232/Ethernet) | "Parameter Syntax Rules" | Read until terminator sequence | No |
| REAL / float formats | Up to 15 significant digits, exponent ±E20 | "Table 15. Response Data Types" | Use high-precision float parser; expect scientific notation | No |
| Integer responses | Decimal integers, range -32768 to 32768 for some controllers | "Table 15. Response Data Types" | Standard integer parsing; some values may exceed 16-bit signed range (e.g., status register bytes 0-255) | No |
| String responses | Any ASCII characters including quotation mark delimiters | "Table 15. Response Data Types" | Handle quoted strings; preserve internal spaces | No |
| CRD (Character Response Data) | Always a keyword (e.g., `ACV`, `ON`, `OFF`) | "Table 15. Response Data Types" | Match against documented keyword sets | No |
| IAD (Indefinite ASCII) | Any ASCII characters followed by EOM; must be last query in a program message | "Table 15. Response Data Types" | Read until EOM/terminator; cannot combine with subsequent queries in same message | No |
| Point counts / arrays | `OUT?` returns 5 comma-separated fields; `*PUD?` returns binary block | `OUT?`, `*PUD?` descriptions | Split comma-separated fields; handle variable field counts | No |
| Long text responses | CAL reports and lists containing Line Feeds are typically IAD | "Table 15. Response Data Types" | Parser must accept multi-line responses for certain queries | No |
| Unit suffixes in responses | Units appear as separate comma-separated fields or suffixes (e.g., `V`, `A`, `HZ`, `CEL`) | `OUT?`, `AC_REP?`, `TC_REF?` descriptions | Extract and validate units; do not treat as part of numeric value unless documented | No |
| Trace/table/waveform transfers | No explicit binary waveform or trace transfer commands identified in reviewed sections | Reviewed sections | `needs-verification`: Prompt 05 should verify whether scope or measurement data involves block transfers beyond `*PUD` | needs-verification |

# STATUS, ERROR, AND SYNCHRONIZATION NOTES

- `*OPC?`: Returns `1` after all pending operations complete. Must be followed by a read.
- `*OPC`: Sets bit 0 (OPC) in ESR when pending operations complete. Useful for SRQ-based completion detection.
- `*WAI`: Halts execution until prior overlapped commands complete. Do not insert between coupled commands.
- Status Byte Register (STB): Bits include RQS(6), ESB(5), MAV(4), EAV(3), ISCB(2). Read via serial poll or `*STB?`.
- Service Request Enable (SRE): Masks STB bits; max value 191 (bit 6 not used). `*SRE` / `*SRE?`.
- Event Status Register (ESR): Bits PON(7), CME(5), EXE(4), DDE(3), QYE(2), OPC(0). Cleared on read. `*ESR?`.
- Event Status Enable (ESE): Masks ESR bits. `*ESE` / `*ESE?`.
- Instrument Status Register (ISR): Bits include BOOST(13), SETTLED(12), REMOTE(10), TRIPPED(9), HIVOLT(7), OPER(0). `ISR?`.
- Instrument Status Change Registers (ISCR0, ISCR1): Cleared on read, power-up, or `*CLS`. `ISCR0?`, `ISCR1?`, `ISCR?`.
- Instrument Status Change Enable (ISCE0, ISCE1, ISCE): Mask registers for ISCR transitions. `ISCE0`, `ISCE1`, `ISCE` and queries.
- Error queue: Read with `ERR?` (returns code + explanation) or `FAULT?` (returns code only). Empty response is `0` or `0,"No Error"`. `EXPLAIN? <code>` returns text for a specific code.
- `*CLS`: Clears ESR, ISCR registers, error queue, and RQS bit. Terminates pending `*OPC` / `*OPC?`.
- `*RST`: Reset to power-up state. Overlapped command that holds off subsequent commands until complete.
- SRQ:
  - IEEE-488: Asserted when RQS=1; cleared by serial poll, `*CLS`, or MSS cleared.
  - USBTMC: SRQ message via Interrupt IN endpoint.
  - RS-232/Ethernet: No SRQ line; SRQSTR string sent when RQS/MSS set.
- Serial poll: IEEE-488 SPE/SPD messages; RS-232 Terminal mode uses `^P` (Ctrl-P) to print SPLSTR.
- Output queue: Up to 800 characters; MAV indicates data available.

# SAFETY AND RISK HINTS FROM PROGRAMMING GUIDE

| Topic | Risk hint | PyMeasure implication | Hardware-test implication | Source evidence |
|---|---|---|---|---|
| Hazardous voltage capability | Calibrator can produce voltages up to 1020 V rms | Driver must not automate hazardous outputs without explicit safeguards; require operator confirmation or interlock | Any hardware test that sources voltage must include explicit safety gating and documented hazard acknowledgment | "Remote Operations" XW Warning |
| Unintended output | Programs must be tested carefully to avoid unintended hazardous outputs without sufficient warning | Implement `STBY` in error/exception paths; validate output values before `OPER` | Test scripts must include error handlers that place instrument in standby | "Remote Operations" XW Warning |
| Error handling recommendation | Fluke recommends routines to catch errors; use SRQ mechanism where supported | Implement error queue polling (`ERR?`, `FAULT?`) after operations; handle exceptions gracefully | Device tests should verify error paths and fault queue behavior | "Remote Operations" XW Warning |
| Reset behavior | `*RST` resets to power-up state and holds off subsequent commands; it is an overlapped command | Do not treat `*RST` as harmless; ensure synchronization after reset | Tests involving reset must wait for completion before sending further commands | `*RST` description |
| No SRQ on RS-232 | Serial remote control has no SRQ capability | Driver should not rely on SRQ for RS-232; use polling (`*STB?`) or string-based status instead | RS-232 device tests must use polling-based synchronization | "Exceptions for Serial and Ethernet Remote Control" |
| Output settle synchronization | Overlapped commands (e.g., `OUT`, `OPER`) require `*WAI` / `*OPC?` before assuming output is stable | Always synchronize after output changes before measurement or DUT interaction | Hardware tests must verify settle behavior with `*OPC?` | "Overlapped Commands", `*OPC?` description |

# DO-NOT-INFER LIST

- Do not infer command syntax from natural-language function names.
- Do not infer query forms from set forms.
- Do not infer set forms from query forms.
- Do not infer value ranges unless documented.
- Do not infer hardware safety from command names.
- Do not treat interface messages as data commands.
- Do not treat high-value command examples as complete inventory.
- Do not claim that any list in this file is a complete command inventory; full command inventory is deferred to Prompt 05.

# OCR_AND_CONVERSION_NOTES

- No obvious OCR artifacts detected in reviewed sections.
- Some sections may still require verification during Prompt 05.
- Command syntax with unusual symbols (e.g., `#0`, `#2`, `^C`, `^T`, `^P`) must be checked against the source.
- The source manual contains repeated heading artifacts and table fragmentation due to Markdown conversion; Prompt 05 should read atomic command reference subsections for authoritative syntax rather than summary tables alone.
- One noted typo in source: `ISCRO?` should likely be `ISCR0?` in example text (line ~3536). This is an `inference-needs-verification` item.
- Needs-verification items: scope/transfer block data commands, whether any commands accept or return binary data beyond `*PUD`, exact completeness of the functional command index versus the alphabetical reference.

# STEP 05 HANDOFF CHECKLIST

Prompt 05 must perform these exact checks:

- [ ] Re-read `programming_guide.md` from the authoritative source file.
- [ ] Extract commands from both the functional command index and the detailed atomic command reference.
- [ ] Deduplicate entries but preserve meaningful variants (e.g., set-only, query-only, command-query pairs).
- [ ] Classify each entry as command-only, query-only, or command-query pair.
- [ ] Mark ambiguous entries with `needs-verification`.
- [ ] Create `commands.txt` with the complete, deduplicated command inventory.
- [ ] Do not rely only on high-value commands from `programming_guide_llm.md`.
- [ ] Verify that `*IDN?` is documented as query-only; do not introduce `*IDN` as a set command unless explicitly found.
- [ ] Verify RS-232/Ethernet-only commands (`LOCAL`, `REMOTE`, `LOCKOUT`, `SP_SET`, `SP_SET?`, `SRQSTR?`, `SPLSTR?`, `EOLSTR`, `EOLSTR?`, `COMM_MODE`, `COMM_MODE?`, `COMM_ENABLE`, `COMM_ENABLE?`, `COMM_LOCK`, `COMM_LOCK?`) are captured.
- [ ] Verify interface-message emulation characters (`^C`, `^T`, `^P`) are noted as non-literal control characters, not as SCPI commands.
- [ ] Confirm that dual output, inductance, and 52120-related commands are marked as not available on 5540A per source note.
