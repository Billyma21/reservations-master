from django.db import models
from .artist_type import *
from .show import *

class Artist_type_show(models.Model):
    artist_type   = models.ForeignKey(Artist_type, on_delete=models.CASCADE)
    show    = models.ForeignKey(Show, on_delete=models.CASCADE)
    
    class Meta:
	    db_table = "artist_type_show"    