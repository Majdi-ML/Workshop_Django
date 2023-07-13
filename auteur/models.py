from django.db import models
from django.contrib.auth.models import AbstractUser


class Auteur(AbstractUser):
    username = models.CharField(unique=True, max_length=8)
    bio = models.CharField("bio", max_length=50)

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = "Auteur"
