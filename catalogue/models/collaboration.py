from django.db import models
from .show import *
from .ArtistType import *


class Collaboration(models.Model):
    # Clé primaire
    id = models.BigAutoField(primary_key=True, verbose_name="ID_collaboration")
    # Clé étrangère vers ArtistType
    artist_type = models.ForeignKey(ArtistType, on_delete=models.CASCADE, verbose_name="Artiste_type")
    # Clé étrangère vers Show
    show = models.ForeignKey(Show, on_delete=models.CASCADE, verbose_name="Shows")
