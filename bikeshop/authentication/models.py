from django.db import models
class Person(models.Model):
    person_ID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default='')
    surname = models.CharField(max_length=50, default='')
    email = models.CharField(max_length=50, default='')
    phoneNumber = models.CharField(max_length=20, default='')


    class Meta:
        abstract = True


class Worker(Person):
    another_field = models.CharField(max_length=50, default='')


class Consumer(Person):
    random_field = models.CharField(max_length=50, default='')

