# Codex worklog template

Instrument: `<vendor> <model>`  
Branch: `dev/<vendor>-<model>`  
Local repo: `<path>`  
Device address: `<VISA address if available>`  
Operator: `<name or initials>`

## Session log

### Session 001 — `<YYYY-MM-DD HH:MM>`

#### Goal

```text
<What Codex was asked to do>
```

#### Prompt sent to Codex

```text
<Paste exact prompt here>
```

#### Files changed

```text
<Paste git diff --stat here>
```

#### Commands run

```powershell
python -m pytest tests/instruments/<vendor>/test_<model>.py -q
git diff --check
git diff --stat
```

#### Test output

```text
<Paste full output here>
```

#### First traceback, if any

```text
<Paste first traceback here>
```

#### Hardware test output, if any

```powershell
python -m pytest tests/instruments/<vendor>/test_<model>_with_device.py --device-address "<VISA_ADDRESS>" -q -s
```

```text
<Paste full hardware test output here>
```

#### Instrument diagnostics

```text
*IDN?:
<response>

*OPT?:
<response>

SYSTem:ERRor?:
<response(s)>
```

#### Safety state after test

```text
Source/output disabled: yes/no/not applicable
Instrument error queue clear: yes/no/unknown
Unexpected front panel state: yes/no
```

#### Architect review notes

```text
<What should be checked or fixed next>
```

---

## Reusable diagnostic commands

### Git state

```powershell
git branch --show-current
git status --short
git diff --check
git diff --stat
```

### Protocol tests

```powershell
python -m pytest tests/instruments/<vendor>/test_<model>.py -q
```

### Hardware tests

```powershell
python -m pytest tests/instruments/<vendor>/test_<model>_with_device.py --device-address "<VISA_ADDRESS>" -q -s
```

### Import check

```powershell
python -c "from pymeasure.instruments.<vendor> import <ClassName>; print(<ClassName>)"
```

## Known hardware notes

```text
- VISA backend:
- GPIB controller:
- Device address:
- Firmware:
- Options:
- Required timeout:
- Termination quirks:
- Known slow commands:
- Known unsafe commands:
```
