from django.db import models

# Create your models here.
from django.db import models


class Country(models.Model):
    country_name = models.CharField(max_length=100)
    country_code = models.CharField(max_length=10)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.country_name


class State(models.Model):
    country_id = models.ForeignKey(Country, on_delete=models.CASCADE)
    state_name = models.CharField(max_length=100)
    state_code = models.CharField(max_length=10)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.state_name


class City(models.Model):
    country_id = models.ForeignKey(Country, on_delete=models.CASCADE)
    state_id = models.ForeignKey(State, on_delete=models.CASCADE)
    city_name = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.city_name

PROPERTY_TYPE_CHOICES = [
    ('Apartment', 'Apartment'),
    ('Villa', 'Villa'),
    ('Office', 'Office'),
    ('Shop', 'Shop'),
    ('Land', 'Land'),
]


class Agent(models.Model):
    country_id = models.ForeignKey(Country, on_delete=models.CASCADE)
    state_id = models.ForeignKey(State, on_delete=models.CASCADE)
    city_id = models.ForeignKey(City, on_delete=models.CASCADE)

    agent_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    profile_image = models.ImageField(upload_to='agents/')
    experience = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.agent_name


class PropertyCategory(models.Model):
    category_name = models.CharField(max_length=100)
    category_image = models.ImageField(upload_to='categories/')
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_name


class Property(models.Model):
    category_id = models.ForeignKey(PropertyCategory, on_delete=models.CASCADE)
    agent_id = models.ForeignKey(Agent, on_delete=models.CASCADE)

    property_title = models.CharField(max_length=100)
    description = models.TextField()

    property_type = models.CharField(
        max_length=20,
        choices=PROPERTY_TYPE_CHOICES
    )

    price = models.FloatField()
    address = models.TextField()
    property_image = models.ImageField(upload_to='properties/')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.property_title

STATUS_CHOICES = [
    ('Scheduled', 'Scheduled'),
    ('Completed', 'Completed'),
    ('Cancelled', 'Cancelled'),
]

INQUIRY_STATUS = [
    ('Pending', 'Pending'),
    ('Replied', 'Replied'),
    ('Closed', 'Closed'),
]

BOOKING_STATUS = [
    ('Pending', 'Pending'),
    ('Confirmed', 'Confirmed'),
    ('Cancelled', 'Cancelled'),
]

PAYMENT_METHOD = [
    ('Cash', 'Cash'),
    ('Card', 'Card'),
    ('UPI', 'UPI'),
    ('Net Banking', 'Net Banking'),
]

PAYMENT_STATUS = [
    ('Pending', 'Pending'),
    ('Paid', 'Paid'),
    ('Failed', 'Failed'),
]
class Customer(models.Model):
    country_id = models.ForeignKey(Country, on_delete=models.CASCADE)
    state_id = models.ForeignKey(State, on_delete=models.CASCADE)
    city_id = models.ForeignKey(City, on_delete=models.CASCADE)

    customer_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    profile_image = models.ImageField(upload_to='customers/')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.customer_name
class PropertyVisit(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    property_id = models.ForeignKey(Property, on_delete=models.CASCADE)

    visit_date = models.DateField()
    visit_time = models.TimeField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES
    )

    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.customer_id)
class PropertyInquiry(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    property_id = models.ForeignKey(Property, on_delete=models.CASCADE)

    message = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=INQUIRY_STATUS
    )

    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.customer_id)

class PropertyBooking(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    property_id = models.ForeignKey(Property, on_delete=models.CASCADE)

    booking_amount = models.FloatField()
    booking_date = models.DateField()

    status = models.CharField(
        max_length=20,
        choices=BOOKING_STATUS
    )

    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.customer_id)
class Payment(models.Model):
    booking_id = models.ForeignKey(PropertyBooking, on_delete=models.CASCADE)

    amount = models.FloatField()

    payment_method = models.CharField(
        max_length=20,
        choices=PAYMENT_METHOD
    )

    transaction_id = models.CharField(max_length=100)

    payment_status = models.CharField(
        max_length=20,
        choices=PAYMENT_STATUS
    )

    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.transaction_id

class Review(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    property_id = models.ForeignKey(Property, on_delete=models.CASCADE)

    rating = models.IntegerField()
    comment = models.TextField()

    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.customer_id)