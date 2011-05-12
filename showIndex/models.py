from django.db import models
from django.contrib import admin

# Create your models here.

class District(models.Model):
    district = models.CharField(max_length=50)

class Person(models.Model):
    first_name = models.CharField(max_length=200)
    second_name = models.CharField(max_length=200)
    district_big = models.ForeignKey(District)
    district_medium = models.CharField(max_length=200)
    odzial = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    streat = models.CharField(max_length=200)
    number = models.CharField(max_length=30)
    mobile_phone = models.CharField(max_length=10)
    phone = models.CharField(max_length=14)
    email = models.CharField(max_length=50)
    skype = models.CharField(max_length=50)
    gadu = models.CharField(max_length = 12)
    date_entered = models.DateField()
    skill = models.CharField(max_length=400)
    
admin.site.register(Person)
admin.site.register(District)
