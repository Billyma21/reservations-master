from django.db import models

class User(models.Model):
	#Clé primaire
	id = models.BigAutoField(primary_key=True, verbose_name="ID_user")
	login = models.CharField(max_length=30)
	password = models.CharField(max_length=255)
	firstname = models.CharField(max_length=60)
	lastname = models.CharField(max_length=60)
	email = models.CharField(max_length=100)
	langue = models.CharField(max_length=2)
	
	class Meta:
		db_table = "users"

	def __str__(self):
		return self.firstname +" "+ self.lastname