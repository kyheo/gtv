from django.dispatch import receiver
from django.db.models import signals
from django.contrib.gis.geos import Point

from PIL import Image

import models


@receiver(signals.post_delete, sender=models.Photo)
def Photo_post_delete(sender, instance, **kwargs):
    instance.file.delete(False)


@receiver(signals.pre_save, sender=models.Photo)
def Photo_pre_save(sender, instance, **kwargs):
    if instance.id:
        old_instance = sender.objects.get(pk=instance.id)
        old_instance.file.delete(False)

    image = Image.open(instance.file)
    info = image._getexif()
    # as defined in http://www.exiv2.org/tags.html
    if 34853 in info and info[34853]:
        value = info[34853]
        lat = [float(x)/float(y) for x, y in value[2]]
        lon = [float(x)/float(y) for x, y in value[4]]
        lat = lat[0] + lat[1]/60 + lat[2]/3600
        lon = lon[0] + lon[1]/60 + lon[2]/3600
        if value[1] == 'S':
            lat = -lat
        if value[3] == 'W':
            lon = -lon
        alt = value[6][0] / value[6/1] if '6' in value else None
        instance.point = Point(lon, lat, alt)
