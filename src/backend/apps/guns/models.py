from django.db import models


class Gun(models.Model):
    for_sale = models.BooleanField(default=False)
    stock_quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    manufacturer = models.CharField(max_length=40)
    model = models.CharField(max_length=20)
    caliber = models.CharField(max_length=15)
    current_owner = models.CharField(max_length=40)
