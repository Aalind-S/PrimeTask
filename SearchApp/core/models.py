from django.db import models

# Create your models here.
class Restaurant(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=500)
    location = models.CharField(max_length=500)
    latitude = models.DecimalField(max_digits=22, decimal_places=16)
    longitude = models.DecimalField(max_digits=22, decimal_places=16)
    menu_items = models.JSONField()
    full_details = models.JSONField(blank=True, null=True)

"""class RestuarantMenu(models.Model):
    id = id = models.IntegerField(primary_key=True)"""
    