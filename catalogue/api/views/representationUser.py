from catalogue.models import *
from ..serializers import *
from rest_framework import generics


#GENERIC CLASS
class RepresentationUserList(generics.ListCreateAPIView):
    queryset = RepresentationUser.objects.all()
    serializer_class = RepresentationUserSerializer


class RepresentationUserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = RepresentationUser.objects.all()
    serializer_class = RepresentationUserSerializer