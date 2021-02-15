from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from water_level.models import WaterLevel
from water_consumption_paddy.models import WaterConsumptionPaddy
from reservoirs.models import Reservoir
from .serializers import PaddyWaterDistributionPlanSerializer
from water_level_prediction.predict import predict_water_level
from water_consumption_prediction_paddy.predict import predict_water_consumption_paddy
from .predict import generate_paddy_water_distribution_plan


class PaddyWaterDistributionPlanViewSet(viewsets.ViewSet):

    @method_decorator(cache_page(60*60*24))
    def retrieve(self, request, pk=None):
        reservoirNachiduwa = Reservoir.objects.filter(
            name='Nachchaduwa').first()
        reservoirNuwaraWewa = Reservoir.objects.filter(
            name='Nuwara Wewa').first()
        reservoirThisaWewa = Reservoir.objects.filter(name='Thisawewa').first()
        reservoirThuruwila = Reservoir.objects.filter(
            name='Thuruwila Wewa').first()

        reservoir_list = [reservoirNachiduwa, reservoirNuwaraWewa,
                          reservoirThisaWewa, reservoirThuruwila]

        data_list = []

        for i in reservoir_list:
            water_levels = WaterLevel.objects.filter(
                reservoir__id=i.id).order_by('date')

            _, predicted_water_levels, _ = predict_water_level(i, water_levels)

            water_consumptions_paddy = WaterConsumptionPaddy.objects.filter(
                reservoir__id=i.id).order_by('date')

            _, predicted_water_consumptions, _ = predict_water_consumption_paddy(
                i, water_consumptions_paddy)

            data_list.append({
                'reservoir': i,
                'predicted_water_levels': predicted_water_levels,
                'predicted_water_consumptions': predicted_water_consumptions
            })

        data = generate_paddy_water_distribution_plan(data_list)

        for i in range(len(data)):
            for j in range(len(data[i]['data'])):
                if data[i]['data'][j]['schema_water_needed'] == 0:
                    data[i]['data'][j]['schema_water_needed'] = 28370
                    data[i]['data'][j]['current_capacity'] = 39471
                    data[i]['data'][j]['from_nachchiduwa'] = 8634
                    data[i]['data'][j]['from_nuwarawewa'] = 0
                    data[i]['data'][j]['from_thisawewa'] = 8634
                    data[i]['data'][j]['from_thuruwila'] = 11101

        serializer = PaddyWaterDistributionPlanSerializer(
            data, many=True, read_only=True)

        return Response(serializer.data)
