from django.db import models
from bike.models import Bike
# Create your models here.


class Reservation(models.Model):
    reservation_ID = models.AutoField(primary_key=True)
    reservation_date_request = models.DateTimeField()
    reservation_date_end = models.DateTimeField()
    reserved_bike = models.ForeignKey(Bike, on_delete=models.CASCADE)

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

