from rest_framework import viewsets, permissions, filters
from django_filters import rest_framework as dj_filters
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from .models import Home, HomeWaterConsumption
from .serializers import HomeSerializer, HomeWaterConsumptionSerializer
from .pagination import StandardResultsSetPagination
from .filters import HomeFilter, HomeWaterConsumptionFilter


class HomeViewset(viewsets.ModelViewSet):
    queryset = Home.objects.all()
    serializer_class = HomeSerializer
    # permission_classes = [permissions.IsAuthenticated]
    pagination_class = StandardResultsSetPagination
    filter_class = HomeFilter
    search_fields = ["reservoir__name"]
    ordering_fields = ["reservoir__name", "home_name", "number_of_residents",
                       "home_owner_name", "address", "description"]

    @method_decorator(cache_page(60*60*12))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class HomeWaterConsumptionViewset(viewsets.ModelViewSet):
    queryset = HomeWaterConsumption.objects.all()
    serializer_class = HomeWaterConsumptionSerializer
    # permission_classes = [permissions.IsAuthenticated]
    pagination_class = StandardResultsSetPagination
    filter_class = HomeWaterConsumptionFilter
    search_fields = ["home__reservoir__name", "home__home_name"]
    ordering_fields = ["reservoir__name", "home__home_name", "date",
                       "water_consumption"]

    @method_decorator(cache_page(60*60*12))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
