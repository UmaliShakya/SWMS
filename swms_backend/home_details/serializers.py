from rest_framework import serializers
from .models import Home, HomeWaterConsumption


class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = '__all__'
        depth = 1


class HomeWaterConsumptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeWaterConsumption
        fields = '__all__'
        depth = 2
