# 02 — Ekstrakcja commands.txt

## DLA CZŁOWIEKA — co robi ten prompt

Ten prompt tworzy audytowalny plik `commands.txt` z pełnym spisem komend zdalnych.

To jest najważniejszy krok przed coverage. Składnia komend ma pochodzić wyłącznie z `programming_guide.md`. `service_manual.md` może dodać tylko ogólne wskazówki ryzyka, ale nie może wprowadzać nowych komend.

Nie implementuje kodu i nie dotyka sprzętu.

## PROMPT DO CODEXA

Przed tym promptem wklej uzupełniony blok `SOURCE DATA FOR CODEX` z pliku `00_PROJECT_CONTEXT_TEMPLATE.md`.

```text
Goal: create COMMANDS_TXT as an audit-friendly inventory of all remote-control commands found in PROGRAMMING_GUIDE. Do not implement a driver.

Rules:
1. Read PROGRAMMING_GUIDE.
2. If SERVICE_MANUAL exists, use it only for general safety/risk hints. Do not extract command syntax from it.
3. Extract commands from:
   - command index,
   - command summary,
   - table of contents command entries,
   - detailed command reference sections,
   - common commands,
   - subsystem command sections,
   - appendices containing command lists.
4. The detailed command reference has higher authority than a summary or table of contents.
5. Preserve manufacturer notation:
   - SCPI uppercase/lowercase notation,
   - query marks `?`,
   - optional nodes such as `[:STATe]`,
   - index notation such as `[1|2|3|4]`,
   - optional subsystem prefixes,
   - command/query variants.
6. Do not guess command forms.
7. If a command form is unclear because of OCR, formatting, duplication, or conflicting text, mark it as `needs-verification`.

Create COMMANDS_TXT with these sections:
1. Metadata
2. Source rules
3. Interface summary
4. Command form legend
5. Command inventory

The command inventory table must have exactly these columns:
Subsystem | Command | Form | Short description | Source evidence | Notes

Allowed Form values:
- command only
- query only
- command/query
- unknown
- needs-verification

Add these sections after the inventory:
- Command counts
- Counts per subsystem
- Command groups for next workflow step
- Parser candidates
- Risk hints for later hardware test design
- PyMeasure notes for next prompt

Modification scope:
- Modify only COMMANDS_TXT.
- Do not create COMMAND_COVERAGE.
- Do not modify driver, tests, or docs.
- Do not use VISA.

Run:
git status --short
git diff --check
git diff --stat

Report:
- total unique commands,
- command only count,
- query only count,
- command/query count,
- parser candidates count,
- risky/unsafe hints count,
- needs-verification count.
```
