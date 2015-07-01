from django.contrib.gis import admin as geoadmin
import models


class PhotoAdmin(geoadmin.OSMGeoAdmin):
    list_display_links = ('id', 'image_thumb')
    list_display = ('id', 'image_thumb', 'created', 'updated')
    readonly_fields = ('image_thumb', 'created', 'updated', 'user')

    def image_thumb(self, instance):
        return '<img src="{}" ' \
            'style="display: block; max-width:230px; max-height:95px;' \
            'width: auto; height: auto;"/>' \
            .format(instance.file.url)
    image_thumb.allow_tags = True

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()
geoadmin.site.register(models.Photo, PhotoAdmin)
