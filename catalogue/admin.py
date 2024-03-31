#Bilal Maayoud - coté Admin

from django.contrib import admin

from .models import *
from .models.representation import Representation
from .models.user import User
from .models.roleUser import RoleUser
from .models.representationUser import RepresentationUser
from .models.artistTypeShow import ArtistTypeShow



#Edward Abrahamian - for import/export CSV
from import_export.admin import ImportExportModelAdmin


admin.site.register(Artist, ImportExportModelAdmin)
class ArtistAdmin(admin.ModelAdmin):
    pass

admin.site.register(ArtistType, ImportExportModelAdmin)
class ArtistTypeAdmin(admin.ModelAdmin):
    pass

admin.site.register(ArtistTypeShow, ImportExportModelAdmin)
class ArtistTypeShowAdmin(admin.ModelAdmin):
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

admin.site.register(Representation, ImportExportModelAdmin)
class RepresentationAdmin(admin.ModelAdmin):
    pass

admin.site.register(RepresentationUser, ImportExportModelAdmin)
class RepresentationUserAdmin(admin.ModelAdmin):
    pass

admin.site.register(User, ImportExportModelAdmin)
class UserAdmin(admin.ModelAdmin):
    pass

admin.site.register(RoleUser, ImportExportModelAdmin)
class RoleUserAdmin(admin.ModelAdmin):
    pass