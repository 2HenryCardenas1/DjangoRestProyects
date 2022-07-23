from django.db import models
from django.contrib.auth.models import AbstractUser


# para que se ingrese con el correo
class User(AbstractUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
