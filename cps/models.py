from django.db import models

# Create your models here.

class Genset(models.Model):
    available = models.BooleanField(default=True)
    number = models.IntegerField(unique=True) 
    serial_number = models.CharField(max_length=200)
    make = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    cap_kw = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
