from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Customer, Stylist, Service

admin.site.register(Customer)
admin.site.register(Stylist)
admin.site.register(Service)