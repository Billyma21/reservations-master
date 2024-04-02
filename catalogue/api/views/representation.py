from catalogue.models import *
from ..serializers import *
from rest_framework import generics


#GENERIC CLASS
class RepresentationList(generics.ListCreateAPIView):
    queryset = Representation.objects.all()
    serializer_class = RepresentationSerializer


class RepresentationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Representation.objects.all()
    serializer_class = RepresentationSerializer