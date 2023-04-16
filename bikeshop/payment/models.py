from django.db import models

# Create your models here.

class Payment(models.Model):
    payment_ID = models.AutoField(primary_key=True)
    payment_date = models.DateTimeField()

