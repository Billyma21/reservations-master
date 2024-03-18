from django.db import models
from .location import *

# Create your models here.
class Show(models.Model):
    # Clé primaire
    id = models.BigAutoField(primary_key=True, verbose_name="ID_spectacle")
    # Clé étrangère vers Location
    location = models.ForeignKey('Location', on_delete=models.SET_NULL, null=True, verbose_name="shows")
    slug = models.CharField(max_length=60, unique=True)
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255, null=True)
    posterUrl = models.CharField(max_length=255, null=True)
    bookable = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = "shows"
