from django.db import models
from django.contrib.auth.models import User
from authentication.models import Worker, Mechanic
from datetime import datetime
from reservation.models import Reservation


# Create your models here.
class Complaint(models.Model):
    comp_ID = models.AutoField(primary_key=True)
    description = models.CharField(max_length=300, default='')
    last_updated = models.DateTimeField(default=datetime.now())
    issue_person = models.ForeignKey(User, on_delete=models.PROTECT)
    worker = models.ForeignKey(Worker, on_delete=models.PROTECT, null=True, blank=True)
    mechanic = models.ForeignKey(Mechanic, on_delete=models.PROTECT, null=True, blank=True)
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE, null=True, blank=True,)

    class Status(models.TextChoices):
        closed = 'closed',
        opened = 'opened',
        solved = 'solved',

    status = models.CharField(
        max_length=6,
        choices=Status.choices,
        default=Status.closed,
    )

