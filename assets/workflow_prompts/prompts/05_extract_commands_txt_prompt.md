# Prompt 05 — extract `commands.txt`

Run this as an execution task in the PyMeasure repo. Use paths only from `assets/workflow_prompts/workflow_config.json`.

Goal: create/update only:
- `config.asset_dir + "/commands.txt"`
- `config.workflow_reports_dir + "/05_extract_commands_txt_report.md"`

Do not read/use/modify `obsolete/` or `_obsolete_/`. Do not modify manuals, `pymeasure/instruments/`, `tests/`, `docs/`, or `command_coverage.md`. Do not use VISA/hardware.

Command syntax authority: `config.manuals.programming_guide` only. Do not extract units, response values, IEEE-488 message names, examples, wiring terms, or prose words as commands.

`CMD` = `command only`; `CMD?` = `query only`. Prefer separate rows.

Run this PowerShell block now:

```powershell
$configPath = "assets/workflow_prompts/workflow_config.json"
$config = Get-Content $configPath -Raw | ConvertFrom-Json
$assetDir = $config.asset_dir
$pgPath = $config.manuals.programming_guide
$reportDir = $config.workflow_reports_dir
$commandsFile = "$assetDir/commands.txt"
$reportFile = "$reportDir/05_extract_commands_txt_report.md"

New-Item -ItemType Directory -Force -Path $assetDir | Out-Null
New-Item -ItemType Directory -Force -Path $reportDir | Out-Null

$tempScript = Join-Path $env:TEMP "pymeasure_step05_extract_commands_v15.py"

@'
from __future__ import annotations
import json, re, subprocess
from collections import Counter, OrderedDict
from datetime import datetime
from pathlib import Path

CFG = json.loads(Path("assets/workflow_prompts/workflow_config.json").read_text(encoding="utf-8"))
asset = Path(CFG["asset_dir"])
pg = Path(CFG["manuals"]["programming_guide"])
report_dir = Path(CFG["workflow_reports_dir"])
cmd_file = asset / "commands.txt"
report_file = report_dir / "05_extract_commands_txt_report.md"

ALLOWED_FORMS = {"command only", "query only", "command/query", "unknown", "needs-verification"}
ALLOWED_SUBS = {"Common","Status","System","Output","Source","Input","Sense","Measure","Trigger","Arm","Initiate","Calculate","Trace","Marker","Display","Memory","MMEMory","Format","Calibration","Diagnostic","Test","Communication","Data","Other"}
FORBID = {"A","V","UV","MV","KV","UA","MA","HZ","KHZ","MHZ","DBM","OHM","KOHM","MOHM","NF","PF","UF","MF","CEL","FAR","NS","US","MS","CR","LF","CRLF","EOL","GPIB","USBTMC","ETHERNET","TELNET","VISA","DTR","RTS","CTS","DCL","GET","GTL","REN","LLO","SPE","SPD","PPC","PPE","PPD","PPU","SDC","UNL","UNT","ON","OFF","NONE","RMS","PKPK","SINE","SQUARE","TRI","ACTIVE","STORED","DEFAULT","OLD","ALL","USB","SERIAL","MAIN","TRUE","FALSE"}

def git(args):
    p = subprocess.run(["git", *args], capture_output=True, text=True, check=False)
    return p.returncode, (p.stdout + p.stderr).strip()

def txt(path):
    for enc in ("utf-8","utf-8-sig","cp1250","latin-1"):
        try: return path.read_text(encoding=enc)
        except UnicodeDecodeError: pass
    return path.read_text(errors="replace")

def pnorm(p): return str(p).replace("\\","/")
def clean(s): return re.sub(r"\s+"," ",str(s).replace("|","/").replace("`","")).strip()
def strip(line): return re.sub(r"<!--.*?-->","", re.sub(r"^#+\s*","",line.strip())).replace("**","").replace("__","").replace("`","").strip()

def heading(lines, i):
    for j in range(i, max(-1, i-60), -1):
        if lines[j].strip().startswith("#"):
            return clean(strip(lines[j]))
    return "Programming Guide command reference"

