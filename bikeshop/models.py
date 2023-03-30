from django.db import models


class Bike(models.Model):
    bike_ID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, default='')
    usable = models.BooleanField(default=False)
    location = models.CharField(max_length=30, default='')
    purchase_date = models.DateTimeField()


class Comment(models.Model):
    comm_ID = models.AutoField(primary_key=True)
    description = models.CharField(max_length=300, default='')


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


class Reservation(models.Model):
    reservation_ID = models.AutoField(primary_key=True)
    reservation_date_request = models.DateTimeField()
    reservation_date_end = models.DateTimeField()
    reserved_bike = models.ForeignKey(Bike, on_delete=models.CASCADE)

    class ReservationStatus(models.TextChoices):
        confirmed = 'confirmed',
        not_confirmed = 'not confirmed',
        finished = 'finished',
        pending = 'pending',

    consumerStatus = models.CharField(
        max_length=13,
        choices=ReservationStatus.choices,
        default=ReservationStatus.pending,
    )


class Payment(models.Model):
    payment_ID = models.AutoField(primary_key=True)
    payment_date = models.DateTimeField()


class Person(models.Model):
    person_ID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default='')
    surname = models.CharField(max_length=50, default='')
    email = models.CharField(max_length=50, default='')
    phoneNumber = models.CharField(max_length=20, default='')
    comments = models.ForeignKey(Comment, on_delete=models.CASCADE)

    class Meta:
        abstract = True

    @classmethod
    def comment(cls):
        pass


class Consumer(Person):
    payments = models.ForeignKey(Payment, on_delete=models.CASCADE)
    reservations = models.ForeignKey(Reservation, on_delete=models.CASCADE)

    class ConsumerStatus(models.TextChoices):
        normal = 'normal',
        blocked = 'blocked',

    consumerStatus = models.CharField(
        max_length=7,
        choices=ConsumerStatus.choices,
        default=ConsumerStatus.normal,
    )

    @classmethod
    def edit_information(cls):
        pass

    @classmethod
    def delete_account(cls):
        pass

    @classmethod
    def close_complaint(cls):
        pass

    @classmethod
    def reopen_complaint(cls):
        pass

    @classmethod
    def issue_complaint(cls):
        pass

    @classmethod
    def create_reservation(cls):
        pass

    @classmethod
    def cancel_reservation(cls):
        pass

    @classmethod
    def pay(cls):
        pass


class Worker(Person):
    reservations = models.ForeignKey(Reservation, on_delete=models.CASCADE)

    @classmethod
    def cancel_reservation(cls):
        pass

    @classmethod
    def confirm_reservation(cls):
        pass

    @classmethod
    def close_complaint(cls):
        pass

    @classmethod
    def delete_consumer(cls):
        pass

    @classmethod
    def suspend_consumer(cls):
        pass

    @classmethod
    def unblock_consumer(cls):
        pass

    @classmethod
    def issue_payment(cls):
        pass


class Mechanic(Person):
    @classmethod
    def transport_bike(cls):
        pass

    @classmethod
    def repair_bike(cls):
        pass

    @classmethod
    def perform_extra_service(cls):
        pass
