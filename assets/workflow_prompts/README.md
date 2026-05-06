# PyMeasure workflow prompts v6 — complete coherent numbering

This package contains a complete, numbered workflow for creating PyMeasure instrument drivers from manufacturer manuals and optional VISA-connected hardware.

The package is designed for repeatability, auditability, and minimal Human-in-the-Loop intervention. Codex should proceed automatically when artifacts pass their quality gates, and should request human action only when the report explicitly marks `HUMAN_REQUIRED: yes`.

## Start here

1. Read `00_PROMPT_SEQUENCE.md`.
2. Read `MODEL_SELECTION_AND_HARDWARE_ACCESS.md`.
3. Read `QUALITY_GATE_MATRIX.md`.
4. Use prompts from `prompts/` in numeric order.
5. Repeat `13_implementation_batch_template_prompt.md` and `14_verify_each_implementation_batch_quality_gate_prompt.md` for each subsystem batch.

## Compliance source

The package includes the upstream repository `AGENTS.md` snapshot in:

```text
reference/AGENTS_upstream_uploaded.md
```

All implementation prompts instruct Codex to follow repository `AGENTS.md` if present, including:

- Python 3.9+ compatibility,
- 100-character line length,
- PEP8 and PEP257,
- lowercase instrument filenames,
- instrument files under `pymeasure/instruments/<manufacturer>/`,
- tests under `tests/instruments/<manufacturer>/`,
- `_with_device.py` suffix for hardware/device tests,
- Sphinx docs under `docs/api/instruments/<manufacturer>/`,
- PyMeasure property creators: `control`, `measurement`, `setting`,
- `expected_protocol` / `ProtocolAdapter` protocol tests,
- `ChannelCreator` / `MultiChannelCreator` channel patterns,
- no public `get_*` or `set_*`,
- no `includeSCPI=True` in new SCPI drivers.

## Local artifacts not for PR

The following are local planning artifacts and must not be included in the final upstream PR:

```text
assets/
AGENTS.md
workflow_reports/
manual PDFs
local worklogs
temporary scripts
```

The final PR should contain only driver, test, and documentation files required by PyMeasure.