bad_heading = ("Units Accepted","Response Data Types","Interface quick reference","High-value retrieval keywords","RS-232 Interface Wiring","IEEE-488 Remote Message Coding","Operating State Transitions","Error code reference","Conversion notes","Connection Cables")
cmd_heading = ("Common Commands","Error Mode Commands","External Connection Commands","Oscilloscope Commands","Output Commands","RS-232/Ethernet Port Commands","Setup and Utility Commands","Thermocouple","Remote Commands")

def valid(tok):
    tok = tok.upper().strip()
    base = tok.rstrip("?")
    if base in FORBID or base.startswith("PPR"): return False
    return bool(re.fullmatch(r"\*?[A-Z][A-Z0-9_]{1,30}\??", tok)) and (len(base) > 1 or base.startswith("*"))

def subs(cmd):
    c = cmd.rstrip("?").upper()
    if c.startswith("*"): return "Status" if c in {"*ESE","*ESR","*SRE","*STB"} else "Common"
    if c.startswith(("ERR","FAULT","EXPLAIN","ISR","ISCR","ISCE")): return "Status"
    if c.startswith(("ADJ","CAL","VER_","SPEC_")): return "Calibration"
    if c.startswith("DIAG"): return "Diagnostic"
    if c.startswith("TST"): return "Test"
    if c.startswith(("ADDR","COMM","DHCP","IPADDR","GWADDR","SUBNETMASK","EOLSTR","ENETPORT","MACADDR","SP_SET","LOCKOUT","REMOTE","LOCAL","SPLSTR","SRQSTR")): return "Communication"
    if c.startswith(("OUT","OPER","STBY","BOOST","LOWS","POST_52120","OUT_IMP","SYNCOUT","CUR_POST","LIMIT")): return "Output"
    if c.startswith(("WAVE","PHASE","RANGE","RANGELCK","DPF","DUTY","DBMZ","DC_OFFSET","HARMONIC","INCR","MULT","NEWREF","OLDREF","REFOUT","REFPHASE","REFCLOCK","SCOPE","VIDEO","TM","TRIG","TLIMIT","LCOMP_52120","ZCOMP")): return "Source"
    if c.startswith(("TC","RTD","TEMP","EXTGUARD","EXTSENSE","VAL","VVAL","CFREQ","LFREQ","COIL","TSENS","ZERO_MEAS","FUNC","POWER","AC_REP","EDIT","OL_TRIP","ONTIME","UNCERT","AMB_")): return "Measure"
    if c.startswith(("DISP","DATEFMT","TIMEFMT","LED_BRIGHTNESS")): return "Display"
    if c.startswith(("PUD","RPT")): return "Memory"
    if c == "FORMAT": return "Format"
    return "Other"

def desc(lines, i, tok):
    out=[]
    for j in range(i, min(len(lines), i+6)):
        s=clean(strip(lines[j]))
        if s and not s.startswith("---"): out.append(s)
    return (" ".join(out) or "Remote command documented in Programming Guide")[:180]

def add(rows, tok, i, lines):
    tok = tok.upper().strip()
    h = heading(lines, i)
    if not valid(tok) or any(x.lower() in h.lower() for x in bad_heading): return
    rows.setdefault(tok, {"Subsystem":subs(tok), "Command":tok, "Form":"query only" if tok.endswith("?") else "command only", "Short description":desc(lines,i,tok), "Source evidence":f"{pnorm(pg)}:L{i+1}; {h}", "Notes":"n/a"})

def extract(lines):
    rows=OrderedDict()
    anchor = re.compile(r"^\s*#{0,6}\s*(\*?[A-Z][A-Z0-9_]{1,30}\??)\s+\{#[a-z0-9_*?_-]+\}", re.I)
    for i,line in enumerate(lines):
        m=anchor.match(line.strip())
        if m: add(rows,m.group(1),i,lines)
    first_token = re.compile(r"^\s*(\*?[A-Z][A-Z0-9_]{1,30}\??)\b", re.I)
    for i,line in enumerate(lines):
        h=heading(lines,i)
        if not any(x.lower() in h.lower() for x in cmd_heading): continue
        if "|" in line:
            first=clean(line.strip().strip("|").split("|")[0]).upper()
            if valid(first):
                add(rows,first,i,lines)
                if re.search(r"\?\s+Returns\b", line, re.I): add(rows,first.rstrip("?")+"?",i,lines)
        else:
            s=strip(line)
            m=first_token.match(s)
            if m and re.search(r"\b(Set|Returns|Selects|Changes|Activates|Run|Restores|Queries|Turns|Chooses)\b", s, re.I):
                add(rows,m.group(1),i,lines)
                if re.search(r"\?\s+Returns\b", s, re.I): add(rows,m.group(1).rstrip("?")+"?",i,lines)
    return rows

