from django.apps import AppConfig


# Aca le indicamos que el modelo POST quiero que me aparesca en DJango Admin
class PostConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'post'
