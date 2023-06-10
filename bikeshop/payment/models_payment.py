from django.db import models
from django.contrib.auth.models import User
from  reservation.models import Reservation
from datetime import datetime
# Create your models here.


class Payment(models.Model):
    payment_ID = models.AutoField(primary_key=True)
    payment_date = models.DateTimeField( default=datetime.now())
    person = models.ForeignKey(User, models.SET_NULL, blank=True, null=True)
    amount = models.FloatField(default=100.0)
    reservation = models.OneToOneField(Reservation, on_delete=models.PROTECT)