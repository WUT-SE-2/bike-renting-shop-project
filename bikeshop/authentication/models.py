from django.db import models
from comment.models import Comment
from complaint.models import Complaint
import datetime
from reservation.models import Reservation

class Person(models.Model):
    person_ID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default='')
    surname = models.CharField(max_length=50, default='')
    email = models.CharField(max_length=50, default='')
    phoneNumber = models.CharField(max_length=20, default='')
    comments = models.ForeignKey(Comment, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class Worker(Person):
    reservations = models.ForeignKey(Reservation, on_delete=models.CASCADE)


# class Mechanic(Person):
