# Keysight35670A Command Coverage Matrix

Auto-audit source files:
- `assets/keysight/keysight35670A/commands Keysight 35670A.txt`
- `pymeasure/instruments/keysight/keysight35670A.py`
- `tests/instruments/keysight/test_keysight35670A.py`
- `tests/instruments/keysight/test_keysight35670A_with_device.py`

Total command rows: **430**
Implemented count: **430**
Not exposed count: **0**
Partial/block-transfer count: **14**
Hardware-tested count: **52**
Destructive/manual-only count: **0**
Missing count: **0**

| Subsystem | Command | Form | Implemented | API exposure | API name | Class | Risk | Test type | Notes |
|---|---|---|---|---|---|---|---|---|---|
| Common Commands | `*CAL?` | query only | yes | yes | `calibration_result` | SCPIMixin / Keysight35670A | long-running | expected_protocol | Implemented in driver. |
| Common Commands | `*CLS` | command only | yes | yes | `clear` | SCPIMixin / Keysight35670A | state-changing | no-hardware-test | Implemented in driver. |
| Common Commands | `*ESE` | command/query | yes | yes | `event_status_enable` | SCPIMixin / Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| Common Commands | `*ESR?` | query only | yes | yes | `standard_event_status` | SCPIMixin / Keysight35670A | safe | expected_protocol | Implemented in driver. |
| Common Commands | `*IDN?` | query only | yes | yes | `id` | SCPIMixin / Keysight35670A | safe | expected_protocol | Implemented in driver. |
| Common Commands | `*OPC` | command/query | yes | yes | `operation_complete()` | SCPIMixin / Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| Common Commands | `*OPT?` | query only | yes | yes | `_installed_options, options()/_installed_options` | SCPIMixin / Keysight35670A | safe | expected_protocol | Implemented in driver. |
| Common Commands | `*PCB` | command only | yes | yes | `not exposed` | SCPIMixin / Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| Common Commands | `*PSC` | command/query | yes | yes | `power_on_status_clear` | SCPIMixin / Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| Common Commands | `*RST` | command only | yes | yes | `reset` | SCPIMixin / Keysight35670A | state-changing | no-hardware-test | Implemented in driver. |
| Common Commands | `*SRE` | command/query | yes | yes | `service_request_enable` | SCPIMixin / Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| Common Commands | `*STB?` | query only | yes | yes | `status_byte` | SCPIMixin / Keysight35670A | safe | expected_protocol | Implemented in driver. |
| Common Commands | `*TRG` | command only | yes | yes | `trigger(), trigger()/trigger` | SCPIMixin / Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| Common Commands | `*TST?` | query only | yes | yes | `self_test_result` | SCPIMixin / Keysight35670A | safe | expected_protocol | Implemented in driver. |
| Common Commands | `*WAI` | command only | yes | yes | `wait()` | SCPIMixin / Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| ABORt | `ABORt` | command only | yes | yes | `abort_curve_fit(), abort_time_capture(), restart_measurement()` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| ARM | `ARM[:IMMediate]` | command only | yes | yes | `arm(), arm_rpm_increment, arm_rpm_mode, arm_rpm_threshold, arm_source, ...` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| ARM | `ARM:RPM:INCRement` | command/query | yes | yes | `arm_rpm_increment` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| ARM | `ARM:RPM:MODE` | command/query | yes | yes | `arm_rpm_mode` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| ARM | `ARM:RPM:THReshold` | command/query | yes | yes | `arm_rpm_threshold` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| ARM | `ARM:SOURce` | command/query | yes | yes | `arm_source` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| ARM | `ARM:TIMer` | command/query | yes | yes | `arm_timer` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:ACTive` | command/query | yes | yes | `active` | Keysight35670ATrace | option-dependent | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:CFIT:ABORt` | command only | yes | yes | `abort_curve_fit()` | Keysight35670ATrace | long-running | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:CFIT:COPY` | command only | yes | yes | `copy_synthesis_to_curve_fit()` | Keysight35670ATrace | long-running | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:CFIT:DATA` | command/query | yes | yes | `cfit_data()` | Keysight35670ATrace | long-running | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:CFIT:DESTination` | command/query | yes | yes | `cfit_destination_register` | Keysight35670ATrace | long-running | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:CFIT:FREQuency[:AUTO]` | command/query | yes | yes | `cfit_frequency_auto_enabled, cfit_frequency_start, cfit_frequency_stop` | Keysight35670ATrace | long-running | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:CFIT:FREQuency:STARt` | command/query | yes | yes | `cfit_frequency_start` | Keysight35670ATrace | long-running | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:CFIT:FREQuency:STOP` | command/query | yes | yes | `cfit_frequency_stop` | Keysight35670ATrace | long-running | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:CFIT:FSCale` | command/query | yes | yes | `cfit_frequency_scale` | Keysight35670ATrace | long-running | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:CFIT[:IMMediate]` | command only | yes | yes | `abort_curve_fit(), cfit_data(), cfit_destination_register, cfit_frequency_auto_enabled, cfit_frequency_scale, ...` | Keysight35670ATrace | long-running | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:CFIT:ORDer:AUTO` | command/query | yes | yes | `cfit_order_auto_enabled` | Keysight35670ATrace | long-running | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:CFIT:ORDer:POLes` | command/query | yes | yes | `cfit_order_poles` | Keysight35670ATrace | long-running | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:CFIT:ORDer:ZERos` | command/query | yes | yes | `cfit_order_zeros` | Keysight35670ATrace | long-running | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:CFIT:TDELay` | command/query | yes | yes | `cfit_time_delay` | Keysight35670ATrace | long-running | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:CFIT:WEIGht:AUTO` | command/query | yes | yes | `cfit_weight_auto_enabled` | Keysight35670ATrace | long-running | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:CFIT:WEIGht:REGister` | command/query | yes | yes | `cfit_weight_register` | Keysight35670ATrace | long-running | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:DATA?` | query only | yes | yes | `cfit_data(), data_points(), math_data(), read_data(), read_lower_limit_report_x(), ...` | Keysight35670ATrace | binary-or-block-transfer | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:DATA:HEADer:POINts` | query only | yes | yes | `data_points()` | Keysight35670ATrace | binary-or-block-transfer | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:FEED` | command/query | yes | yes | `feed` | Keysight35670ATrace | option-dependent | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:FORMat` | command/query | yes | yes | `display_format` | Keysight35670ATrace | option-dependent | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:GDAPerture:APERture` | command/query | yes | yes | `group_delay_aperture` | Keysight35670ATrace | option-dependent | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:LIMit:BEEP[:STATe]` | command/query | yes | yes | `limit_beeper_enabled` | Keysight35670ATrace | option-dependent | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:LIMit:FAIL?` | query only | yes | yes | `limit_failed` | Keysight35670ATrace | option-dependent | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:LIMit:LOWer:CLEar[:IMMediate]` | command only | yes | yes | `clear_lower_limit()` | Keysight35670ATrace | option-dependent | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:LIMit:LOWer:MOVE:Y` | command only | yes | yes | `not exposed` | Keysight35670ATrace | option-dependent | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:LIMit:LOWer:REPort[:DATA]?` | query only | yes | yes | `read_lower_limit_report_x(), read_lower_limit_report_y()` | Keysight35670ATrace | binary-or-block-transfer | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:LIMit:LOWer:REPort:YDATa?` | query only | yes | yes | `read_lower_limit_report_y()` | Keysight35670ATrace | option-dependent | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:LIMit:LOWer:SEGMent` | command/query | yes | yes | `lower_limit_segment` | Keysight35670ATrace | option-dependent | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:LIMit:LOWer:SEGMent:CLEar` | command only | yes | yes | `not exposed` | Keysight35670ATrace | option-dependent | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:LIMit:LOWer:TRACe[:IMMediate]` | command only | yes | yes | `make_lower_limit_from_trace()` | Keysight35670ATrace | option-dependent | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:LIMit:STATe` | command/query | yes | yes | `limit_beeper_enabled, limit_enabled` | Keysight35670ATrace | option-dependent | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:LIMit:UPPer:CLEar[:IMMediate]` | command only | yes | yes | `clear_upper_limit()` | Keysight35670ATrace | option-dependent | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:LIMit:UPPer:MOVE:Y` | command only | yes | yes | `not exposed` | Keysight35670ATrace | option-dependent | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:LIMit:UPPer:REPort[:DATA]?` | query only | yes | yes | `read_upper_limit_report_x(), read_upper_limit_report_y()` | Keysight35670ATrace | binary-or-block-transfer | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:LIMit:UPPer:REPort:YDATa?` | query only | yes | yes | `read_upper_limit_report_y()` | Keysight35670ATrace | option-dependent | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:LIMit:UPPer:SEGMent` | command/query | yes | yes | `upper_limit_segment` | Keysight35670ATrace | option-dependent | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:LIMit:UPPer:SEGMent:CLEar` | command only | yes | yes | `not exposed` | Keysight35670ATrace | option-dependent | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:LIMit:UPPer:TRACe[:IMMediate]` | command only | yes | yes | `make_upper_limit_from_trace()` | Keysight35670ATrace | option-dependent | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:MARKer:BAND:STARt` | command/query | yes | yes | `marker_band_start` | Keysight35670ATrace | option-dependent | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:MARKer:BAND:STOP` | command/query | yes | yes | `marker_band_stop` | Keysight35670ATrace | option-dependent | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:MARKer:COUPled[:STATe]` | command/query | yes | yes | `markers_coupled` | Keysight35670ATrace | option-dependent | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:MARKer:DTABle:CLEar[:IMMediate]` | command only | yes | yes | `clear_marker_data_table()` | Keysight35670ATrace | option-dependent | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:MARKer:DTABle:COPY[1|2|3|4]` | command only | yes | yes | `not exposed` | Keysight35670ATrace | option-dependent | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:MARKer:DTABle[:DATA]?` | query only | yes | yes | `clear_marker_data_table(), delete_marker_data_table_entry(), marker_data_table_insert_x, marker_data_table_label, marker_data_table_selected_point, ...` | Keysight35670ATrace | binary-or-block-transfer | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:MARKer:DTABle:X[:DATA]?` | query only | yes | yes | `delete_marker_data_table_entry(), marker_data_table_insert_x, marker_data_table_label, marker_data_table_selected_point, read_marker_data_table_x()` | Keysight35670ATrace | binary-or-block-transfer | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:MARKer:DTABle:X:DELete` | command only | yes | yes | `delete_marker_data_table_entry()` | Keysight35670ATrace | option-dependent | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:MARKer:DTABle:X:INSert` | command/query | yes | yes | `marker_data_table_insert_x` | Keysight35670ATrace | option-dependent | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:MARKer:DTABle:X:LABel` | command/query | yes | yes | `marker_data_table_label` | Keysight35670ATrace | option-dependent | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:MARKer:DTABle:X:SELect[:POINt]` | command/query | yes | yes | `marker_data_table_selected_point` | Keysight35670ATrace | option-dependent | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:MARKer:FUNCtion` | command/query | yes | yes | `marker_function, marker_function_result` | Keysight35670ATrace | option-dependent | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:MARKer:FUNCtion:RESult?` | query only | yes | yes | `marker_function_result` | Keysight35670ATrace | option-dependent | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:MARKer:HARMonic:COUNt` | command/query | yes | yes | `marker_harmonic_count` | Keysight35670ATrace | option-dependent | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:MARKer:HARMonic:FUNDamental` | command/query | yes | yes | `marker_harmonic_fundamental` | Keysight35670ATrace | option-dependent | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:MARKer:MAXimum[:GLOBal]` | command only | yes | yes | `marker_global_maximum_tracking_enabled, marker_to_global_maximum(), marker_to_left_maximum(), marker_to_right_maximum()` | Keysight35670ATrace | option-dependent | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:MARKer:MAXimum[:GLOBal]:TRACk` | command/query | yes | yes | `marker_global_maximum_tracking_enabled` | Keysight35670ATrace | option-dependent | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:MARKer:MAXimum:LEFT` | command only | yes | yes | `marker_to_left_maximum()` | Keysight35670ATrace | option-dependent | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:MARKer:MAXimum:RIGHt` | command only | yes | yes | `marker_to_right_maximum()` | Keysight35670ATrace | option-dependent | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:MARKer:MODE` | command/query | yes | yes | `marker_mode` | Keysight35670ATrace | option-dependent | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:MARKer:POSition` | command/query | yes | yes | `marker_position, marker_position_point` | Keysight35670ATrace | option-dependent | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:MARKer:POSition:POINt` | command/query | yes | yes | `marker_position_point` | Keysight35670ATrace | option-dependent | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:MARKer:REFerence:X` | command/query | yes | yes | `marker_reference_x` | Keysight35670ATrace | option-dependent | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:MARKer:REFerence:Y` | command/query | yes | yes | `marker_reference_y` | Keysight35670ATrace | option-dependent | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:MARKer:SIDeband:CARRier` | command/query | yes | yes | `marker_sideband_carrier` | Keysight35670ATrace | option-dependent | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:MARKer:SIDeband:COUNt` | command/query | yes | yes | `marker_sideband_count` | Keysight35670ATrace | option-dependent | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:MARKer:SIDeband:INCRement` | command/query | yes | yes | `marker_sideband_increment` | Keysight35670ATrace | option-dependent | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:MARKer[:STATe]` | command/query | yes | yes | `clear_marker_data_table(), delete_marker_data_table_entry(), marker_band_start, marker_band_stop, marker_data_table_insert_x, ...` | Keysight35670ATrace | option-dependent | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:MARKer:X[:ABSolute]` | command/query | yes | yes | `delete_marker_data_table_entry(), marker_data_table_insert_x, marker_data_table_label, marker_data_table_selected_point, marker_reference_x, ...` | Keysight35670ATrace | option-dependent | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:MARKer:X:RELative` | command/query | yes | yes | `marker_x_relative` | Keysight35670ATrace | option-dependent | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:MARKer:Y[:ABSolute]?` | query only | yes | yes | `marker_reference_y, marker_y, marker_y_relative` | Keysight35670ATrace | option-dependent | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:MARKer:Y:RELative` | command/query | yes | yes | `marker_y_relative` | Keysight35670ATrace | option-dependent | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:MATH:CONStant[1|2|3|4|5]` | command/query | yes | yes | `not exposed` | Keysight35670ATrace | option-dependent | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:MATH:DATA` | command/query | yes | yes | `math_data()` | Keysight35670ATrace | binary-or-block-transfer | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:MATH[:EXPRession[1|2|3|4|5]]` | command/query | yes | yes | `math_data(), math_enabled, math_selected_function` | Keysight35670ATrace | option-dependent | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:MATH:SELect` | command/query | yes | yes | `math_selected_function` | Keysight35670ATrace | option-dependent | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:MATH:STATe` | command/query | yes | yes | `math_enabled` | Keysight35670ATrace | option-dependent | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:SYNThesis:COPY` | command only | yes | yes | `copy_curve_fit_to_synthesis()` | Keysight35670ATrace | long-running | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:SYNThesis:DATA` | command/query | yes | yes | `synthesis_data()` | Keysight35670ATrace | long-running | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:SYNThesis:DESTination` | command/query | yes | yes | `synthesis_destination_register` | Keysight35670ATrace | long-running | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:SYNThesis:FSCale` | command/query | yes | yes | `synthesis_frequency_scale` | Keysight35670ATrace | long-running | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:SYNThesis:GAIN` | command/query | yes | yes | `synthesis_gain` | Keysight35670ATrace | long-running | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:SYNThesis[:IMMediate]` | command only | yes | yes | `copy_curve_fit_to_synthesis(), copy_synthesis_to_curve_fit(), run_synthesis(), synthesis_data(), synthesis_destination_register, ...` | Keysight35670ATrace | long-running | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:SYNThesis:SPACing` | command/query | yes | yes | `synthesis_spacing` | Keysight35670ATrace | long-running | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:SYNThesis:TDELay` | command/query | yes | yes | `synthesis_time_delay` | Keysight35670ATrace | long-running | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:SYNThesis:TTYPe` | command/query | yes | yes | `synthesis_table_type` | Keysight35670ATrace | long-running | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:UNIT:AMPLitude` | command/query | yes | yes | `amplitude_unit` | Keysight35670ATrace | option-dependent | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:UNIT:ANGLe` | command/query | yes | yes | `angle_unit` | Keysight35670ATrace | option-dependent | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:UNIT:DBReference` | command/query | yes | yes | `db_reference, db_reference_impedance, db_reference_user_label, db_reference_user_reference` | Keysight35670ATrace | option-dependent | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:UNIT:DBReference:IMPedance` | command/query | yes | yes | `db_reference_impedance` | Keysight35670ATrace | option-dependent | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:UNIT:DBReference:USER:LABel` | command/query | yes | yes | `db_reference_user_label` | Keysight35670ATrace | option-dependent | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:UNIT:DBReference:USER:REFerence` | command/query | yes | yes | `db_reference_user_reference` | Keysight35670ATrace | option-dependent | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:UNIT:MECHanical` | command/query | yes | yes | `mechanical_unit` | Keysight35670ATrace | option-dependent | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:UNIT:VOLTage` | command/query | yes | yes | `voltage_unit` | Keysight35670ATrace | option-dependent | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:UNIT:X` | command/query | yes | yes | `x_order_factor, x_unit, x_user_frequency_factor, x_user_frequency_label, x_user_time_factor, ...` | Keysight35670ATrace | option-dependent | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:UNIT:X:ORDer:FACTor` | command/query | yes | yes | `x_order_factor` | Keysight35670ATrace | option-dependent | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:UNIT:X:USER:FREQuency:FACTor` | command/query | yes | yes | `x_user_frequency_factor` | Keysight35670ATrace | option-dependent | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:UNIT:X:USER:FREQuency:LABel` | command/query | yes | yes | `x_user_frequency_label` | Keysight35670ATrace | option-dependent | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:UNIT:X:USER:TIME:FACTor` | command/query | yes | yes | `x_user_time_factor` | Keysight35670ATrace | option-dependent | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:UNIT:X:USER:TIME:LABel` | command/query | yes | yes | `x_user_time_label` | Keysight35670ATrace | option-dependent | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:WATerfall:COUNt` | command/query | yes | yes | `waterfall_count` | Keysight35670ATrace | long-running | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:WATerfall[:DATA]?` | query only | yes | yes | `waterfall_count, waterfall_data(), waterfall_slice_select, waterfall_slice_select_point, waterfall_trace_select, ...` | Keysight35670ATrace | long-running | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:WATerfall:SLICe:COPY` | command only | yes | yes | `not exposed` | Keysight35670ATrace | long-running | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:WATerfall:SLICe:SELect` | command/query | yes | yes | `waterfall_slice_select, waterfall_slice_select_point` | Keysight35670ATrace | long-running | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:WATerfall:SLICe:SELect:POINt` | command/query | yes | yes | `waterfall_slice_select_point` | Keysight35670ATrace | long-running | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:WATerfall:TRACe:COPY` | command only | yes | yes | `not exposed` | Keysight35670ATrace | long-running | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:WATerfall:TRACe:SELect` | command/query | yes | yes | `waterfall_trace_select, waterfall_trace_select_point` | Keysight35670ATrace | long-running | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:WATerfall:TRACe:SELect:POINt` | command/query | yes | yes | `waterfall_trace_select_point` | Keysight35670ATrace | long-running | expected_protocol | Implemented in driver. |
| CALCulate | `CALCulate[1|2|3|4]:X:DATA?` | query only | yes | yes | `read_marker_data_table_x(), read_x_data()` | Keysight35670ATrace | binary-or-block-transfer | expected_protocol | Implemented in driver. |
| CALibration | `CALibration[:ALL]?` | query only | yes | yes | `calibration_auto, run_calibration()` | Keysight35670A | safe | expected_protocol | Implemented in driver. |
| CALibration | `CALibration:AUTO` | command/query | yes | yes | `calibration_auto` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| DISPlay | `DISPlay:ANNotation[:ALL]` | command/query | yes | yes | `display_annotation_enabled` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| DISPlay | `DISPlay:BODE` | command only | yes | yes | `bode()` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| DISPlay | `DISPlay:BRIGhtness` | command/query | yes | yes | `display_brightness` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| DISPlay | `DISPlay:ERRor` | command only | yes | yes | `not exposed` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| DISPlay | `DISPlay:EXTernal[:STATe]` | command/query | yes | yes | `display_external_enabled` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| DISPlay | `DISPlay:FORMat` | command/query | yes | yes | `display_format` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| DISPlay | `DISPlay:GPIB:ECHO` | command/query | yes | yes | `display_gpib_echo_enabled` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| DISPlay | `DISPlay:PROGram:KEY:BOX` | command/query | yes | yes | `not exposed` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| DISPlay | `DISPlay:PROGram:KEY:BRACket` | command/query | yes | yes | `not exposed` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| DISPlay | `DISPlay:PROGram[:MODE]` | command/query | yes | yes | `display_program_mode, display_program_vector_buffer_enabled` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| DISPlay | `DISPlay:PROGram:VECTor:BUFFer[:STATe]` | command/query | yes | yes | `display_program_vector_buffer_enabled` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| DISPlay | `DISPlay:RPM[:STATe]` | command/query | yes | yes | `display_rpm_enabled` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| DISPlay | `DISPlay:SHOWall[:STATe]` | command/query | yes | yes | `display_show_all_enabled` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| DISPlay | `DISPlay:STATe` | command/query | yes | yes | `data_table_enabled, data_table_marker_enabled, display_enabled, display_external_enabled, display_program_vector_buffer_enabled, ...` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| DISPlay | `DISPlay:TCAPture:ENVelope[:STATe]` | command/query | yes | yes | `display_time_capture_envelope_enabled` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| DISPlay | `DISPlay:VIEW` | command/query | yes | yes | `display_view` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| DISPlay | `DISPlay[:WINDow[1|2|3|4]]:DTABle:MARKer[:STATe]` | command/query | yes | yes | `data_table_marker_enabled` | Keysight35670ADisplayWindow | option-dependent | expected_protocol | Implemented in driver. |
| DISPlay | `DISPlay[:WINDow[1|2|3|4]]:DTABle[:STATe]` | command/query | yes | yes | `data_table_enabled, data_table_marker_enabled` | Keysight35670ADisplayWindow | option-dependent | expected_protocol | Implemented in driver. |
| DISPlay | `DISPlay[:WINDow[1|2|3|4]]:LIMit:STATe` | command/query | yes | yes | `limit_display_enabled` | Keysight35670ADisplayWindow | option-dependent | expected_protocol | Implemented in driver. |
| DISPlay | `DISPlay[:WINDow[1|2|3|4]]:POLar:CLOCkwise` | command/query | yes | yes | `polar_clockwise` | Keysight35670ADisplayWindow | option-dependent | expected_protocol | Implemented in driver. |
| DISPlay | `DISPlay[:WINDow[1|2|3|4]]:POLar:ROTation` | command/query | yes | yes | `polar_rotation` | Keysight35670ADisplayWindow | option-dependent | expected_protocol | Implemented in driver. |
| DISPlay | `DISPlay[:WINDow[1|2|3|4]]:TRACe:APOWer[:STATe]` | command/query | yes | yes | `trace_a_power_enabled` | Keysight35670ADisplayWindow | option-dependent | expected_protocol | Implemented in driver. |
| DISPlay | `DISPlay[:WINDow[1|2|3|4]]:TRACe:BPOWer[:STATe]` | command/query | yes | yes | `trace_b_power_enabled` | Keysight35670ADisplayWindow | option-dependent | expected_protocol | Implemented in driver. |
| DISPlay | `DISPlay[:WINDow[1|2|3|4]]:TRACe:GRATicule:GRID[:STATe]` | command/query | yes | yes | `trace_graticule_grid_enabled` | Keysight35670ADisplayWindow | option-dependent | expected_protocol | Implemented in driver. |
| DISPlay | `DISPlay[:WINDow[1|2|3|4]]:TRACe:LABel` | command/query | yes | yes | `trace_label, trace_label_default_enabled` | Keysight35670ADisplayWindow | option-dependent | expected_protocol | Implemented in driver. |
| DISPlay | `DISPlay[:WINDow[1|2|3|4]]:TRACe:LABel:DEFault[:STATe]` | command/query | yes | yes | `trace_label_default_enabled` | Keysight35670ADisplayWindow | option-dependent | expected_protocol | Implemented in driver. |
| DISPlay | `DISPlay[:WINDow[1|2|3|4]]:TRACe:X:MATCh[1|2|3|4]` | command only | yes | yes | `not exposed` | Keysight35670ADisplayWindow | option-dependent | expected_protocol | Implemented in driver. |
| DISPlay | `DISPlay[:WINDow[1|2|3|4]]:TRACe:X[:SCALe]:AUTO` | command/query | yes | yes | `trace_x_autoscale` | Keysight35670ADisplayWindow | option-dependent | expected_protocol | Implemented in driver. |
| DISPlay | `DISPlay[:WINDow[1|2|3|4]]:TRACe:X[:SCALe]:LEFT` | command/query | yes | yes | `trace_x_left` | Keysight35670ADisplayWindow | option-dependent | expected_protocol | Implemented in driver. |
| DISPlay | `DISPlay[:WINDow[1|2|3|4]]:TRACe:X[:SCALe]:RIGHt` | command/query | yes | yes | `trace_x_right` | Keysight35670ADisplayWindow | option-dependent | expected_protocol | Implemented in driver. |
| DISPlay | `DISPlay[:WINDow[1|2|3|4]]:TRACe:X:SPACing` | command/query | yes | yes | `trace_x_spacing` | Keysight35670ADisplayWindow | option-dependent | expected_protocol | Implemented in driver. |
| DISPlay | `DISPlay[:WINDow[1|2|3|4]]:TRACe:Y:MATCh[1|2|3|4]` | command only | yes | yes | `not exposed` | Keysight35670ADisplayWindow | option-dependent | expected_protocol | Implemented in driver. |
| DISPlay | `DISPlay[:WINDow[1|2|3|4]]:TRACe:Y[:SCALe]:AUTO` | command/query | yes | yes | `trace_y_autoscale` | Keysight35670ADisplayWindow | option-dependent | expected_protocol | Implemented in driver. |
| DISPlay | `DISPlay[:WINDow[1|2|3|4]]:TRACe:Y[:SCALe]:BOTTom` | command/query | yes | yes | `trace_y_bottom` | Keysight35670ADisplayWindow | option-dependent | expected_protocol | Implemented in driver. |
| DISPlay | `DISPlay[:WINDow[1|2|3|4]]:TRACe:Y[:SCALe]:CENTer` | command/query | yes | yes | `trace_y_center` | Keysight35670ADisplayWindow | option-dependent | expected_protocol | Implemented in driver. |
| DISPlay | `DISPlay[:WINDow[1|2|3|4]]:TRACe:Y[:SCALe]:PDIVision` | command/query | yes | yes | `trace_y_per_division` | Keysight35670ADisplayWindow | option-dependent | expected_protocol | Implemented in driver. |
| DISPlay | `DISPlay[:WINDow[1|2|3|4]]:TRACe:Y[:SCALe]:REFerence` | command/query | yes | yes | `trace_y_reference` | Keysight35670ADisplayWindow | option-dependent | expected_protocol | Implemented in driver. |
| DISPlay | `DISPlay[:WINDow[1|2|3|4]]:TRACe:Y[:SCALe]:TOP` | command/query | yes | yes | `trace_y_top` | Keysight35670ADisplayWindow | option-dependent | expected_protocol | Implemented in driver. |
| DISPlay | `DISPlay[:WINDow[1|2|3|4]]:TRACe:Y:SPACing` | command/query | yes | yes | `trace_y_spacing` | Keysight35670ADisplayWindow | option-dependent | expected_protocol | Implemented in driver. |
| DISPlay | `DISPlay[:WINDow[1|2|3|4]]:WATerfall:BASeline` | command/query | yes | yes | `waterfall_baseline` | Keysight35670ADisplayWindow | long-running | expected_protocol | Implemented in driver. |
| DISPlay | `DISPlay[:WINDow[1|2|3|4]]:WATerfall:BOTTom` | command/query | yes | yes | `waterfall_bottom` | Keysight35670ADisplayWindow | long-running | expected_protocol | Implemented in driver. |
| DISPlay | `DISPlay[:WINDow[1|2|3|4]]:WATerfall:COUNt` | command/query | yes | yes | `waterfall_count` | Keysight35670ADisplayWindow | long-running | expected_protocol | Implemented in driver. |
| DISPlay | `DISPlay[:WINDow[1|2|3|4]]:WATerfall:HEIGht` | command/query | yes | yes | `waterfall_height` | Keysight35670ADisplayWindow | long-running | expected_protocol | Implemented in driver. |
| DISPlay | `DISPlay[:WINDow[1|2|3|4]]:WATerfall:HIDDen` | command/query | yes | yes | `waterfall_hidden_enabled` | Keysight35670ADisplayWindow | long-running | expected_protocol | Implemented in driver. |
| DISPlay | `DISPlay[:WINDow[1|2|3|4]]:WATerfall:SKEW` | command/query | yes | yes | `waterfall_skew_angle, waterfall_skew_enabled` | Keysight35670ADisplayWindow | long-running | expected_protocol | Implemented in driver. |
| DISPlay | `DISPlay[:WINDow[1|2|3|4]]:WATerfall:SKEW:ANGLe` | command/query | yes | yes | `waterfall_skew_angle` | Keysight35670ADisplayWindow | long-running | expected_protocol | Implemented in driver. |
| DISPlay | `DISPlay[:WINDow[1|2|3|4]]:WATerfall[:STATe]` | command/query | yes | yes | `waterfall_baseline, waterfall_bottom, waterfall_count, waterfall_enabled, waterfall_height, ...` | Keysight35670ADisplayWindow | long-running | expected_protocol | Implemented in driver. |
| DISPlay | `DISPlay[:WINDow[1|2|3|4]]:WATerfall:TOP` | command/query | yes | yes | `waterfall_top` | Keysight35670ADisplayWindow | long-running | expected_protocol | Implemented in driver. |
| FORMat | `FORMat[:DATA]` | command/query | yes | yes | `data_format, display_format, hardcopy_timestamp_format, mass_memory_store_program_format, mass_memory_store_trace_format` | Keysight35670A | binary-or-block-transfer | expected_protocol | Implemented in driver. |
| HCOPy | `HCOPy:COLor:DEFault` | command only | yes | yes | `hardcopy_color_default()` | Keysight35670A | requires-active-controller | expected_protocol | Implemented in driver. |
| HCOPy | `HCOPy:DESTination` | command/query | yes | yes | `hardcopy_destination` | Keysight35670A | requires-active-controller | expected_protocol | Implemented in driver. |
| HCOPy | `HCOPy:DEVice:LANGuage` | command/query | yes | yes | `hardcopy_device_language` | Keysight35670A | requires-active-controller | expected_protocol | Implemented in driver. |
| HCOPy | `HCOPy:DEVice:RESolution` | command/query | yes | yes | `hardcopy_device_resolution` | Keysight35670A | requires-active-controller | expected_protocol | Implemented in driver. |
| HCOPy | `HCOPy:DEVice:SPEed` | command/query | yes | yes | `hardcopy_device_speed` | Keysight35670A | requires-active-controller | expected_protocol | Implemented in driver. |
| HCOPy | `HCOPy[:IMMediate]` | command only | yes | yes | `hardcopy(), hardcopy_color_default(), hardcopy_destination, hardcopy_device_language, hardcopy_device_resolution, ...` | Keysight35670A | requires-active-controller | expected_protocol | Implemented in driver. |
| HCOPy | `HCOPy:ITEM:FFEed:STATe` | command/query | yes | yes | `hardcopy_form_feed_enabled` | Keysight35670A | requires-active-controller | expected_protocol | Implemented in driver. |
| HCOPy | `HCOPy:ITEM:LABel:COLor` | command/query | yes | yes | `hardcopy_label_color` | Keysight35670A | requires-active-controller | expected_protocol | Implemented in driver. |
| HCOPy | `HCOPy:ITEM:LABel:STATe` | command/query | yes | yes | `hardcopy_label_enabled` | Keysight35670A | requires-active-controller | expected_protocol | Implemented in driver. |
| HCOPy | `HCOPy:ITEM:LABel:TEXT` | command/query | yes | yes | `hardcopy_label_text` | Keysight35670A | requires-active-controller | expected_protocol | Implemented in driver. |
| HCOPy | `HCOPy:ITEM:TDSTamp:FORMat` | command/query | yes | yes | `hardcopy_timestamp_format` | Keysight35670A | requires-active-controller | expected_protocol | Implemented in driver. |
| HCOPy | `HCOPy:ITEM:TDSTamp:STATe` | command/query | yes | yes | `hardcopy_timestamp_enabled` | Keysight35670A | requires-active-controller | expected_protocol | Implemented in driver. |
| HCOPy | `HCOPy:ITEM[:WINDow[1|2|3|4]]:TRACe:COLor` | command/query | yes | yes | `hardcopy_trace_color, hardcopy_trace_graticule_color, hardcopy_trace_marker_color` | Keysight35670A | requires-active-controller | expected_protocol | Implemented in driver. |
| HCOPy | `HCOPy:ITEM[:WINDow[1|2|3|4]]:TRACe:GRATicule:COLor` | command/query | yes | yes | `hardcopy_trace_graticule_color` | Keysight35670A | requires-active-controller | expected_protocol | Implemented in driver. |
| HCOPy | `HCOPy:ITEM[:WINDow[1|2|3|4]]:TRACe:LIMit:LTYPe` | command/query | yes | yes | `hardcopy_trace_limit_line_type` | Keysight35670A | requires-active-controller | expected_protocol | Implemented in driver. |
| HCOPy | `HCOPy:ITEM[:WINDow[1|2|3|4]]:TRACe:LTYPe` | command/query | yes | yes | `hardcopy_trace_limit_line_type, hardcopy_trace_line_type` | Keysight35670A | requires-active-controller | expected_protocol | Implemented in driver. |
| HCOPy | `HCOPy:ITEM[:WINDow[1|2|3|4]]:TRACe:MARKer:COLor` | command/query | yes | yes | `hardcopy_trace_marker_color` | Keysight35670A | requires-active-controller | expected_protocol | Implemented in driver. |
| HCOPy | `HCOPy:PAGE:DIMensions:AUTO` | command/query | yes | yes | `hardcopy_page_dimensions_auto_enabled` | Keysight35670A | requires-active-controller | expected_protocol | Implemented in driver. |
| HCOPy | `HCOPy:PAGE:DIMensions:USER:LLEFt` | command/query | yes | yes | `hardcopy_page_user_lower_left` | Keysight35670A | requires-active-controller | expected_protocol | Implemented in driver. |
| HCOPy | `HCOPy:PAGE:DIMensions:USER:URIGht` | command/query | yes | yes | `hardcopy_page_user_upper_right` | Keysight35670A | requires-active-controller | expected_protocol | Implemented in driver. |
| HCOPy | `HCOPy:PLOT:ADDRess` | command/query | yes | yes | `hardcopy_plot_address` | Keysight35670A | requires-active-controller | expected_protocol | Implemented in driver. |
| HCOPy | `HCOPy:PRINt:ADDRess` | command/query | yes | yes | `hardcopy_print_address` | Keysight35670A | requires-active-controller | expected_protocol | Implemented in driver. |
| HCOPy | `HCOPy:TITLe[1|2]` | command/query | yes | yes | `hardcopy_title1, hardcopy_title2` | Keysight35670A | requires-active-controller | expected_protocol | Implemented in driver. |
| HCOPy | `HCOPy:SOURce` | command/query | yes | yes | `hardcopy_source` | Keysight35670A | requires-active-controller | expected_protocol | Implemented in driver. |
| INITiate | `INITiate:CONTinuous` | command/query | yes | yes | `continuous_initiation_enabled` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| INITiate | `INITiate[:IMMediate]` | command only | yes | yes | `continuous_initiation_enabled, initiate(), restart_measurement()` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| INPut | `INPut[1|2|3|4]:BIAS[:STATe]` | command/query | yes | yes | `bias_enabled` | Keysight35670AInputChannel | option-dependent | expected_protocol | Implemented in driver. |
| INPut | `INPut[1|2|3|4]:COUPling` | command/query | yes | yes | `coupling` | Keysight35670AInputChannel | option-dependent | expected_protocol | Implemented in driver. |
| INPut | `INPut[1|2|3|4]:FILTer:AWEighting[:STATe]` | command/query | yes | yes | `a_weighting_enabled` | Keysight35670AInputChannel | option-dependent | expected_protocol | Implemented in driver. |
| INPut | `INPut[1|2|3|4]:FILTer[:LPASs][:STATe]` | command/query | yes | yes | `a_weighting_enabled, anti_alias_filter_enabled` | Keysight35670AInputChannel | option-dependent | expected_protocol | Implemented in driver. |
| INPut | `INPut[1|2|3|4]:LOW` | command/query | yes | yes | `shield` | Keysight35670AInputChannel | option-dependent | expected_protocol | Implemented in driver. |
| INPut | `INPut[1|2|3|4]:REFerence:DIRection` | command/query | yes | yes | `reference_direction` | Keysight35670AInputChannel | option-dependent | expected_protocol | Implemented in driver. |
| INPut | `INPut[1|2|3|4]:REFerence:POINt` | command/query | yes | yes | `reference_point` | Keysight35670AInputChannel | option-dependent | expected_protocol | Implemented in driver. |
| INPut | `INPut[1|2|3|4][:STATe]` | command/query | yes | yes | `a_weighting_enabled, anti_alias_filter_enabled, bias_enabled, coupling, reference_direction, ...` | Keysight35670AInputChannel | option-dependent | expected_protocol | Implemented in driver. |
| INSTrument | `INSTrument:NSELect` | command/query | yes | yes | `_selected_instrument_number_setting, selected_instrument_number` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| INSTrument | `INSTrument[:SELect]` | command/query | yes | yes | `_selected_instrument_number_setting, instrument_mode, selected_instrument_number` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| MEMory | `MEMory:CATalog[:ALL]?` | query only | yes | yes | `not exposed` | Keysight35670A | safe | expected_protocol | Implemented in driver. |
| MEMory | `MEMory:CATalog:NAME?` | query only | yes | yes | `not exposed` | Keysight35670A | safe | expected_protocol | Implemented in driver. |
| MEMory | `MEMory:DELete:ALL` | command only | yes | yes | `memory_delete_all()` | Keysight35670A | destructive | expected_protocol | Implemented in driver. |
| MEMory | `MEMory:DELete[:NAME]` | command only | yes | yes | `memory_delete_all()` | Keysight35670A | destructive | expected_protocol | Implemented in driver. |
| MEMory | `MEMory:FREE[:ALL]?` | query only | yes | yes | `not exposed` | Keysight35670A | safe | expected_protocol | Implemented in driver. |
| MMEMory | `MMEMory:COPY` | command only | yes | yes | `not exposed` | Keysight35670A | destructive | expected_protocol | Implemented in driver. |
| MMEMory | `MMEMory:DELete` | command only | yes | yes | `not exposed` | Keysight35670A | destructive | expected_protocol | Implemented in driver. |
| MMEMory | `MMEMory:DISK:ADDRess` | command/query | yes | yes | `mass_memory_disk_address` | Keysight35670A | destructive | expected_protocol | Implemented in driver. |
| MMEMory | `MMEMory:DISK:UNIT` | command/query | yes | yes | `mass_memory_disk_unit` | Keysight35670A | destructive | expected_protocol | Implemented in driver. |
| MMEMory | `MMEMory:FSYStem?` | query only | yes | yes | `mass_memory_filesystem` | Keysight35670A | destructive | expected_protocol | Implemented in driver. |
| MMEMory | `MMEMory:INITialize` | command only | yes | yes | `not exposed` | Keysight35670A | destructive | expected_protocol | Implemented in driver. |
| MMEMory | `MMEMory:LOAD:CFIT` | command only | yes | yes | `not exposed` | Keysight35670A | destructive | expected_protocol | Implemented in driver. |
| MMEMory | `MMEMory:LOAD:CONTinue` | command/query | yes | yes | `mass_memory_load_continue(), mass_memory_load_continue_status` | Keysight35670A | destructive | expected_protocol | Implemented in driver. |
| MMEMory | `MMEMory:LOAD:DTABle:TRACe[1|2|3|4]` | command only | yes | yes | `not exposed` | Keysight35670A | destructive | expected_protocol | Implemented in driver. |
| MMEMory | `MMEMory:LOAD:LIMit:LOWer:TRACe[1|2|3|4]` | command only | yes | yes | `not exposed` | Keysight35670A | destructive | expected_protocol | Implemented in driver. |
| MMEMory | `MMEMory:LOAD:LIMit:UPPer:TRACe[1|2|3|4]` | command only | yes | yes | `not exposed` | Keysight35670A | destructive | expected_protocol | Implemented in driver. |
| MMEMory | `MMEMory:LOAD:MATH` | command only | yes | yes | `not exposed` | Keysight35670A | destructive | expected_protocol | Implemented in driver. |
| MMEMory | `MMEMory:LOAD:PROGram` | command only | yes | yes | `not exposed` | Keysight35670A | destructive | expected_protocol | Implemented in driver. |
| MMEMory | `MMEMory:LOAD:STATe` | command only | yes | yes | `not exposed` | Keysight35670A | destructive | expected_protocol | Implemented in driver. |
| MMEMory | `MMEMory:LOAD:SYNThesis` | command only | yes | yes | `not exposed` | Keysight35670A | destructive | expected_protocol | Implemented in driver. |
| MMEMory | `MMEMory:LOAD:TCAPture` | command only | yes | yes | `not exposed` | Keysight35670A | destructive | expected_protocol | Implemented in driver. |
| MMEMory | `MMEMory:LOAD:TRACe` | command only | yes | yes | `not exposed` | Keysight35670A | destructive | expected_protocol | Implemented in driver. |
| MMEMory | `MMEMory:LOAD:WATerfall` | command only | yes | yes | `not exposed` | Keysight35670A | destructive | expected_protocol | Implemented in driver. |
| MMEMory | `MMEMory:MDIRectory` | command only | yes | yes | `not exposed` | Keysight35670A | destructive | expected_protocol | Implemented in driver. |
| MMEMory | `MMEMory:MOVE` | command only | yes | yes | `not exposed` | Keysight35670A | destructive | expected_protocol | Implemented in driver. |
| MMEMory | `MMEMory:MSIS` | command/query | yes | yes | `mass_memory_default_disk` | Keysight35670A | destructive | expected_protocol | Implemented in driver. |
| MMEMory | `MMEMory:NAME` | command/query | yes | yes | `mass_memory_name` | Keysight35670A | destructive | expected_protocol | Implemented in driver. |
| MMEMory | `MMEMory:STORe:CFIT` | command only | yes | yes | `not exposed` | Keysight35670A | destructive | expected_protocol | Implemented in driver. |
| MMEMory | `MMEMory:STORe:CONTinue` | command/query | yes | yes | `mass_memory_store_continue(), mass_memory_store_continue_status` | Keysight35670A | destructive | expected_protocol | Implemented in driver. |
| MMEMory | `MMEMory:STORe:DTABle:TRACe[1|2|3|4]` | command only | yes | yes | `not exposed` | Keysight35670A | destructive | expected_protocol | Implemented in driver. |
| MMEMory | `MMEMory:STORe:LIMit:LOWer:TRACe[1|2|3|4]` | command only | yes | yes | `not exposed` | Keysight35670A | destructive | expected_protocol | Implemented in driver. |
| MMEMory | `MMEMory:STORe:LIMit:UPPer:TRACe[1|2|3|4]` | command only | yes | yes | `not exposed` | Keysight35670A | destructive | expected_protocol | Implemented in driver. |
| MMEMory | `MMEMory:STORe:MATH` | command only | yes | yes | `not exposed` | Keysight35670A | destructive | expected_protocol | Implemented in driver. |
| MMEMory | `MMEMory:STORe:PROGram` | command only | yes | yes | `mass_memory_store_program_format` | Keysight35670A | destructive | expected_protocol | Implemented in driver. |
| MMEMory | `MMEMory:STORe:PROGram:FORMat` | command/query | yes | yes | `mass_memory_store_program_format` | Keysight35670A | destructive | expected_protocol | Implemented in driver. |
| MMEMory | `MMEMory:STORe:STATe` | command only | yes | yes | `not exposed` | Keysight35670A | destructive | expected_protocol | Implemented in driver. |
| MMEMory | `MMEMory:STORe:SYNThesis` | command only | yes | yes | `not exposed` | Keysight35670A | destructive | expected_protocol | Implemented in driver. |
| MMEMory | `MMEMory:STORe:TCAPture` | command only | yes | yes | `not exposed` | Keysight35670A | destructive | expected_protocol | Implemented in driver. |
| MMEMory | `MMEMory:STORe:TRACe` | command only | yes | yes | `not exposed` | Keysight35670A | destructive | expected_protocol | Implemented in driver. |
| MMEMory | `MMEM:STORe:TRACe:FORMat` | command/query | yes | yes | `mass_memory_store_trace_format` | Keysight35670A | destructive | expected_protocol | Implemented in driver. |
| MMEMory | `MMEMory:STORe:WATerfall` | command only | yes | yes | `not exposed` | Keysight35670A | destructive | expected_protocol | Implemented in driver. |
| OUTPut | `OUTPut:FILTer[:LPASs][:STATe]` | command/query | yes | yes | `output_low_pass_filter_enabled` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| OUTPut | `OUTPut[:STATe]` | command/query | yes | yes | `output_low_pass_filter_enabled, source_output_enabled` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| PROGram | `PROGram:EDIT:ENABle` | command/query | yes | yes | `program_edit_enabled` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| PROGram | `PROGram:EXPLicit:DEFine` | command/query | yes | yes | `read_explicit_program_definition()` | Keysight35670A | binary-or-block-transfer | expected_protocol | Implemented in driver. |
| PROGram | `PROGram:EXPLicit:LABel` | command/query | yes | yes | `read_explicit_program_label()` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| PROGram | `PROGram[:SELected]:DEFine` | command/query | yes | yes | `define_program(), read_explicit_program_definition(), read_program_definition()` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| PROGram | `PROGram[:SELected]:DELete:ALL` | command only | yes | yes | `delete_all_programs()` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| PROGram | `PROGram[:SELected]:DELete[:SELected]` | command only | yes | yes | `delete_all_programs(), delete_selected_program()` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| PROGram | `PROGram[:SELected]:LABel` | command/query | yes | yes | `program_label, read_explicit_program_label()` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| PROGram | `PROGram[:SELected]:MALLocate` | command/query | yes | yes | `allocate_program_memory(), program_allocated_memory` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| PROGram | `PROGram[:SELected]:NAME` | command/query | yes | yes | `program_name` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| PROGram | `PROGram[:SELected]:NUMBer` | command/query | yes | yes | `not exposed` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| PROGram | `PROGram[:SELected]:STATe` | command/query | yes | yes | `display_program_vector_buffer_enabled, program_state` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| PROGram | `PROGram[:SELected]:STRing` | command/query | yes | yes | `not exposed` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| [SENSe: | `[SENSe:]AVERage:CONFidence` | command/query | yes | yes | `average_confidence` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| [SENSe: | `[SENSe:]AVERage:COUNt` | command/query | yes | yes | `average_count` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| [SENSe: | `[SENSe:]AVERage:HOLD` | command/query | yes | yes | `average_hold` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| [SENSe: | `[SENSe:]AVERage:IMPulse` | command/query | yes | yes | `average_impulse_enabled` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| [SENSe: | `[SENSe:]AVERage:IRESult:RATE` | command/query | yes | yes | `average_iresult_rate` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| [SENSe: | `[SENSe:]AVERage:IRESult[:STATe]` | command/query | yes | yes | `average_iresult_enabled, average_iresult_rate` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| [SENSe: | `[SENSe:]AVERage:PREView` | command/query | yes | yes | `accept_average_preview(), average_preview, average_preview_time, reject_average_preview()` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| [SENSe: | `[SENSe:]AVERage:PREView:ACCept` | command only | yes | yes | `accept_average_preview()` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| [SENSe: | `[SENSe:]AVERage:PREView:REJect` | command only | yes | yes | `reject_average_preview()` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| [SENSe: | `[SENSe:]AVERage:PREView:TIME` | command/query | yes | yes | `average_preview_time` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| [SENSe: | `[SENSe:]AVERage:TCONtrol` | command/query | yes | yes | `average_tcontrol` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| [SENSe: | `[SENSe:]AVERage:TIME` | command/query | yes | yes | `average_preview_time, average_time` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| [SENSe: | `[SENSe:]AVERage:TYPE` | command/query | yes | yes | `average_type` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| [SENSe: | `[SENSe:]DATA` | command/query | yes | yes | `cfit_data(), data_format, data_points(), math_data(), read_data(), ...` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| [SENSe: | `[SENSE:]DATA:HEADer:FREQuency:STARt?` | query only | yes | yes | `sense_data_frequency_start` | Keysight35670A | safe | expected_protocol | Implemented in driver. |
| [SENSe: | `[SENSE:]DATA:HEADer:FREQuency:STOP?` | query only | yes | yes | `sense_data_frequency_stop` | Keysight35670A | safe | expected_protocol | Implemented in driver. |
| [SENSe: | `[SENSe:]DATA:RANGe` | command/query | yes | yes | `not exposed` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| [SENSe: | `[SENSe:]FEED` | command/query | yes | yes | `feed, sense_feed` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| [SENSe: | `[SENSe:]FREQuency:BLOCksize` | command/query | yes | yes | `frequency_block_size` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| [SENSe: | `[SENSe:]FREQuency:CENTer` | command/query | yes | yes | `frequency_center` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| [SENSe: | `[SENSe:]FREQuency:MANual` | command/query | yes | yes | `frequency_manual` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| [SENSe: | `[SENSe:]FREQuency:RESolution` | command/query | yes | yes | `frequency_resolution, frequency_resolution_auto_enabled, frequency_resolution_auto_max_change, frequency_resolution_auto_minimum, frequency_resolution_octave` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| [SENSe: | `[SENSe:]FREQuency:RESolution:AUTO` | command/query | yes | yes | `frequency_resolution_auto_enabled, frequency_resolution_auto_max_change, frequency_resolution_auto_minimum` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| [SENSe: | `[SENSe:]FREQuency:RESolution:AUTO:MCHange` | command/query | yes | yes | `frequency_resolution_auto_max_change` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| [SENSe: | `[SENSe:]FREQuency:RESolution:AUTO:MINimum` | command/query | yes | yes | `frequency_resolution_auto_minimum` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| [SENSe: | `[SENSe:]FREQuency:RESolution:OCTave` | command/query | yes | yes | `frequency_resolution_octave` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| [SENSe: | `[SENSe:]FREQuency:SPAN` | command/query | yes | yes | `frequency_span, frequency_span_link, set_full_frequency_span()` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| [SENSe: | `[SENSe:]FREQuency:SPAN:FULL` | command only | yes | yes | `set_full_frequency_span()` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| [SENSe: | `[SENSe:]FREQuency:SPAN:LINK` | command/query | yes | yes | `frequency_span_link` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| [SENSe: | `[SENSe:]FREQuency:STARt` | command/query | yes | yes | `cfit_frequency_start, frequency_start, sense_data_frequency_start` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| [SENSe: | `[SENSe:]FREQuency:STEP[:INCRement]` | command/query | yes | yes | `frequency_step_increment` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| [SENSe: | `[SENSe:]FREQuency:STOP` | command/query | yes | yes | `cfit_frequency_stop, frequency_stop, sense_data_frequency_stop` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| [SENSe: | `[SENSe:]HISTogram:BINS` | command/query | yes | yes | `histogram_bins` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| [SENSe: | `[SENSe:]ORDer:MAXimum` | command/query | yes | yes | `order_maximum, order_rpm_maximum` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| [SENSe: | `[SENSe:]ORDer:RESolution` | command/query | yes | yes | `order_resolution, order_track_resolution` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| [SENSe: | `[SENSe:]ORDer:RESolution:TRACk` | command/query | yes | yes | `order_track_resolution` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| [SENSe: | `[SENSe:]ORDer:RPM:MAXimum` | command/query | yes | yes | `order_rpm_maximum` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| [SENSe: | `[SENSe:]ORDer:RPM:MINimum` | command/query | yes | yes | `order_rpm_minimum` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| [SENSe: | `[SENSe:]ORDer:TRACk[1|2|3|4|5]` | command/query | yes | yes | `enabled, order, order_track_resolution` | Keysight35670AOrderTrack | option-dependent | expected_protocol | Implemented in driver. |
| [SENSe: | `[SENSe:]ORDer:TRACk[1|2|3|4|5]:STATe` | command/query | yes | yes | `enabled` | Keysight35670AOrderTrack | option-dependent | expected_protocol | Implemented in driver. |
| [SENSe: | `[SENSe:]REFerence` | command/query | yes | yes | `db_reference_user_reference, marker_reference_x, marker_reference_y, reference_channels, reference_direction, ...` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| [SENSe: | `[SENSe:]REJect:STATe` | command/query | yes | yes | `overload_rejection_enabled` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| [SENSe: | `[SENSe:]SWEep:DIRection` | command/query | yes | yes | `sweep_direction` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| [SENSe: | `[SENSe:]SWEep:DWELl` | command/query | yes | yes | `sweep_dwell` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| [SENSe: | `[SENSe:]SWEep:MODE` | command/query | yes | yes | `sweep_mode` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| [SENSe: | `[SENSe:]SWEep:OVERlap` | command/query | yes | yes | `sweep_overlap` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| [SENSe: | `[SENSe:]SWEep:SPACing` | command/query | yes | yes | `sweep_spacing` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| [SENSe: | `[SENSe:]SWEep:STIMe` | command/query | yes | yes | `sweep_settling_time` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| [SENSe: | `[SENSe:]SWEep:TIME` | command/query | yes | yes | `sweep_time` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| [SENSe: | `[SENSe:]TCAPture:ABORt` | command only | yes | yes | `abort_time_capture()` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| [SENSe: | `[SENSe:]TCAPture:DELete` | command only | yes | yes | `delete_time_capture()` | Keysight35670A | destructive | expected_protocol | Implemented in driver. |
| [SENSe: | `[SENSe:]TCAPture:FILE` | command/query | yes | yes | `load_time_capture_file(), time_capture_file()` | Keysight35670A | binary-or-block-transfer | expected_protocol | Implemented in driver. |
| [SENSe: | `[SENSe:]TCAPture[:IMMediate]` | command only | yes | yes | `abort_time_capture(), allocate_time_capture_memory(), delete_time_capture(), display_time_capture_envelope_enabled, load_time_capture_file(), ...` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| [SENSe: | `[SENSe:]TCAPture:LENGth` | command/query | yes | yes | `time_capture_length` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| [SENSe: | `[SENSe:]TCAPture:MALLocate` | command only | yes | yes | `allocate_time_capture_memory()` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| [SENSe: | `[SENSe:]TCAPture:STARt[1|2|3|4]` | command/query | yes | yes | `time_capture_start1, time_capture_start2, time_capture_start3, time_capture_start4` | Keysight35670A | option-dependent | expected_protocol | Implemented in driver. |
| [SENSe: | `[SENSe:]TCAPture:STOP[1|2|3|4]` | command/query | yes | yes | `time_capture_stop1, time_capture_stop2, time_capture_stop3, time_capture_stop4` | Keysight35670A | option-dependent | expected_protocol | Implemented in driver. |
| [SENSe: | `[SENSe:]TCAPture:TACHometer:RPM:MAXimum` | command/query | yes | yes | `time_capture_tachometer_rpm_maximum` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| [SENSe: | `[SENSe:]TCAPture:TACHometer[:STATe]` | command/query | yes | yes | `time_capture_tachometer_enabled, time_capture_tachometer_rpm_maximum` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| [SENSe: | `[SENSe:]VOLTage[1|2|3|4][:DC]:RANGe:AUTO` | command/query | yes | yes | `autorange_direction, autorange_enabled` | Keysight35670A | option-dependent | expected_protocol | Implemented in driver. |
| [SENSe: | `[SENSe:]VOLTage[1|2|3|4][:DC]:RANGe:AUTO:DIRection` | command/query | yes | yes | `autorange_direction` | Keysight35670A | option-dependent | expected_protocol | Implemented in driver. |
| [SENSe: | `[SENSe:]VOLTage[1|2|3|4][:DC]:RANGe:UNIT:USER:LABel` | command/query | yes | yes | `range_unit_user_label` | Keysight35670A | option-dependent | expected_protocol | Implemented in driver. |
| [SENSe: | `[SENSe:]VOLTage[1|2|3|4][:DC]:RANGe:UNIT:USER:SFACtor` | command/query | yes | yes | `range_unit_user_scale_factor` | Keysight35670A | option-dependent | expected_protocol | Implemented in driver. |
| [SENSe: | `[SENSe:]VOLTage[1|2|3|4][:DC]:RANGe:UNIT:USER[:STATe]` | command/query | yes | yes | `range_unit_user_enabled, range_unit_user_label, range_unit_user_scale_factor` | Keysight35670A | option-dependent | expected_protocol | Implemented in driver. |
| [SENSe: | `[SENSe:]VOLTage[1|2|3|4][:DC]:RANGe:UNIT:XDCR:LABel` | command/query | yes | yes | `range_unit_transducer_label` | Keysight35670A | option-dependent | expected_protocol | Implemented in driver. |
| [SENSe: | `[SENSe:]VOLTage[1|2|3|4][:DC]:RANGe[:UPPer]` | command/query | yes | yes | `autorange_direction, autorange_enabled, range_dbvrms, range_unit_transducer_label, range_unit_user_enabled, ...` | Keysight35670A | option-dependent | expected_protocol | Implemented in driver. |
| [SENSe: | `[SENSe:]WINDow[1|2|3|4]:EXPonential` | command/query | yes | yes | `exponential_window_time_constant` | Keysight35670ASenseWindow | option-dependent | expected_protocol | Implemented in driver. |
| [SENSe: | `[SENSe:]WINDow[1|2|3|4]:FORCe` | command/query | yes | yes | `force_window_width` | Keysight35670ASenseWindow | option-dependent | expected_protocol | Implemented in driver. |
| [SENSe: | `[SENSe:]WINDow[1|2|3|4]:ORDer:DC` | command/query | yes | yes | `order_dc_included` | Keysight35670ASenseWindow | option-dependent | expected_protocol | Implemented in driver. |
| [SENSe: | `[SENSe:]WINDow[1|2|3|4][:TYPE]` | command/query | yes | yes | `data_table_enabled, data_table_marker_enabled, exponential_window_time_constant, force_window_width, hardcopy_trace_color, ...` | Keysight35670ASenseWindow | option-dependent | expected_protocol | Implemented in driver. |
| SOURce | `SOURce:BURSt` | command/query | yes | yes | `source_burst_percent` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| SOURce | `SOURce:FREQuency[:CW]` | command/query | yes | yes | `source_frequency_cw, source_frequency_fixed` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| SOURce | `SOURce:FREQuency:FIXed` | command/query | yes | yes | `source_frequency_fixed` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| SOURce | `SOURce:FUNCtion[:SHAPe]` | command/query | yes | yes | `source_function` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| SOURce | `SOURce:USER:CAPTure` | command/query | yes | yes | `source_user_capture_channel` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| SOURce | `SOURce:USER[:REGister]` | command/query | yes | yes | `source_user_capture_channel, source_user_register, source_user_repeat_enabled` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| SOURce | `SOURce:USER:REPeat` | command/query | yes | yes | `source_user_repeat_enabled` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| SOURce | `SOURce:VOLTage[:LEVel]:AUTO` | command/query | yes | yes | `source_voltage_autolevel_enabled` | Keysight35670AInputChannel | state-changing | expected_protocol | Implemented in driver. |
| SOURce | `SOURce:VOLTage[:LEVel][:IMMediate][:AMPLitude]` | command/query | yes | yes | `source_voltage_amplitude, source_voltage_autolevel_enabled, source_voltage_limit_amplitude, source_voltage_limit_input, source_voltage_offset, ...` | Keysight35670AInputChannel | state-changing | expected_protocol | Implemented in driver. |
| SOURce | `SOURce:VOLTage[:LEVel][:IMMediate]:OFFSet` | command/query | yes | yes | `source_voltage_offset` | Keysight35670AInputChannel | state-changing | expected_protocol | Implemented in driver. |
| SOURce | `SOURce:VOLTage[:LEVel]:REFerence` | command/query | yes | yes | `source_voltage_reference, source_voltage_reference_channel, source_voltage_reference_tolerance` | Keysight35670AInputChannel | state-changing | expected_protocol | Implemented in driver. |
| SOURce | `SOURce:VOLTage[:LEVel]:REFerence:CHANnel` | command/query | yes | yes | `source_voltage_reference_channel` | Keysight35670AInputChannel | state-changing | expected_protocol | Implemented in driver. |
| SOURce | `SOURce:VOLTage[:LEVel]:REFerence:TOLerance` | command/query | yes | yes | `source_voltage_reference_tolerance` | Keysight35670AInputChannel | state-changing | expected_protocol | Implemented in driver. |
| SOURce | `SOURce:VOLTage:LIMit[:AMPLitude]` | command/query | yes | yes | `source_voltage_limit_amplitude, source_voltage_limit_input` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| SOURce | `SOURce:VOLTage:LIMit:INPut` | command/query | yes | yes | `source_voltage_limit_input` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| SOURce | `SOURce:VOLTage:SLEW` | command/query | yes | yes | `source_voltage_slew` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| STATus | `STATus:DEVice:CONDition?` | query only | yes | yes | `device_condition` | Keysight35670A | safe | expected_protocol | Implemented in driver. |
| STATus | `STATus:DEVice:ENABle` | command/query | yes | yes | `device_enable` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| STATus | `STATus:DEVice[:EVENt]?` | query only | yes | yes | `device_condition, device_enable, device_event, device_negative_transition, device_positive_transition` | Keysight35670A | safe | expected_protocol | Implemented in driver. |
| STATus | `STATus:DEVice:NTRansition` | command/query | yes | yes | `device_negative_transition` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| STATus | `STATus:DEVice:PTRansition` | command/query | yes | yes | `device_positive_transition` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| STATus | `STATus:OPERation:CONDition?` | query only | yes | yes | `operation_condition` | Keysight35670A | safe | expected_protocol | Implemented in driver. |
| STATus | `STATus:OPERation:ENABle` | command/query | yes | yes | `operation_enable` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| STATus | `STATus:OPERation[:EVENt]?` | query only | yes | yes | `operation_condition, operation_enable, operation_event, operation_negative_transition, operation_positive_transition` | Keysight35670A | safe | expected_protocol | Implemented in driver. |
| STATus | `STATus:OPERation:NTRansition` | command/query | yes | yes | `operation_negative_transition` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| STATus | `STATus:OPERation:PTRansition` | command/query | yes | yes | `operation_positive_transition` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| STATus | `STATus:PRESet` | command only | yes | yes | `status_preset()` | Keysight35670A | destructive | expected_protocol | Implemented in driver. |
| STATus | `STATus:QUEStionable:CONDition?` | query only | yes | yes | `questionable_condition, questionable_limit_condition, questionable_voltage_condition` | Keysight35670A | safe | expected_protocol | Implemented in driver. |
| STATus | `STATus:QUEStionable:ENABle` | command/query | yes | yes | `questionable_enable, questionable_limit_enable, questionable_voltage_enable` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| STATus | `STATus:QUEStionable[:EVENt]?` | query only | yes | yes | `questionable_condition, questionable_enable, questionable_event, questionable_limit_condition, questionable_limit_enable, ...` | Keysight35670A | safe | expected_protocol | Implemented in driver. |
| STATus | `STATus:QUEStionable:LIMit:CONDition?` | query only | yes | yes | `questionable_limit_condition` | Keysight35670A | safe | expected_protocol | Implemented in driver. |
| STATus | `STATus:QUEStionable:LIMit:ENABle` | command/query | yes | yes | `questionable_limit_enable` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| STATus | `STATus:QUEStionable:LIMit[:EVENt]?` | query only | yes | yes | `questionable_limit_condition, questionable_limit_enable, questionable_limit_event, questionable_limit_negative_transition, questionable_limit_positive_transition` | Keysight35670A | safe | expected_protocol | Implemented in driver. |
| STATus | `STATus:QUEStionable:LIMit:NTRansition` | command/query | yes | yes | `questionable_limit_negative_transition` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| STATus | `STATus:QUEStionable:LIMit:PTRansition` | command/query | yes | yes | `questionable_limit_positive_transition` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| STATus | `STATus:QUEStionable:NTRansition` | command/query | yes | yes | `questionable_limit_negative_transition, questionable_negative_transition, questionable_voltage_negative_transition` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| STATus | `STATus:QUEStionable:PTRansition` | command/query | yes | yes | `questionable_limit_positive_transition, questionable_positive_transition, questionable_voltage_positive_transition` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| STATus | `STATus:QUEStionable:VOLTage:CONDition?` | query only | yes | yes | `questionable_voltage_condition` | Keysight35670A | safe | expected_protocol | Implemented in driver. |
| STATus | `STATus:QUEStionable:VOLTage:ENABle` | command/query | yes | yes | `questionable_voltage_enable` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| STATus | `STATus:QUEStionable:VOLTage[:EVENt]?` | query only | yes | yes | `questionable_voltage_condition, questionable_voltage_enable, questionable_voltage_event, questionable_voltage_negative_transition, questionable_voltage_positive_transition` | Keysight35670AInputChannel | safe | expected_protocol | Implemented in driver. |
| STATus | `STATus:QUEStionable:VOLTage:NTRansition` | command/query | yes | yes | `questionable_voltage_negative_transition` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| STATus | `STATus:QUEStionable:VOLTage:PTRansition` | command/query | yes | yes | `questionable_voltage_positive_transition` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| STATus | `STATus:USER:ENABle` | command/query | yes | yes | `user_status_enable` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| STATus | `STATus:USER[:EVENt]?` | query only | yes | yes | `user_status_enable, user_status_event` | Keysight35670A | safe | expected_protocol | Implemented in driver. |
| STATus | `STATus:USER:PULSe` | command only | yes | yes | `not exposed` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| SYSTem | `SYSTem:BEEPer[:IMMediate]` | command only | yes | yes | `beep(), beeper_enabled` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| SYSTem | `SYSTem:BEEPer:STATe` | command/query | yes | yes | `beeper_enabled` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| SYSTem | `SYSTem:COMMunicate:GPIB[:SELF]:ADDRess` | command/query | yes | yes | `gpib_address` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| SYSTem | `SYSTem:COMMunicate:SERial[:RECeive]:BAUD` | command/query | yes | yes | `serial_receive_baud` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| SYSTem | `SYSTem:COMMunicate:SERial[:RECeive]:BITS` | command/query | yes | yes | `serial_receive_bits` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| SYSTem | `SYSTem:COMMunicate:SERial[:RECeive]:PACE` | command/query | yes | yes | `serial_receive_pace, serial_transmit_pace` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| SYSTem | `SYSTem:COMMunicate:SERial[:RECeive]:PARity:CHECk` | command/query | yes | yes | `serial_receive_parity_check_enabled` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| SYSTem | `SYSTem:COMMunicate:SERial[:RECeive]:PARity[:TYPE]` | command/query | yes | yes | `serial_receive_parity, serial_receive_parity_check_enabled` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| SYSTem | `SYSTem:COMMunicate:SERial[:RECeive]:SBITs` | command/query | yes | yes | `serial_receive_stop_bits` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| SYSTem | `SYSTem:COMMunicate:SERial:TRANsmit:PACE` | command/query | yes | yes | `serial_transmit_pace` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| SYSTem | `SYSTem:DATE` | command/query | yes | yes | `system_date` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| SYSTem | `SYSTem:ERRor?` | query only | yes | yes | `_next_system_error, _raise_if_errors()` | Keysight35670A | safe | expected_protocol | Implemented in driver. |
| SYSTem | `SYSTem:FAN[:STATe]` | command/query | yes | yes | `fan_state` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| SYSTem | `SYSTem:FLOG:CLEar` | command only | yes | yes | `clear_fault_log()` | Keysight35670A | destructive | expected_protocol | Implemented in driver. |
| SYSTem | `SYSTem:KEY` | command/query | yes | yes | `key_code` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| SYSTem | `SYSTem:KLOCk` | command/query | yes | yes | `keyboard_locked` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| SYSTem | `SYSTem:POWer:SOURce?` | query only | yes | yes | `power_source` | Keysight35670A | safe | expected_protocol | Implemented in driver. |
| SYSTem | `SYSTem:POWer:STATe` | command/query | yes | yes | `power_off(), power_state` | Keysight35670A | destructive | expected_protocol | Implemented in driver. |
| SYSTem | `SYSTem:PRESet` | command only | yes | yes | `system_preset()` | Keysight35670A | destructive | expected_protocol | Implemented in driver. |
| SYSTem | `SYSTem:SET` | command/query | yes | yes | `load_system_state(), system_state_data()` | Keysight35670A | binary-or-block-transfer | expected_protocol | Implemented in driver. |
| SYSTem | `SYSTem:TIME` | command/query | yes | yes | `system_time` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| SYSTem | `SYSTem:VERSion?` | query only | yes | yes | `system_version` | Keysight35670A | safe | expected_protocol | Implemented in driver. |
| TEST | `TEST:LOG:CLEar` | command only | yes | yes | `clear_test_log()` | Keysight35670A | destructive | expected_protocol | Implemented in driver. |
| TEST | `TEST:LONG` | command only | yes | yes | `long_test_result, run_long_test()` | Keysight35670A | long-running | expected_protocol | Implemented in driver. |
| TEST | `TEST:LONG:RESult?` | query only | yes | yes | `long_test_result` | Keysight35670A | long-running | expected_protocol | Implemented in driver. |
| TRACe | `TRACe[:DATA]` | command/query | yes | yes | `hardcopy_trace_color, hardcopy_trace_graticule_color, hardcopy_trace_limit_line_type, hardcopy_trace_line_type, hardcopy_trace_marker_color, ...` | Keysight35670A | binary-or-block-transfer | expected_protocol | Implemented in driver. |
| TRACe | `TRACe:WATerfall[:DATA]` | command/query | yes | yes | `read_trace_waterfall_data()` | Keysight35670A | long-running | expected_protocol | Implemented in driver. |
| TRACe | `TRACe:X[:DATA]?` | query only | yes | yes | `read_trace_x_data(), read_trace_x_unit(), trace_x_autoscale, trace_x_left, trace_x_right, ...` | Keysight35670A | binary-or-block-transfer | expected_protocol | Implemented in driver. |
| TRACe | `TRACe:X:UNIT?` | query only | yes | yes | `read_trace_x_unit()` | Keysight35670A | safe | expected_protocol | Implemented in driver. |
| TRACe | `TRACe:Z:UNIT?` | query only | yes | yes | `read_trace_z_unit()` | Keysight35670A | safe | expected_protocol | Implemented in driver. |
| TRIGger | `TRIGger:EXTernal:FILTer[:LPAS][:STATe]` | command/query | yes | yes | `external_trigger_filter_enabled` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| TRIGger | `TRIGger:EXTernal:LEVel` | command/query | yes | yes | `external_trigger_level` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| TRIGger | `TRIGger:EXTernal:RANGe` | command/query | yes | yes | `external_trigger_range` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| TRIGger | `TRIGger[:IMMediate]` | command only | yes | yes | `external_trigger_filter_enabled, external_trigger_level, external_trigger_range, tachometer_holdoff, tachometer_level, ...` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| TRIGger | `TRIGger:LEVel` | command/query | yes | yes | `external_trigger_level, tachometer_level, trigger_level` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| TRIGger | `TRIGger:SLOPe` | command/query | yes | yes | `tachometer_slope, trigger_slope` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| TRIGger | `TRIGger:SOURce` | command/query | yes | yes | `trigger_source` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| TRIGger | `TRIGger:STARt[1|2|3|4]` | command/query | yes | yes | `trigger_start1, trigger_start2, trigger_start3, trigger_start4` | Keysight35670A | option-dependent | expected_protocol | Implemented in driver. |
| TRIGger | `TRIGger:TACHometer:HOLDoff` | command/query | yes | yes | `tachometer_holdoff` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| TRIGger | `TRIGger:TACHometer:LEVel` | command/query | yes | yes | `tachometer_level` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| TRIGger | `TRIGger:TACHometer:PCOunt` | command/query | yes | yes | `tachometer_pulse_count` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| TRIGger | `TRIGger:TACHometer:RANGe` | command/query | yes | yes | `tachometer_range` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |
| TRIGger | `TRIGger:TACHometer[:RPM]?` | query only | yes | yes | `tachometer_holdoff, tachometer_level, tachometer_pulse_count, tachometer_range, tachometer_rpm, ...` | Keysight35670A | safe | expected_protocol | Implemented in driver. |
| TRIGger | `TRIGger:TACHometer:SLOPe` | command/query | yes | yes | `tachometer_slope` | Keysight35670A | state-changing | expected_protocol | Implemented in driver. |

## Missing Commands By Subsystem
- none
