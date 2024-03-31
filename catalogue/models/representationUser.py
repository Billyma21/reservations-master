from django.db import models
from .representation import *
from .user import *

class RepresentationUser(models.Model):
    #Clé primaire
    id = models.BigAutoField(primary_key=True, verbose_name="ID_representation-user")
    #Clé étrangère vers Representation
    representation = models.ForeignKey(Representation, on_delete=models.SET_NULL, null=True, verbose_name="ID_representation")
    #Clé étrangère vers User
    user = models.ForeignKey(User, on_delete=models.SET_NULL , null=True, verbose_name="ID_user")
    places = models.IntegerField

    class Meta:
       db_table = "representation_user"
    
    def __str__(self):
        return self.user.firstname