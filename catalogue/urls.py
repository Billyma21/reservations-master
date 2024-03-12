"""reservations.catalogue URL Configuration
"""
# Imgs 
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
# from django.contrib import admin
# from django.urls import path, include
from . import views
from .views import *
from .views import show 

app_name='catalogue'

urlpatterns = [
    #Bilal - Pour vu sur Admin
    # path('admin/', admin.site.urls),
    # #Bilal - Pour vu sur catalogue
    # path('catalogue/', include('catalogue.urls')),
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
    path('show/', index, name='show_index'),
    path('show/<int:show_id>/', views.show, name='show_show'),


]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

