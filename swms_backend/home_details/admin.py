from django.contrib import admin
from .models import Home, HomeWaterConsumption


class HomeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Home._meta.fields]


admin.site.register(Home, HomeAdmin)


class HomeWaterConsumptionAdmin(admin.ModelAdmin):
    list_display = [field.name for field in HomeWaterConsumption._meta.fields]


admin.site.register(HomeWaterConsumption, HomeWaterConsumptionAdmin)
