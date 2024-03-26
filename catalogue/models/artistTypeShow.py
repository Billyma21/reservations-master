from django.db import models
from .artist import *
from .show import *

# Create your models here.
class ArtistTypeShow(models.Model):
	artist_type_show = models.ForeignKey(Artist, on_delete=models.SET_NULL , null=True, related_name='artiste_type_show')
	show = models.ForeignKey(Show, on_delete=models.SET_NULL , null=True, related_name='artiste_type_show')
	
	class Meta:
		db_table = "artiste_type_show"