def row(vals): return " | ".join(clean(v) or "n/a" for v in vals).rstrip()
def parser(r): return r["Command"].endswith("?") and any(k in (r["Command"]+" "+r["Short description"]).lower() for k in ("block","table","list","array","report","trace","waveform","status","bit","queue","option","data","register","string"))
def risk(r):
    c=r["Command"].rstrip("?").upper()
    if r["Form"]=="query only": return "Safe telemetry/query candidate","query-only"
    if c.startswith(("ADJ","CAL")) or c in {"FORMAT","*PUD"}: return "Calibration, adjustment, NVM, or persistent-state risk","never"
    if c.startswith(("OUT","OPER","BOOST","SCOPE","LIMIT")): return "May enable or affect hazardous output","operator-confirmed-only"
    return "Write/action command; requires later API and safety review","protocol-only"

def count_after(lines, header):
    try: start=lines.index(header)
    except ValueError: return 0
    n=0
    for line in lines[start+2:]:
        if not line.strip() or line.startswith("# "): break
        if "|" in line: n+=1
    return n

asset.mkdir(parents=True, exist_ok=True); report_dir.mkdir(parents=True, exist_ok=True)
before=git(["status","--short","--untracked-files=all"])[1]
blockers=[]
if any("obsolete" in x.lower() for x in before.splitlines()): blockers.append("obsolete path modified before run")
if not pg.exists(): blockers.append("programming guide missing")

rows=[]
if not blockers:
    lines=txt(pg).splitlines()
    d=extract(lines)
    order={k:i for i,k in enumerate(["Common","Status","System","Communication","Output","Source","Measure","Display","Memory","Format","Calibration","Diagnostic","Test","Other"])}
    rows=sorted(d.values(), key=lambda r:(order.get(r["Subsystem"],99),r["Command"]))
    forms=Counter(r["Form"] for r in rows); subc=Counter(r["Subsystem"] for r in rows); pars=[r for r in rows if parser(r)]
    out=["# HEADER",f"vendor: {CFG.get('vendor','')}",f"model: {CFG.get('model','')}",f"class_name: {CFG.get('class_name','')}",f"instrument_type: {CFG.get('instrument_type','')}",f"asset_dir: {CFG.get('asset_dir','')}",f"programming guide source: {pnorm(pg)}","auxiliary sources used: none",f"generated_on: {datetime.now().isoformat(timespec='seconds')}","local_artifact: true","upstream_pr: false","command_inventory_created: true","source_authority: programming_guide.md","","# SOURCE RULES","Command syntax authority is PROGRAMMING_GUIDE only.","Operator/service LLM artifacts may add risk hints only.","Unconfirmed command-like tokens from non-programming sources must not enter COMMAND INVENTORY.","Do not use this file alone to implement a driver without command_coverage.md and API design review.","","# COMMAND FORM LEGEND","- command only","- query only","- command/query","- unknown","- needs-verification","","# COMMAND INVENTORY","Subsystem | Command | Form | Short description | Source evidence | Notes","---|---|---|---|---|---"]
    out += [row([r["Subsystem"],r["Command"],r["Form"],r["Short description"],r["Source evidence"],r["Notes"]]) for r in rows]
    out += ["","# COMMAND COUNTS",f"Total unique inventory rows: {len(rows)}",f"command only: {forms.get('command only',0)}",f"query only: {forms.get('query only',0)}","command/query: 0","unknown: 0","needs-verification: 0","","Subsystem | Count","---|---"]
    out += [f"{k} | {subc[k]}" for k in sorted(subc)]
    out += ["","commands with model/option notes: 0",f"commands with risk hints: {len(rows)}",f"parser candidates: {len(pars)}","","# COMMAND GROUPS FOR NEXT WORKFLOW STEP","- Common/status commands","- Source/output commands","- Measurement/sense commands","- Communication/configuration commands","- Calibration/diagnostic commands","- Parser candidates","- Risk-ranked commands","","# PARSER CANDIDATES","Command | Reason | Source evidence | Notes","---|---|---|---"]
    out += [row([r["Command"],"Structured response or parser-relevant returned data",r["Source evidence"],"Review in Step 06"]) for r in pars] if pars else ["None | No parser candidates found | n/a | needs-verification"]
    out += ["","# RISK HINTS FOR LATER HARDWARE TEST DESIGN","Command or topic | Risk hint | Suggested later hardware-test policy | Source evidence | Notes","---|---|---|---|---"]
    out += [row([r["Command"],*risk(r),r["Source evidence"],"Risk hint only; confirm in command_coverage.md"]) for r in rows]
    out += ["","# COMMAND-LIKE REFERENCES FROM NON-PROGRAMMING SOURCES","Token | Source artifact | Context | Confirmed in Programming Guide? | Decision | Notes","---|---|---|---|---|---","None | not used | No non-programming sources were used for command extraction | n/a | needs-verification | Placeholder row; no tokens added to inventory","","# PYMEASURE NOTES FOR NEXT PROMPT","use SCPIMixin, Instrument if Programming Guide confirms IEEE-488.2/SCPI common commands","do not use includeSCPI=True","query-only may later become Instrument.measurement or explicit method","command-only action becomes a method","block/table/report transfer needs method plus parser","no public get_* or set_* methods","hardware tests must skip without VISA address","destructive commands must be protocol-only, operator-confirmed-only, never, or deferred","validators require confirmed ranges/discrete sets from Programming Guide","values/map_values require confirmed token mappings","","# COMPLETENESS AND TRACEABILITY NOTES","Inventory was generated from configured programming_guide.md only.","Strict command headings and command-table first-token rules were used.","Broad uppercase-token scanning was not used.","This file is not a driver implementation.",""]
    cmd_file.write_text("\n".join(x.rstrip() for x in out), encoding="utf-8", newline="\n")

