from django.contrib import admin
from .models import WaterConsumptionDomestic


class WaterConsumptionDomesticAdmin(admin.ModelAdmin):
    list_display = [
        field.name for field in WaterConsumptionDomestic._meta.fields]


admin.site.register(WaterConsumptionDomestic, WaterConsumptionDomesticAdmin)
