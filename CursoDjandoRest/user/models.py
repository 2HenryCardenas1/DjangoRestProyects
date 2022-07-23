from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True)
    # blank=True es un NULL en DB
    web_site = models.CharField(max_length=255, blank=True)

    # Esto es para iniciar sesion con el email
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
