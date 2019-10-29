import usb.core
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save)
def receive_new_config(sender, **kwargs):
    new_config = kwargs['instance']
    # Ensure config is being uploaded, not just saved
    if new_config.confirmed_uplink:
        print('Writing new config to USB')
        # Write config fields to usb...
        devices = usb.core.find()
