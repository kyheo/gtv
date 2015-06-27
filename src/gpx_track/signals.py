from django.dispatch import receiver
from django.db.models import signals
from django.contrib.gis.geos import Point, LineString,  MultiLineString

import gpxpy
import pytz
from geopy import geocoders

import models


@receiver(signals.pre_save, sender=models.GPXFile)
def GPXFile_pre_save(sender, instance, **kwargs):
    if instance.id:
        old_instance = sender.objects.get(pk=instance.id)
        old_instance.file.delete(False)


@receiver(signals.post_delete, sender=models.GPXFile)
def GPXFile_post_delete(sender, instance, **kwargs):
    instance.file.delete(False)


@receiver(signals.post_save, sender=models.GPXFile)
def GPXFile_post_save(sender, instance, created, **kwargs):
    if not created:
        instance.gpxtrack_set.all().delete()

    gpx = gpxpy.parse(instance.file)
    for track in gpx.tracks:
        new_track = models.GPXTrack()
        new_track.user = instance.user
        new_track.file = instance
        new_track.name = track.name

        center = track.get_center()
        new_track.center = Point(center.longitude, center.latitude,
                                 center.elevation)

        time_bounds = track.get_time_bounds()
        g = geocoders.GoogleV3()
        timezone = g.timezone((center.latitude, center.longitude))

        new_track.date_start = time_bounds.start_time.replace(tzinfo=pytz.UTC)
        new_track.date_end = time_bounds.end_time.replace(tzinfo=pytz.UTC)

        new_track.date_start_at_location = new_track.date_start \
            .astimezone(timezone).isoformat()
        new_track.date_end_at_location = new_track.date_end \
            .astimezone(timezone).isoformat()

        segments = []
        for segment in track.segments:
            points = [Point(e.longitude, e.latitude).coords for e in
                      segment.points]
            segments.append(LineString(points))
        new_track.multiline = MultiLineString(segments)
        new_track.save()
