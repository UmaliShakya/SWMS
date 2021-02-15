from rest_framework import serializers
from month.models import MonthField

from home_details.serializers import HomeSerializer


class DomesticWaterDistributionPlanDataSerializer(serializers.Serializer):
    home = HomeSerializer()
    value = serializers.DecimalField(max_digits=10, decimal_places=4)


class DomesticWaterDistributionPlanSerializer(serializers.Serializer):
    date = serializers.DateField()
    data = DomesticWaterDistributionPlanDataSerializer(many=True)
