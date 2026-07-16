from django.db import models

# Create your models here.
from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    total_orders = models.IntegerField()
    loyalty_points = models.IntegerField()
    is_active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    rating = models.FloatField()
    quantity = models.IntegerField()
    is_available = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    food_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    total_amount = models.FloatField()
    payment_method = models.CharField(max_length=50)
    order_status = models.CharField(max_length=50)
    is_paid = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer_name