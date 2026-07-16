from django.db import models

# Create your models here.
from django.db import models


FUEL_TYPE_CHOICES = [
    ('Petrol', 'Petrol'),
    ('Diesel', 'Diesel'),
    ('Electric', 'Electric'),
    ('CNG', 'CNG'),
]

RENTAL_STATUS_CHOICES = [
    ('Booked', 'Booked'),
    ('Running', 'Running'),
    ('Completed', 'Completed'),
]

PAYMENT_METHOD_CHOICES = [
    ('Cash', 'Cash'),
    ('Card', 'Card'),
    ('UPI', 'UPI'),
]

PAYMENT_STATUS_CHOICES = [
    ('Pending', 'Pending'),
    ('Paid', 'Paid'),
    ('Failed', 'Failed'),
]


class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=15)
    license_no = models.CharField(max_length=50)
    address = models.TextField()
    dob = models.DateField()
    is_active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Car(models.Model):
    car_name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    model_year = models.IntegerField()
    registration_no = models.CharField(max_length=30)
    rent_per_day = models.FloatField()
    fuel_type = models.CharField(max_length=20, choices=FUEL_TYPE_CHOICES)
    is_available = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.car_name


class Rental(models.Model):
    customer_name = models.CharField(max_length=100)
    car_name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    total_amount = models.FloatField()
    status = models.CharField(max_length=20, choices=RENTAL_STATUS_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer_name


class Payment(models.Model):
    rental_id = models.IntegerField()
    amount = models.FloatField()
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
    status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES)
    payment_date = models.DateField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Rental {self.rental_id}"