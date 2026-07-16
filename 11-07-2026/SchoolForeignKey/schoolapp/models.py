from django.db import models

# Create your models here.
from django.db import models


class Teacher(models.Model):
    teacher_name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.teacher_name


class Student(models.Model):
    teacher_id = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE
    )
    student_name = models.CharField(max_length=100)
    standard = models.CharField(max_length=30)
    roll_number = models.IntegerField()
    contact = models.CharField(max_length=15)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.student_name