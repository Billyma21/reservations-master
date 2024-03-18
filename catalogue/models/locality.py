from django.db import models

class Locality(models.Model):
    nom = models.CharField(max_length=255, verbose_name="Nom de la localité")
    code_postal = models.CharField(max_length=12, verbose_name="Code postal")
    id = models.BigAutoField(primary_key=True, verbose_name="ID_localité")

    class Meta:
        db_table = "localities"
        verbose_name = "Localité"
        verbose_name_plural = "Localités"

    def __str__(self):
        return self.nom


