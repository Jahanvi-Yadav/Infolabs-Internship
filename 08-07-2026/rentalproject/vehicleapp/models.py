from django.db import models

# Create your models here.
from django.db import models


class Vehicle(models.Model):
    vehicle_name = models.CharField(max_length=100)
    registration_number = models.CharField(max_length=30)
    fuel_type = models.CharField(max_length=30)
    rental_price = models.FloatField()
    model_year = models.IntegerField()
    color = models.CharField(max_length=30)
    description = models.TextField()
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.vehicle_name