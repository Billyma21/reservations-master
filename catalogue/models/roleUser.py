from django.db import models
from .role import *
from .user import *

class RoleUser (models.Model):
    #Clé primaire
    id = models.BigAutoField(primary_key=True, verbose_name="ID_role-user")
    #Clé étrangère vers Role
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, verbose_name="role_user")
    #Clé étrangère vers User
    user = models.ForeignKey(User, on_delete=models.SET_NULL , null=True, verbose_name="ID_user")

    class Meta:
        db_table = 'role_user'

    def __str__(self):
        return self.user.firstname +" "+ self.user.lastname