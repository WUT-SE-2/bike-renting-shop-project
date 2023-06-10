from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from reservation.models import Reservation
from authentication.models import Consumer, Mechanic
from .models import Payment
from django.contrib.auth.decorators import login_required
from authentication.authentication_helpers import confirm_consumer, confirm_mechanic, confirm_worker
from django.http import HttpResponseForbidden
from django.contrib import messages
from bike.models import Service


# Create your views here.


@login_required(login_url='/login')
def payment(request, reservation_id):
    user = request.user
    if not confirm_consumer(user.id):
        return HttpResponseForbidden()
    if Reservation.objects.filter(reservation_ID=reservation_id).exists():
        reservation = Reservation.objects.filter(reservation_ID=reservation_id).first()
        if reservation.user.id == user.id:
            return render(request, 'html/payment.html', {'reservation': reservation})
    return render(request, 'html/payment.html')


@login_required(login_url='/login')
def pay(request, reservation_id):
    user = request.user
    if not confirm_consumer(user.id):
        return HttpResponseForbidden()
    if request.method == "POST":
        print("post")
        if Reservation.objects.filter(reservation_ID=reservation_id).exists():
            reservation = Reservation.objects.filter(reservation_ID=reservation_id).first()
            if reservation.user.id == user.id:
                consumer = Consumer.objects.filter(user__id=user.id).first()
                if consumer.amount >= reservation.reserved_bike.rent_value:
                    consumer.amount = consumer.amount - reservation.reserved_bike.rent_value
                    reservation.is_paid = True
                    consumer.save()
                    payment = Payment.objects.create(person=user, reservation=reservation,
                                                     amount=reservation.reserved_bike.rent_value)
                    payment.save()
                    reservation.save()
                    messages.success(request, "Payment has been done")
                    # create new service
                    mechanic = Mechanic.objects.all().order_by("active_service_num").first()
                    return redirect('/payment/all')
                else:
                    messages.error(request, "Not enough money")
    return redirect('/reservation/all')


@login_required(login_url='/login')
def all(request):
    user = request.user
    if not confirm_consumer(user.id):
        return HttpResponseForbidden()
    payments = Payment.objects.filter(person__id=user.id).all().order_by('-payment_ID')
    return render(request, 'html/payment-list.html', {'payments': payments})


@login_required(login_url='/login')
def add(request):
    user = request.user
    if not confirm_consumer:
        return HttpResponseForbidden()
    if request.method == "POST":
        amount = request.POST['amount']
        consumer = Consumer.objects.filter(user__id=user.id).first()
        consumer.amount = int(consumer.amount) + int(amount)
        consumer.save()
        messages.success(request,amount + " $ has been added to your account")
        return redirect('/profile')
    return render(request, 'html/payment-add-money.html')
