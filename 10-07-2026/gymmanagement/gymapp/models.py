from django.db import models

# Create your models here.
from django.db import models


MEMBERSHIP_CHOICES = [
    ('Monthly', 'Monthly'),
    ('Quarterly', 'Quarterly'),
    ('Half-Yearly', 'Half-Yearly'),
    ('Yearly', 'Yearly'),
]

SPECIALIZATION_CHOICES = [
    ('Cardio', 'Cardio'),
    ('Yoga', 'Yoga'),
    ('Weight Training', 'Weight Training'),
    ('CrossFit', 'CrossFit'),
]

PAYMENT_METHOD_CHOICES = [
    ('Cash', 'Cash'),
    ('UPI', 'UPI'),
    ('Card', 'Card'),
    ('Net Banking', 'Net Banking'),
]

STATUS_CHOICES = [
    ('Pending', 'Pending'),
    ('Paid', 'Paid'),
    ('Failed', 'Failed'),
]


class Member(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="First Name")
    last_name = models.CharField(max_length=100, verbose_name="Last Name")
    dob = models.DateField(verbose_name="Birth Date")
    contact = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    membership_type = models.CharField(max_length=20, choices=MEMBERSHIP_CHOICES)
    is_active = models.BooleanField(default=True, verbose_name="Active Status")
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name


class Trainer(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="First Name")
    last_name = models.CharField(max_length=100, verbose_name="Last Name")
    specialization = models.CharField(max_length=30, choices=SPECIALIZATION_CHOICES)
    experience = models.IntegerField()
    contact = models.CharField(max_length=15)
    email = models.EmailField()
    salary = models.FloatField()
    is_available = models.BooleanField(default=True, verbose_name="Available Status")
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name


class Package(models.Model):
    package_name = models.CharField(max_length=100)
    duration = models.IntegerField()
    price = models.FloatField()
    description = models.TextField()
    discount = models.FloatField()
    start_date = models.DateField()
    end_date = models.DateField()
    is_available = models.BooleanField(default=True, verbose_name="Available Status")
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.package_name


class Payment(models.Model):
    member_name = models.CharField(max_length=100)
    package_name = models.CharField(max_length=100)
    amount = models.FloatField()
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
    payment_date = models.DateField()
    receipt_no = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    is_verified = models.BooleanField(default=True, verbose_name="Verified Status")
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.member_name