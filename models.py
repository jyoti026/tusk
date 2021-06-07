from django.db import models

# Create your models here.
class Profile(models.Model):



    name = models.CharField(max_length=500)
    email = models.CharField(max_length=500)
    phone = models.CharField(max_length=2000)
    degree = models.CharField(max_length=1000)
    summary = models.TextField(max_length=2000)
    school = models.TextField(max_length=2000)
    university = models.TextField(max_length=2000)
    previous_work = models.TextField(max_length=2000)
    skills = models.TextField(max_length=2000)
