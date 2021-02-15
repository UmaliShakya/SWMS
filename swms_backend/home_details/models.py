from django.db import models
from month.models import MonthField


class Home(models.Model):
    id = models.AutoField(primary_key=True)
    reservoir = models.ForeignKey(
        "reservoirs.Reservoir", on_delete=models.CASCADE)
    home_name = models.CharField(max_length=100)
    number_of_residents = models.IntegerField()
    home_owner_name = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=200, blank=True)
    description = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["home_name"]
        unique_together = ['reservoir', 'home_name']

    def __str__(self):
        return f'Home : {self.home_name}, Reservoir : {self.reservoir.name}'


class HomeWaterConsumption(models.Model):
    id = models.AutoField(primary_key=True)
    home = models.ForeignKey(
        "home_details.Home", on_delete=models.CASCADE)
    date = MonthField("Month Value", help_text="Month Value")
    water_consumption = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["home", "date"]
        unique_together = ['home', 'date']

    def __str__(self):
        return f'Home Water Consumption : Date: {self.date} , Water Consumption {self.water_consumption}, Home : {self.home.home_name}, Reservoir : {self.home.reservoir.name}'
