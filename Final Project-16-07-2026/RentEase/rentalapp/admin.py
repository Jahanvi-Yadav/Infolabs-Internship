from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *

admin.site.register(Country)
admin.site.register(State)
admin.site.register(City)

admin.site.register(Owner)
admin.site.register(Tenant)

admin.site.register(PropertyCategory)
admin.site.register(Amenity)
admin.site.register(Property)

admin.site.register(Booking)
admin.site.register(Payment)
admin.site.register(Review)

admin.site.register(Wishlist)
admin.site.register(ContactMessage)