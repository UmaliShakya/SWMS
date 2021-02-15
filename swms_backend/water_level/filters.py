from django_filters import rest_framework as filters
from .models import WaterLevel


class WaterLevelFilter(filters.FilterSet):
    reservoir_name = filters.CharFilter(
        field_name="reservoir__name", lookup_expr="exact")
    reservoir_id = filters.CharFilter(
        field_name="reservoir__id", lookup_expr="exact")

    class Meta:
        model = WaterLevel
        fields = ["reservoir_name", "reservoir_id"]
