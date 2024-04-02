from catalogue.models import *
from ..serializers import *
#for class using mixins
from rest_framework import generics


#GENERIC CLASS
class ArtistTypeList(generics.ListCreateAPIView):
    queryset = ArtistType.objects.all()
    serializer_class = ArtistTypeSerializer


class ArtistTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ArtistType.objects.all()
    serializer_class = ArtistTypeSerializer