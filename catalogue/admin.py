#Bilal Maayoud - coté Admin

from django.contrib import admin

from .models import *

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    pass

@admin.register(Show)
class ShowAdmin(admin.ModelAdmin):
    pass