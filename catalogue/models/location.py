from django.db import models
from .locality import *

# Create your models here.
class Location(models.Model):
    # Clé primaire
    id = models.BigAutoField(primary_key=True, verbose_name="ID_lieu")
    # Clé étrangère vers Locality
    locality = models.ForeignKey(Locality, on_delete=models.SET_NULL, null=True, verbose_name='locations')
    slug = models.CharField(max_length=60, unique=True)
    designation = models.CharField(max_length=60)
    address = models.CharField(max_length=255)
    website = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=30, null=True)
    
    class Meta:
        db_table = "locations"
    
    def __str__(self):
        return self.slug
