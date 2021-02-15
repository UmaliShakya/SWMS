from rest_framework import serializers
from .models import WaterConsumptionPaddy


class WaterConsumptionPaddySerializer(serializers.ModelSerializer):
    class Meta:
        model = WaterConsumptionPaddy
        fields = '__all__'
        depth = 1
