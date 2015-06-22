from django.db import models


class DbaseElements(models.Model):
    PCname = models.CharField(max_length=100)
    pid = models.IntegerField(max_length=100)
    processName = models.CharField(max_length=100)
    processStatus = models.CharField(max_length=100)
    processPercent = models.FloatField(max_length=100)
    memoryPercent = models.FloatField(max_length=100)
    numberOfThreads = models.IntegerField(max_length=100)
