from django.db import models


class Bike(models.Model):
    bike_ID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, default='')
    usable = models.BooleanField(default=False)
    location = models.CharField(max_length=30, default='')
    purchase_date = models.DateField()
    description = models.CharField(max_length=600, default='This is a bike that could be rented')
    rent_value = models.FloatField(default=100.0)
    hp = models.IntegerField(default=100)
    image = models.ImageField(upload_to='static/bikes', default='', null=True, blank = True)

    class ReservationStatus(models.TextChoices):
        free = 'free',
        rented = 'rented',
        reserved = 'reserved',
        blocked = 'blocked',
        maintain = 'maintain'

    bike_status = models.CharField(
        max_length=13,
        choices=ReservationStatus.choices,
        default=ReservationStatus.free,
    )