# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import gpx_track.models
from django.conf import settings
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GPXFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('file', models.FileField(upload_to=gpx_track.models._upload_to)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='GPXTrack',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('date_start', models.DateTimeField()),
                ('date_end', models.DateTimeField()),
                ('date_start_at_location', models.CharField(max_length=100)),
                ('date_end_at_location', models.CharField(max_length=100)),
                ('multiline', django.contrib.gis.db.models.fields.MultiLineStringField(srid=4326)),
                ('center', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('file', models.ForeignKey(to='gpx_track.GPXFile')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
