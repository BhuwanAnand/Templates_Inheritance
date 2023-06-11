from django.apps import AppConfig


class Inherit1Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Inherit1'
