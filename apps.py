from django.apps import AppConfig


class FilecomparerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'filecomparer'


    def ready(self):
        import filecomparer.signals
