from rest_framework import serializers
from .models import WaterConsumptionDomestic


class WaterConsumptionDomesticSerializer(serializers.ModelSerializer):
    class Meta:
        model = WaterConsumptionDomestic
        fields = '__all__'
        depth = 1
