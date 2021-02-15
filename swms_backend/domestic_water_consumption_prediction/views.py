from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from home_details.models import Home, HomeWaterConsumption
from reservoirs.models import Reservoir
from .serializers import DomesticWaterConsumptionPredictSerializer
from .predict import predict_domestic_water_consumption


class DomesticWaterConsumptionPredictionViewSet(viewsets.ViewSet):

    @method_decorator(cache_page(60*60*24))
    def retrieve(self, request, pk=None):
        home = get_object_or_404(Home, pk=pk)

        home_water_consumption_details = HomeWaterConsumption.objects.filter(
            home__id=pk).order_by('date')

        *_, data = predict_domestic_water_consumption(home, home_water_consumption_details)

        serializer = DomesticWaterConsumptionPredictSerializer(
            data, read_only=True)

        return Response(serializer.data)
