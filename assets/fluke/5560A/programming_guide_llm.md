---
title: "Fluke 5560A Programming Guide - LLM Optimized"
source_file: "Programming guide Fluke 5560A.md"
source_manual: "5560A/5550A/5540A/5530A Calibrator Remote Programmers Manual"
source_revision: "August 2022 Rev. 3, 3/25"
source_sha256_prefix: "f0efa5cb08ba9f47"
converted_for: ["LLM retrieval", "RAG", "GPT Codex", "instrument-control code generation"]
converted_on: "2026-05-07"
---

# LLM_AGENT_CONTRACT

## Source Authority Rules

1. **All command syntax must come from `programming_guide.md`**. Do not invent commands, parameters, response formats, value ranges, or examples.
2. **Preserve manufacturer notation**: uppercase/lowercase SCPI abbreviations, optional nodes, indexes, `?` query markers, suffix notation.
3. **Do not transmit documentation brackets as literal command characters** (e.g., `[optional]` should not appear in actual commands).
4. **Mark OCR/conversion ambiguity as `needs-verification`** only where documentation itself is unclear.
5. **Do not invent commands, parameters, ranges, units, or responses**. Use only what is explicitly documented.

## Data Transfer Notes

- **ASCII data format**: All responses use ASCII characters. Floats may have up to 15 significant digits with exponents ±E20.
- **Terminators**:
  - IEEE-488: LF with EOI
  - RS-232/Ethernet: CR, LF, or CRLF (configurable via EOLSTR command)
