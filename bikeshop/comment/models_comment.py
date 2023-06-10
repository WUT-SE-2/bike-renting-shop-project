from django.db import models
from django.contrib.auth.models import User
from complaint.models import Complaint
# Create your models here.
class Comment(models.Model):
    comm_ID = models.AutoField(primary_key=True)
    description = models.CharField(max_length=300, default='')
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    comment = models.CharField(max_length=300, default='')
    complaint = models.ForeignKey(Complaint, on_delete=models.PROTECT)


