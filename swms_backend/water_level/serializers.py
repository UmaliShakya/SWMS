from rest_framework import serializers
from .models import WaterLevel


class WaterLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = WaterLevel
        fields = '__all__'
        depth = 1
