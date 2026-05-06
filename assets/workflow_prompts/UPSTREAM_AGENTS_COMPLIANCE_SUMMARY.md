# Upstream AGENTS.md integration

The uploaded PyMeasure `AGENTS.md` has been integrated into the workflow prompts.

Key rules carried into prompts:

- Python 3.9+ compatibility.
- Line length 100 characters.
- PEP8 and PEP257.
- Instrument modules use lowercase filenames.
- Instrument drivers live under manufacturer packages.
- Manufacturer `__init__.py` must export new classes.
- Protocol tests use `expected_protocol` / `ProtocolAdapter`.
- Hardware tests use `_with_device.py` suffix and skip without device address.
- Prefer `control`, `measurement`, and `setting` property creators.
- Public getter/setter functions are discouraged.
- Use validators and `map_values=True` when appropriate.
- Use `ChannelCreator` under 16 channels and `MultiChannelCreator` above 16 channels unless justified.
- Documentation uses Sphinx/RST and imperative docstrings.
