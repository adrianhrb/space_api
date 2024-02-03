from rest_framework import serializers

from .models import Astronauts, SpaceMissions


class SpaceMissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpaceMissions
        fields = '__all__'


class AstronautsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Astronauts
        fields = '__all__'
