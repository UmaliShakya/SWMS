from rest_framework import serializers
from .models import Reservoir


class ReservoirSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservoir
        fields = '__all__'
