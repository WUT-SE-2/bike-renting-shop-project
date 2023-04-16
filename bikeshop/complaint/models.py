from django.db import models
from comment.models import Comment

# Create your models here.
class Complaint(models.Model):
    comp_ID = models.AutoField(primary_key=True)
    description = models.CharField(max_length=300, default='')
    comments = models.ForeignKey(Comment, on_delete=models.CASCADE)
    last_updated = models.DateTimeField()

    class Status(models.TextChoices):
        closed = 'closed',
        opened = 'opened',
        solved = 'solved',

    status = models.CharField(
        max_length=6,
        choices=Status.choices,
        default=Status.closed,
    )

