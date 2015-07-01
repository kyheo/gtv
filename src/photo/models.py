import uuid

from django.contrib.gis.db import models
from django.contrib.auth import models as auth_models


def _upload_to(instance, filename):
    # Generate a unique file name
    return '{}/photos/{}-{}-{}'.format(
        instance.user.id, instance.created.strftime('%Y%m%d-%H%M%S'),
        uuid.uuid4(), filename)


class Photo(models.Model):
    user = models.ForeignKey(auth_models.User)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    file = models.FileField(upload_to=_upload_to)
    point = models.PointField(blank=True, null=True)

    def __unicode__(self):
        return self.file.name
