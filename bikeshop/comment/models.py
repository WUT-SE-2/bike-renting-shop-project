from django.db import models

# Create your models here.
class Comment(models.Model):
    comm_ID = models.AutoField(primary_key=True)
    description = models.CharField(max_length=300, default='')

