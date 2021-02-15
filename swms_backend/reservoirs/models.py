from django.db import models


class Reservoir(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200, blank=True)
    division = models.CharField(max_length=100)
    capacity = models.IntegerField()
    catchment_area = models.IntegerField()
    surface_area = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return 'Reservoir : ' + self.name
