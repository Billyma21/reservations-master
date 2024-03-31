from django.db import models
from .location import *
from .show import *

class Representation(models.Model):
	#Clé primaire
	id = models.BigAutoField(primary_key=True, verbose_name="ID_representation")
	#Clé étrangère vers Show
	show = models.ForeignKey(Show, on_delete=models.SET_NULL, null=True, verbose_name="ID_spectacle")
	when = models.DateTimeField
	#Clé étrangère vers Location
	location = models.ForeignKey(Location, on_delete=models.SET_NULL , null=True, verbose_name="ID_lieu")

	class Meta:
		db_table = "representations"
	
	def __str__(self):
		return self.show.slug