from . import utils


# @receiver(post_save)
def receive_new_config(sender, **kwargs):
    new_config = kwargs['instance']
    # Ensure config is being uploaded, not just saved
    if new_config.confirmed_uplink:
        print('Writing new config to USB')
        config_bytes = utils.config_to_binary(new_config)
        with open('D:\\config.bin', 'wb') as file:
            file.write(config_bytes[1])
        with open('D:\\telecommand.bin', 'wb') as file:
            file.write(config_bytes[0])
        # Write config fields to usb...
    return
