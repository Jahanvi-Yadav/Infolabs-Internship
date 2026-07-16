from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Coin, Exchange, Watchlist

admin.site.register(Coin)
admin.site.register(Exchange)
admin.site.register(Watchlist)