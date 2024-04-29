#Bilal Maayoud - coté Admin

from django.contrib import admin

from .models import *
from .models.representation import Representation
from .models.user import User
from .models.roleUser import RoleUser
from .models.representationUser import RepresentationUser
from .models.artistTypeShow import ArtistTypeShow



#Edward Abrahamian - for import/export CSV
#Ed A. - pour les classes modelAdmin, important faire les déclarations dans cet ordre ==> (ImportExportModelAdmin, model) afin d'eviter l'erreur MRO
from import_export.admin import ImportExportModelAdmin

#Probleme avec search_fields concernant les fk des modèles
@admin.register(ArtistTypeShow)
class ArtistTypeShowAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ["artist_type", "show"]
    #search_fields = ["artist_type"]
    
@admin.register(ArtistType)
class ArtistTypeAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ["artist", "type"]

@admin.register(Artist)
class ArtistAdmin(ImportExportModelAdmin, admin.ModelAdmin,):
    list_display = ["id" , "firstname", "lastname"]
    ordering = ["id"]

@admin.register(Locality)
class LocalityAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ["nom" , "code_postal"]

@admin.register(Location)
class LocationAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ["designation", "locality", "address"]

@admin.register(RepresentationUser)
class RepresentationUserAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ["representation", "user", "places"]

@admin.register(Representation)
class RepresentationAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ["show", "when", "location"]

@admin.register(RoleUser)
class RoleUserAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ["user", "role"]

@admin.register(Role)
class RoleAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    pass

@admin.register(Show)
class ShowAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ["title", "location", "bookable", "price"]

@admin.register(Type)
class TypeAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ["type"]

@admin.register(User)
class UserAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ["email", "login", "langue"]
    search_fields = ["email", "login"]