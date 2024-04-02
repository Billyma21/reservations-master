from catalogue.models import *
from ..serializers import *
from rest_framework import generics


#GENERIC CLASS
class ArtistTypeShowList(generics.ListCreateAPIView):
    queryset = ArtistTypeShow.objects.all()
    serializer_class = ArtistTypeShowSerializer


class ArtistTypeShowDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ArtistTypeShow.objects.all()
    serializer_class = ArtistTypeShowSerializer