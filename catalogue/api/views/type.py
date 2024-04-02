from catalogue.models import *
from ..serializers import *
from rest_framework import generics


#GENERIC CLASS
class TypeList(generics.ListCreateAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer


class TypeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = TypeSerializer