# 16 — Operator report template

## DLA CZŁOWIEKA

Po każdym uruchomieniu promptu wklej taki raport do Chata/Architekta. Dzięki temu następny prompt można zawęzić do realnego stanu repozytorium i sprzętu.

```text
PROMPT RUN:
<file name / prompt number>

REPO:
<branch>
<git status --short>

TESTS:
<pytest output>

DIFF:
<git diff --check output>
<git diff --stat output>

COVERAGE CHANGES:
<fragment command_coverage.md / service_coverage.md>

HARDWARE, jeśli dotyczy:
DEVICE_ADDRESS:
<IDN response>
<error queue response>
<final safety state>

PROBLEMS:
<first traceback or unexpected response>

QUESTION FOR ARCHITECT:
<what should be decided next>
```
