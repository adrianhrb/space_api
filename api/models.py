from django.db import models


class SpaceMissions(models.Model):
    mission = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField(blank=True, null=True)
    rocket = models.CharField(max_length=255)
    rocketStatus = models.CharField(max_length=255)
    success = models.BooleanField()

