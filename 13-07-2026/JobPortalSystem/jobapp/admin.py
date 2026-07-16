from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *

admin.site.register(JobSeeker)
admin.site.register(Company)
admin.site.register(JobCategory)
admin.site.register(Job)
admin.site.register(Application)
admin.site.register(Interview)
admin.site.register(SavedJob)
admin.site.register(Review)