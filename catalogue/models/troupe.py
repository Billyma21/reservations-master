from django.db import models

# Modele
class Troupe(models.Model):
    id = models.BigAutoField(primary_key=True, verbose_name="ID_troupe")
    name = models.TextField(max_length=255, unique=True)
    logo_url = models.TextField(max_length=255)

    class Meta:
        db_table = "troupes"

    def __str__(self):
        return self.name