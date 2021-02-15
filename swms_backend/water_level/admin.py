from django.contrib import admin
from .models import WaterLevel


class WaterLevelAdmin(admin.ModelAdmin):
    list_display = [field.name for field in WaterLevel._meta.fields]


admin.site.register(WaterLevel, WaterLevelAdmin)
