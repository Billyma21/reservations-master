from django.db import models
from .location import *

# Create your models here.
class Show(models.Model):
    
	location 	= models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, related_name='shows')    
	slug 		= models.CharField(max_length=60, unique=True)
	title 		= models.CharField(max_length=255)
	posterUrl 	= models.CharField(max_length=255, null=True)

	bookable 	= models.BooleanField(default=True)
	price 		= models.DecimalField(max_digits=10, decimal_places=2, null=True)
	description = models.TextField(max_length=255, null=True)
 
	created_at 	= models.DateTimeField(auto_now_add=True, null=True)
	updated_at 	= models.DateTimeField(auto_now=True)
	
	class Meta:
		db_table = "shows"
