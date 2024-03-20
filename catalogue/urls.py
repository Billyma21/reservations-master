"""reservations.catalogue URL Configuration
"""
# Imgs 
from django.conf import settings
from django.conf.urls.static import static
from catalogue.views import index as home_index  
from django.urls import path, include
# from django.contrib import admin
# from django.urls import path, include
from . import views
from .views import *
from .views import show 
# from django.contrib.auth import views as auth_views

app_name='catalogue'

urlpatterns = [
    path('', views.home.index, name='home_index'),
    #Bilal - Pour vu sur artist
    path('artist/', views.artist.index, name='artist_index'),
    path('artist/<int:artist_id>', views.artist.show, name='artist_show'),
    #Bilal - Pour vu sur type
    path('type/', views.type.index, name='type_index'),
    path('type/<int:type_id>', views.type.show, name='type_show'),
    #Bilal - Pour vu sur locality
    path('locality/', locality.ListeLocalitesView.as_view(), name='locality_index'),
    path('locality/<int:pk>/', locality.DetailLocaliteView.as_view(), name='locality_show'),
    #Bilal - Pour vu sur Role 
    path('role/', views.role.index, name='role_index'),
	path('role/<int:role_id>', views.role.show, name='role_show'),
    #Bilal - Pour vu sur location 
    path('location/', views.location.index, name='location_index'),
	path('location/<int:location_id>', views.location.show, name='location_show'),
    #Bilal - Pour vu sur show 
    # path('show/', views.show.index, name='show_index'),
    # path('show/<int:show_id>', views.show.show, name='show_show'),
    path('show/', views.show, name='show_index'),
    path('show/<int:show_id>/', views.show, name='show_show'),
    #Bilal Ma - Authentifaction dans accounts/ 
    #Bilal ma - Add au panier pour paiement / Remove/ Del/ Add/ ..
    path('add_to_cart/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.view_cart, name='view_cart'), 
    path('remove_from_cart/<int:pk>/', remove_from_cart, name='remove_from_cart'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

