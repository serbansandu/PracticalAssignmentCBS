# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('statistics', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PC',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Statistic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pid', models.IntegerField(max_length=100)),
                ('processName', models.CharField(max_length=100)),
                ('processStatus', models.CharField(max_length=100)),
                ('processPercent', models.FloatField(max_length=100)),
                ('memoryPercent', models.FloatField(max_length=100)),
                ('numberOfThreads', models.IntegerField(max_length=100)),
                ('PC', models.ForeignKey(to='statistics.PC')),
            ],
        ),
        migrations.DeleteModel(
            name='DbaseElements',
        ),
    ]
