from rest_framework import serializers
from month.models import MonthField

from home_details.serializers import HomeSerializer


class DomesticWaterConsumptionDataSerializer(serializers.Serializer):
    date = serializers.DateField()
    water_consumption = serializers.DecimalField(
        max_digits=10, decimal_places=4)


class DomesticWaterConsumptionPredictSerializer(serializers.Serializer):
    home = HomeSerializer()
    real = DomesticWaterConsumptionDataSerializer(many=True)
    predicted = DomesticWaterConsumptionDataSerializer(many=True)
