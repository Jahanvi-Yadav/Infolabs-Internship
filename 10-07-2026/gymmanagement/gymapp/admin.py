from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Member, Trainer, Package, Payment

admin.site.register(Member)
admin.site.register(Trainer)
admin.site.register(Package)
admin.site.register(Payment)