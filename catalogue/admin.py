#Bilal Maayoud - coté Admin

from django.contrib import admin

from .models import *

#EA Import CSV
from import_export.admin import ImportExportModelAdmin


admin.site.register(Artist, ImportExportModelAdmin)
class ArtistAdmin(admin.ModelAdmin):

    pass

admin.site.register(Show, ImportExportModelAdmin)
class ShowAdmin(admin.ModelAdmin):
    pass