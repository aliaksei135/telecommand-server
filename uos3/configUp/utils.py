import struct

from .models import config

# https://truct.readthedocs.io/en/latest/#example-usage

CONFIG_BYTES_FORMAT_STR = ('?'  # CF00 tx_enable 1 
                           'B'  # CF01 tx_interval 8 
                           'B'  # CF02 tx_interval_downlink 8 
                           'B'  # CF03 tx_datarate 4 
                           'B'  # CF04 tx_power 4 
                           'B'  # CF05 batt_overtemp 8 
                           'B'  # CF06 obc_overtemp 8 
                           'B'  # CF07 pa_overtemp 8 
                           'f'  # CF08 low_voltage_threshold 8 
                           'f'  # CF09 low_voltage_recovery 8 
                           'H'  # CF10 eps_health_acquisition_interval 16 
                           'H'  # CF11 check_health_acquisition_interval 16 
                           'H'  # CF12 imu_acquisition_interval 16 
                           'B'  # CF13 imu_sample_count 4 
                           'H'  # CF14 imu_sample_interval 8 
                           'B'  # CF15 imu_gyro_bandwidth 3 
                           'B'  # CF16 imu_gyro_measurement_range 2 
                           'H'  # CF17 gps_acquisition_interval 16 
                           'B'  # CF18 gps_sample_count 3 
                           'H'  # CF19 gps_sample_interval 8 
                           'B'  # CF20 image_acquisition_profile 2 
                           '?'  # CF21 power_rail_1 1 
                           '?'  # CF22 power_rail_3 1 
                           '?'  # CF23 power_rail_5 1 
                           '?'  # CF24 power_rail_6 1 
                           '?'  # CF25 imu_accel_enabled 1 
                           '?'  # CF26 imu_gyro_enabled 1 
                           '?'  # CF27 imu_magno_enabled 1 
                           '?'  # CF28 silent_flag 1
                           )

TELECOMMAND_BYTES_FORMAT_STR = ('L'  # TC0 time 32 
                                'B'  # TC1 operational_mode 4 
                                '?'  # TC2 self_test 1 
                                '?'  # TC3 reset_power_rail_1 1 
                                '?'  # TC4 reset_power_rail_2 1 
                                '?'  # TC5 reset_power_rail_3 1 
                                '?'  # TC6 reset_power_rail_4 1 
                                '?'  # TC7 reset_power_rail_5 1 
                                '?'  # TC8 reset_power_rail_6 1 
                                'H'  # TC9 telemetry_go_silent 16 
                                'L'  # TC10 downlink_stop_time 32 
                                'L'  # TC11 image_acquisition_time 32
                                )


def config_to_binary(instance):
    """
        Encode telecommand and configuration to format specified by
        SCF v2.1 20190830
    :param instance: instance of config model
    :return: tuple of (telecommand bytes, configuration bytes)
    """

    telecommand_bytes = struct.pack(TELECOMMAND_BYTES_FORMAT_STR,
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

    config_bytes = struct.pack(CONFIG_BYTES_FORMAT_STR,
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


def binary_to_config(telecommand_bytes, config_bytes):
    telecommands = struct.unpack(TELECOMMAND_BYTES_FORMAT_STR, telecommand_bytes)
    configuration = struct.unpack(CONFIG_BYTES_FORMAT_STR, config_bytes)

    config_instance = config(
        tx_enable=configuration[0],
        tx_interval=configuration[1],
        tx_interval_downlink=configuration[2],
        tx_datarate=configuration[3],
        tx_power=configuration[4],
        batt_overtemp=configuration[5],
        obc_overtemp=configuration[6],
        pa_overtemp=configuration[7],
        low_voltage_threshold=configuration[8],
        low_voltage_recovery=configuration[9],
        eps_health_acquisition_interval=configuration[10],
        check_health_acquisition_interval=configuration[11],
        imu_acquisition_interval=configuration[12],
        imu_sample_count=configuration[13],
        imu_sample_interval=configuration[14],
        imu_gyro_bandwidth=configuration[15],
        imu_gyro_measurement_range=configuration[16],
        gps_acquisition_interval=configuration[17],
        gps_sample_count=configuration[18],
        gps_sample_interval=configuration[19],
        image_acquisition_profile=configuration[20],
        power_rail_1=configuration[21],
        power_rail_3=configuration[22],
        power_rail_5=configuration[23],
        power_rail_6=configuration[24],
        imu_accel_enabled=configuration[25],
        imu_gyro_enabled=configuration[26],
        imu_magno_enabled=configuration[27],
        silent_flag=configuration[28],

        time=telecommands[0],
        operational_mode=telecommands[1],
        self_test=telecommands[2],
        reset_power_rail_1=telecommands[3],
        reset_power_rail_2=telecommands[4],
        reset_power_rail_3=telecommands[5],
        reset_power_rail_4=telecommands[6],
        reset_power_rail_5=telecommands[7],
        reset_power_rail_6=telecommands[8],
        telemetry_go_silent=telecommands[9],
        downlink_stop_time=telecommands[10],
        image_acquisition_time=telecommands[11]
    )
    return config_instance
