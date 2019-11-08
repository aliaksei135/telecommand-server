from time import time

from django.test import TestCase

from . import utils
from .models import config


class BinaryConversionTests(TestCase):

    def test_binary_encoding_and_decoding(self):
        """binary_encoding_and_decoding returns True if config encoded and decoded successfully"""
        config_instance = config(
            confirmed_uplink=False,
            time=int(time()),
            downlink_stop_time=5,
            image_acquisition_time=5,
            silent_flag=False
        )
        cmd_bytes, config_bytes = utils.config_to_binary(config_instance)
        converted_config = utils.binary_to_config(cmd_bytes, config_bytes)

        config_fields = [f.name for f in config_instance._meta.fields[6:]]
        for field in config_fields:
            if config_instance.__getattribute__(field) != converted_config.__getattribute__(field):
                return False

        return True
