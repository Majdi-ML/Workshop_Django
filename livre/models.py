from django.db import models

# Create your models here.
from datetime import datetime

from auteur.models import Auteur
# Create your models here.


class Livre(models.Model):
    titre = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    date_publication = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True)

    auteur = models.ForeignKey(Auteur, on_delete=models.CASCADE)
