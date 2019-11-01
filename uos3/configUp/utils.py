import bitstruct

# https://bitstruct.readthedocs.io/en/latest/#example-usage

CONFIG_BYTES_FORMAT_STR = ('b1'  # CF00 tx_enable 1 bits
                           'u8'  # CF01 tx_interval 8 bits
                           'u8'  # CF02 tx_interval_downlink 8 bits
                           'u4'  # CF03 tx_datarate 4 bits
                           'u4'  # CF04 tx_power 4 bits
                           'u8'  # CF05 batt_overtemp 8 bits
                           'u8'  # CF06 obc_overtemp 8 bits
                           'u8'  # CF07 pa_overtemp 8 bits
                           'f8'  # CF08 low_voltage_threshold 8 bits
                           'f8'  # CF09 low_voltage_recovery 8 bits
                           'u16'  # CF10 eps_health_acquisition_interval 16 bits
                           'u16'  # CF11 check_health_acquisition_interval 16 bits
                           'u16'  # CF12 imu_acquisition_interval 16 bits
                           'u4'  # CF13 imu_sample_count 4 bits
                           'u8'  # CF14 imu_sample_interval 8 bits
                           'u3'  # CF15 imu_gyro_bandwidth 3 bits
                           'u2'  # CF16 imu_gyro_measurement_range 2 bits
                           'u16'  # CF17 gps_acquisition_interval 16 bits
                           'u3'  # CF18 gps_sample_count 3 bits
                           'u8'  # CF19 gps_sample_interval 8 bits
                           'u2'  # CF20 image_acquisition_profile 2 bits
                           'b1'  # CF21 power_rail_1 1 bits
                           'b1'  # CF22 power_rail_3 1 bits
                           'b1'  # CF23 power_rail_5 1 bits
                           'b1'  # CF24 power_rail_6 1 bits
                           'b1'  # CF25 imu_accel_enabled 1 bits
                           'b1'  # CF26 imu_gyro_enabled 1 bits
                           'b1'  # CF27 imu_magno_enabled 1 bits
                           'b1'  # CF28 silent_flag 1 bits
                           'p1'  # PADDING to bring to multiple of 8
                           )

TELECOMMAND_BYTES_FORMAT_STR = ('u32'  # TC0 time 32 bits
                                'u4'  # TC1 operational_mode 4 bits
                                'b1'  # TC2 self_test 1 bits
                                'b1'  # TC3 reset_power_rail_1 1 bits
                                'b1'  # TC4 reset_power_rail_2 1 bits
                                'b1'  # TC5 reset_power_rail_3 1 bits
                                'b1'  # TC6 reset_power_rail_4 1 bits
                                'b1'  # TC7 reset_power_rail_5 1 bits
                                'b1'  # TC8 reset_power_rail_6 1 bits
                                'u16'  # TC9 telemetry_go_silent 16 bits
                                'u32'  # TC10 downlink_stop_time 32 bits
                                'u32'  # TC11 image_acquisition_time 32 bits
                                'p1'  # PADDING to bring to multiple of 8
                                )


def config_to_binary(instance):
    '''
        Encode telecommand and configuration to format specified by
        SCF v2.1 20190830
    :param instance: instance of config model
    :return: tuple of (telecommand bytes, configuration bytes)
    '''

    telecommand_bytes = bitstruct.pack(TELECOMMAND_BYTES_FORMAT_STR,
                                       instance.time,
                                       instance.operational_mode,
                                       instance.self_test,
                                       instance.reset_power_rail_1,
                                       instance.reset_power_rail_2,
                                       instance.reset_power_rail_3,
                                       instance.reset_power_rail_4,
                                       instance.reset_power_rail_5,
                                       instance.reset_power_rail_6,
                                       instance.telemetry_go_silent,
                                       instance.downlink_stop_time,
                                       instance.image_acquisition_time)

    config_bytes = bitstruct.pack(CONFIG_BYTES_FORMAT_STR,
                                  instance.tx_enable,
                                  instance.tx_interval,
                                  instance.tx_interval_downlink,
                                  instance.tx_datarate,
                                  instance.tx_power,
                                  instance.batt_overtemp,
                                  instance.obc_overtemp,
                                  instance.pa_overtemp,
                                  instance.low_voltage_threshold,
                                  instance.low_voltage_recovery,
                                  instance.eps_health_acquisition_interval,
                                  instance.check_health_acquisition_interval,
                                  instance.imu_acquisition_interval,
                                  instance.imu_sample_count,
                                  instance.imu_sample_interval,
                                  instance.imu_gyro_bandwidth,
                                  instance.imu_gyro_measurement_range,
                                  instance.gps_acquisition_interval,
                                  instance.gps_sample_count,
                                  instance.gps_sample_interval,
                                  instance.image_acquisition_profile,
                                  instance.power_rail_1,
                                  instance.power_rail_3,
                                  instance.power_rail_5,
                                  instance.power_rail_6,
                                  instance.imu_accel_enabled,
                                  instance.imu_gyro_enabled,
                                  instance.imu_magno_enabled,
                                  instance.silent_flag)
    return telecommand_bytes, config_bytes
