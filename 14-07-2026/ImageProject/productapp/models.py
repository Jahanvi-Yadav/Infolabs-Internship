from django.db import models

# Create your models here.
from django.db import models


CATEGORY_CHOICES = [
    ('electronics', 'Electronics'),
    ('fashion', 'Fashion'),
    ('grocery', 'Grocery'),
    ('furniture', 'Furniture'),
]


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    product_description = models.TextField()
    product_price = models.FloatField()
    product_quantity = models.IntegerField()
    product_image = models.ImageField(upload_to='products/')
    created_date = models.DateField()

    def __str__(self):
        return self.product_name