from django.db import models


class SpaceMissions(models.Model):
    """
    All space missions from 1957 to 2022, you cand find the data file in:
    https://www.kaggle.com/datasets/mysarahmadbhat/space-missions
    """

    mission = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    launched = models.DateTimeField()
    rocket = models.CharField(max_length=255)
    rocketStatus = models.CharField(max_length=255)
    success = models.BooleanField()


class Astronauts(models.Model):
    """
    All astronauts that have visited the space, you can find the data file in:
    https://www.kaggle.com/datasets/kaushiksinghrawat/humans-to-have-visited-space
    """

    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    nationality = models.CharField(max_length=255)
    birthdate = models.DateField()
    mission = models.CharField(max_length=255)
