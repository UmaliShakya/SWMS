from rest_framework import serializers
from month.models import MonthField

from reservoirs.serializers import ReservoirSerializer


class WaterConsumptionDomesticDataSerializer(serializers.Serializer):
    date = serializers.DateField()
    water_consumption_domestic = serializers.DecimalField(
        max_digits=10, decimal_places=4)
    population = serializers.DecimalField(
        max_digits=10, decimal_places=4)
    no_of_families = serializers.DecimalField(max_digits=10, decimal_places=4)
    no_of_housing_units = serializers.DecimalField(
        max_digits=10, decimal_places=4)


class WaterConsumptionPredictDomesticSerializer(serializers.Serializer):
    reservoir = ReservoirSerializer()
    real = WaterConsumptionDomesticDataSerializer(many=True)
    predicted = WaterConsumptionDomesticDataSerializer(many=True)
