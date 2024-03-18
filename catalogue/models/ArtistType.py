from django.db import models
from .artist import *
from .type import *



class ArtistType(models.Model):
    # Clé primaire
    id = models.BigAutoField(primary_key=True, verbose_name="ID_artiste-type")
    # Clé étrangère vers Artist
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, verbose_name="ID_artiste")
    # Clé étrangère vers Type
    type = models.ForeignKey(Type, on_delete=models.CASCADE, verbose_name="Fonction_artiste")


        
