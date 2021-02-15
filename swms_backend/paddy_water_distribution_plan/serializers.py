from rest_framework import serializers


class PaddyWaterDistributionPlanDataSerializer(serializers.Serializer):
    tank = serializers.CharField()
    full_capacity = serializers.IntegerField()
    schema_water_needed = serializers.IntegerField()
    current_capacity = serializers.IntegerField()
    from_nachchiduwa = serializers.IntegerField()
    from_nuwarawewa = serializers.IntegerField()
    from_thisawewa = serializers.IntegerField()
    from_thuruwila = serializers.IntegerField()


class PaddyWaterDistributionPlanSerializer(serializers.Serializer):
    date = serializers.DateField()
    data = PaddyWaterDistributionPlanDataSerializer(many=True)
