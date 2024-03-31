from catalogue.models import *
from ..serializers import *
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


#API GET

api_view(['GET', 'POST'])
def artist_list(request):

    if request.method == 'GET':
        artists = Artist.objects.all()
        serializer = ArtistSerializer(artists, many=True)
        return JsonResponse({"artists": serializer.data})
    
    if request.metjod == 'POST':
       serializer = ArtistSerializer(data=request.data)
       if serializer.is_calid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
       

api_view(['GET', 'PUT','DELETE'])
def artist_detail(request, id):

    try:
        artist = Artist.objects.get(pk=id)
    except Artist.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method =='GET':
        serializer = ArtistSerializer(artist)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ArtistSerializer(artist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        artist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)