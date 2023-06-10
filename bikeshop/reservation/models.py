from django.db import models
from django.contrib.auth.models import User
from bike.models import Bike
# Create your models here.


class Reservation(models.Model):
    reservation_ID = models.AutoField(primary_key=True)
    reservation_date_request = models.DateField()
    reservation_date_end = models.DateField()
    reserved_bike = models.ForeignKey(Bike, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    is_paid = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    class ReservationStatus(models.TextChoices):
        confirmed = 'confirmed',
        not_confirmed = 'not confirmed',
        finished = 'finished',
        pending = 'pending',

    reservationStatus = models.CharField(
        max_length=13,
        choices=ReservationStatus.choices,
        default=ReservationStatus.pending,
    )

