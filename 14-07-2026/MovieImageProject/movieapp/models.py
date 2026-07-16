from django.db import models

# Create your models here.
from django.db import models

GENRE_CHOICES = [
    ('action', 'Action'),
    ('comedy', 'Comedy'),
    ('drama', 'Drama'),
    ('thriller', 'Thriller'),
]


class Movie(models.Model):
    movie_title = models.CharField(max_length=100)
    movie_genre = models.CharField(max_length=50, choices=GENRE_CHOICES)
    movie_description = models.TextField()
    movie_duration = models.CharField(max_length=50)
    movie_rating = models.FloatField()
    movie_poster = models.ImageField(upload_to='movies/')
    release_date = models.DateField()

    def __str__(self):
        return self.movie_title