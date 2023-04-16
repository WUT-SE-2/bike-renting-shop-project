from django.db import models


class Bike(models.Model):
    bike_ID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, default='')
    usable = models.BooleanField(default=False)
    location = models.CharField(max_length=30, default='')
    purchase_date = models.DateTimeField()
