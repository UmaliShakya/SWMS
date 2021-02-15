from rest_framework import serializers
from month.models import MonthField

from reservoirs.serializers import ReservoirSerializer


class WaterLevelDataSerializer(serializers.Serializer):
    date = serializers.DateField()
    water_level = serializers.DecimalField(max_digits=10, decimal_places=4)
    rainfall = serializers.DecimalField(max_digits=10, decimal_places=4)
    temperature = serializers.DecimalField(max_digits=10, decimal_places=4)
    evaporation = serializers.DecimalField(max_digits=10, decimal_places=4)


class WaterLevelPredictSerializer(serializers.Serializer):
    reservoir = ReservoirSerializer()
    real = WaterLevelDataSerializer(many=True)
    predicted = WaterLevelDataSerializer(many=True)