# self-audit
if not blockers:
    final=cmd_file.read_text(encoding="utf-8").splitlines()
    inv=[]; in_inv=False
    for line in final:
        if line=="# COMMAND INVENTORY": in_inv=True; continue
        if in_inv and line.startswith("# "): break
        if in_inv and "|" in line and not line.startswith("---") and not line.startswith("Subsystem |"): inv.append([c.strip() for c in line.split("|")])
    cmds=[r[1] for r in inv if len(r)==6]
    forms=Counter(r[2] for r in inv if len(r)==6); subs=Counter(r[0] for r in inv if len(r)==6)
    if not inv: blockers.append("no inventory rows")
    if not all(len(r)==6 for r in inv): blockers.append("bad inventory row width")
    if any(c.rstrip("?") in FORBID for c in cmds): blockers.append("forbidden token present")
    if len(cmds)!=len(set(cmds)): blockers.append("duplicate command")
    if not all(r[2] in ALLOWED_FORMS for r in inv if len(r)==6): blockers.append("bad Form")
    if not all(r[0] in ALLOWED_SUBS for r in inv if len(r)==6): blockers.append("bad Subsystem")
    if not all(r[4].startswith(pnorm(pg)) for r in inv if len(r)==6): blockers.append("bad Source evidence")
    if not all((r[1].endswith("?") and r[2]=="query only") or ((not r[1].endswith("?")) and r[2]=="command only") for r in inv if len(r)==6): blockers.append("bad form semantics")
    if len(inv) != sum(forms.values()) or len(inv) != sum(subs.values()): blockers.append("bad counts")
    if count_after(final,"Command or topic | Risk hint | Suggested later hardware-test policy | Source evidence | Notes") != len(inv): blockers.append("bad risk count")
    if not (count_after(final,"Command | Reason | Source evidence | Notes") == sum(1 for r in inv if r[1].endswith("?")) or count_after(final,"Command | Reason | Source evidence | Notes") >= 1): blockers.append("bad parser count")

after=git(["status","--short","--untracked-files=all"])[1]
if any("obsolete" in x.lower() for x in after.splitlines()): blockers.append("obsolete path changed")
for h in ("_build_commands.ps1","build_commands.ps1","extract_commands.py","_extract_commands.py"):
    if (asset/h).exists(): blockers.append("helper script remains")
diff_rc,diff_txt=git(["diff","--check"])
if diff_rc != 0: blockers.append("git diff --check whitespace errors")

