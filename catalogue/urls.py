"""reservations.catalogue URL Configuration
"""
from django.urls import path

from . import views
from .views import *
app_name='catalogue'

urlpatterns = [
    #Bilal - Pour vu sur artist
    path('artist/', views.artist.index, name='artist_index'),
    path('artist/<int:artist_id>', views.artist.show, name='artist_show'),
    #Bilal - Pour vu sur type
    path('type/', views.type.index, name='type_index'),
    path('type/<int:type_id>', views.type.show, name='type_show'),
    #Bilal - Pour vu sur locality
    path('locality/', locality.ListeLocalitesView.as_view(), name='locality_index'),
    path('locality/<int:pk>/', locality.DetailLocaliteView.as_view(), name='locality_show'),
    #Bilal - 

]