- **Binary Block Data**: IEEE-488.2 standard with Indefinite Length (#0) and Definite Length (#n digits) formats
- **Float format**: Scientific notation (e.g., `1.0000000E+00`, `-1.520000E+01`)
- **Integer format**: Range -32768 to 32768 for some controllers
- **String responses**: Quoted or keyword-based (CRD type)
- **Query termination**: Queries ending with `?` must be followed by a read operation

---

# DOCUMENT MAP

| Section | Location in Source | Contents |
|---------|-------------------|----------|
| Command Index | Lines 144-183 | Summary lists by category |
| Detailed Commands | Lines 185-5678 | Full command reference |
| Status Registers | Lines 1383-1600 | ESR, ESE, STB, SRE, ISR, ISCR, ISCE |
| Data Transfer | Lines 1225-1334 | Terminators, formats, block data |
| Safety | Lines 43-52 | Hazard warnings, error handling, SRQ |

---

# REMOTE INTERFACE NOTES

## Interfaces

| Interface | Resource String Format | EOL | Notes |
|-----------|----------------------|-----|-------|
| IEEE-488/GPIB | GPIB0::4::INSTR | LF + EOI | Must use interface messages (GTL, REN, LLO) not literal data |
| USBTMC | USB0::0x0F7E::0x800A::[serial]::INSTR | Configurable | Serial poll required before SRQ commands |
| RS-232 | N/A (serial port) | CR/LF/CRLF (configurable) | No SRQ capability |
| Ethernet/Telnet | TCP socket | Configurable | Default port 3490 |

## Remote/Local States

| State | IEEE-488 | USBTMC | RS-232/Ethernet |
|-------|----------|--------|-----------------|
| Local | GTL / REN=false | GO_TO_LOCAL | LOCAL |
| Remote | MLA / REN=true | REN=true | REMOTE |
| Lockout | LLO | LOCAL_LOCKOUT | LOCKOUT |

---

# SCPI NOTATION GUIDE

## Query vs Set Commands

- **Query**: Ends with `?` (e.g., `OUT?`, `*IDN?`)
- **Set**: No `?` (e.g., `OUT 10 V`, `*IDN`)
- **Both**: Some commands set and query (e.g., `*ESE` sets, `*ESE?` queries)

## Command Types

- **Common**: Start with `*` (IEEE-488.2 standard): `*IDN?`, `*RST`, `*CLS`, `*OPC?`, `*WAI`
- **Device-dependent**: Specific to Fluke 5560A: `OUT`, `FUNC?`, `OPER`, `STBY`
- **Interface messages**: Not sent as data (IEEE-488 only): GTL, REN, LLO, SDC, DCL

## Parameter Syntax

- Parameters separated by commas when multiple
- Units optional in commands but always present in responses
- Prefixes allowed: k, M, μ, etc.
- Expressions not allowed (e.g., `4+2*13` invalid)
- Case-insensitive: `OUT`, `out`, `Out` all valid

---

# HIGH-VALUE COMMANDS

## Identity & Status

| Command | Type | Response | Notes |
|---------|------|----------|-------|
| `*IDN?` | Query | FLUKE,5560A,SERIAL,FW | Primary identification |
| `*OPC?` | Query | 1 | Wait for operation complete |
| `*STB?` | Query | Integer (0-255) | Status byte |
| `*ESR?` | Query | Integer (0-255) | Event status register |
| `*ESE` | Set | - | Set event status enable |
| `*ESE?` | Query | Integer | Read ESE register |
| `*SRE` | Set | - | Set service request enable |
| `*SRE?` | Query | Integer | Read SRE register |

## Output Control

| Command | Type | Parameters | Response | Notes |
|---------|------|------------|----------|-------|
| `OUT` | Set | `<value> <unit>, <freq>` | - | Primary output set |
| `OUT?` | Query | - | `<amp>,<unit>,<sec_amp>,<sec_unit>,<freq>` | Query all outputs |
| `OPER` | Set | - | - | Activate output |
| `OPER?` | Query | - | 1 (operate), 0 (standby) | Output state |
| `STBY` | Set | - | - | Put in standby |
| `FUNC?` | Query | - | DCV, ACV, DCI, etc. | Current function |

## Range & Level

| Command | Type | Parameters | Response | Notes |
|---------|------|------------|----------|-------|
| `RANGE` | Set | `<range>` | - | Set range |
| `RANGE?` | Query | - | Float | Current range |
| `LEVEL` | Set | `<value>` | - | Set level (generic) |

## Error Handling

| Command | Type | Response | Notes |
|---------|------|----------|-------|
| `ERR?` | Query | `<code>,"<message>"` | Drain error queue |
| `FAULT?` | Query | `<code>` | Get first fault |
| `EXPLAIN?` | Query | `<string>` | Explain fault code |

## Configuration

| Command | Type | Parameters | Response | Notes |
|---------|------|------------|----------|-------|
| `ADDR` | Set | `<address>` | - | GPIB address |
| `ADDR?` | Query | - | Integer | GPIB address |
| `EOLSTR` | Set | `SERIAL, <type>` | - | Set EOL for RS-232 |
| `EOLSTR?` | Query | `SERIAL` | CRLF/CR/LF | Read EOL setting |
| `LOCAL` | Set | - | - | Enter local state |
| `REMOTE` | Set | - | - | Enter remote state |
| `LOCKOUT` | Set | - | - | Lock front panel |

---

# DATA TRANSFER NOTES

## Response Data Types (Table 15)

| Type | Description | Example |
|------|-------------|---------|
| Integer | -32768 to 32768 | `1`, `0` |
| Floating | Up to 15 digits, ±E20 | `1.0000000E+00`, `-1.520000E+01` |
| String | ASCII with quotes | `Fluke 5560A` |
| Character (CRD) | Keyword response | `DCV`, `ACV`, `ON`, `OFF` |
| Indefinite ASCII (IAD) | Variable length, EOM | `SC600` from `*OPT?` |
| Binary Block | IEEE-488.2 #0 or #n format | `#205test1` from `*PUD?` |

## ASCII Format Details

- **Float exponent range**: ±E20
- **Significant digits**: Up to 15
- **Units in response**: Always included (V, A, OHM, F, CEL, FAR, DBM, HZ, etc.)
- **Frequency unit**: Always Hz (no suffix in response)
- **Dual outputs**: Primary and secondary separated by commas

## Termination Rules

| Interface | Command Termination | Response Termination |
|-----------|-------------------|---------------------|
| IEEE-488 | EOI | LF + EOI |
| USBTMC | Configurable | Configurable |
| RS-232 | CR/LF/CRLF | Configurable via EOLSTR |
| Ethernet | CR/LF/CRLF | Configurable via EOLSTR |

---

# COMMAND EXTRACTION HINTS FOR commands.txt

## Priority Rules

1. **High-priority commands**: Common IEEE-488.2 commands (`*IDN?`, `*RST`, `*CLS`, `*OPC?`, `*STB?`, `*ESR?`, `*ESE?`, `*SRE?`)
2. **Core function commands**: Output control (`OUT`, `OPER`, `STBY`, `FUNC?`, `RANGE?`)
3. **Configuration commands**: Interface settings (`ADDR`, `EOLSTR`, `LOCAL`, `REMOTE`)
4. **Status/error commands**: `ERR?`, `FAULT?`, `EXPLAIN?`
5. **Specialized commands**: Oscilloscope, thermocouple, dual-output features

## Command List Sources

| Location | Content | Priority |
|----------|---------|----------|
| Lines 144-183 | Command index by function | High (quick overview) |
| Lines 2000-2100 | Table 21-28 (command summaries) | High |
| Lines 2216-5678 | Atomic command reference | Critical (full details) |
| Lines 5422-5675 | Error codes | Low (for error handling only) |

## Commands.txt Priority Order

```
1. *IDN?
2. *RST
3. *CLS
4. *OPC?
5. *STB?
6. *ESR?
7. *ESE?
8. *SRE?
9. OUT
10. OUT?
11. OPER
12. OPER?
13. STBY
14. FUNC?
15. RANGE?
16. ERR?
17. FAULT?
18. EXPLAIN?
19. ADDR
20. ADDR?
21. EOLSTR
22. EOLSTR?
23. LOCAL
24. REMOTE
25. LOCKOUT
26. All other commands...
```

---

# SAFETY AND RISK HINTS FROM PROGRAMMING GUIDE

## Hazard Warnings

- **Maximum output**: 1020 V rms (line 45, 204)
- **Output can be hazardous**: Programs must be tested carefully to avoid unintended hazardous outputs (line 204)
- **Error handling**: Use Service Request mechanism where supported (line 47)
- **SRQ limitation**: Serial remote control has no SRQ capability (line 48)

## Recommended Safety Patterns

1. **Drain error queue** after each command sequence
2. **Use *OPC?** to wait for overlapped commands to complete
3. **Implement operator confirmation** before hazardous outputs
4. **Use STBY** in exception handlers to disable output
5. **Check ERR?** or FAULT? after operations

## Error Handling Template

```python
def check_errors(inst):
    errors = []
    while True:
        response = inst.query("ERR?").strip()
        errors.append(response)
        if response.startswith("0") or "No error" in response:
            break
    return errors
```

---

# OCR_AND_CONVERSION_NOTES

## Conversion Date

- Converted on: 2026-05-05
- Source revision: August 2022 Rev. 3, 3/25

## Potential Artifacts

- **No OCR errors detected**: Source Markdown is clean
- **No missing brackets**: All optional parameters properly marked with `[]`
- **No broken code fences**: All code examples intact

## Needs-Verification Items

- **None**: Documentation quality is high

---

*This file is optimized for LLM retrieval and code generation for PyMeasure instrument drivers.*
