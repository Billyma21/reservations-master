"""reservations.catalogue URL Configuration
"""
from django.urls import path

from . import views
from .views import *
app_name='catalogue'

urlpatterns = [
    path('artist/', views.artist.index, name='artist_index'),
    path('artist/<int:artist_id>', views.artist.show, name='artist_show'),
    path('type/', views.type.index, name='type_index'),
    path('type/<int:type_id>', views.type.show, name='type_show'),
    path('locality/', locality.ListeLocalitesView.as_view(), name='locality_index'),
    path('locality/<int:pk>/', locality.DetailLocaliteView.as_view(), name='locality_show'),

]
