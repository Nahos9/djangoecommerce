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
    image = models.CharField(max_length=5000,blank=True)
    date_added = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-date_added"]

class Commande(models.Model):
    items = models.CharField(max_length=150,default="{}")
    nom = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    adresse = models.CharField(max_length=50)
    ville = models.CharField(max_length=50)
    pays = models.CharField(max_length=50)
    zip = models.CharField(max_length=50)
    pricetotal = models.CharField(max_length=12,default=0)
    date_commande = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_commande']
    def __str__(self):
        return self.nom
    
