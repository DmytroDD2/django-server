from django.apps import AppConfig


class MyModelConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'my_model'
