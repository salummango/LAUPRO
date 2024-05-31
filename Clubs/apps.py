from django.apps import AppConfig

class ClubsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Clubs'

    def ready(self):
        import Clubs.signals  # Import signals module