from django.db import models

class Role(models.Model):
    name = models.CharField(max_length=60, unique=True, verbose_name="Nom du rôle")

    class Meta:
        db_table = "roles"
        verbose_name = "Rôle"
        verbose_name_plural = "Rôles"

    def __str__(self):
        return self.name
