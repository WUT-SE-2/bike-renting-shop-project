from django.db import models
from authentication.models import Consumer
# Create your models here.

class Payment(models.Model):
    payment_ID = models.AutoField(primary_key=True)
    payment_date = models.DateTimeField()
    person = models.ForeignKey(Consumer, models.SET_NULL, blank=True, null=True)