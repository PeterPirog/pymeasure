# Agilent 35670A Service Guide — LLM-Optimized Markdown Reference

> Source transformed from: `Manual guide Agilent 35670A.md`  
> Original document: **Agilent 35670A Service Guide**, Agilent Part Number **35670-90066**, for instruments with firmware version **A.00.00**, print date **October 2011**.  
> Purpose: make the converted manual easier for LLM agents to search, reason over, and use safely.

---

## LLM_AGENT_CONTRACT

Use this document as a **service, installation, verification, troubleshooting, adjustment, parts, circuit, and voltage/signal reference** for the Agilent/HP/Keysight 35670A Dynamic Signal Analyzer.

### What this document is

This is a service-oriented manual. It covers:

- instrument specifications,
- preparation for use,
- operation and performance verification,
- troubleshooting,
- adjustment procedures,
- assembly replacement,
- replaceable parts,
- circuit descriptions,
- voltages and signals,
- internal tests, calibration routines, fault logs, and self-tests.

### What this document is not

This document is **not** the primary GPIB/SCPI command reference. For remote programming and SCPI command syntax, use the separate optimized programming guide.

### Agent behavior rules

When answering from this document, the agent must:

1. Distinguish between **operator-safe tasks** and **service-only tasks**.
2. Preserve all safety constraints involving grounding, fuses, covers, power, and qualified service personnel.
3. Never invent voltage levels, fuse ratings, part numbers, adjustment points, test points, or calibration procedures.
4. Treat OCR-converted tables as potentially noisy; verify suspicious values against nearby section context.
5. When a procedure involves internal access, power supply work, exposed assemblies, or adjustments with covers removed, explicitly state that it is for trained service personnel only.
6. Keep front-panel key names in square brackets, for example `[Source]`, `[Trigger]`, `[Rtn]`.
7. Do not convert this service manual into a general operating tutorial unless the user asks for operator-level guidance.
8. If a user asks for a service action that may expose hazardous voltages, include a safety warning before technical steps.
9. If an answer depends on an option, for example AY6, 1D0, 1D1, 1D2, 1D4, or UK4, state the option dependency.
10. If the source text is ambiguous because of OCR artifacts, say so and point to the relevant section instead of guessing.

---

## SAFETY_FIRST_RULES_FOR_AGENTS

The manual repeatedly treats the 35670A as a line-powered Safety Class 1 instrument. The following rules override all procedural summaries.

### Hard safety constraints

- The chassis and cover must remain connected to protective earth ground during normal powered operation.
- Use only fuses with the required current, voltage, and type. Do not use repaired fuses or short-circuited fuse holders.
- Do not operate the instrument in the presence of flammable gases or fumes.
- Operators must not remove instrument covers.
- Internal adjustments and component replacement are for qualified service personnel only.
- Damaged or defective instruments should be made inoperative and secured against unintended operation until repaired.
- When performing adjustment procedures with power applied and covers removed, treat the procedure as hazardous service work.
- Battery replacement must use the same or equivalent listed type, and used batteries must be discarded according to manufacturer instructions.

### Agent response template for hazardous procedures

When a user asks for an internal repair, adjustment, disassembly, or powered service procedure, answer using this structure:

```text
Safety status: service-only / trained personnel required.
Hazards: electrical shock, fire, stored energy, wrong fuse, or incorrect adjustment.
Preconditions: power state, grounding, warm-up, required equipment, options.
Procedure summary: concise steps from the manual.
Expected result: voltage, signal, status, or assembly isolation result.
Do not proceed if: missing equipment, damaged unit, ambiguous OCR, unverified rating.
```

---

## DOCUMENT_ROUTING_MAP

Use this map before answering detailed questions.

| User intent | Use section/chapter | Notes for LLM |
|---|---|---|
| Find frequency, amplitude, input, source, trigger, tachometer, GPIB, or environmental specs | Chapter 1 — Specifications | Preserve test conditions such as warm-up, line resolution, channel mode, averaging, and option dependencies. |
| Prepare instrument for use | Chapter 2 — Preparing the Analyzer for Use | Includes installation, power, interfaces, screen cleaning, storage, transport, and power-up problems. |
| Run operation/performance verification | Chapter 3 — Verifying Specifications | Includes semiautomated test program, manual mode, and test setups. |
| Diagnose failures | Chapter 4 — Troubleshooting the Analyzer | Prefer fault isolation logic and assembly-level conclusions; do not invent board-level repairs. |
| Perform adjustments | Chapter 5 — Adjusting the Analyzer | Service-only; warm-up and safety conditions matter. |
| Replace assemblies | Chapter 6 — Replacing Assemblies | Service-only; follow before/after replacement procedures. |
| Look up part numbers | Chapter 7 — Replaceable Parts | Confirm option-specific parts. |
| Understand circuit function | Chapter 8 — Circuit Descriptions | Useful for explaining assemblies and signal flow. |
| Find voltages, signals, connectors, or test points | Chapter 9 — Voltages and Signals | Treat OCR tables carefully; verify nearby headings. |
| Understand internal tests, fault logs, calibration routine, self-tests | Chapter 10 — Internal Test Descriptions | Good for interpreting service-test results. |
| Handle older instruments | Chapter 11 — Backdating | Use when serial/firmware/version differences are relevant. |
| Find assembly locations and block diagrams | Chapter 12 — Quick Reference | Use for navigation and service overview. |

---

## QUICK_FACTS_FOR_AGENT_RETRIEVAL

### Instrument identity

- Instrument: **Agilent/HP 35670A Dynamic Signal Analyzer**.
- Manual type: **Service Guide**.
- Agilent part number: **35670-90066**.
- Firmware target in source: **A.00.00**.
- Print date in source: **October 2011**.

### Front panel concepts

- Softkeys select items from the current screen menu.
- Hardkeys have fixed front-panel functions.
- `[Rtn]` returns to the previous menu level.
- DISPLAY keys change only what is shown on traces and do not change measurement parameters.
- MEASUREMENT keys control source, inputs, and measurement parameters; changing a measurement parameter requires a new measurement.
- Standard 2-channel units have source output and two input connectors; Option AY6 4-channel units have four input connectors.
- Input range LEDs indicate over-range and half-range conditions.

### Rear panel concepts

- The GPIB connector links the analyzer to other GPIB devices.
- Serial and parallel ports are used for plotters and printers.
- Rear SOURCE connector outputs the analyzer source signal.
- EXT TRIG accepts an external trigger.
- TACH links to a tachometer.
- DC POWER accepts nominal 12–28 Vdc.
- POWER SELECT chooses AC or DC power input.
- EXT MONITOR links to multi-sync monitors.

### Specification assumptions

Unless a specific section states otherwise, specifications apply after:

- 15 minutes warm-up,
- within 2 hours of the last self-calibration,
- with 400-line frequency resolution.

If the internal cooling fan has been turned off, specifications apply within 5 minutes of the last self-calibration.

### Selected high-value specifications

| Area | Key information |
|---|---|
| Maximum frequency range | 1-channel: 102.4 kHz or 51.2 kHz depending on option; 2-channel: 51.2 kHz; 4-channel Option AY6: 25.6 kHz. |
| Frequency accuracy | ±30 ppm, equivalent to ±0.003%. |
| Input range | +27 dBVrms to −51 dBVrms in 2 dB steps. |
| Maximum input level | 42 Vpk. |
| Input impedance | 1 MΩ ±10%, 90 pF nominal. |
| Floating common-mode range | ±4 Vpk. |
| External trigger maximum input | ±42 Vpk. |
| Tachometer input | 0.5 to 2048 pulses/revolution; maximum pulse rate 400 kHz. |
| Source output types | Sine, random noise, chirp, pink noise, burst random, burst chirp. |
| Source amplitude | AC up to ±5 V peak; DC up to ±10 V, subject to combined AC/DC limits. |
| Source output impedance | <5 Ω. |
| GPIB factory address | 11. |
| GPIB standards | IEEE 488.1, IEEE 488.2-1987, SCPI 1992. |

---

## TASK_TEMPLATES_FOR_LLM

### Template: specification answer

```text
Specification: <name>
Value: <value>
Conditions: <warm-up, channel mode, span, option, averaging, range>
Caveats: <typical/non-warranted/option dependency/OCR uncertainty>
Manual section: <chapter/section>
```

### Template: troubleshooting answer

```text
Symptom: <reported symptom>
Relevant section: Chapter 4 — Troubleshooting the Analyzer
Safety: <operator-safe or service-only>
Initial checks: <inspection, power, connectors, self-test, logs>
Procedure path: <manual procedure names>
Expected result: <reading or state>
If abnormal: <probable assembly or next manual branch>
Do not infer: component-level repair unless the manual explicitly states it.
```

### Template: adjustment answer

```text
Adjustment: <name>
Relevant section: Chapter 5 — Adjusting the Analyzer
Safety: service-only; trained personnel required.
Required warm-up: one hour before adjustments.
Required equipment: see Chapter 1 recommended test equipment.
Procedure summary: <steps only from manual>
Expected result: <target reading or tolerance>
Risk: incorrect adjustment can appear as a hardware failure.
```

### Template: assembly replacement answer

```text
Assembly: <assembly name>
Relevant section: Chapter 6 — Replacing Assemblies
Safety: service-only.
Before replacement: follow the manual’s before-replacement procedure.
After replacement: follow the manual’s after-replacement procedure.
Caveats: firmware, calibration, NVRAM, option configuration, and adjustment may be affected.
```

---

## PROCEDURE_INDEX_AUTODETECTED_FROM_MARKDOWN

The following list was extracted from headings beginning with `To ...` in the converted Markdown. Because the source is OCR/conversion-derived, verify critical steps in the full section.

### Preparation and installation

- To do the incoming inspection
- To install the analyzer
- To connect the analyzer to a dc power source
- To change the fuses
- To connect the analyzer to a serial device
- To connect the analyzer to a parallel device
- To connect the analyzer to an GPIB device
- To connect the analyzer to an external monitor
- To connect the optional keyboard
- To connect the microphone adapter
- To clean the screen
- To store the analyzer
- To transport the analyzer
- To troubleshoot DIN connector failures

### Verification and test setup

- To load the program
- To run the program in semiautomated mode
- To run the program without a printer
- To run the program in manual mode
- To set up the self test
- To set up the dc offset test
- To set up the noise test
- To set up the spurious signals test
- To set up the amplitude accuracy test
- To set up the flatness test
- To set up the amplitude linearity test
- To set up the A-weight filter test
- To set up the channel match test
- To set up the frequency accuracy test
- To set up the anti-alias filter test
- To set up the input coupling test
- To set up the harmonic distortion test
- To set up the intermodulation distortion test
- To set up the cross talk test
- To set up the single channel phase accuracy test
- To set up the external trigger test
- To set up the tach function test
- To set up the input resistance test
- To set up the ICP supply test
- To set up the source amplitude accuracy test
- To set up the source output resistance test
- To set up the source dc offset test
- To set up the source flatness test
- To set up the source distortion test

### Troubleshooting and self-tests

- To perform initial verification
- To troubleshoot the power supply
- To troubleshoot power-up failures
- To troubleshoot CPU, memory, and buses failures
- To troubleshoot display failures
- To troubleshoot IIC bus failures
- To troubleshoot fast bus failures
- To perform self tests
- To troubleshoot self-test lockup failures
- To troubleshoot intermittent failures
- To troubleshoot performance test failures
- To troubleshoot source and calibrator failures
- To troubleshoot input and ADC failures
- To troubleshoot input failures on four channel analyzers
- To troubleshoot distortion failures
- To troubleshoot disk drive failures
- To troubleshoot auto-range failures
- To troubleshoot DIN connector failures
- To troubleshoot trigger failures
- To troubleshoot memory battery failures
- To troubleshoot microphone power and adapter failures
- To troubleshoot tachometer failures

### Adjustments

- To adjust the frequency reference
- To adjust the source
- To adjust the ADC gain, offset and reference

### Replacement / disassembly candidates

- No procedure headings detected in this category.

---

## OCR_AND_CONVERSION_NOTES

The source Markdown was converted from a PDF and contains OCR artifacts. Common issues:

- broken softkey notation split across lines,
- tables converted into plain text blocks,
- missing hyphenated page numbers,
- footer or reseller text repeated in the original PDF conversion,
- symbols such as Ω, µ, ±, ≤, ≥, and dB values may require manual verification,
- service procedures may have step labels such as `q Step`, caused by bullet conversion.

When precision matters, use the nearby heading, chapter, and context to validate the value before using it in code, calibration, repair instructions, or safety-relevant answers.

---

## CROSS_REFERENCE_WITH_PROGRAMMING_GUIDE

Use this Service Guide for:

- installation,
- verification,
- troubleshooting,
- adjustment,
- assemblies,
- parts,
- circuits,
- voltages and signals,
- self-tests and fault logs.

Use the GPIB Programming Guide for:

- SCPI/GPIB command syntax,
- remote programming,
- binary/ASCII data transfer,
- status registers from the remote-control perspective,
- command synchronization.

If the user asks for both a manual front-panel procedure and remote-control automation, combine this file with the optimized programming guide, but keep the distinction explicit.

---

## ORIGINAL_CONVERTED_TEXT_CLEANED_FOR_SEARCH

The following section preserves the converted manual text after light cleanup of repeated reseller footer lines and removal of the initial reseller advertisement. It remains the detailed source for retrieval.

Agilent 35670A Service Guide

Agilent Part Number: 35670 - 90066

For instruments with firmware version A.00.

Printed in Malaysia

Print Date: October 2011

Copyright © Agilent Technologies, Inc. 1992- 2011

All Rights Reserved


The Agilent 35670A at a Glance (Front Panel)


Agilent 35670A Front Panel

## 1-Use the softkeys to select items from the current menu. A softkey’s function is indicated by a video label on the analyzer’s screen.

