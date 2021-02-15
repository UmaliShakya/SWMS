from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from water_consumption_domestic.models import WaterConsumptionDomestic
from reservoirs.models import Reservoir
from .serializers import WaterConsumptionPredictDomesticSerializer
from .predict import predict_water_consumption_domestic


class WaterConsumptionPredictionDomesticViewSet(viewsets.ViewSet):

    @method_decorator(cache_page(60*60*24))
    def retrieve(self, request, pk=None):
        reservoir = get_object_or_404(Reservoir, pk=pk)

        water_consumptions_domestic = WaterConsumptionDomestic.objects.filter(
            reservoir__id=pk).order_by('date')

        *_, data = predict_water_consumption_domestic(
            reservoir, water_consumptions_domestic)

        serializer = WaterConsumptionPredictDomesticSerializer(
            data, read_only=True)

        return Response(serializer.data)
