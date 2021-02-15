from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from home_details.models import Home, HomeWaterConsumption
from water_level.models import WaterLevel
from reservoirs.models import Reservoir
from .serializers import DomesticWaterDistributionPlanSerializer
from water_level_prediction.predict import predict_water_level
from domestic_water_consumption_prediction.predict import predict_domestic_water_consumption
from .predict import generate_water_distribution_plan


class DomesticWaterDistributionPlanViewSet(viewsets.ViewSet):

    @method_decorator(cache_page(60*60*24))
    def retrieve(self, request, pk=None):
        reservoir = get_object_or_404(Reservoir, pk=pk)

        homes = Home.objects.filter(reservoir__id=pk)

        water_levels = WaterLevel.objects.filter(
            reservoir__id=pk).order_by('date')

        _, predicted_water_levels, _ = predict_water_level(
            reservoir, water_levels)

        predicted_water_consumption_data_list = []

        for home in homes:
            home_water_consumption_details = HomeWaterConsumption.objects.filter(
                home__id=home.id).order_by('date')

            _, predicted_water_consumption, _ = predict_domestic_water_consumption(
                home, home_water_consumption_details)

            predicted_water_consumption_data_list.append({
                'home': home,
                'data': predicted_water_consumption
            })

        data = generate_water_distribution_plan(
            predicted_water_levels, predicted_water_consumption_data_list)

        serializer = DomesticWaterDistributionPlanSerializer(
            data, many=True, read_only=True)

        return Response(serializer.data)
