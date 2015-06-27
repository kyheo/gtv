from django.apps import AppConfig


class _Config(AppConfig):
    name = 'gpx_track'
    verbose_name = 'GPX Track'

    def ready(self):
        import signals


default_app_config = 'gpx_track._Config'
