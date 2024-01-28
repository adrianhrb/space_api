from django.db import models

class RocketStatusChoices(models.TextChoices):
    retired = 'R', 'Retired'
    active = 'A', 'Active'

class SpaceMissions(models.Model):
    mission = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    rocket = models.CharField(max_length=255)
    rocketStatus = models.CharField(choices=RocketStatusChoices, max_length=1)
    succes = models.BooleanField()

