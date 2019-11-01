import datetime

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class config(models.Model):
    choices_tx_interval_downlink = (
        (0, '0 ms'),
        (50, '500 ms'),
        (60, '600 ms'),
        (70, '700 ms'),
        (80, '800 ms'),
        (90, '900 ms'),
        (100, '1000 ms'),
        (150, '1500 ms'),
        (200, '2000 ms'),
    )
    choices_tx_datarate = (
        (0, '0.25 kbps'),
        (3, '0.5 kbps'),
        (6, '1 kbps'),
        (9, '3 kbps'),
        (12, '6 kbps'),
    )
    choices_tx_power = (
        (0, '10 mW'),
        (3, '50 mW'),
        (6, '100 mW'),
        (9, '200 mW'),
        (12, '300 mW'),
    )
    choices_imu_gyro_bandwidth = (
        (0, '5Hz'),
        (1, '10Hz'),
        (2, '20Hz'),
        (3, '41Hz'),
        (4, '92Hz'),
        (5, '184Hz'),
        (6, '250Hz'),
        (7, '3600Hz')
    )
    choices_imu_gyro_measurement_range = (
        (0, '+250dps'),
        (1, '+500dps'),
        (2, '+1000dps'),
        (3, '+2000dps')
    )
    choices_image_acquisition_profile = (
        (0, '1600x1200'),
        (1, '1280x960'),
        (2, '800x600'),
        (3, '640x480'),
    )
    choices_operational_mode = (
        (0, 'Normal Mode'),
        (2, 'Safe Mode'),
    )
    choices_bool = (
        (0, 'Off'),
        (1, 'On'),
    )

    # Meta fields
    date_submitted = models.DateTimeField(auto_now_add=True, editable=False)
    date_modified = models.DateTimeField(auto_now=True, editable=False)
    user_submitted = models.CharField(max_length=64, default='uos3', editable=False)
    confirmed_uplink = models.BooleanField(default=False, editable=False)
    date_uplink = models.DateTimeField(default=datetime.datetime(1970, 1, 1), editable=False, blank=True)

    # Config fields
    tx_enable = models.BooleanField(choices=choices_bool, default=True)
    tx_interval = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(255)],
                                                   default=60)
    tx_interval_downlink = models.IntegerField(choices=choices_tx_interval_downlink, default=50)
    tx_datarate = models.IntegerField(choices=choices_tx_datarate, default=12)
    tx_power = models.IntegerField(choices=choices_tx_power, default=12)

    batt_overtemp = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(255)],
                                                     default=40)
    obc_overtemp = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(255)],
                                                    default=75)
    pa_overtemp = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(255)],
                                                   default=75)

    low_voltage_threshold = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(25.5)], default=7.5)
    low_voltage_recovery = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(25.5)], default=7.8)

    eps_health_acquisition_interval = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(65535)], default=300)
    check_health_acquisition_interval = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(65535)], default=30)

    imu_acquisition_interval = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(65535)],
                                                           default=600)
    imu_sample_count = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(6)],
                                                        default=6)
    imu_sample_interval = models.PositiveSmallIntegerField(validators=[MinValueValidator(10), MaxValueValidator(2550)],
                                                           default=500)
    imu_gyro_bandwidth = models.IntegerField(choices=choices_imu_gyro_bandwidth, default=4)
    imu_gyro_measurement_range = models.IntegerField(choices=choices_imu_gyro_measurement_range, default=0)

    gps_acquisition_interval = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(65535)],
                                                           default=600)
    gps_sample_count = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(4)],
                                                        default=4)
    gps_sample_interval = models.PositiveSmallIntegerField(validators=[MinValueValidator(10), MaxValueValidator(2550)],
                                                           default=500)

    image_acquisition_profile = models.IntegerField(choices=choices_image_acquisition_profile, default=3)

    power_rail_1 = models.IntegerField(choices=choices_bool, default=True)
    power_rail_3 = models.IntegerField(choices=choices_bool, default=True)
    power_rail_5 = models.IntegerField(choices=choices_bool, default=True)
    power_rail_6 = models.IntegerField(choices=choices_bool, default=True)

    imu_accel_enabled = models.IntegerField(choices=choices_bool, default=True)
    imu_gyro_enabled = models.IntegerField(choices=choices_bool, default=True)
    imu_magno_enabled = models.IntegerField(choices=choices_bool, default=True)

    silent_flag = models.BooleanField(choices=choices_bool, default=False)

    # Telecommand fields
    time = models.BigIntegerField(validators=[MinValueValidator(0), MaxValueValidator(4294967295)])
    operational_mode = models.IntegerField(choices=choices_operational_mode, default=0)
    self_test = models.IntegerField(choices=choices_bool, default=False)
    reset_power_rail_1 = models.IntegerField(choices=choices_bool, default=False)
    reset_power_rail_2 = models.IntegerField(choices=choices_bool, default=False)
    reset_power_rail_3 = models.IntegerField(choices=choices_bool, default=False)
    reset_power_rail_4 = models.IntegerField(choices=choices_bool, default=False)
    reset_power_rail_5 = models.IntegerField(choices=choices_bool, default=False)
    reset_power_rail_6 = models.IntegerField(choices=choices_bool, default=False)
    telemetry_go_silent = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(32768)],
                                                           default=0)
    downlink_stop_time = models.BigIntegerField(validators=[MinValueValidator(0), MaxValueValidator(4294967295)])
    image_acquisition_time = models.BigIntegerField(validators=[MinValueValidator(0), MaxValueValidator(4294967295)])
