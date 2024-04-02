from catalogue.models import *
from ..serializers import *
from rest_framework import generics


#GENERIC CLASS
class LocalityList(generics.ListCreateAPIView):
    queryset = Locality.objects.all()
    serializer_class = LocalitySerializer


class LocalityDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Locality.objects.all()
    serializer_class = LocalitySerializer