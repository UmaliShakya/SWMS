from rest_framework import viewsets, permissions, filters
from django_filters import rest_framework as dj_filters
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from .models import Reservoir
from .serializers import ReservoirSerializer
from .pagination import StandardResultsSetPagination


class ReservoirViewset(viewsets.ModelViewSet):
    queryset = Reservoir.objects.all()
    serializer_class = ReservoirSerializer
    # permission_classes = [permissions.IsAuthenticated]
    pagination_class = StandardResultsSetPagination
    search_fields = ["name", "division"]
    filterset_fields = ["division"]
    ordering_fields = ["name", "division",
                       "capacity", "catchment_area", "surface_area"]

    @method_decorator(cache_page(60*60*12))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
