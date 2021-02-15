from rest_framework import viewsets, permissions, filters
from django_filters import rest_framework as dj_filters
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from .models import WaterConsumptionPaddy
from .serializers import WaterConsumptionPaddySerializer
from .pagination import StandardResultsSetPagination
from .filters import WaterConsumptionPaddyFilter


class WaterConsumptionPaddyViewset(viewsets.ModelViewSet):
    queryset = WaterConsumptionPaddy.objects.all()
    serializer_class = WaterConsumptionPaddySerializer
    # permission_classes = [permissions.IsAuthenticated]
    pagination_class = StandardResultsSetPagination
    filter_class = WaterConsumptionPaddyFilter
    search_fields = ["reservoir__name"]
    # filterset_fields = ["reservoir__name", "reservoir__id"]
    ordering_fields = ["reservoir__name", "date", "water_consumption_paddy",
                       "rainfall", "temperature", "evaporation"]

    @method_decorator(cache_page(60*60*12))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
