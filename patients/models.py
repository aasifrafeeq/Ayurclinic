from django.db import models
from django.db.models.fields import DateField

import datetime

# Create your models here.

class Patient(models.Model):
    name=models.CharField(max_length=100)
    gender=models.CharField(max_length=10,default="NIL")
    age=models.PositiveIntegerField()
    diagnosis=models.CharField(max_length=2000,default="NIL")
    date=models.DateField(default=datetime.date.today)
    
    def __str__(self):
        return f"Name:{self.name} Age:{self.age}"

class Medicine(models.Model):
    name = models.CharField(max_length=128)
    price = models.IntegerField()
    users=models.ManyToManyField(Patient,blank=True,related_name="medicines")
    def __str__(self):
        return f"{self.name }: Rs.{self.price}"
