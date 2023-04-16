# from django.db import models
# import datetime
#
#
# class Comment(models.Model):
#     comm_ID = models.AutoField(primary_key=True)
#     description = models.CharField(max_length=300, default='')
#
#
# class Complaint(models.Model):
#     comp_ID = models.AutoField(primary_key=True)
#     description = models.CharField(max_length=300, default='')
#     comments = models.ForeignKey(Comment, on_delete=models.CASCADE)
#     last_updated = models.DateTimeField()
#
#     class Status(models.TextChoices):
#         closed = 'closed',
#         opened = 'opened',
#         solved = 'solved',
#
#     status = models.CharField(
#         max_length=6,
#         choices=Status.choices,
#         default=Status.closed,
#     )
#
#
# class Reservation(models.Model):
#     reservation_ID = models.AutoField(primary_key=True)
#     reservation_date_request = models.DateTimeField()
#     reservation_date_end = models.DateTimeField()
#     reserved_bike = models.ForeignKey(Bike, on_delete=models.CASCADE)
#
#     class ReservationStatus(models.TextChoices):
#         confirmed = 'confirmed',
#         not_confirmed = 'not confirmed',
#         finished = 'finished',
#         pending = 'pending',
#
#     reservationStatus = models.CharField(
#         max_length=13,
#         choices=ReservationStatus.choices,
#         default=ReservationStatus.pending,
#     )
#
#
# class Payment(models.Model):
#     payment_ID = models.AutoField(primary_key=True)
#     payment_date = models.DateTimeField()
#
#
# class Person(models.Model):
#     person_ID = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=50, default='')
#     surname = models.CharField(max_length=50, default='')
#     email = models.CharField(max_length=50, default='')
#     phoneNumber = models.CharField(max_length=20, default='')
#     comments = models.ForeignKey(Comment, on_delete=models.CASCADE)
#
#     class Meta:
#         abstract = True
#
#     @classmethod
#     def comment(cls, description):
#         comment = Comment(description=description)
#         comment.save()
#
#
# class Consumer(Person):
#     payments = models.ForeignKey(Payment, on_delete=models.CASCADE)
#     reservations = models.ForeignKey(Reservation, on_delete=models.CASCADE)
#
#     class ConsumerStatus(models.TextChoices):
#         normal = 'normal',
#         blocked = 'blocked',
#
#     consumerStatus = models.CharField(
#         max_length=7,
#         choices=ConsumerStatus.choices,
#         default=ConsumerStatus.normal,
#     )
#
#     @classmethod
#     def edit_information(cls, name, surname, email, phone_number):
#         cls.name = name
#         cls.surname = surname
#         cls.email = email
#         cls.phoneNumber = phone_number
#
#     @classmethod
#     def delete_account(cls):
#         cls.delete()
#
#     @classmethod
#     def close_complaint(cls, complaint):
#         complaint.status = complaint.Status.closed
#
#     @classmethod
#     def reopen_complaint(cls, complaint):
#         complaint.status = complaint.Status.opened
#
#     @classmethod
#     def issue_complaint(cls, description):
#         new_complaint = Complaint(description=description, last_updated=datetime.datetime.now())
#         new_complaint.save()
#
#     @classmethod
#     def create_reservation(cls, reservation_date_request, reservation_date_end, reserved_bike):
#         new_reservation = Reservation(reservation_date_request=reservation_date_request, reservation_date_end=reservation_date_end, reserved_bike=reserved_bike)
#         new_reservation.save()
#
#     @classmethod
#     def cancel_reservation(cls):
#         pass
#
#     @classmethod
#     def pay(cls):
#         pass
#
#
# class Worker(Person):
#     reservations = models.ForeignKey(Reservation, on_delete=models.CASCADE)
#
#     @classmethod
#     def cancel_reservation(cls):
#         pass
#
#     @classmethod
#     def confirm_reservation(cls, reservation):
#         reservation.reservationStatus = reservation.ReservationStatus.confirmed
#
#     @classmethod
#     def close_complaint(cls, complaint):
#         complaint.status = complaint.Status.closed
#
#     @classmethod
#     def delete_consumer(cls, consumer):
#         consumer.delete()
#
#     @classmethod
#     def suspend_consumer(cls, consumer):
#         consumer.consumerStatus = consumer.ConsumerStatus.blocked
#
#     @classmethod
#     def unblock_consumer(cls, consumer):
#         consumer.consumerStatus = consumer.ConsumerStatus.normal
#
#     @classmethod
#     def issue_payment(cls):
#         pass
#
#
# class Mechanic(Person):
#     @classmethod
#     def transport_bike(cls, new_location, bike):
#         bike.location = new_location
#
#     @classmethod
#     def repair_bike(cls):
#         pass
#
#     @classmethod
#     def perform_extra_service(cls):
#         pass
