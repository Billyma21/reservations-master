from django.db import models

# Create your models here.
class Type(models.Model):
    # Clé primaire
    id = models.BigAutoField(primary_key=True, verbose_name="ID_type")
    type = models.CharField(max_length=60, verbose_name="Fonction_artiste")
    
    class Meta:
        db_table = "types"
