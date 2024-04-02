from catalogue.models import *
from ..serializers import *
from rest_framework import generics


#GENERIC CLASS
class RoleUserList(generics.ListCreateAPIView):
    queryset = RoleUser.objects.all()
    serializer_class = RoleUserSerializer


class RoleUserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RoleUser.objects.all()
    serializer_class = RoleUserSerializer