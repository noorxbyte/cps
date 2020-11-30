from django.db import models

# Create your models here.

class Genset(models.Model):
    number = models.IntegerField(unique=True) 
    serial_number = models.CharField(max_length=200)
    make = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    cap_kw = models.IntegerField()
