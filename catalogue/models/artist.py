# models artirst

from django.db import models

class Artist(models.Model):
    #Clé primaire
    id = models.BigAutoField(primary_key=True, verbose_name="ID_artiste")
    firstname = models.CharField(max_length=60)
    lastname = models.CharField(max_length=60)
    
    def __str__(self):
        return self.firstname +" "+ self.lastname
    
    class Meta:
        db_table = "artists"
  