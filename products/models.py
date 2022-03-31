from django.db import models
from django.forms import IntegerField

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=255)
    descriptions = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    inventtory_quantity = IntegerField()