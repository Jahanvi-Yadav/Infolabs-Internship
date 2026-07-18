from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *

admin.site.register(Country)
admin.site.register(State)
admin.site.register(City)

admin.site.register(Agent)
admin.site.register(PropertyCategory)
admin.site.register(Property)

admin.site.register(Customer)
admin.site.register(PropertyVisit)
admin.site.register(PropertyInquiry)
admin.site.register(PropertyBooking)
admin.site.register(Payment)
admin.site.register(Review)