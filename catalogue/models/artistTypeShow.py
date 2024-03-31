from django.db import models
from .ArtistType import *
from .show import *

# Create your models here.
class ArtistTypeShow(models.Model):
	#Clé primaire
	id = models.BigAutoField(primary_key=True, verbose_name="ID_artiste-type-show")
	#Clé étrangère vers Artist
	artist_type = models.ForeignKey(ArtistType, on_delete=models.SET_NULL , null=True, verbose_name="ID_artiste-type")
	#Clé étrangère vers Show
	show = models.ForeignKey(Show, on_delete=models.SET_NULL , null=True, verbose_name="ID_spectacle")
	
	class Meta:
		db_table = "artiste_type_show"

	def __str__(self):
		return self.artist_type.artist.firstname +" "+ self.artist_type.artist.lastname