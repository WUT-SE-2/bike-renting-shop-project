from django.db import models
from authentication.models import Consumer, Worker
# Create your models here.
class Comment(models.Model):
    comm_ID = models.AutoField(primary_key=True)
    description = models.CharField(max_length=300, default='')
    consumer = models.ForeignKey(Consumer, on_delete=models.SET_NULL, blank=True, null=True)
    worker = models.ForeignKey(Worker, on_delete=models.SET_NULL, blank=True, null=True)