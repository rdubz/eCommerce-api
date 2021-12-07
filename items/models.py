from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Item(models.Model):

    name = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=False)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=False, null=True)
    sale_price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)


class Size(models.Model):

    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='sizes')
    size = models.CharField(max_length=20, blank=False)
    quantity = models.IntegerField(blank=False)


class Photo(models.Model):

    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='photos')
    photo = models.ImageField(upload_to='images')
