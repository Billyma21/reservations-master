from django.db import models
from .locality import *

# Create your models here.
class Location(models.Model):
	locality 	= models.ForeignKey(Locality, on_delete=models.SET_NULL , null=True, related_name='locations')
	slug 		= models.CharField(max_length=60, unique=True)
	designation = models.CharField(max_length=60)
 
	address 	= models.CharField(max_length=255)
	website 	= models.CharField(max_length=255, null=True)
	phone 		= models.CharField(max_length=30, null=True)
	
	class Meta:
		db_table = "locations"
