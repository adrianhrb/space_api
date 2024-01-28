from rest_framework import serializers
from .models import SpaceMissions

class SpaceMissionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpaceMissions
        fields = ('id', 'mission', 'company', 'location', 'date', 'time', 'rocket', 'rocketStatus', 'success')