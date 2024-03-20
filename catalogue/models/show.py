from django.db import models
from .location import *

# Bm - Models show
class Show(models.Model):
    # Clé primaire
    id = models.BigAutoField(primary_key=True, verbose_name="ID_spectacle")
    # Clé étrangère vers Location
    location = models.ForeignKey('Location', on_delete=models.SET_NULL, null=True, verbose_name="localition_shows")
    slug = models.CharField(max_length=60, unique=True)
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255, null=True)
    poster = models.ImageField(upload_to='show/', null=True, blank=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, related_name='shows')
    bookable = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = "shows"
