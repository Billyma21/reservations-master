from django.db import models

class Locality(models.Model):
    code_postal = models.CharField(max_length=6, verbose_name="Code postal")
    locality = models.CharField(max_length=60, verbose_name="Désignation officielle de la localité")

    class Meta:
        db_table = "localities"
        verbose_name = "Localité"
        verbose_name_plural = "Localités"

    def __str__(self):
        return self.nom


