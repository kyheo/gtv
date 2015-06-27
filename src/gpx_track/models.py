import uuid

from django.contrib.gis.db import models
from django.contrib.auth import models as auth_models


def _upload_to(instance, filename):
    # Generate a unique file name
    return '{}/gpx_files/{}-{}'.format(
        instance.user.id, instance.created.strftime('%Y%m%d-%H%M%S'),
        uuid.uuid4())


class GPXFile(models.Model):
    user = models.ForeignKey(auth_models.User)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    file = models.FileField(upload_to=_upload_to)

    def __unicode__(self):
        return self.file.name


class GPXTrack(models.Model):
    objects = models.GeoManager()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(auth_models.User)
    file = models.ForeignKey(GPXFile)
    name = models.CharField(max_length=255)
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    date_start_at_location = models.CharField(max_length=100)
    date_end_at_location = models.CharField(max_length=100)
    multiline = models.MultiLineStringField()
    center = models.PointField()

    def __unicode__(self):
        return unicode(self.name)
