from django.contrib import admin
from .models import Reservoir


class ReservoirAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Reservoir._meta.fields]


admin.site.register(Reservoir, ReservoirAdmin)
