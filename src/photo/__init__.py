from django.apps import AppConfig


class _Config(AppConfig):
    name = 'photo'
    verbose_name = 'Photo'

    def ready(self):
        import signals


default_app_config = 'photo._Config'

