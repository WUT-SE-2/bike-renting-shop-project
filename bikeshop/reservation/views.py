from django.shortcuts import render, redirect
from bike.models import Bike
from .models import Reservation
from datetime import datetime, date
from django.contrib.auth.decorators import login_required
from authentication.authentication_helpers import confirm_consumer, confirm_mechanic, confirm_worker
from django.http import HttpResponseForbidden
from django.contrib import messages

# Create your views here.


@login_required(login_url='/login')
def detail(request, reservation_id):
    reservation = Reservation.objects.filter(reservation_ID=reservation_id).first()
    if reservation is not None:
        return render(request, 'html/reservation-detail.html', {'reservation': reservation})
    return redirect('/reservation/all')


@login_required(login_url='/login')
def all(request):
    user = request.user
    reservations = Reservation.objects.all().order_by('-reservation_ID')
    if confirm_consumer(request.user.id):
        reservations = reservations.filter(user__id=user.id).all()
        return render(request, 'html/reservation-list.html', {'reservations': reservations})
    if confirm_worker(user.id):
        return render(request, 'html/reservation-list-worker.html', {'reservations': reservations})
    return HttpResponseForbidden()


@login_required(login_url='/login')
def cancel(request, reservation_id):
    if not confirm_consumer(request.user.id):
        return HttpResponseForbidden()
    reservation = Reservation.objects.filter(reservation_ID=reservation_id).first()
    reservation.delete()
    bike = Bike.objects.filter(bike_ID=reservation.reserved_bike.bike_ID).first()
    bike.bike_status = 'free'
    bike.save()
    messages.success(request, "Reservation cancelled")
    return redirect('/reservation/all')


@login_required(login_url='/login')
def reserve(request, bike_id):
    if not confirm_consumer(request.user.id):
        return HttpResponseForbidden()
    bike = Bike.objects.filter(bike_ID=bike_id).first()
    # check if the bike is not reserved and then
    if request.method == "POST":
        # case when the method is post
        date_from = request.POST['date_from']
        date_till = request.POST['date_till']
        date_format = '%Y-%m-%d'
        date_from_date = datetime.strptime(date_from, date_format)
        date_till_date = datetime.strptime(date_till, date_format)
        today = datetime.today()
        user = request.user
        if date_from_date > date_till_date or today > date_from_date:
            messages.error(request, "Wrong date. Please choose a proper date")
            return render(request, 'html/bike-reservation.html', {'bike': bike})
        reservation = Reservation.objects.create(reservation_date_request=date_from,
                                                 reservation_date_end=date_till,
                                                 reserved_bike=bike,
                                                 user=user)
        bike.bike_status = Bike.ReservationStatus.reserved
        reservation.reservationStatus = 'pending'
        bike.bike_status = 'reserved'
        reservation.save()
        bike.save()
        messages.success(request, "Reservation done. Please wait for confirmation")
        return redirect('/reservation/all/')
    return render(request, 'html/bike-reservation.html', {'bike': bike})


def confirm(request, reservation_id):
    user = request.user
    if confirm_worker(user.id):
        reservation = Reservation.objects.filter(reservation_ID=reservation_id).first()
        if reservation is not None:
            reservation.reservationStatus = 'confirmed'
            bike = reservation.reserved_bike
            bike.save()
            reservation.save()
            messages.success(request, "Reservation completed")
            return redirect('/reservation/all')
    return HttpResponseForbidden()


def decline(request, reservation_id):
    user = request.user
    if confirm_worker(user.id):
        reservation = Reservation.objects.filter(reservation_ID=reservation_id).first()
        if reservation is not None:
            reservation.reservationStatus = 'not confirmed'
            bike = reservation.reserved_bike
            bike.bike_status = 'free'
            bike.save()
            reservation.save()
            messages.success(request, "Reservation has been declined")
            return redirect('/reservation/all')
    return HttpResponseForbidden()