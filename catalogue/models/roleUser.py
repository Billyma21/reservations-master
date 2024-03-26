from django.db import models
from .role import *
from .user import *

class RoleUser (models.Model):
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True, related_name='role_user')
    user = models.ForeignKey(User, on_delete=models.SET_NULL , null=True, related_name='role_user')

    class Meta:
        db_table = 'role_user'