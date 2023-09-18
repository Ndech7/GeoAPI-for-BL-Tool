from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from . models import Sites

# Register your models here.
@admin.register(Sites)
class SitesAdmin(OSMGeoAdmin):
    list_display = ('name', 'location')
