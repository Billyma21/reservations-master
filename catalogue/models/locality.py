from django.db import models

class Locality(models.Model):
    #Clé primaire
    id = models.BigAutoField(primary_key=True, verbose_name="ID_localité")
    code_postal = models.CharField(unique=True ,max_length=12, verbose_name="Code postal")
    nom = models.CharField(unique=True, max_length=255, verbose_name="Nom de la localité")

    class Meta:
        db_table = "localities"
        verbose_name = "Localité"
        verbose_name_plural = "Localités"

    def __str__(self):
        return self.nom


