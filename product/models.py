from operator import mod
from unicodedata import category
from unittest.util import _MAX_LENGTH
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    date_added = models.DateField(auto_now=True)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ["-date_added"]

class Product(models.Model):
    title = models.CharField(max_length=50)
    price = models.FloatField()
    description = models.TextField()
    category = models.ForeignKey(Category,related_name='category',on_delete=models.CASCADE)
    image = models.ImageField(max_length=5000)
    date_added = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-date_added"]
    
