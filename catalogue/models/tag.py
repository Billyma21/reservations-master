from django.db import models
from .show import *

# Create your models here.
class Tag(models.Model):
    # Clé primaire
    id = models.BigAutoField(primary_key=True, verbose_name="ID_tag")
    #Clé étrangère vers Show
    show = models.ForeignKey(Show, on_delete=models.SET_NULL , null=True, verbose_name="ID_spectacle")
    type = models.TextField(unique=True, max_length=30, verbose_name="Mot_cle")
    
    class Meta:
        db_table = "tags"

    def __str__(self):
        return self.type
