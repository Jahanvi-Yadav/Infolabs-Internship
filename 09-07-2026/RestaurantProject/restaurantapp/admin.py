from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Customer, FoodItem, Order

admin.site.register(Customer)
admin.site.register(FoodItem)
admin.site.register(Order)