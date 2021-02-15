from rest_framework import viewsets, permissions, filters
from django_filters import rest_framework as dj_filters
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from .models import WaterConsumptionDomestic
from .serializers import WaterConsumptionDomesticSerializer
from .pagination import StandardResultsSetPagination
from .filters import WaterConsumptionDomesticFilter


class WaterConsumptionDomesticViewset(viewsets.ModelViewSet):
    queryset = WaterConsumptionDomestic.objects.all()
    serializer_class = WaterConsumptionDomesticSerializer
    # permission_classes = [permissions.IsAuthenticated]
    pagination_class = StandardResultsSetPagination
    filter_class = WaterConsumptionDomesticFilter
    search_fields = ["reservoir__name"]
    # filterset_fields = ["reservoir__name", "reservoir__id"]
    ordering_fields = ["reservoir__name", "date", "water_consumption_domestic",
                       "population", "no_of_families", "no_of_housing_units"]

    @method_decorator(cache_page(60*60*12))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
