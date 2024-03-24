#Bilal Maayoud - coté Admin

from django.contrib import admin

from .models import *

#Edward Abrahamian - for import/export CSV
from import_export.admin import ImportExportModelAdmin


admin.site.register(Artist, ImportExportModelAdmin)
class ArtistAdmin(admin.ModelAdmin):
    pass

admin.site.register(Show, ImportExportModelAdmin)
class ShowAdmin(admin.ModelAdmin):
    pass

admin.site.register(Type, ImportExportModelAdmin)
class TypeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Role, ImportExportModelAdmin)
class RoleAdmin(admin.ModelAdmin):
    pass

admin.site.register(Location, ImportExportModelAdmin)
class LocationAdmin(admin.ModelAdmin):
    pass

admin.site.register(Locality, ImportExportModelAdmin)
class LocalityAdmin(admin.ModelAdmin):
    pass