from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import MovieCategory, Director, Movie

admin.site.register(MovieCategory)
admin.site.register(Director)
admin.site.register(Movie)