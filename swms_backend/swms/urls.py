from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers, permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from reservoirs.views import ReservoirViewset
from water_level.views import WaterLevelViewset
from water_level_prediction.views import WaterLevelPredictionViewSet
from water_consumption_prediction_domestic.views import WaterConsumptionPredictionDomesticViewSet
from water_consumption_prediction_paddy.views import WaterConsumptionPredictionPaddyViewSet
from home_details.views import HomeViewset, HomeWaterConsumptionViewset
from domestic_water_consumption_prediction.views import DomesticWaterConsumptionPredictionViewSet
from domestic_water_distribution_plan.views import DomesticWaterDistributionPlanViewSet
from paddy_water_distribution_plan.views import PaddyWaterDistributionPlanViewSet
from water_consumption_domestic.views import WaterConsumptionDomesticViewset
from water_consumption_paddy.views import WaterConsumptionPaddyViewset

schema_view = get_schema_view(
    openapi.Info(
        title="SWMS API",
        default_version='v1',
        description="API for SWMS",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register(r'reservoirs', ReservoirViewset)
router.register(r'water_level', WaterLevelViewset)
router.register(r'water_consumption_domestic', WaterConsumptionDomesticViewset)
router.register(r'water_consumption_paddy', WaterConsumptionPaddyViewset)
router.register(r'water_level_prediction',
                WaterLevelPredictionViewSet, basename='water_level_prediction')
router.register(r'water_consumption_prediction_domestic',
                WaterConsumptionPredictionDomesticViewSet, basename='water_consumption_prediction_domestic')
router.register(r'water_consumption_prediction_paddy',
                WaterConsumptionPredictionPaddyViewSet, basename='water_consumption_prediction_paddy')
router.register(r'homes', HomeViewset)
router.register(r'home_details', HomeWaterConsumptionViewset)
router.register(r'domestic_water_level_consumption_prediction',
                DomesticWaterConsumptionPredictionViewSet, basename='domestic_water_consumption_prediction')
router.register(r'domestic_water_distribution_plan',
                DomesticWaterDistributionPlanViewSet, basename='domestic_water_distribution_plan')
router.register(r'paddy_water_distribution_plan',
                PaddyWaterDistributionPlanViewSet, basename='paddy_water_distribution_plan')

urlpatterns = [
    path('', include(router.urls)),
    url(r'^auth/', include('djoser.urls')),
    url(r'^auth/', include('djoser.urls.authtoken')),
    url(r'^swagger(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger',
                                           cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc',
                                         cache_timeout=0), name='schema-redoc'),
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
