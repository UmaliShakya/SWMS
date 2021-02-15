from django.db import models
from month.models import MonthField


class WaterConsumptionDomestic(models.Model):
    id = models.AutoField(primary_key=True)
    reservoir = models.ForeignKey(
        "reservoirs.Reservoir", on_delete=models.CASCADE)
    date = MonthField("Month Value", help_text="Month Value")
    water_consumption_domestic = models.IntegerField()
    population = models.IntegerField()
    no_of_families = models.IntegerField()
    no_of_housing_units = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["reservoir", "date"]
        unique_together = ['reservoir', 'date']

    def __str__(self):
        return 'Water Consumption Domestic : ' + self.reservoir.name + ", " + str(self.date)
