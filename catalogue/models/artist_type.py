from django.db import models
from .artist import *
from .type import *

class Artist_type(models.Model):
    artist   = models.ForeignKey(Artist, on_delete=models.CASCADE)
    type    = models.ForeignKey(Type, on_delete=models.CASCADE)
    
    class Meta:
	    db_table = "artist_type"
  