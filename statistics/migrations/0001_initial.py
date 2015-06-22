# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DbaseElements',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('PCname', models.CharField(max_length=100)),
                ('pid', models.IntegerField(max_length=100)),
                ('processName', models.CharField(max_length=100)),
                ('processStatus', models.CharField(max_length=100)),
                ('processPercent', models.FloatField(max_length=100)),
                ('memoryPercent', models.FloatField(max_length=100)),
                ('numberOfThreads', models.IntegerField(max_length=100)),
            ],
        ),
    ]
