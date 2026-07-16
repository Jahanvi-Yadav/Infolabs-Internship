from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Customer, Car, Rental, Payment

admin.site.register(Customer)
admin.site.register(Car)
admin.site.register(Rental)
admin.site.register(Payment)