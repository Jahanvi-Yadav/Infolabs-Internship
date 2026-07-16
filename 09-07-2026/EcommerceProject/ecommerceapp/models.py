from django.db import models

# Create your models here.
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    price = models.FloatField()
    quantity = models.IntegerField()
    brand = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    total_price = models.FloatField()
    payment_status = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer_name