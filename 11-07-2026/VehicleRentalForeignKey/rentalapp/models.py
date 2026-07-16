from django.db import models

# Create your models here.
from django.db import models


class VehicleType(models.Model):
    vehicle_type = models.CharField(max_length=100)
    fuel_type = models.CharField(max_length=50)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.vehicle_type


class Vehicle(models.Model):
    vehicle_type_id = models.ForeignKey(
        VehicleType,
        on_delete=models.CASCADE
    )
    vehicle_name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    rent_per_day = models.FloatField()
    registration_number = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.vehicle_name