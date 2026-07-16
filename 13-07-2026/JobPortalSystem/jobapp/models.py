from django.db import models

# Create your models here.
from django.db import models


class JobSeeker(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField()
    resume_url = models.URLField()
    skills = models.TextField()
    experience = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Company(models.Model):
    company_name = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=15)
    address = models.TextField()
    website_url = models.URLField()
    logo_url = models.URLField()
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company_name


class JobCategory(models.Model):
    category_name = models.CharField(max_length=100)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category_name


class Job(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    category = models.ForeignKey(JobCategory, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=100)
    description = models.TextField()
    salary = models.FloatField()
    location = models.CharField(max_length=100)
    vacancies = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.job_title


class Application(models.Model):
    jobseeker = models.ForeignKey(JobSeeker, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    apply_date = models.DateField()
    cover_letter = models.TextField()
    status = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.jobseeker} - {self.job}"


class Interview(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    interview_date = models.DateField()
    interview_time = models.TimeField()
    interview_mode = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.application)


class SavedJob(models.Model):
    jobseeker = models.ForeignKey(JobSeeker, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    notes = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.job)


class Review(models.Model):
    jobseeker = models.ForeignKey(JobSeeker, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    rating = models.FloatField()
    comment = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.company)