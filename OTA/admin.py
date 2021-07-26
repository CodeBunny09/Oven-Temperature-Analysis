from django.contrib import admin
from .models import Temp, Oven
from import_export import resources
from import_export.admin import ImportExportActionModelAdmin
# Register your models here.


admin.site.register(Oven)

class TempResource(resources.ModelResource):
    class Meta:
        model = Temp

class TempAdmin(ImportExportActionModelAdmin):
    resource_class = TempResource
    ordering = ('id',)
    list_display = ('id', 'date', 'time', 'cyclic_hours', 'temperature', 'oven')

admin.site.register(Temp, TempAdmin)