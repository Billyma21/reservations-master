from django.db import models

class Role(models.Model):
    #Clé primaire
    id = models.BigAutoField(primary_key=True, verbose_name="ID_role")
    name = models.CharField(max_length=60, unique=True, verbose_name="Nom du rôle")

    class Meta:
        db_table = "roles"
        verbose_name = "Rôle"
        verbose_name_plural = "Rôles"

    def __str__(self):
        return self.name