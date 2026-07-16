from django.db import models

# Create your models here.
from django.db import models


class Course(models.Model):
    course_name = models.CharField(max_length=100)
    instructor = models.CharField(max_length=100)
    price = models.FloatField()
    duration = models.IntegerField()
    description = models.TextField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.course_name