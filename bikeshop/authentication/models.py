from django.db import models
from django.contrib.auth.models import User
from django.dispatch.dispatcher import receiver
from django.db.models.signals import post_save


class Worker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phoneNumber = models.CharField(max_length=20, default='')
    manager_email = models.CharField(max_length=50, default='head.admin@gmail.com')
    active_ticket_num = models.IntegerField(default=0)
    total_tickets_num= models.IntegerField(default=0)


class Consumer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phoneNumber = models.CharField(max_length=20, default='')
    amount = models.FloatField(default=100.0)

    class AccountStatus(models.TextChoices):
        active = 'active',
        blocked = 'blocked',
        deactivated = 'deactivated'
        not_confirmed = 'not_confirmed'
    account_status = models.CharField(
        max_length=13,
        choices=AccountStatus.choices,
        default=AccountStatus.not_confirmed,
    )


class Mechanic(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phoneNumber = models.CharField(max_length=20, default='')
    company = models.CharField(max_length=50, default='Bike Industries')
