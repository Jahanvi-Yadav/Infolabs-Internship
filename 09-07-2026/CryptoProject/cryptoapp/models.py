from django.db import models

# Create your models here.
from django.db import models


class Coin(models.Model):
    coin_name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=20)
    current_price = models.FloatField()
    market_cap = models.BigIntegerField()
    rank = models.IntegerField()
    is_active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.coin_name


class Exchange(models.Model):
    exchange_name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    website = models.URLField()
    trading_volume = models.BigIntegerField()
    rating = models.FloatField()
    is_active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.exchange_name


class Watchlist(models.Model):
    user_name = models.CharField(max_length=100)
    coin_name = models.CharField(max_length=100)
    target_price = models.FloatField()
    notes = models.TextField()
    added_date = models.DateField()
    is_active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_name