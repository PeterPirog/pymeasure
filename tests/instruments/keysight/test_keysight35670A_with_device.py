#
# This file is part of the PyMeasure package.
#
# Copyright (c) 2013-2026 PyMeasure Developers
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#

# Call signature:
# $ pytest test_keysight35670A_with_device.py --device-address "GPIB0::14::INSTR"

import pytest

from pymeasure.instruments.keysight import Keysight35670A


def _system_error_code(reply):
    """Extract the integer code from a SYSTem:ERRor? reply."""
    token = str(reply).split(",", 1)[0].strip()
    return int(float(token))


def _drain_system_error_queue(analyzer, max_reads=32):
    """Drain and return non-zero system-error replies."""
    errors = []
    for _ in range(max_reads):
        reply = analyzer.system_error()
        if _system_error_code(reply) == 0:
            break
        errors.append(str(reply))
    return errors


def _assert_no_system_error(analyzer, max_reads=32):
    """Fail if the system error queue is not empty."""
    errors = _drain_system_error_queue(analyzer, max_reads=max_reads)
    if errors:
        pytest.fail(f"System error queue is not empty: {errors}")


@pytest.fixture(scope="module")
def analyzer(connected_device_address):
    instr = Keysight35670A(connected_device_address, timeout=20000)
    instr.source_output_enabled = False
    _drain_system_error_queue(instr)
    yield instr
    instr.source_output_enabled = False
    _assert_no_system_error(instr)
    adapter = getattr(instr, "adapter", None)
    if adapter is not None:
        try:
            adapter.close()
        except Exception:
            pass
        finally:
            if hasattr(adapter, "connection"):
                adapter.connection = None


@pytest.fixture(autouse=True)
def ensure_safe_state(analyzer):
    analyzer.source_output_enabled = False
    yield
    analyzer.source_output_enabled = False
    assert analyzer.source_output_enabled is False
    _assert_no_system_error(analyzer)


def test_hardware_id_options_system_version_and_system_error(analyzer):
    """Verify ID/options/system version/system error queries."""
    assert "35670A" in analyzer.id.upper()
    analyzer.check_id()
    assert isinstance(analyzer.options(), str)
    assert isinstance(analyzer.system_version, str)

    reply = analyzer.system_error()
    assert isinstance(reply, str)
    assert _system_error_code(reply) == 0


def test_hardware_status_condition_and_event_queries(analyzer):
    """Verify status condition/event query smoke tests."""
    assert isinstance(analyzer.operation_condition, int)
    assert isinstance(analyzer.operation_event, int)
    assert isinstance(analyzer.questionable_condition, int)
    assert isinstance(analyzer.questionable_event, int)
    assert isinstance(analyzer.device_condition, int)
    assert isinstance(analyzer.device_event, int)


def test_hardware_selected_instrument_mode_queries(analyzer):
    """Verify selected instrument mode queries."""
    assert isinstance(analyzer.instrument_mode, str)
    assert isinstance(analyzer.selected_instrument_number, int)


def test_hardware_input_ch1_coupling_roundtrip_and_autorange_query(analyzer):
    """Verify safe CH1 coupling roundtrip and autorange query."""
    original_coupling = analyzer.ch1.coupling
    target_coupling = "DC" if str(original_coupling).upper().startswith("AC") else "AC"

    try:
        analyzer.ch1.coupling = target_coupling
        assert str(analyzer.ch1.coupling).upper().startswith(target_coupling)
    finally:
        analyzer.ch1.coupling = original_coupling

    assert str(analyzer.ch1.coupling).upper().startswith(str(original_coupling).upper()[:2])
    assert isinstance(analyzer.ch1.autorange_enabled, bool)


def test_hardware_source_configuration_roundtrip(analyzer):
    """Verify safe source configuration roundtrip with output off."""
    analyzer.source_output_enabled = False
    analyzer.source_function = "sine"
    analyzer.source_frequency = 1000.0

    assert analyzer.source_function == "sine"
    assert analyzer.source_frequency == pytest.approx(1000.0, abs=1e-3, rel=1e-6)

    analyzer.source_output_enabled = False
    assert analyzer.source_output_enabled is False


def test_hardware_trace1_data_points_read_data_read_x_data_after_safe_fft_setup(analyzer):
    """Verify trace1 data queries after safe FFT setup."""
    original_data_format = analyzer.data_format
    analyzer.source_output_enabled = False
    analyzer.instrument_mode = "fft"
    analyzer.trace1.feed = "power_spectrum_ch1"
    analyzer.data_format = "ascii"

    try:
        analyzer.initiate()
        analyzer.wait_for_completion()

        points = analyzer.trace1.data_points()
        y_data = analyzer.trace1.read_data()
        x_data = analyzer.trace1.read_x_data()

        assert isinstance(points, int)
        assert points > 0
        assert isinstance(y_data, list)
        assert isinstance(x_data, list)
        assert len(y_data) > 0
        assert len(x_data) > 0
        assert isinstance(y_data[0], float)
        assert isinstance(x_data[0], float)
    finally:
        analyzer.source_output_enabled = False
        analyzer.data_format = original_data_format


def test_hardware_display_state_query_and_restore_display_on(analyzer):
    """Verify display state query and force display on at end."""
    assert isinstance(analyzer.display_enabled, bool)
    analyzer.display_enabled = True
    assert isinstance(analyzer.display_enabled, bool)


def test_hardware_trigger_and_tachometer_query_only(analyzer):
    """Verify trigger and tachometer query-only smoke tests."""
    assert isinstance(analyzer.trigger_source, str)
    assert isinstance(analyzer.trigger_slope, str)
    assert isinstance(analyzer.trigger_level, float)
    assert isinstance(analyzer.tachometer_range, str)
    assert isinstance(analyzer.tachometer_slope, str)
    assert isinstance(analyzer.tachometer_rpm, float)


def test_hardware_memory_catalog_and_free_query_only(analyzer):
    """Verify memory catalog/free query-only smoke tests."""
    assert isinstance(analyzer.memory_catalog(), str)
    assert isinstance(analyzer.memory_free(), str)


def test_hardware_format_data_query_only(analyzer):
    """Verify format data query-only smoke test."""
    assert analyzer.data_format in {"ascii", "real"}


def test_hardware_power_source_query_only(analyzer):
    """Verify power source query-only smoke test."""
    assert isinstance(analyzer.power_source, str)
