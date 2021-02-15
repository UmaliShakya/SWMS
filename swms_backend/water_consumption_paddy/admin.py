from django.contrib import admin
from .models import WaterConsumptionPaddy


class WaterConsumptionPaddyAdmin(admin.ModelAdmin):
    list_display = [
        field.name for field in WaterConsumptionPaddy._meta.fields]


admin.site.register(WaterConsumptionPaddy, WaterConsumptionPaddyAdmin)
