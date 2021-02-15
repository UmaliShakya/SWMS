from django_filters import rest_framework as filters
from .models import Home, HomeWaterConsumption


class HomeFilter(filters.FilterSet):
    reservoir_name = filters.CharFilter(
        field_name="reservoir__name", lookup_expr="exact")
    reservoir_id = filters.CharFilter(
        field_name="reservoir__id", lookup_expr="exact")

    class Meta:
        model = Home
        fields = ["reservoir_name", "reservoir_id"]


class HomeWaterConsumptionFilter(filters.FilterSet):
    reservoir_name = filters.CharFilter(
        field_name="home__reservoir__name", lookup_expr="exact")
    reservoir_id = filters.CharFilter(
        field_name="home__reservoir__id", lookup_expr="exact")
    home_name = filters.CharFilter(
        field_name="home__home_name", lookup_expr="exact")
    home_id = filters.CharFilter(field_name="home__id", lookup_expr="exact")

    class Meta:
        model = HomeWaterConsumption
        fields = ["reservoir_name", "reservoir_id", "home_name", "home_id"]
