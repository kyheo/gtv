
from django.contrib import admin
from django.contrib.gis import admin as geoadmin
import models


@admin.register(models.GPXFile)
class GPXFileAdmin(admin.ModelAdmin):
    list_display = ('id', 'file_name', 'user', 'updated')
    list_display_links = ('id',)
    readonly_fields = ('created', 'updated', 'user')

    def file_name(self, instance):
        return instance.file.name

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()


class GPXTrackAdmin(geoadmin.OSMGeoAdmin):
    modifiable = False
    list_display = ('id', 'name', 'date_start_at_location',
                    'date_end_at_location', 'updated')
    readonly_fields = ('date_start', 'date_end', 'date_start_at_location',
                       'date_end_at_location', 'created', 'updated', 'user',
                       'file',)
geoadmin.site.register(models.GPXTrack, GPXTrackAdmin)
