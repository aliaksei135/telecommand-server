from django.apps import AppConfig

class ConfigupConfig(AppConfig):
    name = 'configUp'

    def ready(self):
        # Register signals from decorations
        pass
