from rest_framework import serializers
from month.models import MonthField

from reservoirs.serializers import ReservoirSerializer


class WaterConsumptionDataSerializer(serializers.Serializer):
    date = serializers.DateField()
    water_consumption_paddy = serializers.DecimalField(
        max_digits=10, decimal_places=4)
    rainfall = serializers.DecimalField(
        max_digits=10, decimal_places=4)
    temperature = serializers.DecimalField(max_digits=10, decimal_places=4)
    evaporation = serializers.DecimalField(max_digits=10, decimal_places=4)


class WaterConsumptionPredictSerializer(serializers.Serializer):
    reservoir = ReservoirSerializer()
    real = WaterConsumptionDataSerializer(many=True)
    predicted = WaterConsumptionDataSerializer(many=True)