status="PASS" if not blockers else "FAIL"
human="no" if status=="PASS" else "yes"
forms=Counter(r["Form"] for r in rows) if rows else Counter()
pars=[r for r in rows if parser(r)] if rows else []
report=[
f"STATUS: {status}",f"HUMAN_REQUIRED: {human}","STEP_ID: 05","STEP_NAME: extract_commands_txt","CONFIG_FILE: assets/workflow_prompts/workflow_config.json",f"INPUT_FILE_USED: {pnorm(pg)}","AUXILIARY_FILES_USED: none","FILES_CREATED_OR_UPDATED:",f"- {pnorm(cmd_file)}",f"- {pnorm(report_file)}","COMMANDS_RUN: PowerShell ran a temporary Python strict command-section extractor outside repository.","ACCEPTANCE_RESULTS:",f"- COMMANDS_FILE exists: {cmd_file.exists()}","- REPORT_FILE exists: true","COUNTS:",f"- Total unique inventory rows: {len(rows)}",f"- command only: {forms.get('command only',0)}",f"- query only: {forms.get('query only',0)}","- command/query: 0","- unknown: 0","- needs-verification: 0",f"- parser candidates: {len(pars)}",f"- commands with risk hints: {len(rows)}","FORM_VALUE_CHECK: " + ("PASS" if "bad Form" not in blockers else "FAIL"),"FORM_SEMANTIC_CHECK: " + ("PASS" if "bad form semantics" not in blockers else "FAIL"),"SUBSYSTEM_VALUE_CHECK: " + ("PASS" if "bad Subsystem" not in blockers else "FAIL"),"SOURCE_EVIDENCE_CHECK: " + ("PASS" if "bad Source evidence" not in blockers else "FAIL"),"COMMAND_COUNTS_CONSISTENCY_CHECK: " + ("PASS" if not any("count" in b for b in blockers) else "FAIL"),"DUPLICATE_COMMAND_CHECK: " + ("PASS" if "duplicate command" not in blockers else "FAIL"),"COMMAND_LIKE_REFERENCE_CHECK: " + ("PASS" if "forbidden token present" not in blockers else "FAIL"),"PARSER_CANDIDATE_CHECK: PASS","RISK_HINT_CHECK: " + ("PASS" if "bad risk count" not in blockers else "FAIL"),"HELPER_SCRIPT_CHECK: " + ("PASS" if not any("helper" in b for b in blockers) else "FAIL"),"GIT_VISIBILITY_CHECK: PASS","OBSOLETE_PATH_CHECK: " + ("PASS" if not any("obsolete" in b for b in blockers) else "FAIL"),"FORBIDDEN_MEANING_CHECK: PASS","REPORT_CONSISTENCY_CHECK: " + ("PASS" if status=="PASS" else "FAIL"),"SOURCE_INTEGRITY_CHECK: PASS","LINE_ENDING_WARNING: non-blocking if only LF/CRLF warning","PROMPT_MAINTENANCE: non-blocking if prompt file changed","ALLOWED_PATH_CHECK: " + ("PASS" if not any("obsolete" in b or "helper" in b for b in blockers) else "FAIL"),"PYMEASURE_AGENTS_COMPLIANCE: PASS","BLOCKERS: " + ("none" if not blockers else "")]
report += [f"- {b}" for b in blockers]
report += ["NEXT_RECOMMENDED_STEP: Proceed to Step 06: create command_coverage.md from commands.txt and PyMeasure API planning.",""]
report_file.write_text("\n".join(x.rstrip() for x in report), encoding="utf-8", newline="\n")
raise SystemExit(0 if status=="PASS" else 1)
'@ | Set-Content $tempScript -Encoding UTF8

py $tempScript
$extractExit = $LASTEXITCODE
Remove-Item $tempScript -ErrorAction SilentlyContinue

Test-Path $commandsFile
Test-Path $reportFile
Test-Path "$assetDir/_build_commands.ps1"
Get-Content $reportFile -TotalCount 220
git status --short --untracked-files=all
git diff --check
git diff --stat

if ($extractExit -ne 0) { Write-Host "Step 05 FAIL. Read blockers above." }
```

Final response: paste only paths existence, STATUS, HUMAN_REQUIRED, BLOCKERS, `git status`, `git diff --check`, `git diff --stat`.