Throughout this book, softkeys are printed like this: [
FFT ANALYSIS

```
].
```
Hardkeys are front-panel buttons whose functions are always the same. They have a label printed directly on the key itself.

Throughout this book, hardkeys are printed like this: [
Inst Mode

```
].
```
## 2-The analyzer’s screen is divided into the menu area and the display area. The menu area displays video labels for the softkeys. The

data area displays measurement data and information about the parameter settings.

## 3-The [

Rtn

```
] key returns the menu to the previous level.
```
## 4-The POWER switch turns on the analyzer.

## 5-Use the SYSTEM keys to control various system-level functions. These functions include saving files, plotting measurement data,

and accessing online help.

## 6-Use the disk drive to save your work on 3.5 inch flexible disks.

## 7-The knob moves the markers and the cursor. It also steps through numeric values and scrolls through online help.

## 8-Use the DISPLAY keys to control what appears on the analyzer’s traces. They only affect how data is displayed; DISPLAY keys

do not change measurement parameters. _You can press keys in the DISPLAY menus without losing measurement parameters._

## 9-Use the MARKER keys to select a variety of marker features.

## 10-Use the MEASUREMENT keys to control the analyzer’s source and inputs. They also control measurement parameters. You

_must make a new measurement if you change a MEASUREMENT parameter._

## 11-Use the numeric-entry keys to enter a numeric value.

## 12-The microphone power connector provides power (8 Vdc) for the Microphone Adapter Kit (Option UK4).

## 13-The connector area of the front panel has two different configurations. The standard analyzer has a source output connector and

two input connectors. The 4-channel analyzer (Option AY6) has four input connectors.

Range indicators are located next to each input connector. The upper LED is the over range indicator (the signal level exceeds the

current range setting). The lower LED is the half range indicator (the signal level exceeds half the current range setting).

## 14-A source on/off indicator is located at the left edge of the connector area.

The standard Agilent 35670A (2 channel) has a source connector on the front panel.


The Agilent 35670A at a Glance (Rear Panel)


Agilent 35670A Rear Panel

## 1-The GPIB connector links the Agilent 35670A to other GPIB devices. GPIB parameters are set in the[

```
Local/GPIB
```
```
] and
```
[
Plot/Print

```
] menus.
```
## 2-The SERIAL PORT and the PARALLEL PORT link the analyzer to plotters and printers. These parameters are set in the

[
Plot/Print

```
] menu.
```
## 3-The SOURCE connector outputs the analyzer’s source signal. An LED on the front panel indicates if the source is on or off. The

source parameters are set in the [Source] menu.

The standard Agilent 35670A (2 channel) also has a source connector on the front panel.

## 4-The EXT TRIG connector links the analyzer to an external trigger signal. The external trigger parameters are set in the[Trigger]

menu.

## 5-The TACH connector links the analyzer to a tachometer. The tachometer parameters are set in the [

```
Input
```
```
] menu.
```
## 6-The KEYBOARD connector attaches an optional keyboard to the analyzer.

## 7-The DC POWER connector accepts DC power levels from 12 - 28 Vdc (nominal).

## 8-The AC POWER connector accept a wide range of ac voltage levels.

## 9-The POWER SELECT switch determines whether the analyzer is powered via the AC POWER connector or the DC POWER

connector.

## 10-The EXT MONITOR port links the analyzer to multi-sync monitors.


The following general safety precautions must be observed during all phases of

operation of this instrument. Failure to comply with these precautions or with

specific warnings elsewhere in this manual violates safety standards of design,

manufacture, and intended use of the instrument. Agilent Technologies, Inc.

assumes no liability for the customer’s failure to comply with these

requirements.

**GENERAL**

This product is a Safety Class 1 instrument (provided with a protective earth

terminal). The protective features of this product may be impaired if it is used in

a manner not specified in the operation instructions.

All Light Emitting Diodes (LEDs) used in this product are Class 1 LEDs as per

IEC 60825-1.

**ENVIRONMENTAL CONDITIONS**

This instrument is intended for indoor use in an installation category II, pollution

degree 2 environment. It is designed to operate at a maximum relative humidity

for the ac mains voltage requirements and ambient operating temperature range.

**BEFORE APPLYING POWER**

Verify that the product is set to match the available line voltage, the correct fuse

is installed, and all safety precautions are taken. Note the instrument’s external

markings described under Safety Symbols.

**GROUND THE INSTRUMENT**

To minimize shock hazard, the instrument chassis and cover must be connected

to an electrical protective earth ground. The instrument must be connected to

the ac power mains through a grounded power cable, with the ground wire

firmly connected to an electrical ground (safety ground) at the power outlet.

Any interruption of the protective (grounding) conductor or disconnection of

the protective earth terminal will cause a potential shock hazard that could

result in personal injury.

**_Safety Summary_**

of 95% and at altitudes of up to 4600 meters. Refer to the specifications tables


**FUSES**

Only fuses with the required rated current, voltage, and specified type (normal

blow, time delay, etc.) should be used. Do not use repaired fuses or

short-circuited fuse holders. To do so could cause a shock or fire hazard.

**DO NOT OPERATE IN AN EXPLOSIVE ATMOSPHERE**

Do not operate the instrument in the presence of flammable gases or fumes.

**DO NOT REMOVE THE INSTRUMENT COVER**

Operating personnel must not remove instrument covers. Component

replacement and internal adjustments must be made only by qualified service

personnel.

Instruments that appear damaged or defective should be made inoperative and

secured against unintended operation until they can be repaired by qualified

service personnel.

**WARNING The WARNING sign denotes a hazard. It calls attention to a procedure,**

**practice, or the like, which, if not correctly performed or adhered to,**

**could result in personal injury. Do not proceed beyond a WARNING**

**sign until the indicated conditions are fully understood and met.**

## Caution The CAUTION sign denotes a hazard. It calls attention to an operating

procedure, or the like, which, if not correctly performed or adhered to, could

result in damage to or destruction of part or all of the product. Do not proceed

beyond a CAUTION sign until the indicated conditions are fully understood and

met.


Accessories

The accessories listed in the following table are supplied with the

Agilent 35670A.

Supplied Accessories Part Number

Line Power Cable See page 2-

Standard Data Format Utilities HP 5061-

_Agilent 35670A Operator’s Guide_ Agilent35670-

_Agilent 35670A Quick Start_ Agilent 35670-

_Agilent 35670A Installation and Verification Guide_ Agilent 35670-

_Agilent 35670A GPIB Command Reference_ Agilent 35670-

_GPIB Programmer’s Guide_ Agilent 5960-

_Agilent 35670A GPIB Commands: Quick Reference_ Agilent 35670-

The accessories listed in the following table are available for the

Agilent 35670A.

Available Accessories Part Number

DC Power Cable, 3 meter HP 35250A

DC Power Cable with Cigarette Lighter Adapter HP 35251A

Box of ten 3.5-inch double-sided, double-density disks HP 92192A

_Using Instrument BASIC with the Agilent 35670A_ Agilent 35670-

_Instrument BASIC User’s Handbook_ HP E2083-

HP Thinkjet Printer HP 2225A

HP Quietjet Printer HP 2227A

HP Jet Paper, 2500 sheets HP 92261N

GPIB Cable, 1 meter HP 10833A

GPIB Cable, 2 meter HP 10833B

GPIB Cable, 4 meter HP 10833C

GPIB Cable, 0.5 meter HP 10833D


In This Book

This guide provides instructions for installing, verifying performance, and repairing

the Agilent 35670A Dynamic Signal Analyzer.

Chapter 1, ‘’Specifications,’’ lists the specifications for the Agilent 35670A and the

specifications for the required test equipment.

Chapter 2, ‘’Preparing the Analyzer for Use,’’ provides step-by-step instructions for

getting the analyzer ready to use and instructions on cleaning the screen, storing, and

transporting.

Chapter 3, ‘’Verifying Specifications,’’ provides step-by-step instructions for

installing and running the semiautomated performance test software. This chapter also

provides illustrations that show the equipment set up for each test and a copy of the

test records.

Chapter 4, ‘’Troubleshooting the Analyzer,’’ provides step-by-step instructions for

isolating most failures to the faulty assembly.

Chapter 5, ‘’Adjusting the Analyzer,’’ provides step-by-step instructions for adjusting

the analyzer.

Chapter 6, ‘’Replacing Assemblies,’’ provides step-by-step instructions to follow

before and after replacing an assembly. This chapter also provides step-by-step

instructions for disassembling the analyzer.

Chapter 7, ‘’Replaceable Parts,’’ provides ordering information and lists the

replaceable parts.

Chapter 8, ‘’Circuit Descriptions,’’ provides the overall instrument description and

individual assembly descriptions.

Chapter 9, ‘’Voltages and Signals,’’ shows where the signals and voltages are used in

the analyzer and describes each signal.

Chapter 10, ‘’Internal Test Descriptions,’’ describes the power-on test, calibration

routine, fault log messages, and self tests.

Chapter 11, ‘’Backdating,’’ provides information necessary to modify this manual for

instruments that differ from those currently being produced.

Chapter 12, ‘’Quick Reference,’’ shows assembly locations, cable connections, and all

the block diagrams.


## Table of Contents

## Tachometer 1-

## Source Output 1-


## To connect the analyzer to a serial device 2-

## To connect the analyzer to a parallel device 2-

## To connect the analyzer to an GPIB device 2-

## To run the program in manual mode 3-


## To remove power supply 6-


- Frequency 1- 1 Specifications
- Single Channel Amplitude 1-
- FFT Dynamic Range 1-
- Input Noise 1-
- Window Parameters 1-
- Single Channel Phase 1-
- Cross Channel Amplitude 1-
- Cross Channel Phase 1-
- Input 1-
- Time Domain 1-
- Trigger 1-
- Tachometer 1-
- Source Output 1-
- Digital Interfaces 1-
- General Specifications 1-
- Order Tracking Option 1D0 1-
- Swept Sine Measurements Option 1D2 1-
- Arbitrary Waveform Source Option 1D4 1-
- Real Time Octave Analysis Option 1D1 1-
- Recommended Test Equipment 1-
- To do the incoming inspection 2- 2 Preparing the Analyzer for Use
- To install the analyzer 2-
- To connect the analyzer to a dc power source 2-
- To change the fuses 2-
- To connect the analyzer to a serial device 2-
- To connect the analyzer to a parallel device 2-
- To connect the analyzer to an GPIB device 2-
- To connect the analyzer to an external monitor 2-
- To connect the optional keyboard 2-
- To connect the microphone adapter 2-
- To clean the screen 2-
- To store the analyzer 2-
- To transport the analyzer 2-
- If the analyzer will not power up 2-
- If the analyzer operates intermittently on dc power 2-
- To load the program 3- 3 Verifying Specifications
- To run the program in semiautomated mode 3-
- To run the program without a printer 3-
- To run the program in manual mode 3-
- To set up the self test 3-
- To set up the dc offset test 3-
- To set up the noise test 3-
- To set up the spurious signals test 3-
- To set up the amplitude accuracy test 3-
- To set up the flatness test 3-
- To set up the amplitude linearity test 3-
- To set up the A-weight filter test 3-
- To set up the channel match test 3-
- To set up the frequency accuracy test 3-
- To set up the anti-alias filter test 3-
- To set up the input coupling test 3-
- To set up the harmonic distortion test 3-
- To set up the intermodulation distortion test 3-
- To set up the cross talk test 3-
- To set up the single channel phase accuracy test 3-
- To set up the external trigger test 3-
- To set up the tach function test 3-
- To set up the input resistance test 3-
- To set up the ICP supply test 3-
- To set up the source amplitude accuracy test 3-
- To set up the source output resistance test 3-
- To set up the source dc offset test 3-
- To set up the source flatness test 3-
- To set up the source distortion test 3-
- Measurement Uncertainty 3-
- Performance Test Record - Two Channel 1 of
- Performance Test Record - Four Channel 1 of
- Operation Verification Test Record - Two Channel 1 of
- Operation Verification Test Record - Four Channel 1 of
- How to troubleshoot the analyzer 4- 4 Troubleshooting the Analyzer
- To perform initial verification 4-
- To troubleshoot the power supply 4-
- To troubleshoot power-up failures 4-
- To troubleshoot CPU, memory, and buses failures 4-
- To troubleshoot display failures 4-
- To troubleshoot IIC bus failures 4-
- To troubleshoot fast bus failures 4-
- To perform self tests 4-
- To troubleshoot self-test lockup failures 4-
- To troubleshoot intermittent failures 4-
- To troubleshoot performance test failures 4-
- To troubleshoot source and calibrator failures 4-
- To troubleshoot input and ADC failures 4-
- To troubleshoot input failures on four channel analyzers 4-
- To troubleshoot distortion failures 4-
- To troubleshoot disk drive failures 4-
- To troubleshoot auto-range failures 4-
- To troubleshoot DIN connector failures 4-
- To troubleshoot trigger failures 4-
- To troubleshoot memory battery failures 4-
- To troubleshoot microphone power and adapter failures 4-
- To troubleshoot tachometer failures 4-
- To adjust the frequency reference 5- 5 Adjusting the Analyzer
- To adjust the source 5-
- To adjust the ADC gain, offset and reference 5-
- To adjust the input dc offset 5-
- To adjust common mode rejection 5-
- To adjust filter flatness 5-
- To adjust the display voltage 5-
- What to do before replacing the CPU assembly 6- 6 Replacing Assemblies
- What to do after replacing an assembly 6-
- To remove cover 6-
- To remove rear panel 6-
- To remove front panel 6-
- To remove disk drive 6-
- To remove CPU 6-
- To remove NVRAM 6-
- To remove memory 6-
- To remove power supply 6-
- To remove motherboard 6-
- To remove dc-dc converter 6-
- Ordering Information 7- 7 Replaceable Parts
- Assemblies 7-
- Cables 7-
- Instrument Covers and Handles 7-
- Assembly Covers and Brackets 7-
- Front Panel Parts 7-
- Rear Panel Parts 7-
- Chassis Parts 7-
- Screws, Washers, and Nuts 7-
- Miscellaneous Parts 7-
- Option UK4 Parts 7-
- Overall Instrument Description 8- 8 Circuit Descriptions
- A1 Input 8-
- A2 Input 8-
- A5 Analog 8-
- A6 Digital 8-
- A7 CPU 8-
- A8 Memory 8-
- A9 NVRAM 8-
- A10 Rear Panel 8-
- A11 Keyboard Controller 8-
- A12 BNC 8-
- A13 Primary Keypad 8-
- A14 Secondary Keypad 8-
- A15 Primary Keypad 8-
- A22 BNC 8-
- A90 Fan 8-
- A98 Power Supply 8-
- A99 Motherboard 8-
- A100 Disk Drive 8-
- A101 Display 8-
- A102 DC-DC Converter 8-
- Option UK4 Microphone Adapter and Power Supply 8-


9 Voltages and Signals

## Assembly Locations and Connections 9-

## Power Supply Voltage Distribution 9-

## A1 Input 8-

## A2 Input 8-

## A8 Memory 8-

## A9 NVRAM 8-

## Rear Panel Parts 7-

## A11 Keyboard Controller 8-

## A12 BNC 8-

## A13 Primary Keypad 8-

## A14 Secondary Keypad 8-

## A22 BNC 8-

## A99 Motherboard 8-

## A100 Disk Drive 8-

## A101 Display 8-

## A102 DC-DC Converter 8-

10 Internal Test Descriptions

## Power-on Test Description 10-

## Calibration Routine Description 10-

## Fault Log Messages 10-

## Self-Test Descriptions 10-

11 Backdating

12 Quick Reference

Index

Guide to Agilent 35670A Documentation

Need Assistance?


# 1

## Specifications

1-


Specifications

## This chapter contains the specifications for the Agilent 35670A Dynamic

## Signal Analyzer and the critical specifications for the equipment required to

## test the Agilent 35670A.

## Instrument specifications apply after 15 minutes warm-up and within 2 hours of

## the last self-calibration. When the internal cooling fan has been turned OFF,

## specifications apply within 5 minutes of the last self-calibration. All

## specifications are with 400 line frequency resolution unless stated otherwise.

## Four channel instruments are unspecified in the one channel mode where alias

## protection filters are not connected.

## Abbreviations

dBVrms = dB relative to 1 Volt rms.

dBfs = dB relative to full scale amplitude range. Full scale is approximately 2 dB below ADC

overload.

FS or fs Full scale; synonymous with input range.

Real Time or Online = Refer to the collecting and displaying of information with no dropouts

or missing information.

Rload = Load resistance connected to the analyzer’s source.

Typical = Typical, non-warranted, performance specification included to provide general

product information.

Vpk = Peak of the ac voltage.

1-2


Frequency

```
Maximum range
```
```
1 channel mode
```
```
2 channel mode
```
```
4 channel mode (option AY6 only)
```
```
102.4 kHz, 51.2 kHz (option AY6†)
```
```
51.2 kHz
```
```
25.6 kHz
```
```
Spans
```
```
1 channel mode
```
```
2 channel mode
```
```
4 channel mode (option AY6 only)
```
```
195.3 mHz to 102.4 kHz
```
```
97.7 mHz to 51.2 kHz
```
```
48.8 mHz to 25.6 kHz
```
```
Minimum resolution
```
```
1 channel mode
```
```
2 channel mode
```
```
4 channel mode (option AY6 only)
```
```
122 mHz (1600 line display)
```
```
61 mHz (1600 line display)
```
```
61 mHz (800 line display)
```
```
Maximum real-time bandwidth (FFT span for continuous data acquistion) (preset, fast averaging)
```
```
1 channel mode
```
```
2 channel mode
```
```
4 channel mode (option AY6 only)
```
```
25.6 kHz
```
```
12.8 kHz
```
```
6.4 kHz
```
```
Measurement rate (typical) (preset, fast averaging)
```
```
1 channel mode
```
```
2 channel mode
```
```
4 channel mode (option AY6 only)
```
```
≥70 averages/second (≥170 with 100 line display)
```
```
≥33 averages/second
```
```
≥15 averages/second
```
```
Display update rate (typical)
```
```
(preset, fast average off)
```
```
5 updates/second
```
```
9 updates/second (single channel, single display,
```
```
undisplayed traces set with static data: e.g., data
```
```
register)
```
```
Accuracy
```
±30 ppm (±0.003%)

† Option AY6 single channel maximum range extends to 102.4 kHz without anti alias filter protection.

Agilent 35670A Specifications

Frequency

1-3


Single Channel Amplitude

```
Absolute amplitude accuracy (FFT)
```
```
(A combination of full scale accuracy, full
```
```
scale flatness, and amplitude linearity.)
```
±2.92% (0.25 dB) of reading

±0.025% of full scale

```
FFT full scale accuracy at 1 kHz (0 dBfs)
```
±0.15 dB (1.74%)

```
FFT full scale flatness (0 dBfs) relative to 1
```
```
kHz
```
±0.2 dB (2.33%)

```
FFT amplitude linearity at 1 kHz
```
```
Measured on +27 dBVrms range with time
```
```
average, 0 to−80 dBfs.
```
±0.58% (0.05 dB) of reading

±0.025% of full scale

```
Amplitude resolution (16 bits less 2 dB over-range)
```
```
with averaging
```
```
0.0019% of full scale (typical)
```
```
Residual dc response
```
```
FFT mode frequency display
```
```
(excludes A-weight filter)
```
```
<−30 dBfs or 0.5 mVdc (whichever is greater)
```
Specifications Agilent 35670A

Single Channel Amplitude

1-4


FFT Dynamic Range

Spurious free dynamic range

(Includes spurs, harmonic distortion,

intermodulation distortion, alias products)

Excludes alias responses at extremes of span.

Source impedance = 50Ω

<−80 dBfs (90 dB typical)

FFT noise floor (typical)

Flat top window, 64 RMS averages

Harmonic distortion

Single tone (in band),≤0 dBfs

<−80 dBfs

Post-filter harmonic distortion (alias

responses) of a single tone≤102.4 kHz,≤ 0

dBfs

<−80 dBfs

Intermodulation distortion

Two tones (in-band), each≤−6.02 dBfs

<−80 dBfs

Spurious and residual responses

Source impedance = 50Ω

<−80 dBfs

Frequency alias responses

Single tone (out of displayed range),

≤0 dBfs,≤1 MHz (≤200 kHz with ICP on)

2.5% to 97.5% of the frequency span

Lower and upper 2.5% of frequency span

<−80 dBfs

<−65 dBfs

Agilent 35670A Specifications

FFT Dynamic Range

1-5


Input Noise

Input noise level

Flat top window,−51 dBVrms range, source impedance = 50Ω, 32 rms averages

Above 1280 Hz

160 Hz to 1.28 kHz (6.4 kHz span)

<–140 dBVrms/√

—

Hz

<–130 dBVrms/√

—

Hz<%0 >

Note: To calculate noise as dB below full scale:

```
Noise [dBfs] Noise [dBVrms/ Hz ] + 10LOG(NEBW) Range [dBVrms].
```
```
See ‘’Window Parameters,’’ below, for noise equivalent bandwidths (NEBW).
```
Window Parameters

Uniform Hann Flat Top

−3 dB bandwidth †

Noise equivalent bandwidth †

Attenuation at±1/2 bin

Shape factor (−60 dB BW/−3dBBW)

0.125% of span

0.125% of span

4.0 dB

716

0.185% of span

0.1875% of span

1.5 dB

9.1

0.450% of span

0.4775% of span

0.01 dB

2.6

† For 800 line displays. With 400, 200, or 100 line displays, multiply bandwidths by 2, 4, and 8,

respectively. With 1600 line displays (only available in 1 or 2 channel mode), divide bandwidths by 2.

Single Channel Phase

Phase accuracy relative to external trigger

16 RMS averages, center of bin, dc coupled,

0 dBfs to−50 dBfs, 0 Hz < freq≤10.24 kHz only

±4.0 degree

For Hann and flat top windows, phase is referenced to a cosine wave at the center of the time

record. For the uniform, force, and exponential windows, phase is referenced to a cosine wave

at the beginning of the time record.

Specifications Agilent 35670A

Input Noise

1-6


Cross Channel Amplitude

```
FFT cross channel gain accuracy
```
```
Frequency response mode, same amplitude range
```
```
(AC coupled, Peroidic Chirp, Uniform Window, < =4Hz)
```
```
At full scale: Tested with 10 rms averages
```
```
on the−11 to +27 dBvrms ranges, and 100 rms
```
```
averages on the−51 dBVrms range
```
±0.04 dB (0.46%)

```
At−20 dBfs: Tested with 200 rms averages on
```
```
the−11 to +27 dBVrms ranges, and 2000 rms
```
```
averages on the−51 dBVrms range
```
±0.08 dB (0.92%)

Cross Channel Phase

```
Cross channel phase accuracy
```
```
(same conditions as cross-channel amplitude)
```
±0.5 degree

Agilent 35670A Specifications

Cross Channel Amplitude

1-7


Input

Input ranges

(full scale) (auto-range capability)

+27 dBVrms (31.7 Vpk) to−51 dBVrms

(3.99 mVpk) in 2 dB steps

Maximum input levels 42 Vpk

```
Input impedance
1MΩ±10%, 90 pF nominal
```
Low side to chassis impedance

Floating mode

Grounded mode

1MΩ±30%, <0.010μF (typical)

≤ 100 Ω

AC coupling rolloff <3 dB rolloff at 1 Hz

Common mode rejection ratio

Single tone at or below 1 kHz

–51 dBVrms to –11 dBVrms ranges

–9 dBVrms to +9 dBVrms ranges

+11 dBVrms to +27 dBVrms ranges

>75 dB typical

>60 dB typical

>40 dB typical

Note: CM dBfs = CM signal input [dBVrms]−CMRR [dB]−range [dBVrms]

```
Common mode range (floating mode)
±4 Vpk
```
Amplitude over-range detection +3 dB typical

ICP signal conditioning

Current source

Open circuit voltage

4.25 ±1.5 mA

+26 to +32 Vdc

A-weight filter

Conforms to ANSI Standard S1.4-1983; and

to IEC 651-1979; 10 Hz to 25.6 kHz

Type 0 Tolerance

Crosstalk

Between input channels, and source-to-input

(receiving channel source impedance = 50Ω)

<–135 dB below signal or <–80 dBfs of

receiving channel, whichever response is

greater in amplitude

Specifications Agilent 35670A

Input

1-8


Time Domain

```
Specifications apply in histogram/time mode, unfiltered time display
```
```
DC amplitude accuracy
```
±5.0%fs

```
Rise time of−1 V to 0 V test pulse
```
```
<11.4 ms
```
```
Settling time of−1 V to 0 V test pulse
```
```
<16 ms to 1%
```
```
Pulse aberrations (peak overshoot)
```
```
of−1 V to 0 V test pulse
```
```
Peak aberration relative to the mode-to-mode
```
```
difference (most common values)
```
```
<3 %
```
```
Sampling period
```
```
1 channel mode
```
```
2 channel mode
```
```
4 channel mode (option AY6 only)
```
```
3.815 ms (1/262144 Hz) to2sin2×steps
```
```
7.629 ms (1/131072 Hz) to4sin2×steps
```
```
15.26 ms (1/65536 Hz) to8sin2×steps
```
Trigger

```
Trigger modes Internal trigger
```
```
External trigger
```
```
Source trigger
```
```
GPIB trigger
```
```
Maximum trigger delay
```
```
Post trigger
```
```
Pre trigger
```
```
No two channels can be further than ±7168 samples
```
```
from each other.
```
```
8191 seconds
```
```
8191 sample periods
```
```
External trigger maximum input
```
±42 Vpk

```
External trigger range
```
```
Low range
```
```
High range
```
```
−2Vto+2V
```
```
−10 V to +10 V
```
```
External trigger resolution
```
```
Low range
```
```
High range
```
```
15.7 mV
```
```
78 mV
```
Agilent 35670A Specifications

Time Domain

1-9


Tachometer

Pulses per revolution 0.5 to 2048

```
RPM accuracy
±100 ppm (0.01%) (typical)
```
Tachometer level range

Low range

High range

–4Vto+4V

–20 V to +20 V

Tachometer level resolution

Low range

High range

100 mV

500 mV

Tachometer level accuracy (as a % of

tachometer range setting)

±10% of range

```
Maximum tachometer input level
±42 Vpk
```
Minimum tachometer pulse width 600 ns

Maximum tachometer pulse rate 400 kHz

Specifications Agilent 35670A

Tachometer

1-10


Source Output

```
Source types Sine, random noise, chirp, pink noise, burst
```
```
random, burst chirp
```
```
Amplitude range
```
ac:±5 V peak †

dc:±10V†

```
† Vac
pk
```
```
+ |Vdc|≤10 V
```
```
AC amplitude resolution
```
Voltage≥0.2 Vrms

```
Voltage < 0.2 Vrms
```
```
2.5 mVpk
```
```
0.25 mVpk
```
```
DC offset accuracy
```
```
±15 mV±3% of ( |Vdc| +Vac
pk
```
```
) settings
```
```
Pink noise adder Add 600 mV typical when using pink noise
```
```
Output impedance
```
<5Ω

```
Maximum loading
```
```
Current
```
```
Capacitance
```
±20 mA peak

```
0.01 mF
```
```
Sine amplitude accuracy at 1 kHz
```
Rload >250Ω

```
0.1 Vpk to 5 Vpk
```
±4% (0.34 dB) of setting

```
Sine flatness (relative to 1 kHz)
```
```
0.1 V to 5 V peak, 0 Hz to 102.4 kHz
```
±1dB

```
Harmonic and sub-harmonic distortion and spurious signals (in band)
```
```
0.1 Vpk to 5 Vpk sine wave
```
```
Fundamental <30 kHz
```
```
Fundamental≥30 kHz
```
```
<−60 dBc
```
```
<−40 dBc
```
Agilent 35670A Specifications

Source Output

1-11


Digital Interfaces

External keyboard Compatible with PC-style 101-key keyboard

model number HP C1405A (#ABA) (DIN

connector) and HP keyboard cable part

number 5081-2249.

GPIB Conforms to the following standards: IEEE

488.1 (SH1, AH1, T6, TEO, L4, LE0, RS1,

RL1, PP0, DC1, DT1, C1, C2, C3, C12, E2)

IEEE 488.2-1987

Complies with SCPI 1992

Factory set address: 11

Data transfer rate

(REAL 64 Format)

<45 ms for a 401 point trace

Serial port (printing, plotting) 300 baud to 9600 baud

Parallel port (printing, plotting)

Specifications Agilent 35670A

Digital Interfaces

1-12


Agilent 35670A Specifications

General Specifications

1-13

General Specifications

```
Safety Standards IEC61010-1:2001/EN61010-1:2001 (2nd Edition)
```
```
Canada: CAN/CSA-C22.2 No. 61010.1-2004
```
```
USA: ANSI/UL 61010-1:2004
```
```
EMC Standards Canada: ICES-001:2004
```
```
IEC 61326-1:2005/EN61326-1:2006
```
```
Australia/New Zealand: AS/NZS CISPR11:2004
```
```
Acoustics LpA <55 dB (cooling fan at high speed setting)
```
```
LpA <45 dB (auto speed setting at 25 °C)
```
```
Fan speed setting of high, automatic, and off are available. The fan off setting can be
```
```
enabled for a short period of time, except at higher ambient temperatures where the fan
```
```
will stay on.
```
```
Environmental
```
```
Operating Restrictions
```
```
Operating:
```
```
Disk in Drive
```
```
Operating:
```
```
No Disk in Drive
```
```
Storage and
```
```
Transport
```
```
Ambient Temperature 4 °C to 45 °C 0 °C to 55 °C –40 °C to 70 °C
```
```
Relative Humidity (non-condensing)
```
```
Minimum 20% 15% 5%
```
```
Maximum 80% at 32 °C 95% at 40 °C 95% at 50 °C
```
```
Vibration (5 – 500 Hz) 0.6 Grms 2.1 Grms 3.41 Grms
```
```
Shock 5 G
```
```
(10 ms 1/2 sine)
```
```
5 G
```
```
(10 ms 1/2 sine)
```
```
40 G
```
```
(3 ms 1/2 sine)
```
```
Maximum Altitude 4600 meters (15,000 feet)
```
```
AC Power 100 Vrms to 240 Vrms (47 Hz to 440 Hz)
```
```
350 VA maximum
```
```
DC Power 12 Vdc to 28 Vdc nominal
```
```
200 VA maximum
```
```
DC Current at 12V (typical) 10 A (standard)
```
```
12 A (4 Channel, Option AY6)
```
```
Warm-Up Time 15 minutes
```
```
Weight 15 kg (33 lbs) net
```
```
29 kg (64 lbs) shipping
```
```
Dimensions
```
```
(excluding bail handle and
```
```
impact cover)
```
```
Height: 190 mm (7.5 in)
```
```
Width: 340 mm (13.4 in)
```
```
Depth: 465 mm (18.3 in)
```
```
IEC 801-3 (Radiated Immunity): Performance degradation may occur at Security Level 2.
```

Order Tracking — Option 1D0

_Max Order Max RPM_

_60_

×

≤

Real time (online)

1 channel mode

2 channel mode

4 channel mode

25,600 Hz

12,800 Hz

6,400 Hz

Capture playback †

1 channel mode

2 channel mode

4 channel mode

102,400 Hz

51,200 Hz

25,600 Hz

Specified for

5 ≤RPM≤60,000 (online), 5≤RPM≤491,519 (capture playback); and

number of orders≤ 200

† Signals are captured online and then postprocessed in capture playback mode.

Delta order 1/128 to 1/1

Resolution

(maximum order)/(delta order)

≤ 200

Maximum RPM ramp rate

1000 to 10,000 RPM run up

maximum order = 10

delta order = 0.1

RPM step = 30 (1 channel)

= 60 (2 channel)

= 120 (4 channel)

750 RPM/second (typical for real time)

```
Order track amplitude accuracy
±1 dB (typical)
```
Specifications Agilent 35670A

Order Tracking — Option 1D0

1-14


Swept Sine Measurements —Option 1D2

Dynamic range

Default span: 51.2 Hz to 51.2 kHz

Fast average ON, 101 point log sweep

Tested with 11 dBVrms source level at 100 ms

integration (approximately 60 second sweep)

130 dB typical

Arbitrary Waveform Source—Option 1D4

Amplitude Range Arb: ±5 Vpk †

dc: ±10 V †

```
†V
pk
```
+|Vdc|≤10 V

Record Length

Depends on measurement resolution (100,

200, 400, 800, and 1600 lines)

# of points = 2.56 x lines of resolution, or # of

complex points = 1.28 x lines of resolution

Point spacing Matches the measurement sample rate.

DAC Resolution

0.2828 Vpk to 5 Vpk

<0.2828 Vpk

2.5 mV

0.25 mV

Agilent 35670A Specifications

Swept Sine Measurements —Option 1D2

1-15


Recommended Test Equipment

The following table lists the recommended equipment needed to test the performance

of the Agilent 35670A Dynamic Signal Analyzer. The table on page 1-20 lists

additional equipment needed to adjust and troubleshoot the analyzer. Other equipment

may be substituted for the recommended model if it meets or exceeds the listed critical

specifications. When substitutions are made, you may have to modify the procedures

to accommodate the different operating characteristics.

Recommended Test Equipment

Instrument Critical Specifications Recommended Model

AC Calibrator 10 Hz to 102.4 kHz; 1 mV to 10 V

Amplitude

Amplitude Accuracy:±0.1% phase locking

capability

Fluke 5700A †

Alternate

Fluke 5200A †

Datron 4200, 4700, or 4708 ‡

HP 745A

Frequency

Synthesizer

Frequency Range: 10 Hz to 1 MHz

Frequency Accuracy:≤5 ppm

Amplitude Accuracy:

0.2 dB from 1 Hz to 100 kHz

1 dB from 100 kHz to 1 MHz

Harmonic Distortion:≤–70 dBc

Spurious:≤–70 dBc

<±1 deg phase shift between output and

sync

HP 3326A

Alternate

(2) HP 3325A/B Opt 001

Low Distortion

Oscillator

Frequency Range: 10 Hz to 100 kHz

Harmonic Distortion:≤–93 dB, 10 Hz to

20 kHz

HP 339A ††

Alternate

HP 3326A with notch filter ††

HP 3325A/B with notch

filter††

Digital

Multimeter

5 1/2 digit True rms ac Voltage:

30 Hz to 100 kHz; 0.1 to 500 V;±0.1%;

≥1MΩinput impedance dc Voltage:

1 V to 300 V; ±0.1%

HP 3458A

Alternate

HP 3456A , HP 3455A

HP 3478A

Feedthrough

Termination (2)

(4 for option

AY6)

50 Ω: ±2% at dc

Pomona Elect Model 4119-50

‡‡

Alternate

HP 11048C, HP 10100C

† John Fluke Manufacturing Co., Inc., PO Box C9090, Everett, WA 98206 U.S.A. (206) 347 6100

‡ Wavetek, 5808 Churchman Bypass, Indianapolis, IN 46203 U.S.A.

†† This equipment is not required for Operation Verification. The parts and schematic for the notch

```
filter are shown on page 1 19.
```
‡‡ ITT Pomona Electronics, 1500 East Ninth Street, Pomona, CA 91769 U.S.A. (714) 469 2900

```
FAX (206) 629 3317
```
Agilent 35670A Specifications

Recommended Test Equipment

1-17


Recommended Test Equipment (continued)

Instrument Critical Specifications Recommended Model

Cables BNC-to-Dual Banana

(6) BNC-to-BNC 30 cm

BNC-to-BNC 122 cm

HP 11001-60001

HP 8120-1838

HP 8120-1840

Adapters BNC(m)-to-Dual Banana Plug

BNC(f)-to-Dual Banana Plug

BNC(f)-to-BNC (f)

(4) BNC Tee (m)(f)(f)

HP 10110B

HP 1251-2277

HP 1250-0080

HP 1250-0781

```
Resistor (2)†
Value: 1 kΩ
```
Accuracy: 1%

Power: 0.25W

HP 0757-0280

† See the following for suggested assembly.

## Suggested Assembly for Series Resistor

## The following is a suggested assembly for the 1 kΩseries resistor. Two 1 kΩ

## series resistors are required for the Intermodulation Distortion performance

## test.

- Cut resistor leads to 12 mm on each end.
- Solder one resistor lead to the center conductor of the BNC female connector.
- Solder the conductor center pin to the other lead of the resistor.
- Screw the sleeve and the BNC male connector into place. Tighten securely.

Specifications Agilent 35670A

Recommended Test Equipment

1-18


## Schematic and Parts List for Notch Filter

The Harmonic Distortion performance test requires either an HP 339A or an

HP 3326A or HP 3325A/B with notch filter. The following shows the schematic and

parts list for the notch filter.

Reference Description Agilent Part

Number

```
C1-C4
0.025μF ±2.5%, 100 V polypropelene-metalized
```
HP 0160-6809

```
R1-R2
249 Ω±1% metal film, 0.125 W
```
HP 0698-4421

```
R3
118 Ω±1% metal film, 0.125 W
```
HP 0698-4407

```
R4-R6
20 Ωtrimmer, 1 turn
```
HP 2100-3409

Agilent 35670A Specifications

Recommended Test Equipment

1-19


Additional Recommended Test Equipment

Instrument Critical Specifications Recommended Model

Frequency Counter Frequency Range: 0 Hz to 100 MHz

Frequency Accuracy: 7.5 ppm or better

at 20 MHz

HP 5350B

Alternate

HP 5351B, HP 5335A

Oscilloscope Bandwidth: >50 MHz

Two Channel; External Trigger; 1 MΩ

Input

HP 54111D

Alternate

HP 1980B, HP 1740

```
Oscilloscope Probe
Impedance:≥1MΩ
```
Division Ratio: 10:1

Maximum Voltage:≥20 Vdc

HP 10431A

Oscilloscope Probe

Impedance:≥1MΩ

Division Ratio: 1:1

HP 10438A

Spectrum Analyzer Frequency Range: 10 Hz to 100 kHz

Dynamic Range:≥70 dB

HP 3562A

Alternate

HP 3561A, HP

3585A/B

Logic Probe TTL HP 545A

Alternate

HP 5006A,

HP5005A/B

Patch Cord Minigrabber test clips Pomona 3781-8-7

Cable BNC(m)-to-SMB(f) HP 03585-61616

Adapter SMB(m)-to-SMB(m) HP 1250-0669

Specifications Agilent 35670A

Recommended Test Equipment

1-20


# 2

## Preparing the Analyzer for

## Use

2-1


Preparing the Analyzer for Use

## This chapter contains instructions for inspecting and installing the

## Agilent 35670A Dynamic Signal Analyzer. This chapter also includes

## instructions for cleaning the screen, transporting and storing the analyzer.

## DC Power Requirements

## The analyzer can operate from a dc power source supplying a true range of 10.8

## to 30.8 Vdc. With all options installed, power consumption is less than

## 200 VA. The following table shows typical current requirements at different

## operating voltages for the standard two-channel analyzer and for the optional

## four-channel analyzer.

Operating Typical Current

Voltage Standard 2 channel

Agilent 35670A

Optional 4 channel Agilent 35670A

12 Vdc 8.0 amps 11.0 amps

24 Vdc 4.0 amps 5.5 amps

## AC Power Requirements

## The analyzer can operate from a 47 to 440 Hz, single-phase, ac power source

## supplying 90 to 264 Vrms. With all options installed, power consumption is

## less than 350 VA.

Warning Only a qualified service person, aware of the hazards involved, should measure

the line voltage.

2-2


## DC Power Cable and Grounding Requirements

## The negative side of the dc input connector is not connected to chassis ground.

## In dc mode operation, the chassis will float. The chassis ground lug on the rear

## panel and the negative side of the dc input connector should both be connected

## to a known reference potential.

## Two dc power cables are available the HP 35250A dc power cable and the

## HP 35251A dc power cable with cigarette lighter adapter. Both cables contain

## a 30 amp, 32 volt fuse (HP 2110-0920).

Warning The tip of the cigarette lighter adapter may get hot during use. After unpluging

the adapter, be careful of the heat from the adapter’s tip.

Caution Although shorter cables may reduce dc voltage loss, use the standard cables. The dc

inrush current may pit the connector contacts in shorter cables.

## AC Power Cable and Grounding Requirements

## On the GPIB connector, pin 12 and pins 18 through 24 are tied to chassis

## ground and the GPIB cable shield. The instrument frame, chassis, and covers

## are connected to chassis ground. The input BNCs are floating unless ground

## mode is selected.

## The analyzer is equipped with a three-conductor power cord that grounds the

## analyzer when plugged into an appropriate receptacle. The type of power cable

## plug shipped with each analyzer depends on the country of destination. The

## following figure shows available power cables and plug configurations.

Agilent 35670A Preparing the Analyzer for Use

2-3


```
*The number shown for the plug is the industry identifier for the plug only, the number shown for the
```
```
cable is an HP part number for a complete cable including the plug.
```
```
**UL listed for use in the United States of America.
```
Warning The power cable plug must be inserted into an outlet provided with a protective

earth terminal. Defeating the protection of the grounded analyzer cabinet can

subject the operator to lethal voltages.

Preparing the Analyzer for Use Agilent 35670A

2-4


- Check that the correct fuses are installed in the fuse holders.

An 8 amp, 250 volt, normal blow fuse is required for ac operation. A 30 amp, 32 volt,

normal blow fuse is required for dc operation. Both fuses are installed at the factory.

For instructions on removing the fuses or fuse part numbers, see ‘’To change the

fuses.’’

- Using the supplied power cord, connect the analyzer to an appropriate

receptacle.

The analyzer is shipped with a three-conductor power cord that grounds the analyzer

when plugged into an appropriate receptacle. The type of power cable plug shipped

with each analyzer depends on the country of destination.

- Set the analyzer’s power switch to on.

Press the switch located on the analyzer’s lower left-hand corner. The switch is in the

on (l) position when in the ‘’in’’ position. The analyzer requires about 20 seconds to

complete its power-on routine.

- Test the electrical performance of the analyzer using the operation verification

or the performance tests in chapter 3, ‘’Verifying Specifications.’’

The operation verification tests verify the basic operating integrity of the analyzer;

these tests take about 1

```
1
```
```
2
```
hours to complete and are a subset of the performance tests.

The performance tests verify that the analyzer meets all the performance

specifications; these tests take about 2

```
1
```
```
2
```
hours to complete.

Preparing the Analyzer for Use Agilent 35670A

To do the incoming inspection

2-6


To install the analyzer

The analyzer is shipped with rubber feet and bail handle in place, ready for use as a

portable or bench analyzer.

- Install the analyzer to allow free circulation of cooling air.

Cooling air enters the analyzer through the right side and exhausts through the left side

and rear panel.

- To install the analyzer in an equipment cabinet, follow the instructions shipped with

the rack mount kit.

Warning To prevent potential fire or shock hazard, do not expose the analyzer to rain or

other excessive moisture.

- Protect the analyzer from moisture and temperatures or temperature changes that cause

condensation within the analyzer.

The operating environment specifications for the analyzer are listed in chapter 1,

‘’Specifications.’’

- Protect the analyzer’s disk drive from dirt and dust.

Remove the screw to the right of the disk drive and use it to attach the supplied disk

drive cover. The disk drive cover is located inside the front-panel impact cover.

Caution Use of the equipment in an environment containing dirt, dust, or corrosive substances

will drastically reduce the life of the disk drive and the flexible disks. To minimize

damage, use the disk drive cover and store the flexible disks in a dry, static-free

environment.

Agilent 35670A Preparing the Analyzer for Use

To install the analyzer

2-7


To connect the analyzer to a dc power source

In applications requiring a portable dc power source, use a properly protected dc

power system. The dc system should contain a deep cycle battery rather than a

standard automobile battery. A standard automobile battery will fail prematurely if

repeatedly discharged. Also, select a battery that provides the best compromise

between operation time and portability.

- Set the analyzer’s power switch to off (O).
- Set the analyzer’s POWER SELECT switch to the DC position.

The switch is in the DC position when in the ‘’out’’ position.

- Connect the dc power cable to the dc power source.

Using the dc power cable (HP 35250A), attach the black cable to the common terminal

and the red cable to the positive terminal of the dc power source. Using the dc power

cable with cigarette lighter adapter (HP 35251A), plug the cigarette lighter adapter into

an automotive cigarette lighter receptacle.

- Connect the analyzer’s ground terminal to the same reference potential as the

common terminal of the dc power source.

Using a wire, connect the analyzer’s GROUND terminal to the common terminal of

the dc source. If you are using the dc power cable with cigarette lighter adapter,

connect the GROUND terminal to the automobile chassis.

- Plug the dc power cable into the analyzer’s DC POWER receptacle. Make sure

to align the red dot on the plug with the red dot on the receptacle.

Preparing the Analyzer for Use Agilent 35670A

To connect the analyzer to a dc power source

2-8


- Turn on the dc power source.

If the dc power source is supplied by an automobile, start the automobile. The

automobile must be running to provide adequate dc power.

Warning The tip of the cigarette lighter adapter may get hot during use. After unpluging

the adapter, be careful of the heat from the adapter’s tip.

- Set the analyzer’s power switch to on (l).

If the analyzer will not power up or operates intermittently on dc power, see ‘’If the

analyzer will not power up’’ or ‘’If the analyzer operates intermittently on dc power’’

at the end of this chapter.

Agilent 35670A Preparing the Analyzer for Use

To connect the analyzer to a dc power source

2-9


To change the fuses

Both fuses are installed at the factory.

- Unplug the power cord from the analyzer.
- Press in and turn the appropriate fuse holder cap counter-clockwise (use a

small screw driver for the ac fuse). Remove when the fuse cap is free from the

housing.

- Pull the fuse from the fuse holder cap.
- To reinstall, select the proper fuse and place in the fuse holder cap.

DC Fuse AC Fuse

HP 2110-0920 30 A 32 V Normal Blow HP 2110-0342 8 A 250 V Normal Blow

- Place the fuse holder cap in the housing. Press in and turn clockwise.

Preparing the Analyzer for Use Agilent 35670A

To change the fuses

2-10


To connect the analyzer to a serial device

The Serial Port is a 9-pin, EIA-574 port that is only available using option 1C2,

Instrument Basic. The total allowable transmission path length is 50 feet.

- Connect the analyzer’s rear panel SERIAL PORT to a serial device using a 9-pin

female to 25-pin RS-232-C cable.

Part Number Cable Description

HP 24542G 9-pin female to 25-pin male RS-232

HP 24542H 9-pin female to 25-pin female RS-232

For additional information, see chapter 9 in the _Agilent 35670A Service Guide_.

To connect the analyzer to a parallel device

The Parallel Port is a 25-pin, Centronics port. The Parallel Port can interface with

PCL printers or HP-GL plotters.

- Connect the analyzer’s rear panel PARALLEL PORT connector to a plotter or printer

using a Centronics interface cable.

Part Number Cable Description

HP 92284A 25-pin male to 36-pin male 2-meter Centronics

HP C2912B 25-pin male to 36-pin male 3-meter Centronics

For additional information, see chapter 9 in the _Agilent 35670A Service Guide_.

Agilent 35670A Preparing the Analyzer for Use

To connect the analyzer to a serial device

2-11


To connect the analyzer to an GPIB device

The analyzer is compatible with the Agilent Technologies Interface Bus (GPIB). The

GPIB is Agilent Technologies’s implementation of IEEE Standard 488.1. Total

allowable transmission path length is 2 meters times the number of devices or 20

meters, whichever is less. Operating distances can be extended using an GPIB

Extender.

GPIB peripherals include HP-GL plotters, PCL printers, and SS-80 external disks.

- Connect the analyzer’s rear panel GPIB connector to an GPIB device using an

GPIB interface cable.

Caution The analyzer contains metric threaded GPIB cable mounting studs as opposed to

English threads. Use only metric threaded GPIB cable lockscrews to secure the cable

to the analyzer. Metric threaded fasteners are black, while English threaded fasteners

are silver.

For GPIB programming information, see the _Agilent 35670A GPIB Programming_

_Reference_.

Preparing the Analyzer for Use Agilent 35670A

To connect the analyzer to an GPIB device

2-12


To connect the analyzer to an external monitor

The External Monitor connector is a 9-pin D female miniature connector that can

interface with an external, multisync monitor. The monitor must be compatible with

the 24.8 kHz line rate, 55 Hz frame rate, and TTL signals provided by the

Agilent 35670A. A SONY CPD-1302 monitor and a NEC Multisync 3D monitor with

EZPIXpc† driver has been checked and found compatible with the Agilent 35670A

external monitor mode operation.

- Set the analyzer’s power switch to on (l).
- Set the monitor’s power switch to on and configure the input and timing mode

if necessary.

See the manual supplied with the monitor for information on configuring the monitor’s

input and timing mode.

- Connect the external monitor’s input cable to the analyzer’s rear panel EXT

MONITOR connector.

A cable with a 9-pin connector option or an adapter to a 9-pin connector is required to

connect the monitor to the Agilent 35670A.

- Press the following keys to enable external mode:

[Disp Format]

[MORE]

[MORE]

[EXT MONON OFF ]

Pin Number Signal Name Pin Number Signal Name

3 R 8 HSYNC

4 G 9 VSYNC

5 B 1, 2, 6 GND

† The EZPIXpc driver converts TTL video signals into RGB analog signals, drives 75 ohm coax cable,

provides RGB composite sync or RGB sync on green, for monitors with RGB input capability. EZPIXpc,

Covid, Inc., 1725 West 17th St, Tempe, Arizona 85281, 800 638 6104

Agilent 35670A Preparing the Analyzer for Use

To connect the analyzer to an external monitor

2-13


To connect the optional keyboard

The analyzer may be connected to an optional external keyboard. The keyboard

remains active even when the analyzer is not in alpha entry mode. This means that

you can operate the analyzer using the external keyboard rather than the front panel.

Pressing the appropriate keyboard key does the same thing as pressing a hardkey or a

softkey on the analyzer’s front panel.

- Set the power switch to off (O).

Caution Do not connect or disconnect the keyboard cable with the line power turned on (l).

Connecting or disconnecting the keyboard while power is applied may damage the

keyboard or the analyzer.

- Connect the round plug on the keyboard cable to the KEYBOARD connector

on the analyzer’s rear panel. Make sure to align the plug with the connector

pins.

Preparing the Analyzer for Use Agilent 35670A

To connect the optional keyboard

2-14


- Connect the other end of the keyboard cable to the keyboard.

Caution In addition to the U.S. English keyboard, the Agilent 35670A Dynamic Signal

Analyzer supports U.K. English, German, French, Italian, Spanish, and Swedish. Use

only the Agilent Technologies approved keyboard for this product. Agilent

Technologies does not warrant damage or performance loss caused by a non-approved

keyboard. See the beginning of this guide for part numbers of approved Agilent

Technologies keyboards.

- To configure your analyzer for a keyboard other than U.S. English, press

[

System Utility

][

KEYBOARD SETUP

]. Then press the appropriate softkey to

select the language.

Configuring your analyzer to use a keyboard other than U.S. English only ensures that

the analyzer recognizes the proper keys for that particular keyboard. Configuring your

analyzer to use another keyboard _does not_ localize the on-screen annotation or the

analyzer’s online HELP facility.

Agilent 35670A Preparing the Analyzer for Use

To connect the optional keyboard

2-15


To connect the microphone adapter

The Microphone Adapter and Power Supply (option UK4) simplifies microphone

connections. The mic connector on the analyzer’s front panel provides 8 Vdc to power

the adapter. The adapter’s internal power supply uses a step-up converter to provide

28 V and 200 V on the seven-pin input connectors. The 28 V pins power the

microphone pre-amplifiers. The 200 V pins polarize the condenser microphone

cartridges.

- Flip the bail handle down to support the front of the analyzer.
- Insert the threaded ends of the adapter’s two knurled knobs into the standoffs

on the bottom of the analyzer’s case, then tighten the knobs with your fingers.

- Attach the adapter’s mic cable to mic connector on the analyzer’s front panel.
- Connect the adapter’s BNCs to the corresponding BNCs on the analyzer’s

front panel.

Standard 2 channel Agilent 35670A Optional 4 channel

Agilent 35670A

Preparing the Analyzer for Use Agilent 35670A

To connect the microphone adapter

2-16


To clean the screen

The analyzer’s display is covered with a plastic diffuser screen (this is not removable

by the operator). Under normal operating conditions, the only cleaning required will

be an occasional dusting. However, if a foreign material adheres itself to the screen,

do the following:

- Set the power switch to off (O).
- Remove the power cord.
- Dampen a soft, lint-free cloth with a mild detergent mixed in water.
- Carefully wipe the screen.

Caution Do not apply any water mixture directly to the screen or allow moisture to go behind

the front panel. Moisture behind the front panel will severely damage the instrument.

To prevent damage to the screen, do not use cleaning solutions other than the above.

To store the analyzer

- Store the analyzer in a clean, dry, and static free environment.

For other requirements, see environmental specifications in chapter 1,

‘’Specifications.’’

Agilent 35670A Preparing the Analyzer for Use

To clean the screen

2-17


To transport the analyzer

- Package the analyzer using the original factory packaging or packaging identical to the

factory packaging.

Containers and materials identical to those used in factory packaging are available

through Agilent Technologies offices.

- If returning the analyzer to Agilent Technologies for service, attach a tag describing

the following:

- Type of service required
- Return address
- Model number
- Full Serial number
- In any correspondence, refer to the analyzer by model number and full serial

number

- Mark the container FRAGILE to ensure careful handling.
- If necessary to package the analyzer in a container other than original packaging,

observe the following (use of other packaging is not recommended):

- Snap the impact cover in place to protect the front panel.
- Wrap the analyzer in heavy paper or anti-static plastic.
- Use a double-wall carton made of at least 350-pound test material.
- Cushion the analyzer to prevent damage.

Caution Do not use styrene pellets in any shape as packing material for the analyzer. The

pellets do not adequately cushion the analyzer and do not prevent the analyzer from

shifting in the carton. In addition, the pellets create static electricity which can

damage electronic components.

Preparing the Analyzer for Use Agilent 35670A

To transport the analyzer

2-18


If the analyzer will not power up

q Check that the power cord is connected to the Agilent 35670A and to a live power

source.

q Check that the front-panel switch is on (l).

q Check that the rear-panel AC/DC power select switch is properly set.

q Check that the fuse is good.

See ‘’To change the fuses’’ on page 2-10.

q Check that the analyzer’s air circulation is not blocked.

Cooling air enters the analyzer through the right side and exhausts through the left side

and rear panel. If the analyzer’s air circulation is blocked, the analyzer powers down

to prevent damage from excessive temperatures. The analyzer remains off until it

cools down and its power switch is set to off (O) then to on (l).

q Obtain Agilent service, if necessary. See ‘’Need Assistance?’’ at the end of this guide.

Agilent 35670A Preparing the Analyzer for Use

If the analyzer will not power up

2-19


If the analyzer operates intermittently on dc power

The analyzer powers down when operating on dc power if no measurement has been

made within 30 minutes.

q Check that the dc power source can supply the required power.

The dc power source must have a true range of 10.8 to 30.8 Vdc. At the minimum

voltage of 10.8 Vdc, the dc power source must be able to supply approximately

8.7 amps for a two-channel analyzer and 12.2 amps for a four-channel analyzer. The

voltage loss through an automotive cigarette lighter system can cause the dc voltage to

go below 10.8 Vdc.

q Check that power transients are not causing the dc voltage to go below 10.8 Vdc.

The dc voltage provided by an automobile is susceptible to power transients. For

example, power transients may occur when lights or fans turn on or off, when power

door locks engage or disengage, and when windshield wipers operate. If the dc supply

voltage falls below 10.8 V, the analyzer automatically turns off. However, the

analyzer is not affected by power transients that occur within the range of 10.8 to 30.8

Vdc.

q Check that the cable connections are not loose.

q Obtain Agilent service, if necessary. See ‘’Need Assistance?’’ at the end of this guide.

Preparing the Analyzer for Use Agilent 35670A

If the analyzer operates intermittently on dc power

2-20


# 3

## Verifying Specifications

3-1


Verifying Specifications

## This chapter tells you how to use the Agilent 35670A Semiautomated Performance

## Test Disk. The performance test disk contains a program that semiautomates the

## operation verification tests and performance tests.

## After you review this chapter, follow the directions in ‘’To load the program’’

## then continue with one of the following:

- ‘’To run the program in semiautomated mode’’
- ‘’To run the program without a printer’’
- ‘’To run the program in manual mode’’

Caution Before applying line power to the analyzer or testing its electrical performance, see

chapter 2, ‘’Preparing the Analyzer for Use.’’

## Overview

## The Semiautomated Performance Test Disk contains a program (ITM_35670A)

## and two procedure files (OP_VERIFY and PERFORMAN). ITM_35670A is

## the test manager program. OP_VERIFY is the operation verification procedure

## file and PERFORMAN is performance test procedure file. The procedure files

## contain an ordered list of tests, and each test contains one or more

## measurements. Since ITM_35670A reads the procedure files, the disk must

## remain in the disk drive during testing.

## If you do not have a keyboard connected to the analyzer, use the numeric key

## pad and the alpha keys when the program prompts you to type in information.

## See the analyzer’s help text for a description of the alpha keys.

## If a test fails, contact your local Agilent Technologies sales and service office

## or have a qualified service technician see chapter 4, ‘’Troubleshooting the

## Analyzer,’’ in the Agilent 35670A Service Guide.

3-2


## Features of the Program

- The program can automatically create a printout similar to the test records at the

back of this chapter.

- The program can beep when equipment connections need to be changed.
- The program can start the test sequence at any test in the operation verification or

performance test list.

- The program can stop after each measurement or alternatively, only if a failure

occurs.

- The program can be run in manual mode.

## Test Duration

## In semiautomated mode, the operation verification tests require approximately

## 1

```
1
```
```
2
```
## hours and the performance tests require approximately 2

```
1
```
```
2
```
## hours.

## Calibration Cycle

## To verify the Agilent 35670A Dynamic Signal Analyzer is meeting its

## published specifications, do the performance tests every 12 months.

## Recommended Test Equipment

## The equipment needed for operation verification and performance tests is listed

## on page 1-18. Other equipment may be substituted for the recommended

## model if it meets or exceeds the listed critical specifications.

## Also, if you want the test record to be automatically printed, you need an GPIB

## printer. If you want the printer to automatically leave top and bottom margins

## on every page, enable perforation skip mode (see your printer’s manual for

## directions). If you do not have an GPIB printer you must record the results of

## each test in the test records. These test records may be reproduced without

## written permission of Agilent Technologies.

Agilent 35670A Verifying Specifications

3-3


Program Controlled Test Equipment

## This program automatically controls the instruments listed in the following

## table using GPIB commands. If you use a test instrument other than those

## shown in the table, the program prompts you to set the instrument state during

## testing.

Test Equipment Program Controlled Model

AC Calibrator Fluke 5700A

Alternate

Fluke 5200A

Datron 4200, 4707, 4708

Frequency Synthesizer HP 3326A

Alternate

(2) HP 3325A/B

Digital Multimeter HP 3458A

Alternate

HP 3455A

HP 3456A

HP 3478A

Measurement Uncertainty

## A table starting on page 3-56 lists the measurement uncertainty and ratio for

## each performance test using the recommended test equipment. Except for the

## External Trigger test, the ratios listed for the recommended test equipment

## meet or exceed the measurement uncertainty ratio required byU.S.

## MIL-STD-45662A. The table also provides a place to record the measurement

## uncertainty and ratio for each performance test using equipment other than the

## recommended test equipment. The table may be reproduced without written

## permission of Agilent Technologies.

## Operation Verification and Performance Tests

## The operation verification tests give a high confidence level (>90%) that the

## Agilent 35670A Dynamic Signal Analyzer is operating properly and within

## specifications. The operation verification tests are a subset of the performance

## tests. The operation verification tests should be used for incoming and

## after-repair inspections. The performance tests provide the highest level of

## confidence and are used to verify that the Agilent 35670A Dynamic Signal

## Analyzer conforms to its published specifications. Some repairs require a

## performance test to be done after the repair (see chapter 6, ‘’Replacing

## Assemblies’’ in the Agilent 35670A Service Guide for this information). The

## following table lists the operation verification and performance tests.

Verifying Specifications Agilent 35670A

3-4


Operation Verification Tests Performance Tests

Self Test Self Test

DC Offset DC Offset

Noise Noise

Spurious Signals Spurious Signals

Amplitude Accuracy Amplitude Accuracy

Flatness Flatness

Amplitude Linearity Amplitude Linearity

A-Weight Filter A-Weight Filter

Channel Match Channel Match

Frequency Accuracy Frequency Accuracy

Single Channel Phase Accuracy Anti-Alias Filter

Tach Function Input Coupling

ICP Supply Harmonic Distortion

Source Amplitude Accuracy Intermodulation Distortion

Source Flatness Cross Talk

Source Distortion Single Channel Phase Accuracy

External Trigger

Tach Function

Input Resistance

ICP Supply

Source Amplitude Accuracy

Source Output Resistance

Source DC Offset

Source Flatness

Source Distortion

Agilent 35670A Verifying Specifications

3-5


## Specifications and Performance Tests

The following table lists specifications and the performance test or tests that verify

each specification.

Specification Performance Test

Frequency

Accuracy Frequency Accuracy

Single Channel Amplitude

Residual dc response

FFT full scale accuracy at 1 kHz

FFT full scale flatness

FFT amplitude linearity at 1 kHz

DC Offset

Amplitude Accuracy

Flatness

Amplitude Linearity

FFT Dynamic Range

Frequency alias responses

Harmonic distortion

Intermodulation distortion

Spurious and residual responses

Anti-Alias Filter

Harmonic Distortion

Intermodulation Distortion

Spurious Signals

Input Noise Noise

Single Channel Phase Single Channel Phase Accuracy

Cross Channel Amplitude Channel Match

Cross Channel Phase Channel Match

Input

ac coupling rolloff

Cross talk

Input impedance

ICP signal conditioning

A-weight filter

Input Coupling

Cross Talk

Input Resistance

ICP Supply

A-Weight Filter

Trigger

External trigger External Trigger

Tachometer

Tachometer level accuracy Tach Function

Source Output

Sine flatness

Harmonic and sub-harmonic distortion

Sine amplitude accuracy at 1 kHz

Resistance

dc offset accuracy

Source Flatness

Source Distortion

Source Amplitude Accuracy

Source Output Resistance

Source DC Offset

Verifying Specifications Agilent 35670A

3-6


To load the program

For information about the program’s softkeys, see the menu descriptions starting on

page 3-51.

- Set the Agilent 35670A Dynamic Signal Analyzer’s power switch to off (O),

then connect the analyzer, test instruments, and printer using GPIB cables.

- If you have the PC Style Keyboard, option 1CL, connect the keyboard to the

analyzer using the keyboard cable (see ‘’To connect the optional keyboard’’ in

chapter 2).

- Insert theSemiautomated Performance Test Diskinto the analyzer’s disk drive,

then set the power switch to on (l).

- After the analyzer finishes its power-up calibration routine, press the following

keys:

[Local/GPIB]

[SYSTEM CONTROLLR]

[System Utility]

[MEMORY USAGE]

[REMOVE WATERFALL]

[CONFIRM REMOVE]

[RETURN]

[MORE]

[SERVICE TESTS]

[PERFRMANC TEST]

- Now go to one of the following procedures to continue:
- ‘’To run the program in semiautomated mode’’
- ‘’To run the program without a printer’’
- ‘’To run the program in manual mode’’

Agilent 35670A Verifying Specifications

To load the program

3-7


To run the program in semiautomated mode

You must have an GPIB printer connected to your system to run the program in

semiautomated mode. If you do not have a printer, see ‘’To run the program without a

printer’’ later in this chapter.

- Press the following keys and when the program prompts you, type in the

information for the title page of the test record and press [ENTER]:

[TITLE PAGE]

[TEST FACILITY]

[FACILITY ADDRESS]

[TESTED BY]

[REPORT NUMBER]

[CUSTOMER]

[MORE]

[TEMP]

[HUMIDITY]

[LINE FREQUENCY]

[RETURN]

- Press the following keys and when the program prompts you, type in the

equipment configuration information:

[EQUIP CONFIG]

[AC CALIBRATO]

[SYNTH. 1]

[SYNTH. 2] (If needed)

[LOW-D OSCILLATO] (If needed)

[MULTIMETER]

[RETURN]

The GPIB address is 100 x (interface select code) + (primary address). The interface

select code for the test equipment and printer is 7 (for example, if the primary address

is 8, the GPIB address is 708).

When entering the calibration due date, only four characters are displayed on the

screen. However, you can enter up to nine characters and they will be printed.

Verifying Specifications Agilent 35670A

To run the program in semiautomated mode

3-8


- Press the following keys and type in the printer address when the program

prompts you:

[TEST CONFIG]

[PRINTER ADDRESS]

[PROCEDURE]

[OP VERIFY]or[PERFORMAN]

[STOP AFTER]

[LIMIT FAILURE]or[NONE]

[RETURN]

- Press the following keys to start the test:

[START TESTING]

[START BEGINNING]

When you select [START BEGINNING], the data is written to a file on the disk and

printed only after all tests are done. When you select [START MIDDLE]or

[ONE TEST], the data is printed immediately after each measurement.

- Follow the directions on the display.

Warning During the test, the program prompts you to change the test equipment

connections. Always turn the ac calibrator output to OFF or STANDBY before

changing test equipment connections. The ac calibrator can produce output

voltages that could result in injury to personnel.

The directions on the display briefly tell you how to connect test equipment. For

detailed illustrations of equipment setup, see the setup illustrations starting on page

3-13.

If you want to pause the program and return the Agilent 35670A Dynamic Signal

Analyzer to front panel control, press [BASIC]. To continue the program, press

[BASIC][DISPLAY SETUP][LOWER][RETURN][CONTINUE]. If you changed

any instrument setup states, press [RESTART TEST] instead of [CONTINUE]to

ensure accurate measurement results.

Agilent 35670A Verifying Specifications

To run the program in semiautomated mode

3-9


To run the program without a printer

Use this procedure if you do not have an GPIB printer connected to yout system.

- Write in the information needed on the title page of the selected test record.

The test records are located near the back of this chapter and may be copied without

written permission of Agilent Technologies.

- Press the following keys and when the program prompts you, type in the model

number and GPIB address:

[EQUIP CONFIG]

[AC CALIBRATO]

[SYNTH. 1]

[SYNTH. 2] (If needed)

[LOW-D OSCILLATO] (If needed)

[MULTIMETER]

[RETURN]

The GPIB addresses equals 100(interface select code) + (primary address). The

interface select code for the test equipment is 7 (for example, if the primary address is

8, the GPIB address is 708).

- Press the following keys:

[TEST CONFIG]

[PROCEDURE]

[OP VERIFY]or[PERFORMAN]

[STOP AFTER]

[EACH MEASUREMENT]

[RETURN]

- Press the following keys to start the test:

[START TESTING]

[START BEGINNING]

Verifying Specifications Agilent 35670A

To run the program without a printer

3-10


- Now follow the directions on the display and record every measurement result

in the selected test record.

Warning During the test, the program prompts you to change the test equipment

connections. Always turn the ac calibrator output to OFF or STANDBY before

changing test equipment connections. The ac calibrator can produce output

voltages that could result in injury to personnel.

The directions on the display briefly tell you how to connect test equipment. For

detailed illustrations of equipment setup, see the setup illustrations starting on page

3-13.

If you want to pause the program and return the Agilent 35670A Dynamic Signal

Analyzer to front panel control, press [BASIC]. To continue the program, press

[BASIC][DISPLAY SETUP][LOWER][RETURN][CONTINUE]. If you changed

any instrument setup states, press [RESTART TEST] instead of [CONTINUE]to

ensure accurate measurement results.

Agilent 35670A Verifying Specifications

To run the program without a printer

3-11


To run the program in manual mode

Use this procedure if you want to run the program in manual mode. You will be

prompted to set up all test equipment and you can check the analyzer’s setup state after

each measurement.

- Write in the information needed on the title page of the selected test record.

The test records are located near the back of this chapter and may be copied without

written permission of Agilent Technologies.

- Press the following keys and when the program prompts you, set all GPIB

addresses to 0:

[EQUIP CONFIG]

[AC CALIBRATO]

[SYNTH. 1]

[SYNTH. 2] (If needed)

[LOW-D OSCILLATO] (If needed)

[MULTIMETER]

[RETURN]

- Press the following keys:

[TEST CONFIG]

[PROCEDURE]

[OP VERIFY]or[PERFORMAN]

[STOP AFTER]

[EACH MEASUREMENT]

[RETURN]

- Press the following keys to start the test:

[START TESTING]

[START BEGINNING]

- Now follow the directions on the display and record the measurement result in

the selected test record after every measurement.

If you want to view the analyzer’s setup state, press [BASIC][Disp Format]

[MEASURMNT STATE]or[INPUT STATE]. To continue the program, press

[BASIC][DISPLAY SETUP][LOWER][RETURN][CONTINUE]. If you changed

any instrument setup states, press [RESTART TEST] instead of [CONTINUE]to

ensure accurate measurement results.

Warning During the test, the program prompts you to change the test equipment

connections. Always turn the ac calibrator output to OFF or STANDBY before

changing test equipment connections. The ac calibrator can produce output

voltages that could result in injury to personnel.

The directions on the display briefly tell you how to connect test equipment. For

detailed illustrations of equipment setup, see the setup illustrations starting on the next

page.

Verifying Specifications Agilent 35670A

To run the program in manual mode

3-12


To set up the self test

Performance Test and Operation Verification

This test checks the measurement hardware in the Agilent 35670A. No

performance tests should be attempted until the analyzer passes this test. This test

takes approximately one minute to complete, and requires no external equipment.

1

Agilent 35670A Verifying Specifications

To set up the self test

3-13


To set up the dc offset test

Performance Test and Operation Verification

This test verifies that the Agilent 35670A meets its single channel amplitude

specification for residual dc responses. In this test, the Agilent 35670A measures

its internal residual dc offset at two amplitudes.

1 2ch

1 4ch

Verifying Specifications Agilent 35670A

To set up the dc offset test

3-14


To set up the noise test

Performance Test and Operation Verification

This test verifies that the Agilent 35670A meets its input noise specification. In

this test, the Agilent 35670A measures its internal noise level.

1 2ch

1 4ch

Agilent 35670A Verifying Specifications

To set up the noise test

3-15


To set up the spurious signals test

Performance Test and Operation Verification

This test verifies that the Agilent 35670A meets its FFT dynamic range

specification for spurious and residual responses. In this test, the Agilent 35670A

measures its internal spurious signals. The test records at the end of this chapter list

the frequencies that are checked.

1 2ch

1 4ch

Verifying Specifications Agilent 35670A

To set up the spurious signals test

3-16


To set up the amplitude accuracy test

Performance Test and Operation Verification

This test verifies that the Agilent 35670A meets its single channel amplitude

specification for FFT full scale accuracy at 1 kHz. In this test, an ac calibrator

outputs a 1 kHz signal with an exact amplitude to all channels. This test checks

amplitude accuracy at 27, 19, 9, 1,−11,−27,−35,−43, and−51 dBVrms.

1 2ch

1 4ch

Agilent 35670A Verifying Specifications

To set up the amplitude accuracy test

3-17


To set up the flatness test

Performance Test and Operation Verification

This test verifies that the Agilent 35670A meets its single channel amplitude

specification for FFT full scale flatness relative to 1 kHz. In this test, the ac

calibrator outputs a signal with an exact amplitude to all channels. The test records

at the end of this chapter list the amplitudes and frequencies that are checked.

1 2ch

1 4ch

Verifying Specifications Agilent 35670A

To set up the flatness test

3-18


To set up the amplitude linearity test

Performance Test and Operation Verification

This test verifies that the Agilent 35670A meets its single channel amplitude

specification for FFT amplitude linearity at 1 kHz. In this test, the ac calibrator

outputs a 1 kHz signal with an an exact amplitude to all channels. This test checks

amplitude linearity at 27, 13,−1,−15,−29,−43, and−53 dBVrms.

1 2ch

1 4ch

Agilent 35670A Verifying Specifications

To set up the amplitude linearity test

3-19


To set up the A-weight filter test

Performance Test and Operation Verification

This test verifies that the Agilent 35670A meets its input specification for A-weight

filter. In this test, an ac calibrator outputs a 1 dBVrms signal with an exact

amplitude to all channels. The test records at the end of this chapter list the

frequencies that are checked.

1 2ch

1 4ch

Verifying Specifications Agilent 35670A

To set up the A-weight filter test

3-20


To set up the channel match test

Performance Test and Operation Verification

This test verifies that the Agilent 35670A meets its cross channel amplitude and

cross channel phase specification. In this test, the Agilent 35670A’s source outputs

an identical signal to all channels. The Agilent 35670A measures the amplitude

and phase of the signal and compares the values measured on one channel to the

values measured on another channel.

1 2ch

1 4ch

Agilent 35670A Verifying Specifications

To set up the channel match test

3-21


To set up the frequency accuracy test

Performance Test and Operation Verification

This test verifies that the Agilent 35670A meets its frequency accuracy

specification. In this test, the analyzer measures the frequency of an accurate

50 kHz signal.

1 2ch

1 4ch

Verifying Specifications Agilent 35670A

To set up the frequency accuracy test

3-22


To set up the anti-alias filter test

Performance Test only

This test verifies that the Agilent 35670A meets its FFT dynamic range

specification for frequency alias responses. In this test, a frequency synthesizer

outputs a−9 dBVrms signal known to cause an alias frequency to all channels. The

Agilent 35670A then measures the alias frequency to determine how well the alias

frequency was rejected. The test records at the end of this chapter list the

frequencies that are checked.

1 2ch

1 4ch

Agilent 35670A Verifying Specifications

To set up the anti-alias filter test

3-23


To set up the input coupling test

Performance Test only

This test verifies that the Agilent 35670A meets its input specification for ac

coupling rolloff. In this test, a frequency synthesizer outputs a 1 Hz signal to all

channels. The signal is measured in both ac and dc coupled modes. The value

measured in ac coupled mode is subtracted from the value measured in dc coupled

mode to determine the ac coupling rolloff.

1 2ch

1 4ch

Verifying Specifications Agilent 35670A

To set up the input coupling test

3-24


To set up the harmonic distortion test

Performance Test only

This test verifies that the Agilent 35670A meets its FFT dynamic range

specification for harmonic distortion. In this test, a low distortion oscillator or a

frequency synthesizer and 24.5 kHz notch filter outputs a signal to all channels.

The second, third, fourth, or fifth harmonic is then measured. If the harmonic falls

outside the analyzer’s frequency range, the analyzer measures the alias frequencies.

The test records at the end of this chapter list the fundamental frequencies. If you

are using the synthesizer and notch filter, the frequencies listed in the test record are

approximate.

1 2ch Using an HP339A

1 4ch Using an HP 339A

Agilent 35670A Verifying Specifications

To set up the harmonic distortion test

3-25


1 A2ch Using a synthesizer and notch filter

2A2ch Using a synthesizer and notch filter

1 A4ch Using a synthesizer and notch filter

Verifying Specifications Agilent 35670A

To set up the harmonic distortion test

3-26


2 A4ch Using a synthesizer and notch filter

Agilent 35670A Verifying Specifications

To set up the harmonic distortion test

3-27


To set up the intermodulation distortion test

Performance Test only

This test verifies that the Agilent 35670A meets its FFT dynamic range

specification for intermodulation distortion. In this test, two signals are combined

to provide a composite signal to all channels. The intermodulation products are

found at the sum (F1 + F2) and difference (F1−2F2) frequencies. The analyzer

measures the amplitude of each intermodulation product.

1 2ch Using an HP 3326A

1 4ch Using an HP 3326A

Verifying Specifications Agilent 35670A

To set up the intermodulation distortion test

3-28


1 A2ch Using 2 HP 3325’s

1 A4ch Using 2 HP 3325’s

Agilent 35670A Verifying Specifications

To set up the intermodulation distortion test

3-29


To set up the cross talk test

Performance Test only

This test verifies that the Agilent 35670A meets its input specification for

channel-to-channel and channel-to-source cross talk. In this test, the

Agilent 35670A measures the amount of energy induced from the source or input

channel to another input channel. For source-to-channel crosstalk, the analyzer’s

source is set for 25.6 kHz, 9 dBVrms and the signal level at the input channels is

measured. For channel-to-channel crosstalk, the frequency synthesizer outputs a

25.6 kHz or 51.2 kHz, 9 dBVrms signal to all but one input channel and the signal

level at the unused input channel is measured.

1 2ch

2 2ch

Verifying Specifications Agilent 35670A

To set up the cross talk test

3-30


3 2ch

1 4ch

2 4ch

Agilent 35670A Verifying Specifications

To set up the cross talk test

3-31


3 4ch

4 4ch

Verifying Specifications Agilent 35670A

To set up the cross talk test

3-32


5 4ch

Agilent 35670A Verifying Specifications

To set up the cross talk test

3-33


To set up the single channel phase accuracy test

Performance Test and Operation Verification

This test verifies that the Agilent 35670A meets its single channel phase accuracy

specification. In this test, a frequency synthesizer outputs an identical square wave

to all channels and a synchronized TTL-level signal to the trigger input. The phase

difference between the trigger and each channel is measured to determine phase

accuracy.

1 2ch

1 4ch

Verifying Specifications Agilent 35670A

To set up the single channel phase accuracy test

3-34


To set up the external trigger test

Performance Test only

This test verifies that the Agilent 35670A meets its trigger specification for external

trigger level accuracy. In this test, a frequency synthesizer outputs a 1 kHz signal

to the external trigger input and a 12.8 kHz signal to channel 1. The analyzer

makes an accurate triggered measurement on channel 1 to verify the trigger level

and slope.

1 2ch Using an HP 3326A

1 4ch Using an HP 3326A

Agilent 35670A Verifying Specifications

To set up the external trigger test

3-35


1A2ch Using two HP 3325’s

1A4ch Using two HP 3325’s

Verifying Specifications Agilent 35670A

To set up the external trigger test

3-36


To set up the tach function test

Performance Test and Operation Verification

This test is only for Agilent 35670A’s with option 1D0, computed order tracking.

This test verifies that the Agilent 35670A meets its tachometer specification for

trigger level accuracy. In this test, a frequency synthesizer outputs a signal to the

tachometer input and to channel 1. The analyzer makes an accurate order

measurement on channel 1 to verify the trigger level and slope.

1 2ch Using an HP 3326A

1 4ch Using an HP 3326A

Agilent 35670A Verifying Specifications

To set up the tach function test

3-37


1A2ch Using two HP 3325’s

1A4ch Using two HP 3325’s

Verifying Specifications Agilent 35670A

To set up the tach function test

3-38


To set up the input resistance test

Performance Test only

This test verifies that the Agilent 35670A meets its input resistance specification.

In this test, a digital multimeter directly measures the input resistance of each

channel. The digital multimeter is set to the 1 MΩrange.

1 2ch

2 2ch

1 4ch

Agilent 35670A Verifying Specifications

To set up the input resistance test

3-39


2 4ch

3 4ch

4 4ch

Verifying Specifications Agilent 35670A

To set up the input resistance test

3-40


To set up the ICP supply test

Performance Test and Operation Verification

This test verifies that the Agilent 35670A meets its input specification for ICP

signal conditioning. In this test, a digital multimeter directly measures the open

circuit voltage of each channel. The digital multimeter measures the current souce

of each channel by measuring the voltage across a 50Ωfeedthrough termination.

The digital multimeter is set to the 100 V range to measure open circuit voltage and

set to the 1 V range to measure the current source.

1 2ch

2 2ch

Agilent 35670A Verifying Specifications

To set up the ICP supply test

3-41


3 2ch

4 2ch

1 4ch

2 4ch

Verifying Specifications Agilent 35670A

To set up the ICP supply test

3-42


3 4ch

4 4ch

5 4ch

6 4ch

Agilent 35670A Verifying Specifications

To set up the ICP supply test

3-43


7 4ch

8 4ch

Verifying Specifications Agilent 35670A

To set up the ICP supply test

3-44


To set up the source amplitude accuracy test

Performance Test and Operation Verification

This test verifies that the Agilent 35670A meets its source output specification for

sine amplitude accuracy at 1 kHz. In this test, a digital multimeter measures the

amplitude accuracy of the source. Source amplitude accuracy is checked at

0.1 Vpk with the digital multimeter set to the 100 mVrms range and at 3.0 and

5.0 Vpk with the digital multimeter set to the 10 Vrms range. For the standard two

channel analyzer, the digital multimeter is connected to the rear panel source

connector instead of the front panel source connector. This is the only test that

verifies the rear panel source port on the standard two channel analyzer.

1 2ch

1 4ch

Agilent 35670A Verifying Specifications

To set up the source amplitude accuracy test

3-45


To set up the source output resistance test

Performance Test only

This test verifies that the Agilent 35670A meets its source output specification for

resistance. In this test, a digital multimeter measures the 50Ωfeedthrough

termination. The channel 1 input then measures the source output across the

feedthrough termination, then in an open circuit condition. The resistance is

calculated using the following formula:

Rs = R1((Vopen - Vload)/Vload)

Note: Use the same 50Ωfeedthrough termination for steps 1 and 2.

1 2ch

2 2ch

Verifying Specifications Agilent 35670A

To set up the source output resistance test

3-46


3 2ch

1 4ch

2 4ch

3 4ch

Agilent 35670A Verifying Specifications

To set up the source output resistance test

3-47


To set up the source dc offset test

Performance Test only

This test verifies that the Agilent 35670A meets its source output specification for

dc offset accuracy. In this test, a digital multimeter measures the dc offset voltage

of the source with and without an ac component. The frequency of the ac

component is 96 kHz. The test records at the end of this chapter list the voltages

that are checked.

1 2ch

1 4ch

Verifying Specifications Agilent 35670A

To set up the source dc offset test

3-48


To set up the source flatness test

Performance Test and Operation Verification

This test verifies that the Agilent 35670A meets its source output specification for

sine flatness. In this test, the analyzer’s channel 1 input measures the flatness of its

source.

1 2ch

1 4ch

Agilent 35670A Verifying Specifications

To set up the source flatness test

3-49


To set up the source distortion test

Performance Test and Operation Verification

This test verifies that the Agilent 35670A meets its source output specification for

harmonic and sub-harmonic distortion and spurious signals. In this test, the

analyzer’s source is connected to its channel 1 input. The source is set for a

maximum output level (5 Vpk) and the input range is set equal to the source level.

The fundamental and harmonic is measured. The test records at the end of this

chapter list the fundamental frequencies that are checked.

1 2ch

1 4ch

Verifying Specifications Agilent 35670A

To set up the source distortion test

3-50


Agilent 35670A Verifying Specifications

3-51

## ITM_35670A Main Menu Descriptions

If you do not have a keyboard connected

to the analyzer, use the numeric key pad

and the alpha keys to enter names or

numbers. See the analyzer’s help text

for a description of the alpha keys.

Load and run the ITM 35670A program

to display the following softkeys:

[START TESTING]

Displays a menu that allows you to start

testing with any test or to select just one

test in the list. Before pressing this

softkey, use [TEST CONFIG] and

[EQUIP CONFIG ].

[TEST CONFIG]

Displays the test configuration and a

menu that allows you to enter the

procedure, stop conditions, beeper

prompt, and GPIB address for the

analyzer and printer.

[EQUIP CONFIG]

Displays the test equipment

configuration and a menu that allows

you to enter the model number,

calibration due date, serial number, and

GPIB address for each test instrument.

[TITLE PAGE]

Displays the test record title page

information and a menu that allows you

to enter information for the analyzer.

[STOP ITM]

Stops the ITM 35670A program.


Verifying Specifications Agilent 35670A

3-52

## Start Testing Menu Descriptions

Press [START TESTING] to display the

following softkeys:

[START BEGINNING]

Prints the test record title page

information and starts the selected test

procedure at the beginning. When you

select [START BEGINNING], the data

is written to a file on the disk and

printed only after all tests are done.

[START MIDDLE]

Displays a list of all the tests in the

selected procedure. Testing starts with

the test you select and continues through

the remainder of the tests in the list.

When you select [START MIDDLE],

the data is printed immediately after

each measurement.

[ONE TEST]

Displays all the tests in the selected

procedure. The test you select is the

only test performed. When you select [

ONE TEST], the data is printed

immediately after each measurement.

[RETURN]

Returns to the ITM 35670A main

menu.

Start a test to display the following

softkeys:

[STOP TESTING]

Stops the test and returns to the

ITM 35670A main menu.

[RESTART TEST]

Starts the current test over. Any

connection prompts are repeated.

[RESTART MEAS]

Starts the current measurement over.

The following softkeys also appear

when the program is waiting for you to

press [CONTINUE]:

[STOP BEEPING]

Turns off the beeper prompt for the

remainder of this measurement.

[CONTINUE]

Continues the test. Press this key after

following the directions on the display.


Agilent 35670A Verifying Specifications

3-53

## Test Configuration Menu Descriptions

Press [TEST CONFIG] to display the

test configuration and the following

softkeys:

[Agilent 35670A ADDRESS]

Prompts you to enter the GPIB address

for the Agilent 35670A Dynamic Signal

Analyzer.

The GPIB addresses equals 100

(interface select code) + (primary

address). The interface select code for

the printer and test equipment is 7 (for

example, if the primary address is 8, the

GPIB address is 708).

[PRINTER ADDRESS]

Prompts you to enter the GPIB address

for the printer. To disable the printer,

set the printer address to 0.

[PROCEDURE]

Prompts you to select the operation

verification procedure (OP VERIFY) or

the performance test procedure

(PERFORMAN).

[BEEPER]

Toggles the beeper on and off. When

the beeper is on, the program beeps

approximately every 2 minutes while

waiting for you to follow the directions

on the display and press [CONTINUE].

[RETURN]

Returns to the ITM 35670A main

menu.

[STOP AFTER]

Prompts you to select stop after limit

failure, stop after each measurement, or

do not stop after a limit failure or

measurement. If [Limit Failure]is

selected, the program stops after the

failing measurement is displayed but

before it is printed. At this point you

can continue on and print the failing

measurement or restart the

measurement.


Verifying Specifications Agilent 35670A

3-54

## Equipment Configuration Menu Descriptions

Press [EQUIP CONFIG] to display the

test equipment configuration and the

following softkeys:

[AC CALIBRATO]

Prompts you to enter the model, serial

number, GPIB address, and calibration

due date for the ac calibrator.

If you select [Other] for model, the

program prompts you to type in a

model, serial number, and calibration

due date but not an GPIB address.

When entering the calibration due date,

only four characters are displayed on the

screen. However, you can enter up to

nine characters and they will be printed.

[SYNTH. 1]

Prompts you to enter the model, serial

number, GPIB address, and calibration

due date for the synthesizer.

[SYNTH. 2]

Prompts you to enter the model, serial

number, GPIB address, and calibration

due date for the second synthesizer. If

the first synthesizer is an Agilent 3326A

or if you are only performing the

operation verification tests, you do not

need a second synthesizer.

[LOW-D. OSCILLATO]

Prompts you to enter the model, serial

number, and calibration due date for the

low-distortion oscillator. If you have a

24.5 kHz notch filter or if you are only

performing the operation verification

tests, you do not need a low-distortion

oscillator.

[MULTIMETER]

Prompts you to enter the model, serial

number, GPIB address, and calibration

due date for the multimeter.

[SAVE SETUP]

Saves the current equipment

configuration to a file for future recall.

[RECALL SETUP]

Recalls an equipment configuration that

was previously saved using [SAVE

SETUP].

[RETURN]

Returns to the ITM 35670A main

menu.


Agilent 35670A Verifying Specifications

3-55

## Title Page Menu Descriptions

Press [TITLE PAGE] to display the title

page information and the following

softkeys:

[TEST FACILITY]

Prompts you to enter the name or

number of the testing entity.

[FACILITY ADDRESS]

Prompts you to enter the address of the

testing entity.

[TESTED BY]

Prompts you to enter the name or

number of the person performing the

test.

[REPORT NUMBER]

Prompts you to enter the analyzer’s

report number.

[CUSTOMER]

Prompts you to enter the name or

number of the person requesting the test.

[SERIAL NUMBER]

Prompts you to enter the analyzer’s

serial number.

[MORE]

Displays the next page.

[RETURN]

Returns to the ITM 35670A main

menu.

[OPTIONS]

Prompts you to enter the analyzer’s

options.

[DATE]

Prompts you to enter the test date.

[TEMP]

Prompts you to enter the temperature of

the environment during the test.

[HUMIDITY]

Prompts you to enter the humidity of the

environment during the test.

[LINE FREQUENCY]

Prompts you to enter the power line

frequency.

[MORE]

Displays the first page.

[RETURN]

Returns to the ITM 35670A main

menu.

The title page information is printed at

the beginning of the test procedure.


Measurement Uncertainty

The following table lists the measurement uncertainty and ratio for each performance

test using the recommended test equipment. Except for the External Trigger test, the

ratios listed for the recommended test equipment meet or exceed the measurement

uncertainty ratio required by U.S. MIL-STD-45662A.

- If you are using equipment other than the recommended test equipment, you may

calculate and record the measurement uncertainty and ratio for each performance test.

The table may be reproduced without written permission of Agilent Technologies.

Performance Test Using Recommended Test

Equipment

Using Other Test Equipment

Measurement Uncertainty Ratio Measurement Uncertainty Ratio

Self Test NA NA NA NA

DC Offset NA NA NA NA

Noise NA NA NA NA

Spurious Signals NA NA NA NA

Amplitude Accuracy

−51 dBVrms

−43 dBVrms

−35 dBVrms

−27 dBVrms

−11 dBVrms

1 dBVrms

9 dBVrms

19 dBVrms

27 dBVrms

±0.020 dB

±0.0084 dB

±0.004 dB

±0.003 dB

±0.001 dB

±0.0008 dB

±0.001 dB

±0.00081 dB

±0.00117 dB

7.7:1

>10:1

>10:1

>10:1

>10:1

>10:1

>10:1

>10:1

>10:1

Flatness

25.6 kHz, 27 dBVrms

25.6 kHz, 9 dBVrms

25.6 kHz,−11 dBVrms

51.2 kHz, 27 dBVrms

51.2 kHz, 9 dBVrms

51.2 kHz,−11 dBVrms

99.84 kHz, 27 dBVrms

99.84 kHz, 9 dBVrms

99.84 kHz,−11 dBVrms

±0.01487 dB

±0.01277 dB

±0.01277 dB

±0.02025 dB

±0.01460 dB

±0.01583 dB

±0.02025 dB

±0.01460 dB

±0.01583 dB

>10:1

>10:1

>10:1

10:1

>10:1

>10:1

10:1

>10:1

>10:1

```
NA (not applicable) internal test
```
Verifying Specifications Agilent 35670A

Measurement Uncertainty

3-56


**Performance Test
Using Recommended Test**

```
Equipment
```
```
Using Other Test Equipment
```
```
Measurement Uncertainty
```
```
Ratio
Measurement Uncertainty
```
```
Ratio
```
Amplitude Linearity

13 dBVrms

−1 dBVrms

−15 dBVrms

−29 dBVrms

−43 dBVrms

−53 dBVrms

±0.0020 dB

±0.0020 dB

±0.0026 dB

±0.0046 dB

±0.0096 dB

±0.0255 dB

>10:1

>10:1

>10:1

>10:1

>10:1

>10:1

A-Weight Filter

10 Hz

31.62 Hz

100 Hz

1 kHz

10 kHz

25.120 kHz

0.016 dB

0.012 dB

0.012 dB

0.011 dB

0.011 dB

0.012 dB

>10:1

>10:1

>10:1

>10:1

>10:1

>10:1

Channel Match

magnitude

phase

±0.00001 dB

±0.01 mdeg

>10:1

>10:1

Frequency Accuracy
±6.25 ppm

4.8:1

Anti-Alias Filter

<100 kHz

<1 MHz

±0.1 dB

±0.3 dB

>10:1

>10:1

Input Coupling
±0.001 dB

>10:1

Harmonic Distortion

using HP 339A

using HP 3326A with filter

±0.184 dB

±0.92 dB

4.46:1

10:1

Intermodulation Distortion
±0.83 dB

10:1

Cross Talk

channel to channel

source to input

±0.1 dB

±1.34 dB

>10:1

6:1

Single Channel Phase Accuracy
±0.25 deg †

>10:1

External Trigger
280 mVpk 3.6:1 ‡

Tach Function
330 mV 6:1

Input Resistance
±17Ω

>10:1

ICP Supply

oven circuit voltage

current

17 Ω

±320 mV

±132<M > mA

>10:1

>10:1

Agilent 35670A Verifying Specifications

Measurement Uncertainty

3-57


```
† The sync output to signal output phase error was determined to be less than 0.25 degrees.
```
```
‡ If measured value is within3% of specification, verify synthesizer level accuracy. Note: Without 50Ωtermination, observed levels
```
```
are twice the setting into high impedance.
```
**Performance Test
Using Recommended Test**

**Equipment**

**Using Other Test Equipment**

**Measurement**

**Uncertainty**

```
Ratio
Measurement
```
**Uncertainty**

```
Ratio
```
Source Amplitude Accuracy

0.1 Vpk

3.0 Vpk

5.0 Vpk

± 9.83 mVpk

± 492.9 mVpk

±633.0 mVpk

>10:1

>10:1

>10:1

Source Output Resistance
±0.15Ω

>10:1

Source DC Offset

0 Vdc, 0 Vac-pk

±10 Vdc, 0 Vac-pk

0 Vdc, 5 Vac-pk

±5 Vdc, 5 Vac-pk

± 238 nV

±84mV

± 2.123 mV

±43 mV

>10:1

>10:1

>10:1

>10:1

Source Flatness
±0.2 dB

5.24:1

Source Distortion

fundamental <30 kHz

fundamental≥30 kHz

±0.5 dB

±0.5 dB

6.3:1

>10:1

Verifying Specifications Agilent 35670A

Measurement Uncertainty

3-58


Performance Test Record - Two Channel

Test Facility ___________________________________________________________

Facility Address ________________________________________________________

Tested By _____________________________________________________________

Report Number_________________________________________________________

Customer Name________________________________________________________

Serial Number__________________________________________________________

Installed Options _______________________________________________________

Date _________________________________________________________________

Temperature___________________________________________________________

Humidity _____________________________________________________________

Power Line Frequency ___________________________________________________

## Test Instruments Used

```
Instrument Model ID or Serial Number Calibration Due
```
```
AC Calibrator
```
```
Synthesizer 1
```
```
Synthesizer 2
```
```
Low-D Oscillator
```
```
Multimeter
```
Agilent 35670A Verifying Specifications

Performance Test Record - Two Channel

1of14


## Spurious Signals

```
Two Ch, 0 Hz Start, Ch 1
− 80
```
```
Two Ch, 0 Hz Start, Ch 2
− 80
```
```
Two Ch, 200 Hz Start, Ch 1
− 80
```
```
Two Ch, 200 Hz Start, Ch 2
− 80
```
```
Two Ch, 400 Hz Start, Ch 1
− 80
```
```
Two Ch, 400 Hz Start, Ch 2
− 80
```
```
Two Ch, 600 Hz Start, Ch 1
− 80
```
```
Two Ch, 600 Hz Start, Ch 2
− 80
```
```
Two Ch, 800 Hz Start, Ch 1 − 80
```
```
Two Ch, 800 Hz Start, Ch 2
− 80
```
```
Two Ch, 1000 Hz Start, Ch 1
− 80
```
```
Two Ch, 1000 Hz Start, Ch 2 − 80
```
```
Two Ch, 1200 Hz Start, Ch 1
− 80
```
```
Two Ch, 1200 Hz Start, Ch 2
− 80
```
```
Two Ch, 1400 Hz Start, Ch 1
− 80
```
```
Two Ch, 1400 Hz Start, Ch 2
− 80
```
```
Two Ch, 1600 Hz Start, Ch 1
− 80
```
```
Two Ch, 1600 Hz Start, Ch 2
− 80
```
```
Two Ch, 3200 Hz Start, Ch 1
− 80
```
```
Two Ch, 3200 Hz Start, Ch 2
− 80
```
```
Two Ch, 4800 Hz Start, Ch 1
− 80
```
```
Two Ch, 4800 Hz Start, Ch 2
− 80
```
```
Two Ch, 6400 Hz Start, Ch 1
− 80
```
```
Two Ch, 6400 Hz Start, Ch 2
− 80
```
```
Two Ch, 8000 Hz Start, Ch 1 − 80
```
```
Two Ch, 8000 Hz Start, Ch 2
− 80
```
```
Two Ch, 9600 Hz Start, Ch 1
− 80
```
```
Two Ch, 9600 Hz Start, Ch 2
− 80
```
```
Two Ch, 11200 Hz Start, Ch 1
− 80
```
```
Two Ch, 11200 Hz Start, Ch 2
− 80
```
```
Two Ch, 12800 Hz Start, Ch 1
− 80
```
```
Two Ch, 12800 Hz Start, Ch 2
− 80
```
```
Two Ch, 14400 Hz Start, Ch 1
− 80
```
Serial Number:_______________________Report Number:____________________

Test Date:___/___/___

Agilent 35670 Verifying Specifications

Performance Test Record - Two Channel

3of14


```
Two Ch, 14400 Hz Start, Ch 2
− 80
```
```
Two Ch, 16000 Hz Start, Ch 1
− 80
```
```
Two Ch, 16000 Hz Start, Ch 2
− 80
```
```
Two Ch, 17600 Hz Start, Ch 1
− 80
```
```
Two Ch, 17600 Hz Start, Ch 2
− 80
```
```
Two Ch, 19200 Hz Start, Ch 1
− 80
```
```
Two Ch, 19200 Hz Start, Ch 2
− 80
```
```
Two Ch, 20800 Hz Start, Ch 1
− 80
```
```
Two Ch, 20800 Hz Start, Ch 2 − 80
```
```
Two Ch, 22400 Hz Start, Ch 1
− 80
```
```
Two Ch, 22400 Hz Start, Ch 2
− 80
```
```
Two Ch, 24000 Hz Start, Ch 1 − 80
```
```
Two Ch, 24000 Hz Start, Ch 2
− 80
```
```
Two Ch, 25600 Hz Start, Ch 1
− 80
```
```
Two Ch, 25600 Hz Start, Ch 2
− 80
```
```
Two Ch, 27200 Hz Start, Ch 1
− 80
```
```
Two Ch, 27200 Hz Start, Ch 2
− 80
```
```
Two Ch, 28800 Hz Start, Ch 1
− 80
```
```
Two Ch, 28800 Hz Start, Ch 2
− 80
```
```
Two Ch, 30400 Hz Start, Ch 1
− 80
```
```
Two Ch, 30400 Hz Start, Ch 2
− 80
```
```
Two Ch, 32000 Hz Start, Ch 1
− 80
```
```
Two Ch, 32000 Hz Start, Ch 2
− 80
```
```
Two Ch, 33600 Hz Start, Ch 1 − 80
```
```
Two Ch, 33600 Hz Start, Ch 2
− 80
```
```
Two Ch, 35200 Hz Start, Ch 1
− 80
```
```
Two Ch, 35200 Hz Start, Ch 2
− 80
```
```
Two Ch, 36800 Hz Start, Ch 1 − 80
```
```
Two Ch, 36800 Hz Start, Ch 2
− 80
```
```
Two Ch, 38400 Hz Start, Ch 1
− 80
```
```
Two Ch, 38400 Hz Start, Ch 2
− 80
```
```
Two Ch, 40000 Hz Start, Ch 1 − 80
```
```
Two Ch, 40000 Hz Start, Ch 2
− 80
```
```
Two Ch, 41600 Hz Start, Ch 1
− 80
```
```
Two Ch, 41600 Hz Start, Ch 2
− 80
```
Serial Number:_______________________Report Number:____________________

Test Date:___/___/___

Verifying Specifications Agilent 35670A

Performance Test Record - Two Channel

4of14


```
Two Ch, 43200 Hz Start, Ch 1 − 80
```
```
Two Ch, 43200 Hz Start, Ch 2
− 80
```
```
Two Ch, 44800 Hz Start, Ch 1
− 80
```
```
Two Ch, 44800 Hz Start, Ch 2
− 80
```
```
Two Ch, 46400 Hz Start, Ch 1 − 80
```
```
Two Ch, 46400 Hz Start, Ch 2
− 80
```
```
Two Ch, 48000 Hz Start, Ch 1
− 80
```
```
Two Ch, 48000 Hz Start, Ch 2
− 80
```
```
Two Ch, 49600 Hz Start, Ch 1 − 80
```
```
Two Ch, 49600 Hz Start, Ch 2
− 80
```
```
One Ch, 79200 Start, Ch 1
− 80
```
```
One Ch, 80800 Start, Ch 1
− 80
```
```
One Ch, 85600 Start, Ch 1 − 80
```
```
One Ch, 87200 Start, Ch 1
− 80
```
Serial Number:_______________________Report Number:____________________

Test Date:___/___/___

Agilent 35670A Verifying Specifications

Performance Test Record - Two Channel

5of14


## Spurious Signals (continued)

```
Measurement Lower Limit Upper Limit
```
```
(dBfs)
```
```
Measured Value
```
```
(dBfs)
```
```
Pass/Fail
```
```
One Ch, 88800 Start, Ch 1
− 80
```
```
One Ch, 97000 Start, Ch 1
− 80
```
```
One Ch, 98600 Start, Ch 1
− 80
```
```
One Ch, 100200 Start, Ch 1
− 80
```
```
One Ch, 101800 Start, Ch 1
− 80
```
## Amplitude Accuracy

```
Measurement Lower Limit
```
```
(dBVrms)
```
```
Upper Limit
```
```
(dBVrms)
```
```
Measured Value
```
```
(dBVrms)
```
```
Pass/Fail
```
```
−51 dBVrms, Ch 1 −51.15 −50.85
```
```
−51 dBVrms, Ch 2 −51.15 −50.85
```
```
−43 dBVrms, Ch 1 −43.15 −42.85
```
```
−43 dBVrms, Ch 2 −43.15 −42.85
```
```
−35 dBVrms, Ch 1 −35.15 −34.85
```
```
−35 dBVrms, Ch 2 −35.15 −34.85
```
```
−27 dBVrms, Ch 1 −27.15 −26.85
```
```
−27 dBVrms, Ch 2 −27.15 −26.85
```
```
−11 dBVrms, Ch 1 −11.15 −10.85
```
```
−11 dBVrms, Ch 2 −11.15 −10.85
```
```
1 dBVrms, Ch 1
```
```
0.85 1.15
```
```
1 dBVrms, Ch 2
```
```
0.85 1.15
```
```
9 dBVrms, Ch 1
```
```
8.85 9.15
```
```
9 dBVrms, Ch 2
8.85 9.15
```
```
19 dBVrms, Ch 1
18.85 19.15
```
```
19 dBVrms, Ch 2
```
```
18.85 19.15
```
```
27 dBVrms, Ch 1
```
```
26.85 27.15
```
```
27 dBVrms, Ch 2
```
```
26.85 27.15
```
## Flatness

```
Measurement Lower Limit
```
```
(dB)
```
```
Upper Limit
```
```
(dB)
```
```
Measured Value
```
```
(dB)
```
```
Pass/Fail
```
```
27 dBVrms, 99.84 kHz, One Ch, Ch 1
−0.2
```
### 0.2

```
9 dBVrms, 99.84 kHz, One Ch, Ch 1 −0.2 0.2
```
Serial Number:_______________________Report Number:____________________

Test Date:___/___/___

Verifying Specifications Agilent 35670A

Performance Test Record - Two Channel

6of14


```
Measurement Lower Limit
```
```
(dB)
```
```
Upper Limit
```
```
(dB)
```
```
Measured Value
```
```
(dB)
```
```
Pass/Fail
```
```
−11 dBVrms, 99.84 kHz, One Ch, Ch 1 −0.2
```
### 0.2

```
27 dBVrms, 51.2 kHz, Two Ch, Ch 1
−0.2
```
### 0.2

```
27 dBVrms, 51.2 kHz, Two Ch, Ch 2
−0.2
```
### 0.2

```
9 dBVrms, 51.2 kHz, Two Ch, Ch 1
−0.2
```
### 0.2

```
9 dBVrms, 51.2 kHz, Two Ch, Ch 2
−0.2
```
### 0.2

```
−11 dBVrms, 51.2 kHz, Two Ch, Ch 1 −0.2
```
### 0.2

```
−11 dBVrms, 51.2 kHz, Two Ch, Ch 2 −0.2 0.2
```
## Amplitude Linearity

```
Measurement Lower Limit
```
```
(dB)
```
```
Upper Limit
```
```
(dB)
```
```
Measured Value
```
```
(dB)
```
```
Pass/Fail
```
```
13 dBVrms, Ch 1 −0.0615 0.061
```
```
13 dBVrms, Ch 2
−0.0615
```
### 0.061

```
−1 dBVrms, Ch 1 −0.105
```
### 0.104

```
−1 dBVrms, Ch 2 −0.105
```
### 0.104

```
−15 dBVrms, Ch 1 −0.33
```
### 0.318

```
−15 dBVrms, Ch 2 −0.33
```
### 0.318

```
−29 dBVrms, Ch 1 −1.551
```
### 1.316

```
−29 dBVrms, Ch 2 −1.551
```
### 1.316

```
−43 dBVrms, Ch 1 −13.823
```
### 5.088

```
−43 dBVrms, Ch 2 −13.823
```
### 5.088

```
−53 dBVrms, Ch 1 −30.116
```
### 10.896

```
−53 dBVrms, Ch 2 −30.116
```
### 10.896

Serial Number:_______________________Report Number:____________________

Test Date:___/___/___

Agilent 35670A Verifying Specifications

Performance Test Record - Two Channel

7of14


## A-Weight Filter

```
Measurement Lower Limit
```
```
(dB)
```
```
Upper Limit
```
```
(dB)
```
```
Measured Value
```
```
(dB)
```
```
Pass/Fail
```
```
Ch 1, 10 Hz
− 5
```
### 2

```
Ch 2, 10 Hz
− 5
```
### 2

```
Ch 1, 31.62 Hz
− 1
```
### 1

```
Ch 2, 31.62 Hz
− 1
```
### 1

```
Ch 1, 100 Hz
−0.7
```
### 0.7

```
Ch 2, 100 Hz
−0.7
```
### 0.7

```
Ch 1, 1000 Hz −0.7 0.7
```
```
Ch 2, 1000 Hz
−0.7
```
### 0.7

```
Ch 1, 10000 Hz
− 3
```
### 2

```
Ch 2, 10000 Hz − 3 2
```
```
Ch 1, 25120 Hz
−4.5
```
### 2.4

```
Ch 2, 25120 Hz
−4.5
```
### 2.4

## Channel Match

```
Measurement Lower Limit Upper Limit Measured Value Pass/Fail
```
```
Two Ch, 2/1, 7 dBV FS Mag
−0.04 dB
```
```
0.04 dB dB
```
```
Two Ch, 2/1, 7 dBV FS Phs
−0.5 deg
```
```
0.5 deg deg
```
```
Two Ch, 2/1,−13 dBV FS Mag −0.04 dB
```
```
0.04 dB dB
```
```
Two Ch, 2/1,−13 dBV FS Phs −0.5 deg 0.5 deg deg
```
```
Two Ch, 2/1,−33 dBV FS Mag −0.04 dB
```
```
0.04 dB dB
```
```
Two Ch, 2/1,−33 dBV FS Phs −0.5 deg
```
```
0.5 deg deg
```
```
Two Ch, 2/1, 7 dBV−20dBfs Mag −0.08 dB 0.08 dB dB
```
```
Two Ch, 2/1, 7 dBV−20dBfs Phs −0.5 deg
```
```
0.5 deg deg
```
Serial Number:_______________________Report Number:____________________

Test Date:___/___/___

Verifying Specifications Agilent 35670A

Performance Test Record - Two Channel

8of14


## Frequency Accuracy

```
Measurement Lower Limit
```
```
(kHz)
```
```
Upper Limit
```
```
(kHz)
```
```
Measured Value
```
```
(kHz)
```
```
Pass/Fail
```
```
50 kHz
49.9985 50.0015
```
## Anti-Alias Filter

```
Measurement Lower Limit Upper Limit
```
```
(dBfs)
```
```
Measured Value
```
```
(dBfs)
```
```
Pass/Fail
```
```
One Ch, Ch 1, 102.4 kHz − 80
```
```
Two Ch, Ch 1, 51.2 kHz
− 80
```
```
Two Ch, Ch 2, 51.2 kHz
− 80
```
## Input Coupling

```
Measurement Lower Limit Upper Limit
```
```
(dB)
```
```
Measured Value
```
```
(dB)
```
```
Pass/Fail
```
```
dc - ac, Ch 1
```
```
3
```
```
dc - ac, Ch 2
```
```
3
```
Serial Number:_______________________Report Number:____________________

Test Date:___/___/___

Agilent 35670A Verifying Specifications

Performance Test Record - Two Channel

9of14


## Harmonic Distortion

```
Measurement Lower Limit Upper Limit
```
```
(dBfs)
```
```
Measured Value
```
```
(dBfs)
```
```
Pass/Fail
```
```
Single, 12.25 kHz 2nd, Ch 1
− 80
```
```
Two Ch, 12.25 kHz 2nd, Ch 1
− 80
```
```
Two Ch, 12.25 kHz 2nd, Ch 2
− 80
```
```
Single, 8.167 kHz 3rd, Ch 1
− 80
```
```
Two Ch, 8.167 kHz 3rd, Ch 1
− 80
```
```
Two Ch, 8.167 kHz 3rd, Ch 2
− 80
```
```
Single, 6.125 kHz 4th, Ch 1 − 80
```
```
Two Ch, 6.125 kHz 4th, Ch 1
− 80
```
```
Two Ch, 6.125 kHz 4th, Ch 2
− 80
```
```
Single, 4.9 kHz 5th, Ch 1 − 80
```
```
Two Ch, 4.9 kHz 5th, Ch 1
− 80
```
```
Two Ch, 4.9 kHz 5th, Ch 2
− 80
```
Serial Number:_______________________Report Number:____________________

Test Date:___/___/___

Verifying Specifications Agilent 35670A

Performance Test Record - Two Channel

10 of 14


## Intermodulation Distortion

```
Measurement Lower Limit Upper Limit
```
```
(dBfs)
```
```
Measured Value
```
```
(dBfs)
```
```
Pass/Fail
```
```
One Ch, F1+F2, 102.4 kHz, Ch 1
− 80
```
```
One Ch, F1+F2, 64.096 kHz, Ch 1
− 80
```
```
One Ch, F1-2F2, 99.096 kHz, Ch 1
− 80
```
```
Two Ch, F1+F2, 1952 Hz, Ch 1
− 80
```
```
Two Ch, F1+F2, 1952 Hz, Ch 2
− 80
```
```
Two Ch, F1-2F2, 1048 Hz, Ch 1
− 80
```
```
Two Ch, F1-2F2, 1048 Hz, Ch 2 − 80
```
```
Two Ch, F1+F2, 48.048 kHz, Ch 1
− 80
```
```
Two Ch, F1+F2, 48.048 kHz, Ch 2
− 80
```
```
Two Ch, F1+F2, 33.024 kHz, Ch 1 − 80
```
```
Two Ch, F1+F2, 33.024 kHz, Ch 2
− 80
```
```
Two Ch, F1-2F2, 49.096 kHz, Ch 1
− 80
```
```
Two Ch, F1-2F2, 49.096 kHz, Ch 2
− 80
```
## Cross Talk

```
Measurement Lower Limit Upper Limit
```
```
(dBVrms)
```
```
Measured Value
```
```
(dBVrms)
```
```
Pass/Fail
```
```
Source-to-Ch 1
− 126
```
```
Source-to-Ch 2
− 126
```
```
Receiver Ch 1, Driver Ch 2
− 126
```
```
Receiver Ch 2, Driver Ch 1
− 126
```
Serial Number:_______________________Report Number:____________________

Test Date:___/___/___

Agilent 35670A Verifying Specifications

Performance Test Record - Two Channel

11 of 14


## Single Ch Phase Accuracy

```
Measurement Lower Limit
```
```
(deg)
```
```
Upper Limit
```
```
(deg)
```
```
Measured Value
```
```
(deg)
```
```
Pass/Fail
```
```
Positive slope, Ch 1
− 4
```
### 4

```
Positive slope, Ch 2
− 4
```
### 4

```
Negative slope, Ch 1
− 4
```
### 4

```
Negative slope, Ch 2
− 4
```
### 4

## External Trigger

```
Measurement Lower Limit
```
### (%)

```
Upper Limit
```
### (%)

```
Measured Value
```
### (%)

```
Pass/Fail
```
```
8 V Pos − 10 10
```
```
8 V Neg
− 10
```
### 10

```
−8 V Pos − 10
```
### 10

```
−8 V Neg − 10 10
```
## Tach Function (option D01 only)

```
Measurement Lower Limit
```
### (%)

```
Upper Limit
```
### (%)

```
Measured Value
```
### (%)

```
Pass/Fail
```
```
Trigger level +8V Pos
− 10
```
### 10

```
Trigger level +8V Neg
− 10
```
### 10

```
Trigger level−8V Pos − 10
```
### 10

```
Trigger level−8V Neg − 10
```
### 10

Serial Number:_______________________Report Number:____________________

Test Date:___/___/___

Verifying Specifications Agilent 35670A

Performance Test Record - Two Channel

12 of 14


## Input Resistance

```
Measurement Lower Limit
```
### (%)

```
Upper Limit
```
### (%)

```
Measured Value
```
### (%)

```
Pass/Fail
```
```
27 dBVrms, Ch 1
− 10
```
### 10

```
9 dBVrms, Ch 1
− 10
```
### 10

```
−11 dBVrms, Ch 1 − 10
```
### 10

```
27 dBVrms, Ch 2
− 10
```
### 10

```
9 dBVrms, Ch 2
− 10
```
### 10

```
−11 dBVrms, Ch 2 − 10
```
### 10

## ICP Supply

```
Measurement Lower Limit Upper Limit Measured Value Pass/Fail
```
```
Ch 1 Open Circuit Voltage
26 Vdc 32 Vdc Vdc
```
```
Ch 2 Open Circuit Voltage
```
```
26 Vdc 32 Vdc Vdc
```
```
Ch 1 Current
```
```
2.75 mA 5.75 mA mA
```
```
Ch 2 Current
```
```
2.75 mA 5.75 mA mA
```
## Source Amplitude Accuracy

```
Measurement Lower Limit
```
### (%)

```
Upper Limit
```
### (%)

```
Measured Value
```
### (%)

```
Pass/Fail
```
```
1 kHz, 0.1 Vpk
− 4
```
### 4

```
1 kHz, 3.0 Vpk − 4 4
```
```
1 kHz, 5.0 Vpk
− 4
```
### 4

## Source Output Resistance

```
Measurement Lower Limit Upper Limit
```
```
(ohm)
```
```
Measured Value
```
```
(ohm)
```
```
Pass/Fail
```
```
Resistance
5
```
Serial Number:_______________________Report Number:____________________

Test Date:___/___/___

Agilent 35670A Verifying Specifications

Performance Test Record - Two Channel

13 of 14


## Source DC Offset

```
Measurement Lower Limit
```
```
(mVdc)
```
```
Upper Limit
```
```
(mVdc)
```
```
Measured Value
```
```
(mVdc)
```
```
Pass/Fail
```
```
0 Vdc, 0 Vac(pk)
− 15
```
### 15

```
−10 Vdc, 0 Vac(pk) − 315
```
### 315

```
+10 Vdc, 0 Vac(pk)
− 315
```
### 315

```
−5 Vdc, 5 Vac(pk) − 315
```
### 315

```
+5 Vdc, 5 Vac(pk)
− 315
```
### 315

```
0 Vdc, 5 Vac(pk)
− 165
```
### 165

## Source Flatness

```
Measurement Lower Limit
```
```
(dB)
```
```
Upper Limit
```
```
(dB)
```
```
Measured Value
```
```
(dB)
```
```
Pass/Fail
```
```
12.8 kHz
− 1
```
### 1

```
25.6 kHz − 1 1
```
```
51.2 kHz
− 1
```
### 1

```
102.4 kHz
− 1
```
### 1

## Source Distortion

```
Measurement Lower Limit Upper Limit
```
```
(dBc)
```
```
Measured Value
```
```
(dBc)
```
```
Pass/Fail
```
```
12.8 kHz
− 60
```
```
51.2 kHz
− 40
```
```
102.4 kHz
− 40
```
Serial Number:_______________________Report Number:____________________

Test Date:___/___/___

Verifying Specifications Agilent 35670A

Performance Test Record - Two Channel

14 of 14


Performance Test Record - Four Channel

Test Facility ___________________________________________________________

Facility Address ________________________________________________________

Tested By _____________________________________________________________

Report Number_________________________________________________________

Customer Name________________________________________________________

Serial Number__________________________________________________________

Installed Options _______________________________________________________

Date _________________________________________________________________

Temperature___________________________________________________________

Humidity _____________________________________________________________

Power Line Frequency ___________________________________________________

## Test Instruments Used

```
Instrument Model ID or Serial Number Calibration Due
```
```
AC Calibrator
```
```
Synthesizer 1
```
```
Synthesizer 2
```
```
Low-D Oscillator
```
```
Multimeter
```
Agilent 35670A Verifying Specifications

Performance Test Record - Four Channel

1of20


## Spurious Signals

```
Measurement Lower Limit Upper Limit
```
```
(dBfs)
```
```
Measured Value
```
```
(dBfs)
```
```
Pass/Fail
```
```
Four Ch, 0 Hz Start, Ch 1 − 80
```
```
Four Ch, 0 Hz Start, Ch 2
− 80
```
```
Four Ch, 0 Hz Start, Ch 3
− 80
```
```
Four Ch, 0 Hz Start, Ch 4
− 80
```
```
Four Ch, 200 Hz Start, Ch 1 − 80
```
```
Four Ch, 200 Hz Start, Ch 2
− 80
```
```
Four Ch, 200 Hz Start, Ch 3
− 80
```
```
Four Ch, 200 Hz Start, Ch 4
− 80
```
```
Four Ch, 400 Hz Start, Ch 1
− 80
```
```
Four Ch, 400 Hz Start, Ch 2
− 80
```
```
Four Ch, 400 Hz Start, Ch 3
− 80
```
```
Four Ch, 400 Hz Start, Ch 4
− 80
```
```
Four Ch, 600 Hz Start, Ch 1
− 80
```
```
Four Ch, 600 Hz Start, Ch 2
− 80
```
```
Four Ch, 600 Hz Start, Ch 3
− 80
```
```
Four Ch, 600 Hz Start, Ch 4
− 80
```
```
Four Ch, 800 Hz Start, Ch 1
− 80
```
```
Four Ch, 800 Hz Start, Ch 2
− 80
```
```
Four Ch, 800 Hz Start, Ch 3
− 80
```
```
Four Ch, 800 Hz Start, Ch 4
− 80
```
```
Four Ch, 1000 Hz Start, Ch 1
− 80
```
```
Four Ch, 1000 Hz Start, Ch 2
− 80
```
```
Four Ch, 1000 Hz Start, Ch 3
− 80
```
```
Four Ch, 1000 Hz Start, Ch 4
− 80
```
```
Four Ch, 1200 Hz Start, Ch 1
− 80
```
```
Four Ch, 1200 Hz Start, Ch 2
− 80
```
```
Four Ch, 1200 Hz Start, Ch 3
− 80
```
```
Four Ch, 1200 Hz Start, Ch 4
− 80
```
## Spurious Signals (continued)

```
Four Ch, 1400 Hz Start, Ch 1
− 80
```
```
Four Ch, 1400 Hz Start, Ch 2
− 80
```
```
Four Ch, 1400 Hz Start, Ch 3 − 80
```
```
Four Ch, 1400 Hz Start, Ch 4
− 80
```
Serial Number:_______________________Report Number:____________________

Test Date:___/___/___

Agilent 35670A Verifying Specifications

Performance Test Record - Four Channel

3of20


```
Four Ch, 1600 Hz Start, Ch 1 − 80
```
```
Four Ch, 1600 Hz Start, Ch 2
− 80
```
```
Four Ch, 1600 Hz Start, Ch 3
− 80
```
```
Four Ch, 1600 Hz Start, Ch 4
− 80
```
```
Four Ch, 3200 Hz Start, Ch 1
− 80
```
```
Four Ch, 3200 Hz Start, Ch 2
− 80
```
```
Four Ch, 3200 Hz Start, Ch 3
− 80
```
```
Four Ch, 3200 Hz Start, Ch 4
− 80
```
```
Four Ch, 4800 Hz Start, Ch 1
− 80
```
```
Four Ch, 4800 Hz Start, Ch 2
− 80
```
```
Four Ch, 4800 Hz Start, Ch 3
− 80
```
```
Four Ch, 4800 Hz Start, Ch 4
− 80
```
```
Four Ch, 6400 Hz Start, Ch 1
− 80
```
```
Four Ch, 6400 Hz Start, Ch 2 − 80
```
```
Four Ch, 6400 Hz Start, Ch 3
− 80
```
```
Four Ch, 6400 Hz Start, Ch 4
− 80
```
```
Four Ch, 8000 Hz Start, Ch 1
− 80
```
```
Four Ch, 8000 Hz Start, Ch 2
− 80
```
```
Four Ch, 8000 Hz Start, Ch 3
− 80
```
```
Four Ch, 8000 Hz Start, Ch 4
− 80
```
```
Four Ch, 9600 Hz Start, Ch 1
− 80
```
```
Four Ch, 9600 Hz Start, Ch 2
− 80
```
```
Four Ch, 9600 Hz Start, Ch 3
− 80
```
```
Four Ch, 9600 Hz Start, Ch 4
− 80
```
```
Four Ch, 11200 Hz Start, Ch 1
− 80
```
```
Four Ch, 11200 Hz Start, Ch 2
− 80
```
```
Four Ch, 11200 Hz Start, Ch 3 − 80
```
```
Four Ch, 11200 Hz Start, Ch 4
− 80
```
```
Four Ch, 12800 Hz Start, Ch 1
− 80
```
```
Four Ch, 12800 Hz Start, Ch 2
− 80
```
```
Four Ch, 12800 Hz Start, Ch 3
− 80
```
```
Four Ch, 12800 Hz Start, Ch 4
− 80
```
```
Four Ch, 14400 Hz Start, Ch 1
− 80
```
```
Four Ch, 14400 Hz Start, Ch 2
− 80
```
Serial Number:_______________________Report Number:____________________

Test Date:___/___/___

Verifying Specifications Agilent 35670A

Performance Test Record - Four Channel

4of20


```
Four Ch, 14400 Hz Start, Ch 3 − 80
```
```
Four Ch, 14400 Hz Start, Ch 4
− 80
```
```
Four Ch, 16000 Hz Start, Ch 1
− 80
```
```
Four Ch, 16000 Hz Start, Ch 2
− 80
```
```
Four Ch, 16000 Hz Start, Ch 3
− 80
```
```
Four Ch, 16000 Hz Start, Ch 4
− 80
```
```
Four Ch, 17600 Hz Start, Ch 1
− 80
```
```
Four Ch, 17600 Hz Start, Ch 2
− 80
```
```
Four Ch, 17600 Hz Start, Ch 3
− 80
```
```
Four Ch, 17600 Hz Start, Ch 4
− 80
```
```
Four Ch, 19200 Hz Start, Ch 1
− 80
```
```
Four Ch, 19200 Hz Start, Ch 2
− 80
```
```
Four Ch, 19200 Hz Start, Ch 3
− 80
```
```
Four Ch, 19200 Hz Start, Ch 4 − 80
```
```
Four Ch, 20800 Hz Start, Ch 1
− 80
```
```
Four Ch, 20800 Hz Start, Ch 2
− 80
```
Serial Number:_______________________Report Number:____________________

Test Date:___/___/___

Agilent 35670A Verifying Specifications

Performance Test Record - Four Channel

5of20


## Spurious Signals (continued)

```
Four Ch, 20800 Hz Start, Ch 3 − 80
```
```
Four Ch, 20800 Hz Start, Ch 4
− 80
```
```
Four Ch, 22400 Hz Start, Ch 1
− 80
```
```
Four Ch, 22400 Hz Start, Ch 2
− 80
```
```
Four Ch, 22400 Hz Start, Ch 3
− 80
```
```
Four Ch, 22400 Hz Start, Ch 4
− 80
```
```
Four Ch, 24000 Hz Start, Ch 1
− 80
```
```
Four Ch, 24000 Hz Start, Ch 2
− 80
```
```
Four Ch, 24000 Hz Start, Ch 3
− 80
```
```
Four Ch, 24000 Hz Start, Ch 4
− 80
```
```
Two Ch, 25600 Hz Start, Ch 1
− 80
```
```
Two Ch, 25600 Hz Start, Ch 2
− 80
```
```
Two Ch, 27200 Hz Start, Ch 1
− 80
```
```
Two Ch, 27200 Hz Start, Ch 2 − 80
```
```
Two Ch, 28800 Hz Start, Ch 1
− 80
```
```
Two Ch, 28800 Hz Start, Ch 2
− 80
```
```
Two Ch, 30400 Hz Start, Ch 1
− 80
```
```
Two Ch, 30400 Hz Start, Ch 2
− 80
```
```
Two Ch, 32000 Hz Start, Ch 1
− 80
```
```
Two Ch, 32000 Hz Start, Ch 2
− 80
```
```
Two Ch, 33600 Hz Start, Ch 1
− 80
```
```
Two Ch, 33600 Hz Start, Ch 2
− 80
```
```
Two Ch, 35200 Hz Start, Ch 1
− 80
```
```
Two Ch, 35200 Hz Start, Ch 2
− 80
```
```
Two Ch, 36800 Hz Start, Ch 1
− 80
```
```
Two Ch, 36800 Hz Start, Ch 2
− 80
```
```
Two Ch, 38400 Hz Start, Ch 1 − 80
```
```
Two Ch, 38400 Hz Start, Ch 2
− 80
```
```
Two Ch, 40000 Hz Start, Ch 1 − 80
```
```
Two Ch, 40000 Hz Start, Ch 2
− 80
```
```
Two Ch, 41600 Hz Start, Ch 1
− 80
```
```
Two Ch, 41600 Hz Start, Ch 2
− 80
```
```
Two Ch, 43200 Hz Start, Ch 1 − 80
```
```
Two Ch, 43200 Hz Start, Ch 2
− 80
```
Serial Number:_______________________Report Number:____________________

Test Date:___/___/___

Verifying Specifications Agilent 35670A

Performance Test Record - Four Channel

6of20


```
Two Ch, 44800 Hz Start, Ch 1
− 80
```
```
Two Ch, 44800 Hz Start, Ch 2
− 80
```
```
Two Ch, 46400 Hz Start, Ch 1
− 80
```
```
Two Ch, 46400 Hz Start, Ch 2
− 80
```
```
Two Ch, 48000 Hz Start, Ch 1
− 80
```
```
Two Ch, 48000 Hz Start, Ch 2
− 80
```
```
Two Ch, 49600 Hz Start, Ch 1
− 80
```
```
Two Ch, 49600 Hz Start, Ch 2
− 80
```
## Amplitude Accuracy

```
Measurement Lower Limit
```
```
(dBVrms)
```
```
Upper Limit
```
```
(dBVrms)
```
```
Measured Value
```
```
(dBVrms)
```
```
Pass/Fail
```
```
−51 dBVrms, Ch 1 −51.15 −50.85
```
```
−51 dBVrms, Ch 2 −51.15 −50.85
```
```
−51 dBVrms, Ch 3 −51.15 −50.85
```
```
−51 dBVrms, Ch 4 −51.15 −50.85
```
```
−43 dBVrms, Ch 1 −43.15 −42.85
```
```
−43 dBVrms, Ch 2 −43.15 −42.85
```
```
−43 dBVrms, Ch 3 −43.15 −42.85
```
```
−43 dBVrms, Ch 4 −43.15 −42.85
```
```
−35 dBVrms, Ch 1 −35.15 −34.85
```
Serial Number:_______________________Report Number:____________________

Test Date:___/___/___

Agilent 35670A Verifying Specifications

Performance Test Record - Four Channel

7of20


## Amplitude Accuracy (continued)

```
Measurement Lower Limit Upper Limit
```
```
(dBfs)
```
```
Measured Value
```
```
(dBfs)
```
```
Pass/Fail
```
```
−35 dBVrms, Ch 2 −35.15 −34.85
```
```
−35 dBVrms, Ch 3 −35.15 −34.85
```
```
−35 dBVrms, Ch 4 −35.15 −34.85
```
```
−27 dBVrms, Ch 1 −27.15 −26.85
```
```
−27 dBVrms, Ch 2 −27.15 −26.85
```
```
−27 dBVrms, Ch 3 −27.15 −26.85
```
```
−27 dBVrms, Ch 4 −27.15 −26.85
```
```
−11 dBVrms, Ch 1 −11.15 −10.85
```
```
−11 dBVrms, Ch 2 −11.15 −10.85
```
```
−11 dBVrms, Ch 3 −11.15 −10.85
```
```
−11 dBVrms, Ch 4 −11.15 −10.85
```
```
1 dBVrms, Ch 1
```
```
0.85 1.15
```
```
1 dBVrms, Ch 2
0.85 1.15
```
```
1 dBVrms, Ch 3
0.85 1.15
```
```
1 dBVrms, Ch 4
```
```
0.85 1.15
```
```
9 dBVrms, Ch 1
```
```
8.85 9.15
```
```
9 dBVrms, Ch 2
```
```
8.85 9.15
```
```
9 dBVrms, Ch 3
8.85 9.15
```
```
9 dBVrms, Ch 4
```
```
8.85 9.15
```
```
19 dBVrms, Ch 1
```
```
18.85 19.15
```
```
19 dBVrms, Ch 2
```
```
18.85 19.15
```
```
19 dBVrms, Ch 3
18.85 19.15
```
```
19 dBVrms, Ch 4
18.85 19.15
```
```
27 dBVrms, Ch 1
```
```
26.85 27.15
```
```
27 dBVrms, Ch 2
```
```
26.85 27.15
```
```
27 dBVrms, Ch 3
```
```
26.85 27.15
```
```
27 dBVrms, Ch 4
26.85 27.15
```
Serial Number:_______________________Report Number:____________________

Test Date:___/___/___

Verifying Specifications Agilent 35670A

Performance Test Record - Four Channel

8of20


## Flatness

```
Measurement Lower Limit
```
```
(dB)
```
```
Upper Limit
```
```
(dB)
```
```
Measured Value
```
```
(dB)
```
```
Pass/Fail
```
```
27 dBVrms, 51.2 kHz, One Ch, Ch 1
−0.2
```
### 0.2

```
9 dBVrms, 51.2 kHz, One Ch, Ch 1
−0.2
```
### 0.2

```
−11 dBVrms, 51.2 kHz, One Ch, Ch 1 −0.2
```
### 0.2

```
27 dBVrms, 51.2 kHz, Two Ch, Ch 1
−0.2
```
### 0.2

```
27 dBVrms, 51.2 kHz, Two Ch, Ch 2
−0.2
```
### 0.2

```
9 dBVrms, 51.2 kHz, Two Ch, Ch 1
−0.2
```
### 0.2

```
9 dBVrms, 51.2 kHz, Two Ch, Ch 2
−0.2
```
### 0.2

```
−11 dBVrms, 51.2 kHz, Two Ch, Ch 1 −0.2
```
### 0.2

```
−11 dBVrms, 51.2 kHz, Two Ch, Ch 2 −0.2
```
### 0.2

```
27 dBVrms, 25.6 kHz, Four Ch, Ch 1
−0.2
```
### 0.2

```
27 dBVrms, 25.6 kHz, Four Ch, Ch 2
−0.2
```
### 0.2

```
27 dBVrms, 25.6 kHz, Four Ch, Ch 3 −0.2 0.2
```
```
27 dBVrms, 25.6 kHz, Four Ch, Ch 4
−0.2
```
### 0.2

```
9 dBVrms, 25.6 kHz, Four Ch, Ch 1
−0.2
```
### 0.2

```
9 dBVrms, 25.6 kHz, Four Ch, Ch 2
−0.2
```
### 0.2

```
9 dBVrms, 25.6 kHz, Four Ch, Ch 3
−0.2
```
### 0.2

```
9 dBVrms, 25.6 kHz, Four Ch, Ch 4
−0.2
```
### 0.2

```
−11 dBVrms, 25.6 kHz, Four Ch, Ch 1 −0.2
```
### 0.2

```
−11 dBVrms, 25.6 kHz, Four Ch, Ch 2 −0.2
```
### 0.2

```
−11 dBVrms, 25.6 kHz, Four Ch, Ch 3 −0.2
```
### 0.2

```
−11 dBVrms, 25.6 kHz, Four Ch, Ch 4 −0.2
```
### 0.2

Serial Number:_______________________Report Number:____________________

Test Date:___/___/___

Agilent 35670A Verifying Specifications

Performance Test Record - Four Channel

9of20


## Amplitude Linearity

```
Measurement Lower Limit
```
```
(dB)
```
```
Upper Limit
```
```
(dB)
```
```
Measured Value
```
```
(dB)
```
```
Pass/Fail
```
```
13 dBVrms, Ch 1
−0.0615
```
### 0.061

```
13 dBVrms, Ch 2
−0.0615
```
### 0.061

```
13 dBVrms, Ch 3
−0.0615
```
### 0.061

```
13 dBVrms, Ch 4
−0.0615
```
### 0.061

```
−1 dBVrms, Ch 1 −0.105
```
### 0.104

```
−1 dBVrms, Ch 2 −0.105
```
### 0.104

```
−1 dBVrms, Ch 3 −0.105
```
### 0.104

```
−1 dBVrms, Ch 4 −0.105
```
### 0.104

```
−15 dBVrms, Ch 1 −0.33
```
### 0.318

```
−15 dBVrms, Ch 2 −0.33
```
### 0.318

```
−15 dBVrms, Ch 3 −0.33
```
### 0.318

```
−15 dBVrms, Ch 4 −0.33 0.318
```
```
−29 dBVrms, Ch 1 −1.551
```
### 1.316

```
−29 dBVrms, Ch 2 −1.551
```
### 1.316

```
−29 dBVrms, Ch 3 −1.551
```
### 1.316

```
−29 dBVrms, Ch 4 −1.551
```
### 1.316

```
−43 dBVrms, Ch 1 −13.823
```
### 5.088

```
−43 dBVrms, Ch 2 −13.823
```
### 5.088

```
−43 dBVrms, Ch 3 −13.823
```
### 5.088

```
−43 dBVrms, Ch 4 −13.823
```
### 5.088

```
−53 dBVrms, Ch 1 −30.116
```
### 10.896

```
−53 dBVrms, Ch 2 −30.116
```
### 10.896

```
−53 dBVrms, Ch 3 −30.116
```
### 10.896

```
−53 dBVrms, Ch 4 −30.116
```
### 10.896

Serial Number:_______________________Report Number:____________________

Test Date:___/___/___

Verifying Specifications Agilent 35670A

Performance Test Record - Four Channel

10 of 20


## A-Weight Filter

```
Measurement Lower Limit
```
```
(dB)
```
```
Upper Limit
```
```
(dB)
```
```
Measured Value
```
```
(dB)
```
```
Pass/Fail
```
```
Ch 1, 10 Hz
− 5
```
### 2

```
Ch 2, 10 Hz
− 5
```
### 2

```
Ch 3, 10 Hz
− 5
```
### 2

```
Ch 4, 10 Hz
− 5
```
### 2

```
Ch 1, 31.62 Hz
− 1
```
### 1

```
Ch 2, 31.62 Hz
− 1
```
### 1

```
Ch 3, 31.62 Hz
− 1
```
### 1

```
Ch 4, 31.62 Hz
− 1
```
### 1

```
Ch 1, 100 Hz
−0.7
```
### 0.7

```
Ch 2, 100 Hz
−0.7
```
### 0.7

```
Ch 3, 100 Hz
−0.7
```
### 0.7

```
Ch 4, 100 Hz −0.7 0.7
```
```
Ch 1, 1000 Hz
−0.7
```
### 0.7

```
Ch 2, 1000 Hz
−0.7
```
### 0.7

```
Ch 3, 1000 Hz
−0.7
```
### 0.7

```
Ch 4, 1000 Hz
−0.7
```
### 0.7

```
Ch 1, 10000 Hz
− 3
```
### 2

```
Ch 2, 10000 Hz
− 3
```
### 2

```
Ch 3, 10000 Hz
− 3
```
### 2

```
Ch 4, 10000 Hz
− 3
```
### 2

```
Ch 1, 25120 Hz
−4.5
```
### 2.4

```
Ch 2, 25120 Hz
−4.5
```
### 2.4

```
Ch 3, 25120 Hz
−4.5
```
### 2.4

```
Ch 4, 25120 Hz
−4.5
```
### 2.4

Serial Number:_______________________Report Number:____________________

Test Date:___/___/___

Agilent 35670A Verifying Specifications

Performance Test Record - Four Channel

11 of 20


## Channel Match

```
Two Ch, 2/1, 7 dBV FS Mag −0.04 0.04
```
```
Two Ch, 2/1, 7 dBV FS Phs
−0.5
```
### 0.5

```
Two Ch, 2/1,−13 dBV FS Mag −0.04
```
### 0.04

```
Two Ch, 2/1,−13 dBV FS Phs −0.5
```
### 0.5

```
Two Ch, 2/1,−33 dBV FS Mag −0.04
```
### 0.04

```
Two Ch, 2/1,−33 dBV FS Phs −0.5
```
### 0.5

```
Two Ch, 2/1, 7 dBV−20 dBfs Mag −0.08
```
### 0.08

```
Two Ch, 2/1, 7 dBV−20 dBfs Phs −0.5
```
### 0.5

```
Four Ch, 2/1, 7 dBV FS Mag
−0.04
```
### 0.04

```
Four Ch, 2/1, 7 dBV FS Phs
−0.5
```
### 0.5

```
Four Ch, 2/1,−13 dBV FS Mag −0.04
```
### 0.04

```
Four Ch, 2/1,−13 dBV FS Phs −0.5
```
### 0.5

```
Four Ch, 2/1,−33 dBV FS Mag −0.04
```
### 0.04

```
Four Ch, 2/1,−33 dBV FS Phs −0.5 0.5
```
```
Four Ch, 2/1, 7 dBV−20 dBfs Mag −0.08
```
### 0.08

```
Four Ch, 2/1, 7 dBV−20 dBfs Phs −0.5
```
### 0.5

```
Four Ch, 3/1, 7 dBV FS Mag
−0.04
```
### 0.04

```
Four Ch, 3/1, 7 dBV FS Phs
−0.5
```
### 0.5

```
Four Ch, 3/1,−13 dBV FS Mag −0.04
```
### 0.04

```
Four Ch, 3/1,−13 dBV FS Phs −0.5
```
### 0.5

```
Four Ch, 3/1,−33 dBV FS Mag −0.04
```
### 0.04

```
Four Ch, 3/1,−33 dBV FS Phs −0.5
```
### 0.5

```
Four Ch, 3/1, 7 dBV−20 dBfs Mag −0.08
```
### 0.08

```
Four Ch, 3/1, 7 dBV−20 dBfs Phs −0.5
```
### 0.5

```
Four Ch, 4/1, 7 dBV FS Mag
−0.04
```
### 0.04

```
Four Ch, 4/1, 7 dBV FS Phs
−0.5
```
### 0.5

```
Four Ch, 4/1,−13 dBV FS Mag −0.04 0.04
```
```
Four Ch, 4/1,−13 dBV FS Phs −0.5
```
### 0.5

```
Four Ch, 4/1,−33 dBV FS Mag −0.04
```
### 0.04

```
Four Ch, 4/1,−33 dBV FS Phs −0.5
```
### 0.5

```
Four Ch, 4/1, 7 dBV−20 dBfs Mag −0.08
```
### 0.08

```
Four Ch, 4/1, 7 dBV−20 dBfs Phs −0.5
```
### 0.5

```
Four Ch, 4/3, 7 dBV FS Mag
−0.04
```
### 0.04

Serial Number:_______________________Report Number:____________________

Test Date:___/___/___

Verifying Specifications Agilent 35670A

Performance Test Record - Four Channel

12 of 20


```
Four Ch, 4/3, 7 dBV FS Phs −0.5 0.5
```
```
Four Ch, 4/3,−13 dBV FS Mag −0.04
```
### 0.04

```
Four Ch, 4/3,−13 dBV FS Phs −0.5
```
### 0.5

```
Four Ch, 4/3,−33 dBV FS Mag −0.04
```
### 0.04

```
Four Ch, 4/3,−33 dBV FS Phs −0.5
```
### 0.5

```
Four Ch, 4/3, 7 dBV−20 dBfs Mag −0.08
```
### 0.08

```
Four Ch, 4/3, 7 dBV−20 dBfs Phs −0.5
```
### 0.5

Serial Number:_______________________Report Number:____________________

Test Date:___/___/___

Agilent 35670A Verifying Specifications

Performance Test Record - Four Channel

13 of 20


## Frequency Accuracy

```
Measurement Lower Limit
```
```
(kHz)
```
```
Upper Limit
```
```
(kHz)
```
```
Measured Value
```
```
(kHz)
```
```
Pass/Fail
```
```
50 kHz
```
```
49.9985 50.0015
```
## Anti-Alias Filter

```
Measurement Lower Limit Upper Limit
```
```
(dBfs)
```
```
Measured Value
```
```
(dBfs)
```
```
Pass/Fail
```
```
One Ch, Ch 1, 51.2 kHz
− 80
```
```
Two Ch, Ch 1, 51.2 kHz
− 80
```
```
Two Ch, Ch 2, 51.2 kHz − 80
```
```
Four Ch, Ch 1, 25.6 kHz
− 80
```
```
Four Ch, Ch 2, 25.6 kHz
− 80
```
```
Four Ch, Ch 3, 25.6 kHz − 80
```
```
Four Ch, Ch 4, 25.6 kHz
− 80
```
## Input Coupling

```
Measurement Lower Limit Upper Limit
```
```
(dB)
```
```
Measured Value
```
```
(dB)
```
```
Pass/Fail
```
```
dc - ac, Ch 1
3
```
```
dc - ac, Ch 2
3
```
```
dc - ac, Ch 3
```
```
3
```
```
dc - ac, Ch 4
```
```
3
```
Serial Number:_______________________Report Number:____________________

Test Date:___/___/___

Verifying Specifications Agilent 35670A

Performance Test Record - Four Channel

14 of 20


## Harmonic Distortion

```
Measurement Lower Limit Upper Limit
```
```
(dBfs)
```
```
Measured Value
```
```
(dBfs)
```
```
Pass/Fail
```
```
Two Ch, 12.25 kHz 2nd, Ch 1
− 80
```
```
Two Ch, 12.25 kHz 2nd, Ch 2
− 80
```
```
Four Ch, 12.25 kHz 2nd, Ch 1
− 80
```
```
Four Ch, 12.25 kHz 2nd, Ch 2
− 80
```
```
Four Ch, 12.25 kHz 2nd, Ch 3
− 80
```
```
Four Ch, 12.25 kHz 2nd, Ch 4
− 80
```
```
Two Ch, 8.167 kHz 3rd, Ch 1
− 80
```
```
Two Ch, 8.167 kHz 3rd, Ch 2
− 80
```
```
Four Ch, 8.167 kHz 3rd, Ch 1
− 80
```
```
Four Ch, 8.167 kHz 3rd, Ch 2
− 80
```
```
Four Ch, 8.167 kHz 3rd, Ch 3
− 80
```
```
Four Ch, 8.167 kHz 3rd, Ch 4 − 80
```
```
Two Ch, 6.125 kHz 4th, Ch 1
− 80
```
```
Two Ch, 6.125 kHz 4th, Ch 2
− 80
```
```
Four Ch, 6.125 kHz 4th, Ch 1
− 80
```
```
Four Ch, 6.125 kHz 4th, Ch 2
− 80
```
```
Four Ch, 6.125 kHz 4th, Ch 3
− 80
```
```
Four Ch, 6.125 kHz 4th, Ch 4
− 80
```
```
Two Ch, 4.9 kHz 5th, Ch 1
− 80
```
```
Two Ch, 4.9 kHz 5th, Ch 2
− 80
```
```
Four Ch, 4.9 kHz 5th, Ch 1
− 80
```
```
Four Ch, 4.9 kHz 5th, Ch 2
− 80
```
```
Four Ch, 4.9 kHz 5th, Ch 3
− 80
```
```
Four Ch, 4.9 kHz 5th, Ch 4
− 80
```
Serial Number:_______________________Report Number:____________________

Test Date:___/___/___

Agilent 35670A Verifying Specifications

Performance Test Record - Four Channel

15 of 20


## Cross Talk

```
Measurement Lower Limit Upper Limit
```
```
(dBVrms)
```
```
Measured Value
```
```
(dBVrms)
```
```
Pass/Fail
```
```
Source-to-Ch 1
− 126
```
```
Source-to-Ch 2
− 126
```
```
Source-to-Ch 3
− 126
```
```
Source-to-Ch 4
− 126
```
```
Receiver Ch 1, Driver Ch 2, 3, 4
− 126
```
```
Receiver Ch 2, Driver Ch 1, 3, 4
− 126
```
```
Receiver Ch 3, Driver Ch 1, 2, 4
− 126
```
```
Receiver Ch 4, Driver Ch 1, 2, 3
− 126
```
## Single Ch Phase Accuracy

```
Measurement Lower Limit
```
```
(deg)
```
```
Upper Limit
```
```
(deg)
```
```
Measured Value
```
```
(deg)
```
```
Pass/Fail
```
```
Positive slope, Ch 1
− 4
```
### 4

```
Positive slope, Ch 2 − 4 4
```
```
Positive slope, Ch 3
− 4
```
### 4

```
Positive slope, Ch 4
− 4
```
### 4

```
Negative slope, Ch 1
− 4
```
### 4

```
Negative slope, Ch 2
− 4
```
### 4

```
Negative slope, Ch 3
− 4
```
### 4

```
Negative slope, Ch 4
− 4
```
### 4

Serial Number:_______________________Report Number:____________________

Test Date:___/___/___

Agilent 35670A Verifying Specifications

Performance Test Record - Four Channel

17 of 20


## External Trigger

```
Measurement Lower Limit
```
### (%)

```
Upper Limit
```
### (%)

```
Measured Value
```
### (%)

```
Pass/Fail
```
```
8 V Pos − 10 10
```
```
8 V Neg
− 10
```
### 10

```
−8 V Pos − 10
```
### 10

```
−8 V Neg − 10
```
### 10

## Tach Function (option D01 only)

```
Measurement Lower Limit
```
### (%)

```
Upper Limit
```
### (%)

```
Measured Value
```
### (%)

```
Pass/Fail
```
```
Trigger level +8V Pos
− 10
```
### 10

```
Trigger level +8V Neg
− 10
```
### 10

```
Trigger level−8V Pos − 10 10
```
```
Trigger level−8V Neg − 10
```
### 10

## Input Resistance

```
Measurement Lower Limit
```
### (%)

```
Upper Limit
```
### (%)

```
Measured Value
```
### (%)

```
Pass/Fail
```
```
27 dBVrms, Ch 1 − 10 10
```
```
9 dBVrms, Ch 1
− 10
```
### 10

```
−11 dBVrms, Ch 1 − 10
```
### 10

```
27 dBVrms, Ch 2
− 10
```
### 10

```
9 dBVrms, Ch 2 − 10 10
```
```
−11 dBVrms, Ch 2 − 10
```
### 10

```
27 dBVrms, Ch 3
− 10
```
### 10

```
9 dBVrms, Ch 3
− 10
```
### 10

```
−11 dBVrms, Ch 3 − 10 10
```
```
27 dBVrms, Ch 4
− 10
```
### 10

```
9 dBVrms, Ch 4
− 10
```
### 10

```
−11 dBVrms, Ch 4 − 10
```
### 10

## ICP Supply

```
Measurement Lower Limit Upper Limit Measured Value Pass/Fail
```
```
Ch 1 Open Circuit Voltage
```
```
26 Vdc 32 Vdc Vdc
```
```
Ch 2 Open Circuit Voltage
```
```
26 Vdc 32 Vdc Vdc
```
```
Ch 31 Open Circuit Voltage
26 Vdc 32 Vdc Vdc
```
```
Ch 4 Open Circuit Voltage
26 Vdc 32 Vdc Vdc
```
```
Ch 1 Current
```
```
2.75 mA 5.75 mA mA
```
Serial Number:_______________________Report Number:____________________

Test Date:___/___/___

Verifying Specifications Agilent 35670A

Performance Test Record - Four Channel

18 of 20


```
Measurement Lower Limit Upper Limit Measured Value Pass/Fail
```
```
Ch 2 Current
2.75 mA 5.75 mA mA
```
```
Ch 3 Current
2.75 mA 5.75 mA mA
```
```
Ch 4 Current
```
```
2.75 mA 5.75 mA mA
```
## Source Amplitude Accuracy

```
Measurement Lower Limit
```
### (%)

```
Upper Limit
```
### (%)

```
Measured Value
```
### (%)

```
Pass/Fail
```
```
1 kHz, 0.1 Vpk
− 4
```
### 4

```
1 kHz, 3.0 Vpk
− 4
```
### 4

```
1 kHz, 5.0 Vpk
− 4
```
### 4

## Source Output Resistance

```
Measurement Lower Limit Upper Limit
```
```
(ohm)
```
```
Measured Value
```
```
(ohm)
```
```
Pass/Fail
```
```
Resistance
```
```
5
```
Serial Number:_______________________Report Number:____________________

Test Date:___/___/___

Agilent 35670A Verifying Specifications

Performance Test Record - Four Channel

19 of 20


## Source DC Offset

```
Measurement Lower Limit
```
```
(mVdc)
```
```
Upper Limit
```
```
(mVdc)
```
```
Measured Value
```
```
(mVdc)
```
```
Pass/Fail
```
```
0 Vdc, 0 Vac(pk)
− 15
```
### 15

```
−10 Vdc, 0 Vac(pk) − 315
```
### 315

```
+10 Vdc, 0 Vac(pk)
− 315
```
### 315

```
−5 Vdc, 5 Vac(pk) − 315
```
### 315

```
+5 Vdc, 5 Vac(pk)
− 315
```
### 315

```
0 Vdc, 5 Vac(pk)
− 165
```
### 165

## Source Flatness

```
Measurement Lower Limit
```
```
(dB)
```
```
Upper Limit
```
```
(dB)
```
```
Measured Value
```
```
(dB)
```
```
Pass/Fail
```
```
12.8 kHz
− 1
```
### 1

```
25.6 kHz
− 1
```
### 1

```
51.2 kHz
− 1
```
### 1

## Source Distortion

```
Measurement Lower Limit Upper Limit
```
```
(dBc)
```
```
Measured Value
```
```
(dBc)
```
```
Pass/Fail
```
```
12.8 kHz
− 60
```
```
51.2 kHz
− 40
```
Serial Number:_______________________Report Number:____________________

Test Date:___/___/___

Verifying Specifications Agilent 35670A

Performance Test Record - Four Channel

20 of 20


Operation Verification Test Record - Two Channel

Test Facility ___________________________________________________________

Facility Address ________________________________________________________

Tested By _____________________________________________________________

Report Number_________________________________________________________

Customer Name________________________________________________________

Serial Number__________________________________________________________

Installed Options _______________________________________________________

Date _________________________________________________________________

Temperature___________________________________________________________

Humidity _____________________________________________________________

Power Line Frequency ___________________________________________________

## Test Instruments Used

```
Instrument Model ID or Serial Number Calibration Due
```
```
AC Calibrator
```
```
Synthesizer 1
```
```
Synthesizer 2
```
```
Low-D Oscillator
```
```
Multimeter
```
Agilent 35670A Verifying Specifications

Operation Verification Test Record - Two Channel

1of10


## Spurious Signals

```
Two Ch, 0 Hz Start, Ch 1 − 80
```
```
Two Ch, 0 Hz Start, Ch 2
− 80
```
```
Two Ch, 200 Hz Start, Ch 1
− 80
```
```
Two Ch, 200 Hz Start, Ch 2
− 80
```
```
Two Ch, 400 Hz Start, Ch 1
− 80
```
```
Two Ch, 400 Hz Start, Ch 2
− 80
```
```
Two Ch, 600 Hz Start, Ch 1
− 80
```
```
Two Ch, 600 Hz Start, Ch 2
− 80
```
```
Two Ch, 800 Hz Start, Ch 1
− 80
```
```
Two Ch, 800 Hz Start, Ch 2
− 80
```
```
Two Ch, 1000 Hz Start, Ch 1
− 80
```
```
Two Ch, 1000 Hz Start, Ch 2
− 80
```
```
Two Ch, 1200 Hz Start, Ch 1
− 80
```
```
Two Ch, 1200 Hz Start, Ch 2 − 80
```
```
Two Ch, 1400 Hz Start, Ch 1
− 80
```
```
Two Ch, 1400 Hz Start, Ch 2
− 80
```
```
Two Ch, 1600 Hz Start, Ch 1
− 80
```
```
Two Ch, 1600 Hz Start, Ch 2
− 80
```
```
Two Ch, 3200 Hz Start, Ch 1
− 80
```
```
Two Ch, 3200 Hz Start, Ch 2
− 80
```
```
Two Ch, 4800 Hz Start, Ch 1
− 80
```
```
Two Ch, 4800 Hz Start, Ch 2
− 80
```
```
Two Ch, 6400 Hz Start, Ch 1
− 80
```
```
Two Ch, 6400 Hz Start, Ch 2
− 80
```
```
Two Ch, 8000 Hz Start, Ch 1
− 80
```
```
Two Ch, 8000 Hz Start, Ch 2
− 80
```
```
Two Ch, 9600 Hz Start, Ch 1 − 80
```
```
Two Ch, 9600 Hz Start, Ch 2
− 80
```
```
Two Ch, 11200 Hz Start, Ch 1
− 80
```
```
Two Ch, 11200 Hz Start, Ch 2
− 80
```
```
Two Ch, 12800 Hz Start, Ch 1
− 80
```
```
Two Ch, 12800 Hz Start, Ch 2
− 80
```
```
Two Ch, 14400 Hz Start, Ch 1
− 80
```
Serial Number:_______________________Report Number:____________________

Test Date:___/___/___

Agilent 35670A Verifying Specifications

Operation Verification Test Record - Two Channel

3of10


```
Two Ch, 14400 Hz Start, Ch 2 − 80
```
```
Two Ch, 16000 Hz Start, Ch 1
− 80
```
```
Two Ch, 16000 Hz Start, Ch 2
− 80
```
```
Two Ch, 17600 Hz Start, Ch 1
− 80
```
```
Two Ch, 17600 Hz Start, Ch 2
− 80
```
```
Two Ch, 19200 Hz Start, Ch 1
− 80
```
```
Two Ch, 19200 Hz Start, Ch 2
− 80
```
```
Two Ch, 20800 Hz Start, Ch 1
− 80
```
```
Two Ch, 20800 Hz Start, Ch 2
− 80
```
```
Two Ch, 22400 Hz Start, Ch 1
− 80
```
```
Two Ch, 22400 Hz Start, Ch 2
− 80
```
```
Two Ch, 24000 Hz Start, Ch 1
− 80
```
```
Two Ch, 24000 Hz Start, Ch 2
− 80
```
```
Two Ch, 25600 Hz Start, Ch 1 − 80
```
```
Two Ch, 25600 Hz Start, Ch 2
− 80
```
```
Two Ch, 27200 Hz Start, Ch 1
− 80
```
```
Two Ch, 27200 Hz Start, Ch 2
− 80
```
```
Two Ch, 28800 Hz Start, Ch 1
− 80
```
```
Two Ch, 28800 Hz Start, Ch 2
− 80
```
```
Two Ch, 30400 Hz Start, Ch 1
− 80
```
```
Two Ch, 30400 Hz Start, Ch 2
− 80
```
Serial Number:_______________________Report Number:____________________

Test Date:___/___/___

Verifying Specifications Agilent 35670A

Operation Verification Test Record - Two Channel

4of10


## Spurious Signals (continued)

```
Two Ch, 32000 Hz Start, Ch 1
− 80
```
```
Two Ch, 32000 Hz Start, Ch 2 − 80
```
```
Two Ch, 33600 Hz Start, Ch 1
− 80
```
```
Two Ch, 33600 Hz Start, Ch 2
− 80
```
```
Two Ch, 35200 Hz Start, Ch 1
− 80
```
```
Two Ch, 35200 Hz Start, Ch 2
− 80
```
```
Two Ch, 36800 Hz Start, Ch 1
− 80
```
```
Two Ch, 36800 Hz Start, Ch 2
− 80
```
```
Two Ch, 38400 Hz Start, Ch 1
− 80
```
```
Two Ch, 38400 Hz Start, Ch 2
− 80
```
```
Two Ch, 40000 Hz Start, Ch 1
− 80
```
```
Two Ch, 40000 Hz Start, Ch 2
− 80
```
```
Two Ch, 41600 Hz Start, Ch 1 − 80
```
```
Two Ch, 41600 Hz Start, Ch 2
− 80
```
```
Two Ch, 43200 Hz Start, Ch 1
− 80
```
```
Two Ch, 43200 Hz Start, Ch 2
− 80
```
```
Two Ch, 44800 Hz Start, Ch 1
− 80
```
```
Two Ch, 44800 Hz Start, Ch 2
− 80
```
```
Two Ch, 46400 Hz Start, Ch 1
− 80
```
```
Two Ch, 46400 Hz Start, Ch 2
− 80
```
```
Two Ch, 48000 Hz Start, Ch 1
− 80
```
```
Two Ch, 48000 Hz Start, Ch 2
− 80
```
```
Two Ch, 49600 Hz Start, Ch 1
− 80
```
```
Two Ch, 49600 Hz Start, Ch 2
− 80
```
```
One Ch, 79200 Start, Ch 1
− 80
```
```
One Ch, 80800 Start, Ch 1
− 80
```
```
One Ch, 85600 Start, Ch 1
− 80
```
```
One Ch, 87200 Start, Ch 1
− 80
```
```
One Ch, 88800 Start, Ch 1
− 80
```
```
One Ch, 97000 Start, Ch 1
− 80
```
```
One Ch, 98600 Start, Ch 1
− 80
```
```
One Ch, 100200 Start, Ch 1 − 80
```
```
One Ch, 101800 Start, Ch 1
− 80
```
Serial Number:_______________________Report Number:____________________

Test Date:___/___/___

Agilent 35670A Verifying Specifications

Operation Verification Test Record - Two Channel

5of10


## Amplitude Accuracy

```
Measurement Lower Limit
```
```
(dBVrms)
```
```
Upper Limit
```
```
(dBVrms)
```
```
Measured Value
```
```
(dBVrms)
```
```
Pass/Fail
```
```
−51 dBVrms, Ch 1 −51.15 −50.85
```
```
−51 dBVrms, Ch 2 −51.15 −50.85
```
```
−43 dBVrms, Ch 1 −43.15 −42.85
```
```
−43 dBVrms, Ch 2 −43.15 −42.85
```
```
−35 dBVrms, Ch 1 −35.15 −34.85
```
```
−35 dBVrms, Ch 2 −35.15 −34.85
```
```
−27 dBVrms, Ch 1 −27.15 −26.85
```
```
−27 dBVrms, Ch 2 −27.15 −26.85
```
```
−11 dBVrms, Ch 1 −11.15 −10.85
```
```
−11 dBVrms, Ch 2 −11.15 −10.85
```
```
1 dBVrms, Ch 1
```
```
0.85 1.15
```
```
1 dBVrms, Ch 2
```
```
0.85 1.15
```
```
9 dBVrms, Ch 1
```
```
8.85 9.15
```
```
9 dBVrms, Ch 2
```
```
8.85 9.15
```
```
19 dBVrms, Ch 1
```
```
18.85 19.15
```
```
19 dBVrms, Ch 2
18.85 19.15
```
```
27 dBVrms, Ch 1
26.85 27.15
```
```
27 dBVrms, Ch 2
```
```
26.85 27.15
```
Serial Number:_______________________Report Number:____________________

Test Date:___/___/___

Verifying Specifications Agilent 35670A

Operation Verification Test Record - Two Channel

6of10


## Flatness

```
Measurement Lower Limit
```
```
(dB)
```
```
Upper Limit
```
```
(dB)
```
```
Measured Value
```
```
(dB)
```
```
Pass/Fail
```
```
27 dBVrms, 99.84 kHz, One Ch, Ch 1
−0.2
```
### 0.2

```
9 dBVrms, 99.84 kHz, One Ch, Ch 1
−0.2
```
### 0.2

```
−11 dBVrms, 99.84 kHz, One Ch, Ch 1 −0.2
```
### 0.2

```
27 dBVrms, 51.2 kHz, Two Ch, Ch 1
−0.2
```
### 0.2

```
27 dBVrms, 51.2 kHz, Two Ch, Ch 2
−0.2
```
### 0.2

```
9 dBVrms, 51.2 kHz, Two Ch, Ch 1
−0.2
```
### 0.2

```
9 dBVrms, 51.2 kHz, Two Ch, Ch 2
−0.2
```
### 0.2

```
−11 dBVrms, 51.2 kHz, Two Ch, Ch 1 −0.2
```
### 0.2

```
−11 dBVrms, 51.2 kHz, Two Ch, Ch 2 −0.2
```
### 0.2

## Amplitude Linearity

```
Measurement Lower Limit
```
```
(dB)
```
```
Upper Limit
```
```
(dB)
```
```
Measured Value
```
```
(dB)
```
```
Pass/Fail
```
```
13 dBVrms, Ch 1 −0.0615 0.061
```
```
13 dBVrms, Ch 2
−0.0615
```
### 0.061

```
−1 dBVrms, Ch 1 −0.105
```
### 0.104

```
−1 dBVrms, Ch 2 −0.105
```
### 0.104

```
−15 dBVrms, Ch 1 −0.33
```
### 0.318

```
−15 dBVrms, Ch 2 −0.33
```
### 0.318

```
−29 dBVrms, Ch 1 −1.551
```
### 1.316

```
−29 dBVrms, Ch 2 −1.551
```
### 1.316

```
−43 dBVrms, Ch 1 −13.823
```
### 5.088

```
−43 dBVrms, Ch 2 −13.823
```
### 5.088

```
−53 dBVrms, Ch 1 −30.116
```
### 10.896

```
−53 dBVrms, Ch 2 −30.116
```
### 10.896

## A Weight Filter

```
Measurement Lower Limit
```
```
(dB)
```
```
Upper Limit
```
```
(dB)
```
```
Measured Value
```
```
(dB)
```
```
Pass/Fail
```
```
Ch 1, 10 Hz
− 5
```
### 2

```
Ch 2, 10 Hz
− 5
```
### 2

```
Ch 1, 31.62 Hz
− 1
```
### 1

```
Ch 2, 31.62 Hz
− 1
```
### 1

Serial Number:_______________________Report Number:____________________

Test Date:___/___/___

Agilent 35670A Verifying Specifications

Operation Verification Test Record - Two Channel

7of10


```
Measurement Lower Limit
```
```
(dB)
```
```
Upper Limit
```
```
(dB)
```
```
Measured Value
```
```
(dB)
```
```
Pass/Fail
```
```
Ch 1, 100 Hz
−0.7
```
### 0.7

```
Ch 2, 100 Hz
−0.7
```
### 0.7

```
Ch 1, 1000 Hz
−0.7
```
### 0.7

```
Ch 2, 1000 Hz
−0.7
```
### 0.7

```
Ch 1, 10000 Hz
− 3
```
### 2

```
Ch 2, 10000 Hz
− 3
```
### 2

```
Ch 1, 25120 Hz
−4.5
```
### 2.4

```
Ch 2, 25120 Hz
−4.5
```
### 2.4

## Channel Match

```
Measurement Lower Limit Upper Limit Measured Value Pass/Fail
```
```
Two Ch, 2/1, 7 dBV FS Mag
−0.04 dB
```
```
0.04 dB dB
```
```
Two Ch, 2/1, 7 dBV FS Phs
−0.5 deg
```
```
0.5 deg deg
```
```
Two Ch, 2/1,−13 dBV FS Mag −0.04 dB
```
```
0.04 dB dB
```
```
Two Ch, 2/1,−13 dBV FS Phs −0.5 deg
```
```
0.5 deg deg
```
```
Two Ch, 2/1,−33 dBV FS Mag −0.04 dB
```
```
0.04 dB dB
```
```
Two Ch, 2/1,−33 dBV FS Phs −0.5 deg
```
```
0.5 deg deg
```
```
Two Ch, 2/1, 7 dBV−20dBfs Mag −0.08 dB
```
```
0.08 dB dB
```
```
Two Ch, 2/1, 7 dBV−20dBfs Phs −0.5 deg
```
```
0.5 deg deg
```
Serial Number:_______________________Report Number:____________________

Test Date:___/___/___

Verifying Specifications Agilent 35670A

Operation Verification Test Record - Two Channel

8of10


## Frequency Accuracy

```
Measurement Lower Limit
```
```
(kHz)
```
```
Upper Limit
```
```
(kHz)
```
```
Measured Value
```
```
(kHz)
```
```
Pass/Fail
```
```
50 kHz
```
```
49.9985 50.0015
```
## Single Ch Phase Accuracy

```
Measurement Lower Limit
```
```
(deg)
```
```
Upper Limit
```
```
(deg)
```
```
Measured Value
```
```
(deg)
```
```
Pass/Fail
```
```
Positive slope, Ch 1
− 4
```
### 4

```
Positive slope, Ch 2
− 4
```
### 4

```
Negative slope, Ch 1 − 4 4
```
```
Negative slope, Ch 2
− 4
```
### 4

## Tach Function (option D01 only)

```
Measurement Lower Limit
```
### (%)

```
Upper Limit
```
### (%)

```
Measured Value
```
### (%)

```
Pass/Fail
```
```
Trigger level +8V Pos
− 10
```
### 10

```
Trigger level +8V Neg
− 10
```
### 10

```
Trigger level−8V Pos − 10
```
### 10

```
Trigger level−8V Neg − 10
```
### 10

Serial Number:_______________________Report Number:____________________

Test Date:___/___/___

Agilent 35670A Verifying Specifications

Operation Verification Test Record - Two Channel

9of10


## ICP Supply

```
Measurement Lower Limit Upper Limit Measured Value Pass/Fail
```
```
Ch 1 Open Circuit Voltage
26 Vdc 32 Vdc Vdc
```
```
Ch 2 Open Circuit Voltage
26 Vdc 32 Vdc Vdc
```
```
Ch 1 Current
```
```
2.75 mA 5.75 mA mA
```
```
Ch 2 Current
```
```
2.75 mA 5.75 mA mA
```
## Source Amplitude Accuracy

```
Measurement Lower Limit
```
### (%)

```
Upper Limit
```
### (%)

```
Measured Value
```
### (%)

```
Pass/Fail
```
```
1 kHz, 0.1 Vpk
− 4
```
### 4

```
1 kHz, 3.0 Vpk
− 4
```
### 4

```
1 kHz, 5.0 Vpk
− 4
```
### 4

## Source Flatness

```
Measurement Lower Limit
```
```
(dB)
```
```
Upper Limit
```
```
(dB)
```
```
Measured Value
```
```
(dB)
```
```
Pass/Fail
```
```
12.8 kHz
− 1
```
### 1

```
25.6 kHz
− 1
```
### 1

```
51.2 kHz
− 1
```
### 1

```
102.4 kHz
− 1
```
### 1

## Source Distortion

```
Measurement Lower Limit Upper Limit
```
```
(dBc)
```
```
Measured Value
```
```
(dBc)
```
```
Pass/Fail
```
```
12.8 kHz − 60
```
```
51.2 kHz
− 40
```
```
102.4 kHz
− 40
```
Serial Number:_______________________Report Number:____________________

Test Date:___/___/___

Verifying Specifications Agilent 35670A

Operation Verification Test Record - Two Channel

10 of 10


Operation Verification Test Record - Four Channel

Test Facility ___________________________________________________________

Facility Address ________________________________________________________

Tested By _____________________________________________________________

Report Number_________________________________________________________

Customer Name________________________________________________________

Serial Number__________________________________________________________

Installed Options _______________________________________________________

Date _________________________________________________________________

Temperature___________________________________________________________

Humidity _____________________________________________________________

Power Line Frequency ___________________________________________________

## Test Instruments Used

```
Instrument Model ID or Serial Number Calibration Due
```
```
AC Calibrator
```
```
Synthesizer 1
```
```
Synthesizer 2
```
```
Low-D Oscillator
```
```
Multimeter
```
Agilent 35670A Verifying Specifications

Operation Verification Test Record - Four Channel

1of15


## Spurious Signals

```
Measurement Lower Limit Upper Limit
```
```
(dBfs)
```
```
Measured Value
```
```
(dBfs)
```
```
Pass/Fail
```
```
Four Ch, 0 Hz Start, Ch 1
− 80
```
```
Four Ch, 0 Hz Start, Ch 2
− 80
```
```
Four Ch, 0 Hz Start, Ch 3
− 80
```
```
Four Ch, 0 Hz Start, Ch 4
− 80
```
```
Four Ch, 200 Hz Start, Ch 1
− 80
```
```
Four Ch, 200 Hz Start, Ch 2
− 80
```
```
Four Ch, 200 Hz Start, Ch 3
− 80
```
```
Four Ch, 200 Hz Start, Ch 4
− 80
```
```
Four Ch, 400 Hz Start, Ch 1
− 80
```
```
Four Ch, 400 Hz Start, Ch 2
− 80
```
```
Four Ch, 400 Hz Start, Ch 3
− 80
```
```
Four Ch, 400 Hz Start, Ch 4
− 80
```
```
Four Ch, 600 Hz Start, Ch 1
− 80
```
```
Four Ch, 600 Hz Start, Ch 2
− 80
```
```
Four Ch, 600 Hz Start, Ch 3
− 80
```
```
Four Ch, 600 Hz Start, Ch 4
− 80
```
```
Four Ch, 800 Hz Start, Ch 1
− 80
```
```
Four Ch, 800 Hz Start, Ch 2
− 80
```
```
Four Ch, 800 Hz Start, Ch 3
− 80
```
```
Four Ch, 800 Hz Start, Ch 4
− 80
```
```
Four Ch, 1000 Hz Start, Ch 1
− 80
```
```
Four Ch, 1000 Hz Start, Ch 2 − 80
```
```
Four Ch, 1000 Hz Start, Ch 3
− 80
```
```
Four Ch, 1000 Hz Start, Ch 4
− 80
```
```
Four Ch, 1200 Hz Start, Ch 1
− 80
```
```
Four Ch, 1200 Hz Start, Ch 2 − 80
```
```
Four Ch, 1200 Hz Start, Ch 3
− 80
```
```
Four Ch, 1200 Hz Start, Ch 4
− 80
```
```
Four Ch, 1400 Hz Start, Ch 1
− 80
```
```
Four Ch, 1400 Hz Start, Ch 2
− 80
```
```
Four Ch, 1400 Hz Start, Ch 3
− 80
```
```
Four Ch, 1400 Hz Start, Ch 4
− 80
```
Serial Number:_______________________Report Number:____________________

Test Date:___/___/___

Agilent 35670A Verifying Specifications

Operation Verification Test Record - Four Channel

3of15


```
Four Ch, 1600 Hz Start, Ch 1
− 80
```
```
Four Ch, 1600 Hz Start, Ch 2
− 80
```
```
Four Ch, 1600 Hz Start, Ch 3
− 80
```
```
Four Ch, 1600 Hz Start, Ch 4
− 80
```
```
Four Ch, 3200 Hz Start, Ch 1
− 80
```
```
Four Ch, 3200 Hz Start, Ch 2
− 80
```
```
Four Ch, 3200 Hz Start, Ch 3
− 80
```
```
Four Ch, 3200 Hz Start, Ch 4 − 80
```
```
Four Ch, 4800 Hz Start, Ch 1
− 80
```
```
Four Ch, 4800 Hz Start, Ch 2
− 80
```
```
Four Ch, 4800 Hz Start, Ch 3 − 80
```
```
Four Ch, 4800 Hz Start, Ch 4
− 80
```
```
Four Ch, 6400 Hz Start, Ch 1
− 80
```
```
Four Ch, 6400 Hz Start, Ch 2
− 80
```
```
Four Ch, 6400 Hz Start, Ch 3
− 80
```
```
Four Ch, 6400 Hz Start, Ch 4
− 80
```
```
Four Ch, 8000 Hz Start, Ch 1
− 80
```
```
Four Ch, 8000 Hz Start, Ch 2
− 80
```
```
Four Ch, 8000 Hz Start, Ch 3
− 80
```
```
Four Ch, 8000 Hz Start, Ch 4
− 80
```
```
Four Ch, 9600 Hz Start, Ch 1
− 80
```
```
Four Ch, 9600 Hz Start, Ch 2
− 80
```
```
Four Ch, 9600 Hz Start, Ch 3
− 80
```
```
Four Ch, 9600 Hz Start, Ch 4 − 80
```
```
Four Ch, 11200 Hz Start, Ch 1
− 80
```
```
Four Ch, 11200 Hz Start, Ch 2
− 80
```
```
Four Ch, 11200 Hz Start, Ch 3
− 80
```
```
Four Ch, 11200 Hz Start, Ch 4
− 80
```
```
Four Ch, 12800 Hz Start, Ch 1
− 80
```
```
Four Ch, 12800 Hz Start, Ch 2
− 80
```
```
Four Ch, 12800 Hz Start, Ch 3
− 80
```
```
Four Ch, 12800 Hz Start, Ch 4
− 80
```
```
Four Ch, 14400 Hz Start, Ch 1
− 80
```
```
Four Ch, 14400 Hz Start, Ch 2
− 80
```
Serial Number:_______________________Report Number:____________________

Test Date:___/___/___

Verifying Specifications Agilent 35670A

Operation Verification Test Record - Four Channel

4of15


```
Four Ch, 14400 Hz Start, Ch 3
− 80
```
```
Four Ch, 14400 Hz Start, Ch 4
− 80
```
```
Four Ch, 16000 Hz Start, Ch 1
− 80
```
```
Four Ch, 16000 Hz Start, Ch 2
− 80
```
```
Four Ch, 16000 Hz Start, Ch 3
− 80
```
```
Four Ch, 16000 Hz Start, Ch 4
− 80
```
```
Four Ch, 17600 Hz Start, Ch 1
− 80
```
```
Four Ch, 17600 Hz Start, Ch 2 − 80
```
```
Four Ch, 17600 Hz Start, Ch 3
− 80
```
```
Four Ch, 17600 Hz Start, Ch 4
− 80
```
```
Four Ch, 19200 Hz Start, Ch 1 − 80
```
```
Four Ch, 19200 Hz Start, Ch 2
− 80
```
```
Four Ch, 19200 Hz Start, Ch 3
− 80
```
```
Four Ch, 19200 Hz Start, Ch 4
− 80
```
```
Four Ch, 20800 Hz Start, Ch 1
− 80
```
```
Four Ch, 20800 Hz Start, Ch 2
− 80
```
Serial Number:_______________________Report Number:____________________

Test Date:___/___/___

Agilent 35670A Verifying Specifications

Operation Verification Test Record - Four Channel

5of15


## Spurious Signals (continued)

```
Four Ch, 20800 Hz Start, Ch 3
− 80
```
```
Four Ch, 20800 Hz Start, Ch 4
− 80
```
```
Four Ch, 22400 Hz Start, Ch 1
− 80
```
```
Four Ch, 22400 Hz Start, Ch 2
− 80
```
```
Four Ch, 22400 Hz Start, Ch 3
− 80
```
```
Four Ch, 22400 Hz Start, Ch 4
− 80
```
```
Four Ch, 24000 Hz Start, Ch 1
− 80
```
```
Four Ch, 24000 Hz Start, Ch 2 − 80
```
```
Four Ch, 24000 Hz Start, Ch 3
− 80
```
```
Four Ch, 24000 Hz Start, Ch 4
− 80
```
```
Two Ch, 25600 Hz Start, Ch 1 − 80
```
```
Two Ch, 25600 Hz Start, Ch 2
− 80
```
```
Two Ch, 27200 Hz Start, Ch 1
− 80
```
```
Two Ch, 27200 Hz Start, Ch 2
− 80
```
```
Two Ch, 28800 Hz Start, Ch 1
− 80
```
```
Two Ch, 28800 Hz Start, Ch 2
− 80
```
```
Two Ch, 30400 Hz Start, Ch 1
− 80
```
```
Two Ch, 30400 Hz Start, Ch 2
− 80
```
```
Two Ch, 32000 Hz Start, Ch 1
− 80
```
```
Two Ch, 32000 Hz Start, Ch 2
− 80
```
```
Two Ch, 33600 Hz Start, Ch 1
− 80
```
```
Two Ch, 33600 Hz Start, Ch 2
− 80
```
```
Two Ch, 35200 Hz Start, Ch 1
− 80
```
```
Two Ch, 35200 Hz Start, Ch 2 − 80
```
```
Two Ch, 36800 Hz Start, Ch 1
− 80
```
```
Two Ch, 36800 Hz Start, Ch 2
− 80
```
```
Two Ch, 38400 Hz Start, Ch 1
− 80
```
```
Two Ch, 38400 Hz Start, Ch 2
− 80
```
```
Two Ch, 40000 Hz Start, Ch 1
− 80
```
```
Two Ch, 40000 Hz Start, Ch 2
− 80
```
```
Two Ch, 41600 Hz Start, Ch 1
− 80
```
```
Two Ch, 41600 Hz Start, Ch 2
− 80
```
```
Two Ch, 43200 Hz Start, Ch 1
− 80
```
```
Two Ch, 43200 Hz Start, Ch 2
− 80
```
Serial Number:_______________________Report Number:____________________

Test Date:___/___/___

Verifying Specifications Agilent 35670A

Operation Verification Test Record - Four Channel

6of15


```
Two Ch, 44800 Hz Start, Ch 1
− 80
```
```
Two Ch, 44800 Hz Start, Ch 2
− 80
```
```
Two Ch, 46400 Hz Start, Ch 1
− 80
```
```
Two Ch, 46400 Hz Start, Ch 2
− 80
```
```
Two Ch, 48000 Hz Start, Ch 1
− 80
```
```
Two Ch, 48000 Hz Start, Ch 2
− 80
```
```
Two Ch, 49600 Hz Start, Ch 1
− 80
```
```
Two Ch, 49600 Hz Start, Ch 2
− 80
```
## Amplitude Accuracy

```
Measurement Lower Limit
```
```
(dBVrms)
```
```
Upper Limit
```
```
(dBVrms)
```
```
Measured Value
```
```
(dBVrms)
```
```
Pass/Fail
```
```
−51 dBVrms, Ch 1 −51.15 −50.85
```
```
−51 dBVrms, Ch 2 −51.15 −50.85
```
```
−51 dBVrms, Ch 3 −51.15 −50.85
```
```
−51 dBVrms, Ch 4 −51.15 −50.85
```
```
−43 dBVrms, Ch 1 −43.15 −42.85
```
```
−43 dBVrms, Ch 2 −43.15 −42.85
```
```
−43 dBVrms, Ch 3 −43.15 −42.85
```
```
−43 dBVrms, Ch 4 −43.15 −42.85
```
```
−35 dBVrms, Ch 1 −35.15 −34.85
```
Serial Number:_______________________Report Number:____________________

Test Date:___/___/___

Agilent 35670A Verifying Specifications

Operation Verification Test Record - Four Channel

7of15


## Amplitude Accuracy (continued)

```
Measurement Lower Limit Upper Limit
```
```
(dBfs)
```
```
Measured Value
```
```
(dBfs)
```
```
Pass/Fail
```
```
−35 dBVrms, Ch 2 −35.15 −34.85
```
```
−35 dBVrms, Ch 3 −35.15 −34.85
```
```
−35 dBVrms, Ch 4 −35.15 −34.85
```
```
−27 dBVrms, Ch 1 −27.15 −26.85
```
```
−27 dBVrms, Ch 2 −27.15 −26.85
```
```
−27 dBVrms, Ch 3 −27.15 −26.85
```
```
−27 dBVrms, Ch 4 −27.15 −26.85
```
```
−11 dBVrms, Ch 1 −11.15 −10.85
```
```
−11 dBVrms, Ch 2 −11.15 −10.85
```
```
−11 dBVrms, Ch 3 −11.15 −10.85
```
```
−11 dBVrms, Ch 4 −11.15 −10.85
```
```
1 dBVrms, Ch 1
```
```
0.85 1.15
```
```
1 dBVrms, Ch 2
0.85 1.15
```
```
1 dBVrms, Ch 3
0.85 1.15
```
```
1 dBVrms, Ch 4
```
```
0.85 1.15
```
```
9 dBVrms, Ch 1
```
```
8.85 9.15
```
```
9 dBVrms, Ch 2
```
```
8.85 9.15
```
```
9 dBVrms, Ch 3
8.85 9.15
```
```
9 dBVrms, Ch 4
8.85 9.15
```
```
19 dBVrms, Ch 1
```
```
18.85 19.15
```
```
19 dBVrms, Ch 2
```
```
18.85 19.15
```
```
19 dBVrms, Ch 3
```
```
18.85 19.15
```
```
19 dBVrms, Ch 4
18.85 19.15
```
```
27 dBVrms, Ch 1
26.85 27.15
```
```
27 dBVrms, Ch 2
```
```
26.85 27.15
```
```
27 dBVrms, Ch 3
```
```
26.85 27.15
```
```
27 dBVrms, Ch 4
26.85 27.15
```
Serial Number:_______________________Report Number:____________________

Test Date:___/___/___

Verifying Specifications Agilent 35670A

Operation Verification Test Record - Four Channel

8of15


## Flatness

```
Measurement Lower Limit
```
```
(dB)
```
```
Upper Limit
```
```
(dB)
```
```
Measured Value
```
```
(dB)
```
```
Pass/Fail
```
```
27 dBVrms, 51.2 kHz, One Ch, Ch 1
−0.2
```
### 0.2

```
9 dBVrms, 51.2 kHz, One Ch, Ch 1
−0.2
```
### 0.2

```
−11 dBVrms, 51.2 kHz, One Ch, Ch 1 −0.2
```
### 0.2

```
27 dBVrms, 51.2 kHz, Two Ch, Ch 1
−0.2
```
### 0.2

```
27 dBVrms, 51.2 kHz, Two Ch, Ch 2
−0.2
```
### 0.2

```
9 dBVrms, 51.2 kHz, Two Ch, Ch 1 −0.2 0.2
```
```
9 dBVrms, 51.2 kHz, Two Ch, Ch 2
−0.2
```
### 0.2

```
−11 dBVrms, 51.2 kHz, Two Ch, Ch 1 −0.2
```
### 0.2

```
−11 dBVrms, 51.2 kHz, Two Ch, Ch 2 −0.2 0.2
```
```
27 dBVrms, 25.6 kHz, Four Ch, Ch 1
−0.2
```
### 0.2

```
27 dBVrms, 25.6 kHz, Four Ch, Ch 2
−0.2
```
### 0.2

```
27 dBVrms, 25.6 kHz, Four Ch, Ch 3
−0.2
```
### 0.2

```
27 dBVrms, 25.6 kHz, Four Ch, Ch 4
−0.2
```
### 0.2

```
9 dBVrms, 25.6 kHz, Four Ch, Ch 1
−0.2
```
### 0.2

```
9 dBVrms, 25.6 kHz, Four Ch, Ch 2
−0.2
```
### 0.2

```
9 dBVrms, 25.6 kHz, Four Ch, Ch 3
−0.2
```
### 0.2

```
9 dBVrms, 25.6 kHz, Four Ch, Ch 4
−0.2
```
### 0.2

```
−11 dBVrms, 25.6 kHz, Four Ch, Ch 1 −0.2
```
### 0.2

```
−11 dBVrms, 25.6 kHz, Four Ch, Ch 2 −0.2
```
### 0.2

```
−11 dBVrms, 25.6 kHz, Four Ch, Ch 3 −0.2
```
### 0.2

```
−11 dBVrms, 25.6 kHz, Four Ch, Ch 4 −0.2
```
### 0.2

Serial Number:_______________________Report Number:____________________

Test Date:___/___/___

Agilent 35670A Verifying Specifications

Operation Verification Test Record - Four Channel

9of15


## Amplitude Linearity

```
Measurement Lower Limit
```
```
(dB)
```
```
Upper Limit
```
```
(dB)
```
```
Measured Value
```
```
(dB)
```
```
Pass/Fail
```
```
13 dBVrms, Ch 1
−0.0615
```
### 0.061

```
13 dBVrms, Ch 2
−0.0615
```
### 0.061

```
13 dBVrms, Ch 3
−0.0615
```
### 0.061

```
13 dBVrms, Ch 4
−0.0615
```
### 0.061

```
−1 dBVrms, Ch 1 −0.105
```
### 0.104

```
−1 dBVrms, Ch 2 −0.105 0.104
```
```
−1 dBVrms, Ch 3 −0.105
```
### 0.104

```
−1 dBVrms, Ch 4 −0.105
```
### 0.104

```
−15 dBVrms, Ch 1 −0.33 0.318
```
```
−15 dBVrms, Ch 2 −0.33
```
### 0.318

```
−15 dBVrms, Ch 3 −0.33
```
### 0.318

```
−15 dBVrms, Ch 4 −0.33
```
### 0.318

```
−29 dBVrms, Ch 1 −1.551
```
### 1.316

```
−29 dBVrms, Ch 2 −1.551
```
### 1.316

```
−29 dBVrms, Ch 3 −1.551
```
### 1.316

```
−29 dBVrms, Ch 4 −1.551
```
### 1.316

```
−43 dBVrms, Ch 1 −13.823
```
### 5.088

```
−43 dBVrms, Ch 2 −13.823
```
### 5.088

```
−43 dBVrms, Ch 3 −13.823
```
### 5.088

```
−43 dBVrms, Ch 4 −13.823
```
### 5.088

```
−53 dBVrms, Ch 1 −30.116
```
### 10.896

```
−53 dBVrms, Ch 2 −30.116 10.896
```
```
−53 dBVrms, Ch 3 −30.116
```
### 10.896

```
−53 dBVrms, Ch 4 −30.116
```
### 10.896

Serial Number:_______________________Report Number:____________________

Test Date:___/___/___

Verifying Specifications Agilent 35670A

Operation Verification Test Record - Four Channel

10 of 15


## A Weight Filter

```
Measurement Lower Limit
```
```
(dB)
```
```
Upper Limit
```
```
(dB)
```
```
Measured Value
```
```
(dB)
```
```
Pass/Fail
```
```
Ch 1, 10 Hz
− 5
```
### 2

```
Ch 2, 10 Hz
− 5
```
### 2

```
Ch 3, 10 Hz
− 5
```
### 2

```
Ch 4, 10 Hz − 5 2
```
```
Ch 1, 31.62 Hz
− 1
```
### 1

```
Ch 2, 31.62 Hz
− 1
```
### 1

```
Ch 3, 31.62 Hz − 1 1
```
```
Ch 4, 31.62 Hz
− 1
```
### 1

```
Ch 1, 100 Hz
−0.7
```
### 0.7

```
Ch 2, 100 Hz
−0.7
```
### 0.7

```
Ch 3, 100 Hz
−0.7
```
### 0.7

```
Ch 4, 100 Hz
−0.7
```
### 0.7

```
Ch 1, 1000 Hz
−0.7
```
### 0.7

```
Ch 2, 1000 Hz
−0.7
```
### 0.7

```
Ch 3, 1000 Hz
−0.7
```
### 0.7

```
Ch 4, 1000 Hz
−0.7
```
### 0.7

```
Ch 1, 10000 Hz
− 3
```
### 2

```
Ch 2, 10000 Hz
− 3
```
### 2

```
Ch 3, 10000 Hz
− 3
```
### 2

```
Ch 4, 10000 Hz − 3 2
```
```
Ch 1, 25120 Hz
−4.5
```
### 2.4

```
Ch 2, 25120 Hz
−4.5
```
### 2.4

```
Ch 3, 25120 Hz
−4.5
```
### 2.4

```
Ch 4, 25120 Hz
−4.5
```
### 2.4

Serial Number:_______________________Report Number:____________________

Test Date:___/___/___

Agilent 35670A Verifying Specifications

Operation Verification Test Record - Four Channel

11 of 15


## Channel Match

```
Two Ch, 2/1, 7 dBV FS Mag
−0.04
```
### 0.04

```
Two Ch, 2/1, 7 dBV FS Phs
−0.5
```
### 0.5

```
Two Ch, 2/1,−13 dBV FS Mag −0.04
```
### 0.04

```
Two Ch, 2/1,−13 dBV FS Phs −0.5
```
### 0.5

```
Two Ch, 2/1,−33 dBV FS Mag −0.04
```
### 0.04

```
Two Ch, 2/1,−33 dBV FS Phs −0.5
```
### 0.5

```
Two Ch, 2/1, 7 dBV−20 dBfs Mag −0.08
```
### 0.08

```
Two Ch, 2/1, 7 dBV−20 dBfs Phs −0.5 0.5
```
```
Four Ch, 2/1, 7 dBV FS Mag
−0.04
```
### 0.04

```
Four Ch, 2/1, 7 dBV FS Phs
−0.5
```
### 0.5

```
Four Ch, 2/1,−13 dBV FS Mag −0.04 0.04
```
```
Four Ch, 2/1,−13 dBV FS Phs −0.5
```
### 0.5

```
Four Ch, 2/1,−33 dBV FS Mag −0.04
```
### 0.04

```
Four Ch, 2/1,−33 dBV FS Phs −0.5
```
### 0.5

```
Four Ch, 2/1, 7 dBV−20 dBfs Mag −0.08
```
### 0.08

```
Four Ch, 2/1, 7 dBV−20 dBfs Phs −0.5
```
### 0.5

```
Four Ch, 3/1, 7 dBV FS Mag
−0.04
```
### 0.04

```
Four Ch, 3/1, 7 dBV FS Phs
−0.5
```
### 0.5

```
Four Ch, 3/1,−13 dBV FS Mag −0.04
```
### 0.04

```
Four Ch, 3/1,−13 dBV FS Phs −0.5
```
### 0.5

```
Four Ch, 3/1,−33 dBV FS Mag −0.04
```
### 0.04

```
Four Ch, 3/1,−33 dBV FS Phs −0.5
```
### 0.5

```
Four Ch, 3/1, 7 dBV−20 dBfs Mag −0.08
```
### 0.08

```
Four Ch, 3/1, 7 dBV−20 dBfs Phs −0.5 0.5
```
```
Four Ch, 4/1, 7 dBV FS Mag
−0.04
```
### 0.04

```
Four Ch, 4/1, 7 dBV FS Phs
−0.5
```
### 0.5

```
Four Ch, 4/1,−13 dBV FS Mag −0.04
```
### 0.04

```
Four Ch, 4/1,−13 dBV FS Phs −0.5
```
### 0.5

```
Four Ch, 4/1,−33 dBV FS Mag −0.04
```
### 0.04

```
Four Ch, 4/1,−33 dBV FS Phs −0.5
```
### 0.5

```
Four Ch, 4/1, 7 dBV−20 dBfs Mag −0.08
```
### 0.08

```
Four Ch, 4/1, 7 dBV−20 dBfs Phs −0.5
```
### 0.5

```
Four Ch, 4/3, 7 dBV FS Mag
−0.04
```
### 0.04

Serial Number:_______________________Report Number:____________________

Test Date:___/___/___

Verifying Specifications Agilent 35670A

Operation Verification Test Record - Four Channel

12 of 15


```
Four Ch, 4/3, 7 dBV FS Phs
−0.5
```
### 0.5

```
Four Ch, 4/3,−13 dBV FS Mag −0.04
```
### 0.04

```
Four Ch, 4/3,−13 dBV FS Phs −0.5
```
### 0.5

```
Four Ch, 4/3,−33 dBV FS Mag −0.04
```
### 0.04

```
Four Ch, 4/3,−33 dBV FS Phs −0.5
```
### 0.5

```
Four Ch, 4/3, 7 dBV−20 dBfs Mag −0.08
```
### 0.08

```
Four Ch, 4/3, 7 dBV−20 dBfs Phs −0.5
```
### 0.5

## Frequency Accuracy

```
Measurement Lower Limit
```
```
(kHz)
```
```
Upper Limit
```
```
(kHz)
```
```
Measured Value
```
```
(kHz)
```
```
Pass/Fail
```
```
50 kHz
```
```
49.9985 50.0015
```
Serial Number:_______________________Report Number:____________________

Test Date:___/___/___

Agilent 35670A Verifying Specifications

Operation Verification Test Record - Four Channel

13 of 15


## Single Ch Phase Accuracy

```
Measurement Lower Limit
```
```
(deg)
```
```
Upper Limit
```
```
(deg)
```
```
Measured Value
```
```
(deg)
```
```
Pass/Fail
```
```
Positive slope, Ch 1
− 4
```
### 4

```
Positive slope, Ch 2
− 4
```
### 4

```
Positive slope, Ch 3
− 4
```
### 4

```
Positive slope, Ch 4
− 4
```
### 4

```
Negative slope, Ch 1
− 4
```
### 4

```
Negative slope, Ch 2
− 4
```
### 4

```
Negative slope, Ch 3
− 4
```
### 4

```
Negative slope, Ch 4
− 4
```
### 4

## Tach Function (option D01 only)

```
Measurement Lower Limit
```
### (%)

```
Upper Limit
```
### (%)

```
Measured Value
```
### (%)

```
Pass/Fail
```
```
Trigger level +8V Pos
− 10
```
### 10

```
Trigger level +8V Neg
− 10
```
### 10

```
Trigger level−8V Pos − 10
```
### 10

```
Trigger level−8V Neg − 10
```
### 10

## ICP Supply

```
Measurement Lower Limit Upper Limit Measured Value Pass/Fail
```
```
Ch 1 Open Circuit Voltage
26 Vdc 32 Vdc Vdc
```
```
Ch 2 Open Circuit Voltage
26 Vdc 32 Vdc Vdc
```
```
Ch 3 Open Circuit Voltage
```
```
26 Vdc 32 Vdc Vdc
```
```
Ch 4 Open Circuit Voltage
```
```
26 Vdc 32 Vdc Vdc
```
```
Ch 1 Current
```
```
2.75 mA 5.75 mA mA
```
```
Ch 2 Current
2.75 mA 5.75 mA mA
```
```
Ch 3 Current
2.75 mA 5.75 mA mA
```
```
Ch 4 Current
```
```
2.75 mA 5.75 mA mA
```
Serial Number:_______________________Report Number:____________________

Test Date:___/___/___

Verifying Specifications Agilent 35670A

Operation Verification Test Record - Four Channel

14 of 15


## Source Amplitude Accuracy

```
Measurement Lower Limit
```
### (%)

```
Upper Limit
```
### (%)

```
Measured Value
```
### (%)

```
Pass/Fail
```
```
1 kHz, 0.1 Vpk
− 4
```
### 4

```
1 kHz, 3.0 Vpk
− 4
```
### 4

```
1 kHz, 5.0 Vpk
− 4
```
### 4

## Source Flatness

```
Measurement Lower Limit
```
```
(dB)
```
```
Upper Limit
```
```
(dB)
```
```
Measured Value
```
```
(dB)
```
```
Pass/Fail
```
```
12.8 kHz − 1 1
```
```
25.6 kHz
− 1
```
### 1

```
51.2 kHz
− 1
```
### 1

## Source Distortion

```
Measurement Lower Limit Upper Limit
```
```
(dBc)
```
```
Measured Value
```
```
(dBc)
```
```
Pass/Fail
```
```
12.8 kHz
− 60
```
```
51.2 kHz
− 40
```
Serial Number:_______________________Report Number:____________________

Test Date:___/___/___

Agilent 35670A Verifying Specifications

Operation Verification Test Record - Four Channel

15 of 15


# 4

## Troubleshooting the

## Analyzer

4-1


Troubleshooting the Analyzer

## This chapter contains troubleshooting tests that can isolate most failures to the

## faulty assembly. The section ‘’How to troubleshoot the analyzer’’ tells you

## which test to start with based on the failure. The test you start with will either

## isolate the faulty assembly or send you to another test to continue

## troubleshooting.

## Safety Considerations

## The Agilent 35670A Dynamic Signal Analyzer is a Safety Class 1 instrument

## (provided with a protective earth terminal). Although the instrument has been

## designed in accordance with international safety standards, this manual

## contains information, cautions, and warnings that must be followed to ensure

## safe operation and retain the instrument in safe operating condition. Service

## must be performed by trained service personnel who are aware of the hazards

## involved (such as fire and electrical shock).

Warning Any interruption of the protective (grounding) conductor inside or outside the

analyzer, or disconnection of the protective earth terminal can expose operators

to potentially dangerous voltages.

Under no circumstances should an operator remove any covers, screws, shields or

in any other way access the interior of the Agilent 35670A Dynamic Signal

Analyzer. There are no operator controls inside the analyzer.

Only fuses with the required current rating and of the specified type should be

used for replacement. The use of repaired fuses or short circuiting the fuse

holder is not permitted. Whenever it is likely that the protection offered by the

fuse has been impaired, the analyzer must be made inoperative and secured

against any unintended operation.

When power is removed from the Agilent 35670A Dynamic Signal Analyzer,

+225 volts are present in the display for approximately 5 seconds. Be extremely

careful when working in proximity to this area during this time. The high voltage

can cause serious personal injury if contacted.

Caution Do not connect or disconnect ribbon cables with the power switch set to on (l).

Power transients caused by connecting or disconnecting a cable can damage circuit

assemblies.

4-2


## Equipment Required

See ‘’Recommended Test Equipment’’ starting on page 1-17 for tables listing

recommended equipment. Any equipment which meets the critical specifications

given in the tables may be substituted for the recommended model.

## Troubleshooting Hints

- Incorrect bias supply voltages can cause false diagnostic messages. In most

troubleshooting procedures, the power supply voltages are not checked. If you

suspect incorrect supply voltages to an assembly, use the ‘’Voltages and Signals’’

chapter to check the voltages at the assembly.

- Cables can cause intermittent hardware failures.
- Noise or spikes in the power supply can cause the analyzer to fail.
- Measurements in this chapter are only approximate (usually1 dB or 10%) unless

stated otherwise.

- Use chassis ground for all measurements in this chapter unless stated otherwise.
- To determine your firmware version code, press [System Utility][MORE]

[S/N VERSION].

- Logic levels in this chapter are either TTL level high or TTL level low unless stated

otherwise. Toggling signal levels continually change from one TTL level to the

other.

- The troubleshooting tests in this chapter assume only one independent failure.

Multiple failures can cause false results.

- The troubleshooting procedures do not isolate failures to cables or connectors. If

you suspect a cable or connector failure, check the device for continuity.

- If you abort a self test before the self test is finished, the analyzer may fail its

calibration routine. To prevent this from happening press [Preset][DO PRESET]

or cycle power after you abort the self test.

Agilent 35670A Troubleshooting the Analyzer

4-3


How to troubleshoot the analyzer

- Review ‘’Safety Considerations’’ and ‘’Troubleshooting Hints.’’

Warning Service must be performed by trained service personnel who are aware of the

hazards involved (such as fire and electrical shock).

- See chapter 6, ‘’Replacing Assemblies,’’ to determine how to disassemble and

assemble the analyzer.

- Determine initial test by comparing the analyzer’s symptoms to the symptoms

in the following table.

Symptom Troubleshooting Test

Screen blank †

Screen defective

After power up, >3 minutes before keys active

No response when key is pressed

Incorrect response when key is pressed

Initial verification, page

4-5

Keys are active and screen grid is displayed but screen is defective Display, page 4-22

Error messages

Calibration fails

Performance test fails

Intermittent failure

GPIB fails

Mic pwr fails

Serial port fails

Parallel port fails

External monitor does not work

Self tests, page 4-31

External keyboard does not work DIN connector, page

4-61

External trigger fails Trigger, page 4-62

Nonvolatile states not saved after power cycled

Date display is ‘’Date: 01-01-BL’’

Memory battery, page

4-67

```
† If the analyzer is failing, the grid may not appear for two minutes. Wait two minutes before assuming
```
```
that a low level failure occurred.
```
- Follow the recommended troubleshooting test until you locate the faulty

assembly.

- Replace the faulty assembly and follow the directions in ‘’What to do after

replacing an assembly’’ in chapter 6, ‘’Replacing Assemblies.’’

Troubleshooting the Analyzer Agilent 35670A

How to troubleshoot the analyzer

4-4


To perform initial verification

Use this test to check signals that are vital to the operation of the analyzer.

q Step 1. Check the power select switch and fuse.

- Check that the POWER SELECT switch on the rear of the analyzer is set to

the AC position.

- Check that the correct line fuse is installed in the rear panel fuse holder.

For information on the power select switch and line fuse, see ‘’To do the incoming

inspection’’ on page 2-5 and ‘’To change the fuses’’ on page 2-10.

q Step 2. If the grid appears after power up but there is no response when keys are

pressed, ckeck that the calibration routine is not locking up the analyzer.

- Set the power switch to off (O).
- Set the power switch to on (l) and as soon asBooting Systemappears on the

display, disable the calibration routine by holding [Preset] untilUncalibrated

dataappears.

- If the keys are now active, go to page 4-37, ‘’To troubleshoot self-test lockup

failures.’’

q Step 3. If the analyzer powers up with failure messages, then locks up, but the grid

and lettering appear normal, go to page 4-15, ‘’To troubleshoot power-up failures.’’

Agilent 35670A Troubleshooting the Analyzer

To perform initial verification

4-5


q Step 5. Check the power supply LED and fan.

- Set the power switch to off (O) and disconnect the power cord from the

rear panel.

- Remove the cover.

See ‘’To remove cover’’ on page 6-6.

- Connect the power cord and set the power switch to on (l).
- If the green power supply LED is not lit, go to page 4-11, ‘’To troubleshoot

the power supply.’’

- Check that the fan is turning at a moderate speed for normal room

temperature.

The fan is very quiet. Check air flow before determining that the fan is not turning.

- If the fan is not turning, go to page 4-11, ‘’To troubleshoot the power

supply.’’

Agilent 35670A Troubleshooting the Analyzer

To perform initial verification

4-7


q Step 6. Check the following TTL clock signals using an oscilloscope and a

1MΩ10:1 probe.

Signal Name Test Location Frequency Probable Faulty Assembly

FREQ REF A7 TP1 19.923 MHz A7 CPU

G20MHz A7 J3 pin 32C 19.923 MHz A7 CPU

VCLK A7 P2 pin 13 20 MHz A7 CPU

SYSCLK A6 TP105 10 MHz A6 Digital

Troubleshooting the Analyzer Agilent 35670A

To perform initial verification

4-8


A7 Component Locator, Circuit Side

Agilent 35670A Troubleshooting the Analyzer

To perform initial verification

4-9


q Step 7. Check signals required for power up.

- Using a logic probe, check the following signals.

Signal Name Test Location TTL State Probable Faulty Assembly

PVALID A7 P8 pin 3 High A98 Power Supply

RSTn A7 P8 pin 5 High A7 CPU

CASn A7 P7 pin 3 Toggling A7 CPU

RASn A7 P7 pin 4 Toggling A7 CPU

VDATA A7 P7 pin 7 Toggling A7 CPU

ASn A7 P6 pin 10 Toggling A7 CPU

- Using a logic probe, check that the following TTL signals are toggling just

after power up.

The signals may stop toggling when the CPU assembly finishes the bootrom self

tests.

Signal Name Test Location

PASn A7 P8 pin 7

PDSACK1n A7 P8 pin 8

PDSACK0n A7 P8 pin 9

PRW A7 P8 pin 10

PDSn A7 P8 pin 11

PA(26) A7 P8 pin 12

PA(16) A7 P8 pin 13

- If the signals are not correct, the A7 CPU assembly is probably faulty.
- Using a logic probe, check that A7 P7 pin 2 (SCL) and A7 P7 pin 1 (SDA)

toggle TTL states at least twice just after power up.

- If the signals are not correct, the A7 CPU assembly is probably faulty.
- If the signals are correct, go to page 4-15, ‘’To troubleshoot power-up

failures.’’

Troubleshooting the Analyzer Agilent 35670A

To perform initial verification

4-10


To troubleshoot the power supply

Use this test to check the Power Supply and Fan assemblies. This test can also isolate

the assembly causing the Power Supply to shut down.

q Step 1. Check the power supply LED.

- Set the power switch to off (O).
- Disconnect the ribbon cable from the A98 Power Supply assembly.
- Set the power switch to on (l).
- If the green power supply LED is not lit, the A98 Power Supply assembly is

probably faulty.

- Set the power switch to off (O).
- Reconnect the ribbon cable to the Power Supply assembly.
- Set the power switch to on (l).
- If the power supply LED is on but the fan is not turning, go to Step 7.

A thermistor on the A10 Rear Panel assembly controls the power to the A90 Fan

assembly. As the analyzer’s temperature increases, the fan speed increases. Since

the fan is very quiet, check air flow before determining that the fan is not turning.

Agilent 35670A Troubleshooting the Analyzer

To troubleshoot the power supply

4-11


q Step 2. Determine if the Digital, Analog, or Input assemblies are causing the Power

Supply assembly to shut down.

- Set the power switch to off (O).
- Pull the following assemblies out of the card nest about 1 inch:

A6 Digital

A5 Analog

A2 Input (optional)

A1/A2 Input

- Set the power switch to on (l).
- If the power supply LED is still off, set the power switch to off (O),

reconnect the above assemblies, and go to Step 4.

q Step 3. Repeat the following until the assembly causing the Power Supply assembly to

shut down is located.

- Set the power switch to off (O).
- Reconnect one assembly at a time in the following order.

A6 Digital

A5 Analog

A2 Input (optional)

A1/A2 Input

- Set the power switch to on (l).
- If the green power supply LED is off, the assembly just reconnected is

probably faulty.

The A5 Analog assembly provides over-temperature protection which shuts down

the power supply if the analyzer’s internal temperature becomes excessive. Before

replacing the A5 Analog assembly, check that the fan is turning when the green

power supply LED is on and that the air flow is not restricted (cooling air enters

from the right side and exhausts through the left side and rear panel). Since the fan

is very quiet, check air flow to determine that the fan is turning.

q Step 4. Determine if the CPU assembly or one of the assemblies connected to the

CPU assembly is causing the power supply to shut down.

Troubleshooting the Analyzer Agilent 35670A

To troubleshoot the power supply

4-12


- Remove the A7 CPU assembly.

See ‘’To remove CPU’’ on page 6-11.

- Set the power switch to on (l).
- If the power supply LED is still off, set the power switch to off (O),

reconnect the CPU assembly, and go to Step 6.

q Step 5. Repeat the following steps until the assembly causing the Power Supply

assembly to shut down is located.

- Set the power switch to off (O).
- Reconnect one assembly at a time in the following order:

A7 CPU (A7 P10 to A99 J7)

A8 Memory (A8 P1 to A7 J3)

A102 DC-DC Converter (cable to A7 P2)

A11 Keyboard Controller (cable to A7 P1)

A100 Disk Drive (cable to A7 P3)

- Set the power switch to on (l).
- If the green power supply LED is off, the assembly just reconnected is

probably faulty.

A7 Component Locator, Circuit Side

Agilent 35670A Troubleshooting the Analyzer

To troubleshoot the power supply

4-13


q Step 6. Determine if the Motherboard, Fan, or Rear Panel assembly is causing the

Power Supply to shut down.

- Disconnect the fan cable from A99 P90.
- Set the power switch to on (l).
- If the power supply LED is now on, the A90 Fan assembly is probably

faulty.

- Set the power switch to off (O).
- Reconnect the fan cable.
- Remove the rear panel and disconnect the cable from A10 P100.

See ‘’To remove rear panel’’ on page 6-7.

- Set the power switch to on (l).
- If the power supply LED is now on, the A10 Rear Panel assembly is

probably faulty.

- If the Fan or Rear Panel assembly is not causing the Power Supply assembly

to shut down, then the A99 Motherboard is probably faulty.

q Step 7. Check the Fan assembly.

- Set the power switch to off (O).
- Remove the A7 CPU assembly.

See ‘’To remove CPU’’ on page 6-11.

- Disconnect the fan power cable from A99 P90 (red and black cable).
- Connect 5 Vdc to the fan cable. The fan should be turning slowly.
- Increase the voltage to 10 Vdc. The fan should turn faster as the voltage

increases.

- If the fan did not respond correctly, the A90 Fan assembly is probably

faulty.

- If the fan responded correctly, the A10 Rear Panel assembly is probably

faulty.

Troubleshooting the Analyzer Agilent 35670A

To troubleshoot the power supply

4-14


To troubleshoot power-up failures

Use this test when the screen is defective, when the analyzer does not respond

correctly to the keyboard, or when it takes more than 3 minutes for the keyboard to

become active. Any of the following conditions may cause a power-up failure:

- A defective CPU or Memory assembly.
- A defective assembly connected to the CPU assembly causing a bus failure.
- A defective cable between the CPU assembly and another assembly.
- A defective control line.

q Step 1. Compare the power-up failure messages to the following table.

- Set the power switch to on (l).
- If the screen is blank or no power-up failure messages are displayed, go to

Step 2.

- Determine the probable faulty assembly or next test by comparing the

power-up test result to the following table.

If the power-up failure messages match more than one entry in the table, use the

entry closest to the beginning of the table.

Failing Power-up Message Probable Faulty Assembly or Next Test

LEDs

MC68030 Processor

MC68882 Coprocessor

Bootrom

Display

A7 CPU

Main RAM

Program ROM

CPU, memory, DSP, and buses failures,

page 4-18

DSP A7 CPU

Fast bus IIC Bus failures, page 4-25

MFP A7 CPU

GPIB keypress detected, booting to GPIB Monitor A14 Secondary Keypad

Front Panel failure information:

keyboard IIC chip fails:

IIC: No Device Acknowledge

key stuck: 32

A11 Keyboard Controller

Front Panel failure information:

key stuck: _number_

_where number is 13, 14, 16, 20, 21, 24, 33,_

_35, 36, 37, 38, 40, 43, 52, 53, or 54_

A14 Secondary Keypad

Front Panel failure information:

key stuck: _number_

_all other numbers not listed above_

A13 or A15 Primary Keypad

Agilent 35670A Troubleshooting the Analyzer

To troubleshoot power-up failures

4-15


q Step 2. Determine if the power-on test passed or failed.

- Set the power switch to off (O).
- Set the power switch to on (l) while watching the power-on LEDs.

The power-on LEDs are on the A7 CPU assembly and are visible through the rear

panel. To see the LEDs easier, remove the seven screws holding the rear panel to

the analyzer and lean the rear panel back. This also gives you access to reset switch

SW2.

- If the power-on LEDs responded as follows, the power-on test passed.
- All power-on LEDs are on momentarily.
- DS1 (yellow, +5 LED) remains on as long as power is applied to the assembly.
- DS10 (green, run LED) comes on just after DS1.
- DS5, DS4, DS3, DS2, DS6, DS7, DS8, and DS9 sequence through the codes listed

in the following table.

Troubleshooting the Analyzer Agilent 35670A

To troubleshoot power-up failures

4-16


Binary

(DS5) (DS9)

Hexa-

decimal

~Time LEDs

Visible

Description

1111 1111

0000 0000

FF

00

200 ms on

200 ms off

A7 flashes LEDs

0000 1000 08 † starting A7 test

0000 0010 02 † A8 RAM DSACK test

0001 0100 14 † starting A8 RAM test

0001 0110 16 † starting A8 refresh test

0001 1100 1C 4s starting A8 program ROM test

0000 0000 00 4s clear LEDs

1010 0000 A0 † A7 MFP test

1010 0001 A1 † starting A7 DSP test

1010 0010 A2 † fast bus test

0101 1110 AE 200 ms front panel test

1111 1111 FF Remain on

```
0 LED off
```
```
1 LED on
```
```
† When no failure occurs, these codes appear for only a very short time and probably won’t be visible.
```
- If the power-on LEDs display a code for more than 4 seconds, a failure

occurred in the core assemblies or on the buses.

For additional information on the power-on test, see the ‘’Power-on Test

Descriptions’’ on page 10-3.

q Step 3. Determine the next step by comparing the power-on test results to the

following table.

Power-on LEDs Next Test

LEDs stop and display a fail code.

A7 DS101 (green, run LED) is off.

CPU, memory, and

buses, page 4-18

LEDs pass, but the screen is defective. Display, 4-22

LEDs pass, but it takes more than 3 minutes before the keys are active.

LEDs pass and screen appears normal, but keys do not function.

IIC Bus, page 4-25

Agilent 35670A Troubleshooting the Analyzer

To troubleshoot power-up failures

4-17


To troubleshoot CPU, memory, and buses failures

Use this test to isolate the failure when the power-on LEDs show a fail code or the

analyzer locks up during the power-up tests.

q Step 1. Compare the LED fail code to the following table.

- Set the power switch to off (O).
- Set the power switch to on (l) while watching the power-on LEDs.

The power-on LEDs are on the A7 CPU assembly and are visible through the rear

panel. To see the LEDs easier, remove the seven screws holding the rear panel to

the analyzer and lean the rear panel back. This also gives you access to reset switch

SW2.

- Determine the probable faulty assembly by comparing the power-on LEDs

fail code to the following table.

The power-on LEDs are showing a fail code when the LEDs display a code for

more than 4 seconds.

Troubleshooting the Analyzer Agilent 35670A

To troubleshoot CPU, memory, and buses failures

4-18


Binary

(DS5) (DS9)

Hexadecimal Probable Faulty Assembly

0000 0100

1111 1111

0001 0011

0000 0001

0001 0111

0001 1000

0000 1001

0000 1011

0001 1010

0001 1001

0000 1000

0001 0010

1010 0000

04

FF

13

01

17

18

09

0B

1A

19

08

12

A0

A7 CPU

0000 0010

0001 1011

0001 0100

0001 0110

0001 1100

02

1B

14

16

1C

A8 Memory

```
0 LED off
```
```
1 LED on
```
q Step 2. Determine if the CPU assembly is causing the failure.

- Set the power switch to off (O).
- Pull the following assemblies out of the card nest about 1 inch:

A6 Digital

A5 Analog

A2 Input (optional)

A1 or A2 Input

Agilent 35670A Troubleshooting the Analyzer

To troubleshoot CPU, memory, and buses failures

4-19


- Disconnect the A7 CPU assembly from the Motherboard, Memory

assembly, and cables.

- Reconnect the CPU assembly to the Motherboard (do not connect the

Memory assembly or cables to the CPU assembly).

A7 Component Locator, Circuit Side

- Set the power switch to on (l) while watching the power-on LEDs.
- If the LEDs did not display hexadecimal FF (1111 1111) then hexadecimal

02 (0000 0010), the A7 CPU assembly is probably faulty.

Troubleshooting the Analyzer Agilent 35670A

To troubleshoot CPU, memory, and buses failures

4-20


q Step 3. Determine if the Memory or Display assembly is causing the failure.

- Set the power switch to off (O).
- Reconnect the Memory assembly to the CPU assembly.
- Set the power switch to on (l) while watching the power-on LEDs.

The LEDs should sequence through 00 (clear LEDs) with 00 remaining on the

LEDs.

- Set the power switch to off (O).
- Reconnect the display cable to A7 P2.
- Set the power switch to on (l) while watching the power-on LEDs.

The LEDs should sequence through 00 (clear LEDs) with 00 remaining on the

LEDs. The following is an example of the messages displayed when the CPU and

memory power-on tests pass. The numbers in the messages will most likely be

different in your analyzer.

Copyright 1988, 1990, 1991, 1992, 1993,

Agilent Technologies Company,

All rights reserved.

LEDs

MC68030 Processor

MC68882 Coprocessor

Bootrom revision A.01.17

Main RAM

Testing 8388608 bytes at 0x06c00000

Program ROM

Copyright 1991, 1992, 1993, Agilent Technologies Company

Booting System

- If the screen is defective or blank, go to page 4-22, ‘’To troubleshoot display

failures.’’

- If there is an error message, use the table on page 4-15 in the ‘’To

troubleshoot power-up failures’’ procedure to determine the probable faulty

assembly.

- If the failure still is not isolated, go to page 4-25, ‘’To troubleshoot IIC bus

failures.’’

Agilent 35670A Troubleshooting the Analyzer

To troubleshoot CPU, memory, and buses failures

4-21


To troubleshoot display failures

Use this test to isolate display failures to the A101 Display assembly, A102 DC-DC

Converter assembly, or A7 CPU assembly.

q Step 1. Check the DC-DC Converter assembly.

- Set the power switch to off (O).
- Connect the voltmeter to A102 TP1.
- Set the power switch to on (l).
- Check that the voltage reads is 210 10 Vdc.

Caution The Display assembly will be damaged if the voltage is at or above 235 Vdc.

- If the voltage is incorrect, the A102 DC-DC Converter assembly is probably

faulty.

Troubleshooting the Analyzer Agilent 35670A

To troubleshoot display failures

4-22


q Step 2. Check the CPU signals to the Display assembly.

- Set the power switch to on (l).
- Using a logic probe, check that the following TTL signals are toggling.

Test Location Signal Name In/Out

A7 P2(9) VSYNCEL A7 Out

A7 P2(11) HSYNCELn A7 Out

A7 P2(13) VCLK A7 Out

A7 P2(15) VID A7 Out

- If the signals are incorrect, do the following:
- Set the power switch to off (O).
- Disconnect the display cable from A7 P2.
- Set the power switch to on (l).
- Check the signals again.
- If the signals are now correct, the A101 Display assembly is probably faulty.

A7 Component Locator, Circuit Side

Agilent 35670A Troubleshooting the Analyzer

To troubleshoot display failures

4-23


q Step 3. Determine the probable faulty assembly by comparing the analyzer’s

symptoms to the following table.

Symptom Probable Faulty Assembly

Vertical and horizontal scanning is occurring

Part of information is missing, for example only half letters

Blocks of information are missing

Information on the screen is scrambled or mixed up

Vertical or horizontal stripes appear across the screen

CPU

Screen is blank

Screen is tilted, compressed, or distorted

Line across the screen

Display

Troubleshooting the Analyzer Agilent 35670A

To troubleshoot display failures

4-24


To troubleshoot IIC bus failures

Use this test to isolate IIC (Inter-IC) bus failures to one of the following assemblies:

- A7 CPU
- A1/A2 Input
- A5 Analog
- A10 Rear Panel
- A11 Keyboard Controller

q Step 1. Disconnect all assemblies connected to the CPU assembly’s IIC bus.

- Set the power switch to off (O).
- Remove the rear panel and disconnect the cable from A10 P100.
- Pull the following assemblies out of the card nest about 1 inch:

A5 Analog

A2 Input (optional)

A1/A2 Input

- Disconnect the keyboard cable from A7 P1.

Agilent 35670A Troubleshooting the Analyzer

To troubleshoot IIC bus failures

4-25


q Step 2. Check the serial clock (SCL).

- Attach a logic probe to A7 P7 pin 2 (SCL).
- Set the power switch to on (l).
- Press SW2 (reset switch) while monitoring A7 P7 pin 2 (SCL), the power-on

LEDs, and the display.

The TTL logic level should toggle when 00 is displayed and toggle continuously

whenBooting Systemis displayed. The following failure message should be

displayed afterBooting Systemand the display grid should appear about 2 minutes

after power up.

Front Panel failure information:

keyboard IIC chip fails:

IIC: No Device Acknowledge

key stuck: 32

A power-on test has failed. Refer

servicing to qualified personnel.

Press Start key to attempt to continue

power-up.

Troubleshooting the Analyzer Agilent 35670A

To troubleshoot IIC bus failures

4-26


- If the signal does not toggle after SW2 is pressed, the A7 CPU assembly is

probably faulty.

- If no error messages are displayed afterBooting Systemor A7 DS101 (green

run LED) is off, go to page 4-29, ‘’To troubleshoot fast bus failures.’’

q Step 3. Check the serial data line (SDA).

- Attach the logic probe to A7 P7 pin 1 (SDA).
- Press SW2 while monitoring A7 P7 pin 1 (SDA), the power-on LEDs, and

the display.

The TTL logic level should toggle when 00 is displayed and toggle continuously

whenBooting Systemis displayed. The following failure message should be

displayed afterBooting Systemand the display grid should appear about 2 minutes

after power up.

Front Panel failure information:

keyboard IIC chip fails:

IIC: No Device Acknowledge

key stuck: 32

A power-on test has failed. Refer

servicing to qualified personnel.

Press Start key to attempt to continue

power-up.

- If the signal does not toggle after SW2 is pressed or the failure message is

not displayed, the A7 CPU assembly is probably faulty.

Agilent 35670A Troubleshooting the Analyzer

To troubleshoot IIC bus failures

4-27


q Step 4. Check the assemblies on the IIC bus by repeating the following steps for each

assembly.

- Set the power switch to off (O).
- Reconnect one assembly at a time in the following order.

A11 Keyboard Controller (cable to A7 P1)

A10 Rear Panel (cable to A10 P100)

A5 Analog

A1/A2 Input (lower slot)

A2 Input (upper slot)

- Set the power switch to on (l).
- After the softkey menu appears, (about one minute after power up) press

any key.

- If the analyzer does not respond correctly, the assembly just reconnected is

probably faulty.

q Step 5. If the failure still is not isolated, go to page 4-29, ‘’To troubleshoot fast bus

failures.’’

Troubleshooting the Analyzer Agilent 35670A

To troubleshoot IIC bus failures

4-28


To troubleshoot fast bus failures

Use this test to isolate Fast Bus failures to the A7 CPU assembly or A6 Digital

assembly.

- Set the power switch to off (O).
- Set the power switch to on (l) while holding in the [System Utility] key.

The screen displaysFast Bus Diagnostic Test ...and the power-on LEDs are flashing.

- If the analyzer did not respond correctly, the A7 CPU assembly is probably

faulty.

- Using a logic probe, check the following signals.

A7 P10 Pin Signal Name TTL Logic State In Test Mode

64, 114, 65, 115, 66 FA1 to FA5 Toggling

72 ECLK Toggling

74 FSELAn Toggling

112 BRESETn Low

119 FRW Toggling

123 FIFOENn High

124 FSELSn Toggling

7-11, 21-45, 59, 71, 109,

118, 120, 122, 147, 149

GND Low

- If the signals are correct, the A6 Digital assembly is probably faulty.
- If any signal is incorrect, the A7 CPU assembly is probably faulty.

This is only a partial check of the fast bus signals between the A7 CPU assembly

and the A6 Digital assembly.

Agilent 35670A Troubleshooting the Analyzer

To troubleshoot fast bus failures

4-29


Troubleshooting the Analyzer Agilent 35670A

To troubleshoot fast bus failures

4-30


To perform self tests

Use this test when one of the following occurs:

- Performance test fails
- Calibration fails
- Trigger fails
- GPIB fails
- Microphone power fails
- Serial port fails
- Parallel port fails
- Failure is intermittent

q Step 1. Run all the functional self tests.

- Connect the rear panel SOURCE output to the rear panel TACH input

using a BNC cable.

- Remove all cables from the front panel input connectors.

Caution The ICP self test outputs approximately 30 Vdc on the input connectors. Before

starting the self tests, disconnect all devices connected to the input connectors.

Devices left connected during the ICP self test may be damaged.

- Set the power switch to on (l).
- After calibration is complete, press the following keys:

[Input]

[ALL CHANNELS]

[CH* FIXED RANGE]

[System Utility]

[CALIBRATN]

[AUTO CALOFF]

[Rtn]

[MORE]

[SELF TEST]

[FUNCTIONL TESTS]

[ALL]

[CONTINUE]

Agilent 35670A Troubleshooting the Analyzer

To perform self tests

4-31


q Step 2. Compare the analyzer’s self-test results to the following table.

- When the tests have finished, press the following keys:

[Rtn]

[TEST LOG]

- Press the [PREVIOUS PAGE] softkey until the first page of test log is

displayed.

To print the test log to a GPIB printer, press the following keys:

[Local/GPIB]

[SYSTEM CONTROLLR]

[PRINTER ADDRESS]

( _printer address_ )

[ENTER]

[System Utility]

[MORE]

[SELF TEST]

[TEST LOG]

[Plot/Print]

[ <F"Times""P10 >PLOT/PRNT DEVICE]

( _device type_ )

[Rtn]

[PLOT/PRNT DESTINATN]

[OUTPUT TO GPIB]

[Rtn]

[START PLOT/PRNT]

- If the analyzer did not complete the tests (analyzer locks up), go to page 4-37

‘’To troubleshoot self-test lockup failures.’’

- If the failure is intermittent and the analyzer passed all self tests, go to page

4-40 ‘’To troubleshoot intermittent failures.’’

- If the analyzer completed the tests, compare the analyzer’s test log to the

following table.

If the analyzer’s test log matches more than one entry on the table, use the entry

closest to the beginning of the table. The table lists the probable faulty assembly or

assemblies and any recommended adjustment or troubleshooting procedure to do

before replacing the assembly. If both an adjustment and a test are recommended,

do the adjustment first.

For additional information on the self tests, see ‘’Self-Test Descriptions’’ on page

10-10.

Troubleshooting the Analyzer Agilent 35670A

To perform self tests

4-32


Self-Test Troubleshooting Guide

Failing Self Test Probable Faulty Assembly Adjustment Troubleshooting Test

Interrupt A7 CPU CPU, Memory, and Buses,

page 4-18.

Mult Fctn Peripheral A7 CPU

Front Panel A11 Keyboard Controller

GPIB A10 Rear Panel

Disk Controller A7 CPU

Disk FIFO A7 CPU

IIC Bus (If only one

assembly is failing)

Assembly failing. See Test

Log

IIC Bus (If multiple

assemblies are failing)

See Test Log IIC bus, page 4-25

Fast Bus A7 CPU

A6 Digital

Fast bus, page 4-29

Trigger Gate Array A6 Digital †

LO Gate Array A6 Digital

Digital Filter Gate Array A6 Digital

FIFO A6 Digital

Baseband Zoom

ADC Gate Array

All other self tests pass

A5 Analog

Baseband

Zoom

All other self tests pass

A6 Digital

Baseband A5 Analog

A6 Digital

Source and calibrator,

page 4-45

Zoom A5 Analog

A6 Digital

Source and calibrator,

page 4-45

Source through DSP A6 Digital

Source LO A6 Digital

Source to CPU A6 Digital

```
† Analyers with firmware revision A.00.00 may fail the Trigger Gate Array test when the A1/A2 Input or
```
```
A5 Analog assemblies fail. Go to page 4 45, ‘’To troubleshoot source and calibrator failures,’’ to
```
```
determine the probable faulty assembly.
```
Agilent 35670A Troubleshooting the Analyzer

To perform self tests

4-33


Self-Test Troubleshooting Guide (continued)

Failing Self Test Probable Faulty Assembly Adjustment Troubleshooting Test

Source With LO fails and

Source Without LO passes

A6 Digital

Source Without LO

one channel

A1/A2 Input

A5 Analog

Input and ADC, page 4-51

Four channel, page 4-54

Source Without LO

channel 1 and 3 or

channel 2 and 4

A2 Input

Source With LO

one channel

A1/A2 Input

A5 Analog

Input and ADC, page 4-51

Four channel, page 4-54

Source With LO

channel 1 and 3 or

channel 2 and 4

A2 Input

Input Offset

one channel or

channel 1 and 3 or

channel 2 and 4

A1/A2 Input Input dc offset, page 5-10

ADC Gate Array A5 Analog

A6 Digital

ADC gain, offset, and

reference, page 5-10

Source and calibrator,

page 4-45

Source Without LO

all channels

A5 Analog

A6 Digital

Source and calibrator,

page 4-45

Source With LO

all channels

A5 Analog

A6 Digital

Source and calibrator,

page 4-45

Input Offset

all channels

A5 Analog ADC gain, offset, and

reference, page 5-7

Input Distortion

one channel

A1/A2 Input

A5 Analog

Input and ADC, page 4-51

Four channel, page 4-54

Input Distortion

channel 1 and 3 or

channel 2 and 4

A2 Input

Input Distortion

all channels

A5 Analog

A6 Digital

ADC Gain, offset, and

reference, page 5-7

Source and calibrator,

page 4-45

Input Trigger

one or more channels fail,

but at least one channel

passes

A5 Analog

Input Trigger A5 Analog

A6 Digital

Trigger, page 4-62

Troubleshooting the Analyzer Agilent 35670A

To perform self tests

4-34


Self-Test Troubleshooting Guide (continued)

Failing Self Test Probable Faulty Assembly Adjustment Troubleshooting Test

Input A-Wt Filter

one channel or channel 1 and

3 or channel 2 and 4

A1/A2 Input

Input A-Wt Filter

all channels

A6 Digital

Input AAF/Bypass

one channel or

channel 1 and 3 or

channel 2 and 4

A1/A2 Input Filter flatness, page 5-17

Input AAF/Bypass

all channels

A6 Digital

Input ICP Source

### †

one channel or

channel 1 and 3 or

channel 2 and 4

A1/A2 Input

Tachometer

### ‡

A6 Digital

A10 Rear Panel

Tachometer, page 4-24

Source Filter A5 Analog

Source DC A5 Analog

Quick Confidence A1/A2 Input

A5 Analog

A6 Digital

Input dc offset, page 5-10

ADC gain, offset, and

reference, page 5-7

Filter flatness, page 5-17

Performance test, page 4-42

All self tests pass Next Step

```
† This test fails if a device is connected to the front panel input connectors.
```
```
‡ This test fails if the Source output is not connected to the Tachometer input.
```
Agilent 35670A Troubleshooting the Analyzer

To perform self tests

4-35


q Step 3. Determine the probable faulty assembly and next test by comparing the

analyzer’s symptoms to the following table.

Failure Probable Faulty Assembly Next Test

Disk drive A100 Disk Drive

Flexible disk

Disk drive cable

A7 CPU

Disk drive, page 4-57

GPIB A10 Rear Panel †

Serial port A10 Rear Panel †

Parallel A10 Rear Panel †

External trigger A10 Rear Panel

A5 Analog

Trigger failures, page 4-62

Tachometer A10 Rear Panel

A6 Digital

Tachometer, page 4-24

Source A5 Analog

A6 Digital

Source and calibrator, page 4-45

Autorange

Overrange

A1/A2 Input

A5 Analog

Auto-range, page 4-59

External keyboard A10 F200 fuse

External Keyboard

A10 Rear Panel

DIN connector, page 4-61

External monitor A7 CPU

Microphone power

Microphone adapter

A77 Microphone

A5 Analog

Microphone power, page 4-69

Performance test Performance test, page 4-42

Intermittent failure Intermittent, page 4-40

```
† The circuits for the output ports are located on the A10 Rear Panel assembly except for a few output
```
```
buffers on the A7 CPU assembly. If replacing the A10 Rear Panel assembly does not fix the failure, the
```
```
A7 CPU assembly is probably faulty.
```
```
For additional information on the self tests, see ‘’Self Test Descriptions’’ starting on page 10 10.
```
Troubleshooting the Analyzer Agilent 35670A

To perform self tests

4-36


q Step 2. Run the IIC and fast bus self tests.

- Press the following keys:

[System Utility]

[CALIBRATN]

[AUTO CALOFF]

[Input]

[ALL CHANNELS]

[CH* FIXED RANGE]

1

[Vpk]

[System Utility]

[MORE]

[SELF TEST]

[TEST LOG]

[Rtn]

[FUNCTIONL TESTS]

[I/O]

[IIC BUS]

- If the keyboard is not active, or the analyzer locks up when a key is pressed,

go to page 4-25, ‘’To troubleshoot IIC bus failures.’’

- Press the [FAST BUS] softkey.
- If the analyzer locks up or the digital processor failed the fast bus self test,

go to page 4-29, ‘’To troubleshoot fast bus failures.’’

Troubleshooting the Analyzer Agilent 35670A

To troubleshoot self-test lockup failures

4-38


q Step 4. Run the remaining self tests.

- Connect the rear panel SOURCE output to the rear panel TACH input

using a BNC cable.

- Remove all cables from the front panel input connectors.

Caution The ICP self test outputs approximately 30 Vdc on the input connectors. Before

starting the self tests, disconnect all devices connected to the input connectors.

Devices left connected during the ICP self test may be damaged.

- Until a test fails or the analyzer locks up, press the following keys allowing

enough time for each test to complete before pressing the next key :

[Rtn]

[OTHER]

[INTER RUPT]

[MULT FCTN PERIPHERL]

[MAIN RAM]

[CONTINUE]

[Rtn]

[DIGITAL PROCESSOR]

[ALL]

[Rtn]

[SOURCE]

[SOU RCE LO]

[SOURCE TO CPU]

[CONTINUE]

[Rtn]

[ADC GATE ARRAY]

[INPUTS]

[ <F “Times”>Times"P10ALL ]

[CONTINUE<| >]

[Rtn]

[TACHOMETR]

[CO NTINUE]

A failure may cause the self tests to run very slow. If the analyzer does not

complete a self test within a few minutes (analyzer locks up during the test),

consider it equivalent to displaying FAILS in the test log.

- If any of these self tests fail, locate the test that failed in the ‘’Self-Test

Troubleshooting Guide’’ on page 4-33.

- If the failure still is not isolated, go to page 4-45, ‘’To troubleshoot source

and calibrator failures.’’

Agilent 35670A Troubleshooting the Analyzer

To troubleshoot self-test lockup failures

4-39


To troubleshoot intermittent failures

Use this test to isolate intermittent failures to the assembly.

- Determine if your intermittent failure is caused by one of the following

common causes.

Common Reasons Troubleshooting Procedure

Loose screws

and cables

Check that the screws in the analyzer are tight and that the cables are

firmly in their sockets. This is especially important since grounding for

the analyzer depends on the cables and screws.

Motherboard

connectors

Remove each assembly connected to the Motherboard and check the

connectors for loose or bent pins.

Power supply

voltages

Check for correct power-supply voltages. See ‘’To perform initial

verification’’ on page 4-5.

Out-of-adjustment Do the adjustments for the analyzer in chapter 5.

Low level noise Do ‘’To troubleshoot distortion failures’’ on page 4-56.

Air flow

restricted

Cooling air enters from the right side and exhausts through the left side

and rear panel. Check that the air flow was not restricted in these areas

when the failure occurred.

External voltage Verify that the line voltage is within the electrical specification for the

analyzer. See chapter 2.

- Connect the rear panel SOURCE output to the rear panel TACH input using a

BNC cable. Remove all cables from the front panel input connectors.

Caution The ICP self test outputs approximately 30 Vdc on the input connectors. Before

starting the self tests, disconnect all devices connected to the input connectors.

Devices left connected during the ICP self test may be damaged.

- Set the power switch to on (l).

Troubleshooting the Analyzer Agilent 35670A

To troubleshoot intermittent failures

4-40


- Press the following keys:

[Preset]

[DO PRESET]

[System Utility]

[CALIBRATN]

[AUTO CALOFF]

[Input]

[ALL CHANNELS]

[CH* FIXED RANGE]

1

[Vpk]

[System Utility]

[MORE]

[SELF TEST]

[TEST LOG]

[CLEAR TEST LOG]

[Rtn]

[LOOP MODEON]

[FUNCTIONL TESTS]

[ALL]

[C ONTINUE]

- After this test detects a failure, press the following keys:

[Rtn]

[LOOP MODEOFF]

- Compare the analyzer’s test log to the ‘’Self Test Troubleshooting Guide’’

starting on page 4-33.

If the analyzer’s test log matches more than one entry in the table, use the entry closest

to the beginning of the table. The table lists the probable faulty assembly or

assemblies and any recommended adjustment or troubleshooting procedure to do

before replacing the assembly. If both an adjustment and a test are recommended, do

the adjustment first.

All pass and fail messages are displayed on the test log along with the number of times

a test passes or fails. When loop mode is activated, the analyzer continually repeats a

test until power is cycled or loop mode is aborted by pressing the [LOOP MODE

OFF] softkey. During some tests, the keyboard is not active and loop mode cannot be

turned off. If this occurs, wait for the test to finish.

If you abort a self test before the self test is finished, the analyzer may fail its

calibration routine. To prevent this from happening, press [Preset][DO PRESET]or

cycle power after you abort a self test.

To run a specific self test in loop mode, press the keys listed in step 4 except select the

specific self test instead of [ALL].

Agilent 35670A Troubleshooting the Analyzer

To troubleshoot intermittent failures

4-41


To troubleshoot performance test failures

With the exception of the Quick Confidence test, all functional self tests must pass

before the following table is valid.

q Step 1. If the analyzer failed a performance test, compare the failing performance test

to the following table.

If more than one performance test is failing, use the entry that is closest to the

beginning of the table. The table lists the probable faulty assembly or assemblies and

any recommended adjustment or troubleshooting procedure to do before replacing the

assembly. If both an adjustment and a test are recommended, do the adjustment first.

Failing Performance Test Troubleshooting Guide

Failing Performance Test Probable Faulty Assembly

(in order of probabilty)

Adjustment Troubleshooting Test

DC offset

one channel or

channel 1 and 3 or

channel 2 and 4

A1/A2 Input Input dc offset, page 5-10

ADC gain, offset, and

reference, page 5-7

DC offset

all channels

A5 Analog Input dc offset, page 5-10

ADC gain, offset, and

reference, page 5-7

Amplitude accuracy

one channel

A1/A2 Input

A5 Analog

Input dc offset, page 5-10

ADC gain, offset, and

reference, page 5-7

Input and ADC, page 4-51

Four channel, page 4-54

Amplitude accuracy

channel 1 and 3 or

channel 2 and 4

A2 Input Input dc offset, page 5-10

Amplitude accuracy

all channels

A5 Analog Input dc offset, page 5-10

ADC gain, offset, and

reference, page 5-7

Flatness

one channel

A1/A2 Input

A5 Analog

Input dc offset, page 5-10

ADC gain, offset, and

reference, page 5-7

Input and ADC, page 4-51

Four channel, page 4-54

Flatness

channel 1 and 3 or

channel 2 and 4

A2 Input Input dc offset, page 5-10

Flatness

all channels

A5 Analog Input dc offset, page 5-10

ADC gain, offset, and

reference, page 5-7

Troubleshooting the Analyzer Agilent 35670A

To troubleshoot performance test failures

4-42


Failing Performance Test Probable Faulty Assembly

```
(in order of probabilty)
```
```
Adjustment Troubleshooting Test
```
Amplitude linearity

one channel

```
A1/A2 Input
```
```
A5 Analog
```
```
Input dc offset, page 5-10
```
```
ADC gain, offset, and
```
```
reference, page 5-7
```
```
Input and ADC, page 4-51
```
```
Four channel, page 4-54
```
Amplitude linearity

channel 1 and 3 or

channel 2 and 4

```
A2 Input Input dc offset, page 5-10
```
Amplitude linearity

all channels

```
A5 Analog Input dc offset, page 5-10
```
```
ADC gain, offset, and
```
```
reference, page 5-7
```
Amp_phase match A1/A2 Input

```
A5 Digital
```
```
A6 Digital
```
```
Source and calibrator,
```
```
page 4-45
```
A-weight filter A1/A2 Input

Anti-alias filter A1/A2 Input Filter flatness, page 5-17

Frequency accuracy A7 CPU Frequency reference, page 5-5

Input coupling A1/A2 Input

Single ch phase accuracy A10 Rear Panel

```
A5 Analog
```
```
A6 Digital
```
```
Trigger, page 4-62
```
External trigger A10 Rear Panel

```
A5 Analog
```
```
Trigger, page 4-62
```
Input resistance A1/A2 Input

Input capacitance A1/A2 Input

Harmonic distortion

one channel

```
A1/A2 Input
```
```
A5 Analog
```
```
Input and ADC, page 4-51
```
```
Four channel, page 4-54
```
Harmonic distortion

channel 1 and 3 or

channel 2 and 4

```
A2 Input
```
Harmonic distortion

all channels

```
A5 Analog ADC gain, offset, and
```
```
reference, page 5-7
```
Intermodulation distortion

one channel

```
A1/A2 Input
```
```
A5 Analog
```
```
Input and ADC, page 4-51
```
```
Four channel, page 4-54
```
Intermodulation distortion

channel 1 and 3 or

channel 2 and 4

```
A2 Input
```
Intermodulation distortion

all channels

```
A5 Analog ADC gain, offset, and
```
```
reference, page 5-7
```
Agilent 35670A Troubleshooting the Analyzer

To troubleshoot performance test failures

4-43


Failing Performance Test Troubleshooting Guide

Failing Performance Test Probable Faulty Assembly

```
(in order of probabilty)
```
```
Adjustment Troubleshooting Test
```
Spurious signals

one channel

```
A1/A2 Input
```
```
A5 Analog
```
```
Input and ADC, page 4-51
```
```
Four channel, page 4-54
```
Spurious signals

channel 1 and 3 or

channel 2 and 4

```
A2 Input
```
Spurious signals

all channels

```
A5 Analog
```
```
mechanical
```
```
A6 Digital
```
```
ADC gain, offset, and
```
```
reference, page 5-7
```
```
Distortion, page 4-56
```
Noise

one channel

```
A1/A2 Input
```
```
A5 Analog
```
```
Input and ADC, page 4-51
```
```
Four channel, page 4-54
```
Noise

channel 1 and 3 or

channel 2 and 4

```
A2 Input
```
Noise

all channels

```
A5 Analog
```
```
mechanical
```
```
ADC gain, offset, and
```
```
reference, page 5-7
```
```
Distortion, page 4-56
```
Cross talk A1/A2 Input Distortion, page 4-56

ICP supply A1/A2 Input

Source dc offset A5 Analog

Source amplitude accuracy A5 Analog

Source flatness A5 Analog

Source distortion A5 Analog

Source output resistance A5 Analog

Troubleshooting the Analyzer Agilent 35670A

To troubleshoot performance test failures

4-44


To troubleshoot source and calibrator failures

Use this test to isolate source and calibrator failures to the A6 Digital assembly, the

A5 Analog assembly, the A1/A2 Input assembly, the A12 BNC assembly, or the

A10 Rear Panel assembly.

q Step 1. Check the sine wave output.

- Set the power switch to on (l).
- Connect an oscilloscope to the analyzer’s SOURCE connector using a BNC

cable.

- Set the oscilloscope as follows:

CH1 V/div

Input Impedance

CH1 Coupling

Probe Attenuation

Display Mode

Time/div

Trigger

Trig Src

Trigger Level

400 mV/div

50 Ω

dc

1

Repetitive

20 μs/div

Trg’d Sweep

Chan1

0V

- Press the following keys:

[System Utility]

[CALIBRATN]

[AUTO CALOFF]

[Source]

[SOURCEON]

[LEVEL]

1

[ Vpk ]

- If the oscilloscope displays a 10.2 kHz, 2 Vp-p sine wave with no dc offset, go

to Step 2.

This is only a quick check of the source sine wave. If the source is suspected of

failing at a specific frequency or amplitude, check the source sine wave at the

failing frequency or amplitude.

- Using an oscilloscope and a 1:1 probe, check that the signal at A5 TP8 is a

10.2 kHz, 2 Vp-p sine wave with no dc offset.

- If the signal is correct at A5 TP8 and incorrect at the analyzer’s front panel

SOURCE connector, the A12 BNC assembly is probably faulty.

- If the signal is correct at A5 TP8 and incorrect at the analyzer’s rear panel

SOURCE connector, the A10 Rear Panel assembly is probably faulty.

- If the signal is incorrect, the A5 Analog assembly is probably faulty.

Agilent 35670A Troubleshooting the Analyzer

To troubleshoot source and calibrator failures

4-45


q Step 2. Check the dc offset.

- Connect the voltmeter to A5 TP3.
- Press the following keys:

[LEVEL]

0

[Vpk]

[DC OFFSET]

- Rotate the RPG knob while monitoring the voltmeter.
- If the voltmeter’s voltage does not change from +2.3 to 2.3 as the dc offset

value is varied between 10 and +10 Vdc, the A5 Analog assembly is

probably faulty.

Troubleshooting the Analyzer Agilent 35670A

To troubleshoot source and calibrator failures

4-46


q Step 4. Check the calibrator output.

- Set the power switch to off (O).
- Remove the A1/A2 Input assembly and attach a test clip patch cord to TP
    17. Connect a 10:1 oscilloscope probe to the patch cord and TP 8 (ground).
- Reinstall the Input assembly in the card nest with patch cord and probe

attacted.

- Set the power switch to on (l).

Troubleshooting the Analyzer Agilent 35670A

To troubleshoot source and calibrator failures

4-48


To troubleshoot input and ADC failures

Use this test to isolate input failures in two channel analyzers to the A1 Input

assembly, A5 Analog assembly, or A12 BNC assembly.

q Step 1. Check the input path.

- Set the frequency synthesizer as follows:

Frequency

Amplitude

Function

10 kHz

2 Vp-p

Sine Wave

- Set the oscilloscope as follows:

CH1 V/div

Input Impedance

CH1 coupling

Time/div

Probe Atten

400 mV/div

1MΩ

dc

20 ns/div

1

- Press the following keys:

[System Utility]

[CALIBRATN]

[AUTO CALOFF]

[Input]

[ALL CHANNELS]

[CH* FIXED RANGE]

1

[Vpk]

- Connect the frequency synthesizer to the failing channel’s input connector

using a BNC cable.

- Using the oscilloscope, BNC-to-SMB cable, and SMB-to-SMB adapter,

check the following signals for the failing channel:

Test Location

Amplitude (10%)

Probable Faulty

Assembly

Channel 1

A12 P31 (connected to A1 P100)

A1 P200

2 Vp-p

2.83 Vp-p

A12 BNC

A1 Input

Channel 2

A12 P41 (connected to A1 P600)

A1 P700

2 Vp-p

2.83 Vp-p

A12 BNC

A1 Input

Agilent 35670A Troubleshooting the Analyzer

To troubleshoot input and ADC failures

4-51


This is only a quick check of the Input assembly. If the Input assembly’s amplitude

is still suspected of failing, set the analyzer to the failing range, impedance, and

frequency. Connect a signal equal to the range setting to the failing channel. When

the input level equals the range level, A1 P200 (channel 1) or A1 P700 (channel 2)

should be 2.83 ±0.28 Vp-p.

Troubleshooting the Analyzer Agilent 35670A

To troubleshoot input and ADC failures

4-52


q Step 2. Check the dc offset DAC.

- Using the BNC-to-SMB cable, connect the oscilloscope to A1 P200 to check

channel 1 or to A1 P700 to check channel 2.

If you changed the input signal or range, set the input signal to 2 Vp-p and the

range to 1 Vpk.

- Set the oscilloscope to 700 mV/div.
- Press the following keys:

[System Utility]

[MORE]

[SERVICE TESTS]

[SPCL TEST MODES]

[MORE SPCL MODES]

[CHANNEL 1 SPCL MODE]or[CHANNEL 2 SPCL MODE]

[OFFSET DAC]

0

[ENTER]

- Note the dc offset voltage of the sine wave displayed on the oscilloscope.
- Enter numbers between 127 and +128.

The sine wave dc offset voltage should change about 780 mV for a−127 entry and

−780 mV for a +127 entry.

- If the dc offset function is incorrect, the A1 Input assembly is probably

faulty.

- If the dc offset function is correct, the A5 Analog assembly is probably

faulty.

Agilent 35670A Troubleshooting the Analyzer

To troubleshoot input and ADC failures

4-53


To troubleshoot input failures on four channel analyzers

Use this test to isolate the failure when one channel fails in a four channel analyzer.

q Step 1. Run the input and quick confidence self tests.

- Set the power switch to on (l).
- When the power-up tests are completed, press the following keys:

[System Utility]

[CALIBRATN]

[AUTO CALOFF]

[Input]

[ALL CHANNELS]

[CH* FIXED RANGE]

1

[Vpk]

[System Utility]

[MORE]

[SELF TEST]

[TEST LOG]

[Rtn]

[FUNCTIONL TESTS]

[INPUTS]

[ALL]

[CONTINUE]

[Rtn]

[Rtn]

[QUICK CONF TEST]

- If the self tests fail but do not lockup the analyzer, note the failure messages

and go to Step 2.

- If the analyzer locks up on the Quick Confidence self test but not on the

input self tests, note the failure messages and go to Step 2 but don’t run the

Quick Confidence self test.

- If the analyzer locks up on the input self tests, go to Step 2 to determine if

exchanging the Input assemblies will allow the self tests to run.

This is most likely to occur when channel 1 and 3 are failing.

- If the self tests pass, go to Step 2 but substitute the failure symptom for the

self tests.

If the exact failure symptom is not known, use the performance test procedures to

isolate the failure symptom.

Troubleshooting the Analyzer Agilent 35670A

To troubleshoot input failures on four channel analyzers

4-54


q Step 2. Exchange the Input assemblies.

- Set the power switch to off (O).
- Exchange the Input assembly in the lower slot with the Input assembly in

the upper slot.

- Reconnect the cables to the A5 Analog assembly.
- Set the power switch to on (l).
- Press the following keys:

[System Utility]

[CALIBRATN]

[AUTO CAL OFF]

[Input]

[ALL CHANNELS]

[CH* FIXED RANGE]

1

[Vpk]

[System Utility]

[MORE]

[SELF TEST]

[TEST LOG]

[Rtn]

[FUNCTIONL TESTS]

[INPUTS]

[ALL]

[CONTINUE]

[Rtn]

[Rtn]

[QUICK CONF TEST]

- If the same channel fails as failed before the exchange, the A5 Analog

assembly is probably faulty.

- If a different channel now fails, the A2 Input assembly for the failing

channel is probably faulty.

The Input assembly for channel 1 and 3 is in the lower slot. The Input assembly for

channel 2 and 4 is in the upper slot.

Agilent 35670A Troubleshooting the Analyzer

To troubleshoot input failures on four channel analyzers

4-55


To troubleshoot distortion failures

Use this test to isolate distortion failures to the A1/A2 Input assembly, the A5 Analog

assembly, or to mechanical failures.

q Step 1. Check mechanical ground connections.

- Check that the Digital assembly, Input assembly, and Analog assembly are

completely in the card nest and making good contact with the grounding

guides at the sides of the card nest.

- Check that the screws in the sides, back, and top of the analyzer are tight.

When grounding is inadequate, feedback from the line power frequency and

internal clock frequencies may appear as distortion on the Input assemblies.

q Step 2. Check the analyzer’s clock signals.

Noisy clock signals can cause noise or spurious signals in the analyzer. To check the

analyzer’s clocks, go to page 4-5 ‘’To perform initial verification’’ and do Step 6.

q Step 3. Do the “Spurious signals” and ‘’Noise’’ performance tests.

- Run the “Spurious signals” and ‘’Noise’’ performance tests in chapter 3,

‘’Verifying Specifications.’’

- If all channels fail, the A5 Analog assembly is probably out of adjustment or

faulty.

Do the ‘’ADC gain, offset and reference’’ adjustment on page 5-7 before replacing

the assembly.

- If only one channel, or channel 1 and 3, or channel 2 and 4 fails, the Input

assembly that failed is probably faulty.

- If the ‘’Spurious signals’’ and ‘’Noise’’ performance tests pass, but the

analyzer appears to power up with a high noise floor, an auto-range circuit

may be failing.

To check the auto-range function and isolate a failure, see ‘’To troubleshoot

auto-range failures’’ on page 4-59.

Troubleshooting the Analyzer Agilent 35670A

To troubleshoot distortion failures

4-56


To troubleshoot disk drive failures

This test isolates disk drive failures to the A7 CPU, the A100 Disk Drive assembly, or

the flexible disk.

q Step 1. Check the disk controller on the A7 CPU assembly.

- Press the following keys:

[System Utility]

[MORE]

[SELF TEST]

[TEST LOG]

[Rtn]

[FUNCTIONL TESTS]

[I/O]

[INTERNAL DISK]

[DISK CONTROLLR]

[DISK FIFO]

- If the disk controller test aborts and displays the messageMass Storage Unit

not Present!!, the Disk Drive assembly, or the cable to the Disk Drive assembly

is probably faulty. The A7 CPU assembly could also be faulty but it is less

probable.

- If the disk controller or disk FIFO test fails, the A7 CPU assembly is

probably faulty.

q Step 2. Check the Disk Drive assembly.

- Insert a formatted flexible disk into the Disk Drive assembly and press the

following keys:

[RESTORE]

[RANDOM SEEK]

[SEEK RECORD]

( _any number between 1 and 2771_ )

[READ]

[READ/WRITE]

- If any of the self tests failed, insert a new formatted disk and repeat the

previous step.

- If the disk drive self tests still fail, the A100 Disk Drive assembly is probably

faulty.

If the self test aborts and displays the messageBad or unformatted media, the most

likely cause of the failure is a bad flexible disk. The analyzer can use either LIF

(Logical Interchange Format) or a DOS formatted flexible disk.

Agilent 35670A Troubleshooting the Analyzer

To troubleshoot disk drive failures

4-57


q Step 3. Check that the Disk Drive assembly can read and write to all sectors of a

flexible disk.

The read/write self test can take up to 40 minutes to complete if there are no

failures.

- Press the [READ/WRITE ALL] softkey.
- If the self test aborts and displays the messageBad or unformatted media, insert

a new formatted disk and repeat the previous step.

- If the self test fails a second time, the Disk Drive assembly is probably

faulty.

- If the self test passes, the Disk Drive assembly and flexible disk are

functioning correctly.

Troubleshooting the Analyzer Agilent 35670A

To troubleshoot disk drive failures

4-58


To troubleshoot auto-range failures

Use this test to check the auto-range and overload detector circuits on the A1/A2 Input

assembly. This test assumes that calibration and all self tests passed.

- Set the power switch to on (l).
- Press the following keys:

[System Utility]

[CALIBRATN]

[AUTO CALOFF]

[Inst Mode]

[CHANNELS 4]or[CHANNELS 2]

[Input]

[ALL CHANNELS]

[CH* FIXED RANGE]

1

[dBVrms]

[Source]

[SOURCEON]

[LEVEL]

1

[dBVrms]

[System Utility]

[MORE]

[SERVICE TESTS]

[SPCL TEST MODES]

[SOURCE LEVEL]

The Half range LEDs for all channels should be on and the Over range LEDs

should be off.

- Press the following keys:

[Source]

[LEVEL]

5

[dBVrms]

The Half range and Over range LEDs for all channels should be on.

- Press the following keys:

[Input]

[CH* AUTO RANGE]

After the auto-range routine is finished, the Half range LEDs should be on and the

Over range LEDs should be off.

Agilent 35670A Troubleshooting the Analyzer

To troubleshoot auto-range failures

4-59


- Press the following keys:

[CHANNEL 1]

[CHANNEL 1 RANGE]

The range should be set to 5 dBVrms.

- Press [Rtn].
- Repeat steps 5 and 6 for each channel.
- If only one channel, or channel 1 and 3, or channel 2 and 4 are failing, the

A1/A2 Input assembly is probably faulty.

In the two channel analyzer, the A1 Input assembly provides the circuits for

channel 1 and 2. In the four channel analyzer, the A2 Input assembly in the lower

slot provides the circuits for channel 1 and 3, and the A2 Input assembly in the

upper slot provides the circuits for channel 2 and 4.

- If all channels are failing, the A5 Analog assembly is probably faulty.

Troubleshooting the Analyzer Agilent 35670A

To troubleshoot auto-range failures

4-60


To troubleshoot DIN connector failures

Use this test to determine if the fuse for the DIN connector is failing before replacing

the A10 Rear Panel assembly.

- Set the power switch to on (l).
- Check the voltage on pin 2 of the DIN connector for +5V.
- If the voltage is correct, the A10 Rear Panel assembly is probably faulty.
- If the voltage is incorrect, replace A10 F200.

Agilent 35670A Troubleshooting the Analyzer

To troubleshoot DIN connector failures

4-61


To troubleshoot trigger failures

Use this test when the trigger mode is suspected of failing or the Input Trigger self test

fails on all channels.

q Step 1. Check trigger modes.

- Set the power switch to on (l).
- Press the following keys:

[System Utility]

[CALIBRATN]

[AUTO CAL OFF]

[Input]

[ALL CHANNELS]

[CH* FIXED RANGE]

1

[Vpk]

[Source]

[SOURCEON]

[LEVEL]

1

[Vpk]

[FIXED SINE]

[ 1 ]

[kHz]

[Inst Mode]

[4 CHANNEL]or[2 CHANNEL]

[ACTIVE TRACE]

[ABCD]or[AB]

[Meas Data]

[ALL CHANNELS]

[TIME CHANNEL]

[System Utility]

[MORE]

[SERVICE TESTS]

[SPCL TEST MODES]

[SOURCE LEVEL]

[Trigger]

[SOURCE TRIGGER]

- If the analyzer is not triggering and the messageWAITING FOR SOURCE

TRIGGERis displayed, the A6 Digital assembly is probably faulty.

Fixed sine wave source triggering occurs at a consistent (but not predictable) point

within the time record.

- Set the frequency synthesizer as follows:

Frequency

Amplitude

Function

1 kHz

6 Vp-p

Square Wave

Troubleshooting the Analyzer Agilent 35670A

To troubleshoot trigger failures

4-62


- Connect the frequency synthesizer to the analyzer’s rear panel EXT TRIG

connector using a BNC cable.

- Press the following keys allowing enough time for the analyzer to trigger

before pressing the next key. Note which trigger modes are failing:

[CHANNEL 1]

[CHANNEL 2]

[CHANNEL 3] (option AY6 only)

[CHANNEL 4] (option AY6 only)

[TRIGGER SETUP]

[CHANNEL LEVEL]

200

[mV]

[SLOPE NEG]

[ALL CHANNELS]

[CHANNEL DELAY]

100

[mS]

[ 0 ]

[S]

[Rtn]

[ARM SETUP]

[MANUAL ARM]

[Rtn]

[ARM]

[ARM SETUP]

[AUTOMATIC ARM]

[Rtn]

[EXTERNAL TRIGGER]

[TRIGGER SETUP]

[EXT LEVEL TTL]

[EXT LEVEL USER]

[USER EXT LEVEL]

200

[mV]

[EXT RANGE +/−10 ]

[USER EXT LEVEL]

0

[V]

The messageWAITING FOR mode TRIGGERis displayed when the analyzer is not

triggering.

- Change the frequency synthesizer’s amplitude to 0.3 Vp-p.
- Press [EXT RANGE +/ 2 ].

The analyzer should now trigger.

Agilent 35670A Troubleshooting the Analyzer

To troubleshoot trigger failures

4-63


q Step 2. Determine the probable faulty assembly or next step by comparing the trigger

failure to the following table.

If the trigger failure matches more than one entry in the table, use the entry closest to

the beginning of the table.

Trigger Mode Failing Probable Faulty

Assembly or Next Step

All channels and external trigger fail all trigger modes Step 3

All channels trigger but external trigger fails all trigger modes Step 4

At least one channel or external trigger functions correctly A5 Analog

Channel level fails

Arm fails

External trigger fails user level or TTL level

A5 Analog

External trigger fails EXT RANGE A10 Rear Panel

Trigger delay fails A6 Digital

q Step 3. Check trigger signal to Digital assembly.

- Set the power switch to off (O).
- Remove the A5 Analog assembly and attach a test clip patch cord to TP 204.
- Connect a logic probe to the patch cord and TP 160 (ground).
- Reinstall the Analog assembly in the card nest with patch cord and probe

attached.

- Set the power switch to on (l).
- Press the following keys:

[System Utility]

[CALIBRATN]

[AUTO CALOFF]

[Input]

[ALL CHANNELS]

[CH* FIXED RANGE]

1

[Vpk]

[Source]

[SOURCE ON]

[LEVEL]

[ 1 ]

[Vpk]

[System Utility]

[MORE]

[SERVICE TESTS]

[SPCL TEST MODES]

[SOURCE LEVEL]

[Trigger]

[CHANNEL 1]

Troubleshooting the Analyzer Agilent 35670A

To troubleshoot trigger failures

4-64


- If the signal at A5 TP 204 is toggling, the A6 Digital assembly is probably

faulty.

- If the signal at A5 TP 204 is not toggling, the A5 Analog assembly is

probably faulty.

Agilent 35670A Troubleshooting the Analyzer

To troubleshoot trigger failures

4-65


q Step 4. Check external trigger signal to the Analog assembly.

- Set the power switch to off (O).
- Remove the seven screws holding the rear panel to the analyzer and lean the

rear panel back until the A10 Rear Panel assembly is visible. Keep the

cables connected.

- Set the power switch to on (l).
- Change the frequency synthesizer’s amplitude to 2 Vp-p.
- Set the oscilloscope as follows:

CH1 V/div

Input Impedance

CH1 Coupling

Time/div

Probe Atten

100 mV/div

1MΩ

dc

200 μs/div

10

- Connect the oscilloscope to A10 TP2 using a 10:1 probe.
- Press the following keys:

[Trigger]

[EXTERNAL TRIGGER]

[TRIGGER SETUP]

[EXT LEVEL USER]

[EXT RANGE +/−10 ]

The oscilloscope should display a 37040 mVp-p square wave.

- If the signal is incorrect, the A10 Rear Panel assembly is probably faulty.
- Set the oscilloscope to 300 mV/div.
- Press [EXT RANGE +/ 2 ].

The oscilloscope should display a 1.90.2 Vp-p square wave.

- If the signal is incorrect, the A10 Rear Panel assembly is probably faulty.
- If the external trigger signals are correct, the A5 Analog assembly is

probably faulty.

Troubleshooting the Analyzer Agilent 35670A

To troubleshoot trigger failures

4-66


To troubleshoot memory battery failures

Use this test when battery-backed-up memory is suspected of failing. This test

separates Memory assembly failures from memory battery failures.

- Press the following keys:

[Preset]

[DO PRESET]

[System Utility]

[CLOCK SETUP]

[DATE MMDDYY]

010101

[ENTER]

- Set the power switch to off (O), then to on (l).
- Press the following keys:

[System Utility]

[CLOCK SETUP]

[DATE MMDDYY]

- If the date is 01-01-01, the battery-backed-up memory is functioning

correctly. Enter the current date. Go to page 4-31, ‘’To perform self tests,’’

to continue troubleshooting.

- If the date is incorrect, remove the Memory assembly.

See ‘’To remove memory’’ on page 6-13.

- Check that the voltage at TP200 is 3.5 1V.
- If the voltage is correct, the Memory assembly is probably faulty.
- If the voltage is incorrect, replace the battery (B200).

Caution There is danger of explosion if battery is incorrectly replaced. Replace the battery

with the same or an equivalent type listed on page 7-12. Discard used batteries

according to the battery manufacturer’s instructions.

Agilent 35670A Troubleshooting the Analyzer

To troubleshoot memory battery failures

4-67


Troubleshooting the Analyzer Agilent 35670A

To troubleshoot memory battery failures

4-68


To troubleshoot microphone power and adapter failures

Use this test to isolate Microphone failures to the A5 Analog assembly or option UK4,

Microphone Adapter and Power Supply.

q Step 1. Check mic pwr on the analyzer’s front panel.

- Set the power switch to on (l).
- Check the voltage on pin 2 of the mic pwr connector for +8 ±0.5 Vdc.
- If the voltage is incorrect, the A5 Analog assembly is probably faulty.

q Step 2. Check the power from the Microphone Adapter and Power Supply.

- Connect the mic cable to the analyzer’s mic pwr connector.
- Check the voltage on pins 5 and 6 of each microphone connector for

28±2.8 Vdc.

- If the voltage is incorrect, the A77 Microphone assemby in the Microphone

Adapter and Power Supply is probably faulty.

- Set the switch for each microphone connector to off.
- Check the voltage on pin 3 of each connector for 0 Vdc.
- Set the switch for each microphone connector to on.
-
    Check the voltage on pin 3 of each connector for 200 15 Vdc.
- If the voltage is incorrect, the A77 Microphone assembly in the Microphone

Adapter and Power Supply is probably faulty.

Agilent 35670A Troubleshooting the Analyzer

To troubleshoot microphone power and adapter failures

4-69


q Step 2. Check the tachometer range function.

- Set the oscilloscope for 20 s/div.
- Press the following keys:

[Rtn]

[LOOP MODEOFF]

[Rtn]

[SERVICE TESTS]

[SPCL TEST MODES]

[SOURCE LEVEL]

[Source]

[SOURCEON]

[LEVEL]

500

[mVpk]

[Trigger]

[TACHOMETR SETUP]

[TRG RANGE +/− 20 ]

- Check that the oscilloscope displays a dc voltage of approximately 4 Vdc.
- Press [TRG RANGE +/ 4].
- Check that the oscilloscope displays a 4 0.4 Vp-p, 10.24 kHz sine wave,

with 2 ±0.2 Vdc offset.

- If the signal is incorrect, the A10 Rear Panel assembly is probably faulty.
- If the signal is correct, the A6 Digital assembly is probably faulty.

Agilent 35670A Troubleshooting the Analyzer

To troubleshoot tachometer failures

4-71


# 5

## Adjusting the Analyzer

5-1


Adjusting the Analyzer

## This chapter contains the adjustment procedures for the Agilent 35670A

## Dynamic Signal Analyzer. Use these adjustments if the analyzer does not meet

## its specifications or if instructed in chapter 4, ‘’Troubleshooting the Analyzer,’’

## or chapter 6, ‘’Replacing Assemblies,’’ to perform these adjustments. These

## adjustments are not required for routine maintenance.

## Allow the Agilent 35670A analyzer to warm up for an hour before doing any of

## the adjustments.

## During many of these adjustment procedures, an adjustment message appears

## on the screen. The instructions on the screen are not as complete as the

## instructions in this guide. When an adjustment message appears on the screen,

## continue to follow the instructions in this guide. Failure to follow the

## instructions in this guide may result in an incorrect adjustment, which would

## appear as a hardware failure.

## The following table shows the assembly and components adjusted during each

## adjustment procedure.

Adjustment Assembly Component

Frequency reference A7 CPU A7 C85

Source A5 Analog A5 R48

A5 R59

ADC gain, offset and

reference

A5 Analog A5 R407

A5 R405

A5 R431

Input dc offset A1/A2 Input A1/A2 R39

A1/A2 R539

Common mode rejection A1/A2 Input A1/A2 R43

A1/A2 R543

Filter flatness A1/A2 Input A1/A2 R115

A1/A2 R235

A1/A2 R615

Display voltage A102 DC-DC Converter A102 R25

5-2


## Safety Considerations

Although the Agilent 35670A analyzer is designed in accordance with international

safety standards, this guide contains information, cautions, and warnings that must be

followed to ensure safe operation and to keep the unit in safe condition. Adjustments

in this chapter are performed with power applied and protective covers removed.

These adjustments must be performed by trained service personnel who are aware of

the hazards involved (such as fire and electrical shock).

Warning Any interruption of the protective (grounding) conductor inside or outside the

unit, or disconnection of the protective earth terminal can expose operators to

potentially dangerous voltages.

Under no circumstances should an operator remove any covers, screws, shields or

in any other way access the interior of the Agilent 35670A analyzer. There are no

operator controls inside the analyzer.

## Equipment Required

See chapter 1, ‘’Specifications,’’ for tables listing recommended test equipment. Any

equipment which meets the critical specifications given in the tables may be

substituted for the recommended model.

Agilent 35670A Adjusting the Analyzer

5-3


## Remote Operation

Adjustments can be set up using the remote operation capability of the

Agilent 35670A analyzer. The following table lists the adjustments and corresponding

GPIB codes. See the _Agilent 35670A GPIB Programmer’s Guide_ for general

information on remote operation.

Adjustment GPIB Code

Source DC Offset DIAG:SERV:ADJ:SOUR:OFFS

Source Filter DC Offset DIAG:SERV:ADJ:SOUR:FILT:OFF

S

ADC Second Pass Gain DIAG:SERV:ADJ:ADC:GAIN

ADC Offset DIAG:SERV:ADJ:ADC:OFFS

Channel 1 Offset DIAG:SERV:ADJ:OFFS1

Channel 2 Offset DIAG:SERV:ADJ:OFFS2

Channel 3 Offset (option AY6 only) DIAG:SERV:ADJ:OFFS3

Channel 4 Offset (option AY6 only) DIAG:SERV:ADJ:OFFS4

Channel 1 Common Mode Rejection DIAG:SERV:ADJ:CMRR1

Channel 2 Common Mode Rejection DIAG:SERV:ADJ:CMRR2

Channel 3 Common Mode Rejection (option AY6 only) DIAG:SERV:ADJ:CMRR3

Channel 4 Common Mode Rejection (option AY6 only) DIAG:SERV:ADJ:CMRR4

Channel 1 Flatness at 100 kHz DIAG:SERV:ADJ:FLAT1:FULL

Channel 1 Flatness at 50 kHz (option AY6 only) DIAG:SERV:ADJ:FLAT1:FULL

Channel 1 Flatness at 50 kHz DIAG:SERV:ADJ:FLAT1:CENT

Channel 1 Flatness at 25 kHz (option AY6 only) DIAG:SERV:ADJ:FLAT1:CENT

Channel 2 Flatness at 50 kHz DIAG:SERV:ADJ:FLAT2:FULL

Channel 2 Flatness at 25 kHz (option AY6 only) DIAG:SERV:ADJ:FLAT2:CENT

Channel 3 Flatness at 25 kHz (option AY6 only) DIAG:SERV:ADJ:FLAT3:FULL

Channel 4 Flatness at 25 kHz (option AY6 only) DIAG:SERV:ADJ:FLAT4:FULL

Preset SYST:PRES

Adjusting the Analyzer Agilent 35670A

5-4


To adjust the frequency reference

This procedure adjusts the 19.923 MHz (or, to be exact, 19.922944 MHz) frequency

reference circuit on the A7 CPU assembly. This circuit is the source of the timing

reference for the A1/A2 Input and A5 Analog assemblies.

Equipment Required: Frequency Counter

10:1 Oscilloscope Probe

- Set the power switch to off (O).
- Connect the counter to the 20 MHz test point on A7 using a 10:1 oscilloscope

probe. Attach the probe ground clip to the instrument chassis (ground).

- Set the power switch to on (I).
- Adjust A7 C85 for a counter reading of 19.922944 MHz ±200 Hz.

The analyzer may lock up if C85’s plates touch each other during the adjustment. If

the analyzer locks up, cycle power.

Agilent 35670A Adjusting the Analyzer

To adjust the frequency reference

5-5


To adjust the source

This procedure adjusts the source dc offset on the A5 Analog assembly.

Equipment Required: Multimeter

BNC-to-Dual Banana Cable

- Connect the multimeter to the analyzer’s rear-panel SOURCE connector.
- Press the following keys:

[System Utility]

[MORE]

[SERVICE TESTS]

[ADJUSTMTS]

[SOURCE ADJUSTMNT]

[DC OFFSET]

- Adjust A5 R48 for 0 Vdc±1 mV.
- Press the [FILTER DC OFFSET] softkey.
- Adjust A5 R59 for 0 Vdc ±1 mV.

Adjusting the Analyzer Agilent 35670A

To adjust the source

5-6


To adjust the ADC gain, offset and reference

This procedure adjusts the second-pass gain, the first-pass offset, and the reference

voltage for the ADC on the A5 Analog assembly. This prevents nonlinear

Analog-to-Digital Converter (ADC) operation near the Digital-to-Analog Converter

(DAC) transition levels.

Equipment Required: Oscilloscope

1:1 Oscilloscope Probe

Capacitive Load

BNC-to-BNC Cable

- Set the power switch to off (O).
- Connect the capacitive load (from the service kit) to the oscilloscope input.

Connect the 1:1 oscilloscope probe to the capacitive load. Attach the probe to

A5 TP400 and the probe ground clip to the instrument chassis.

- Connect the oscilloscope’s external trigger connector to the analyzer’s

SOURCE connector using a BNC cable.

Agilent 35670A Adjusting the Analyzer

To adjust the ADC gain, offset and reference

5-7


Artisan Technology Group is an independent supplier of quality pre-owned equipment

## Gold-standard solutions

```
Extend the life of your critical industrial,
```
```
commercial, and military systems with our
```
```
superior service and support.
```
## We buy equipment

```
Planning to upgrade your current
```
```
equipment? Have surplus equipment taking
```
```
up shelf space? We'll give it a new home.
```
## Learn more!

```
Visit us at artisantg.com for more info
```
```
on price quotes, drivers, technical
```
```
specifications, manuals, and documentation.
```
```
```
We're here to make your life easier. How can we help you today?

```
(217) 352-9330 I sales@artisantg.com I artisantg.com
```
