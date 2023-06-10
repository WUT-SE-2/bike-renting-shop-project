from django.shortcuts import render, redirect
from bike.models import Bike, Service
from authentication.authentication_helpers import confirm_consumer, confirm_mechanic, confirm_worker, Mechanic
from django.http import HttpResponseForbidden
from reservation.models import Reservation
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def item(request, bike_id):
    bike = Bike.objects.filter(bike_ID=bike_id).first()
    user = request.user
    if confirm_worker(user.id):
        return render(request, 'html/bike-detail-worker.html', {'bike': bike})
    return render(request, 'html/bike-detail.html', {'bike': bike})


def all(request):
    bikes = Bike.objects.all()
    user = request.user
    if confirm_worker(user.id):
        return render(request, 'html/bike-list-worker.html', {'bikes': bikes})

    return render(request, 'html/bikes-list.html', {'bikes': bikes})


@login_required(login_url='/login')
def service(request, bike_id):
    user = request.user
    if not confirm_worker(user.id):
        return HttpResponseForbidden()
    bike = Bike.objects.filter(bike_ID=bike_id).first()
    if bike is not None:
        bike.bike_status = "maintain"
        mechanic = Mechanic.objects.all().order_by('active_service_num').first()
        service_cur = Service.objects.create(mechanic=mechanic, bike=bike, service_type='service')
        service_cur.save()
        bike.save()
        reservations = Reservation.objects.filter(reserved_bike__bike_ID=bike_id).all()
        if reservations is not None:
            for reservation in reservations:
                reservation.reservationStatus = "not confirmed"
                reservation.save()
                messages.success(request, "Service has been issued for the bike")
    return redirect('/bike/all')


@login_required(login_url='/login')
def service_all(request):
    user = request.user
    if not confirm_mechanic(user.id):
        return HttpResponseForbidden()
    mechanic = Mechanic.objects.filter(user__id=user.id).first()
    services = Service.objects.filter(is_active=True).filter(mechanic=mechanic).all()
    return render(request, 'html/service-all.html', {'services': services})


@login_required(login_url='/login')
def add(request):
    user = request.user
    if confirm_worker(user.id):
        if request.method == "POST":
            name = request.POST['name']
            location = request.POST['location']
            purchase_date = request.POST['purchase_date']
            details = request.POST['details']
            rent_value = request.POST['rent_value']
            service_date = request.POST['service_date']
            hp = request.POST['hp']
            img = request.FILES['img']
            bike = Bike.objects.create(name=name, location=location, purchase_date=purchase_date,
                                       description=details, usable=True, rent_value=rent_value,
                                       service_date=service_date, hp=hp, image=img)
            bike.save()
            messages.success(request, "Bike has been added")
            return redirect('/bike/all')
        return render(request, 'html/add-bike.html')
    return HttpResponseForbidden()


@login_required(login_url='/login')
def send_bike(request, bike_id):
    user = request.user
    if not confirm_mechanic(user.id):
        return HttpResponseForbidden()
    bike = Bike.objects.filter(bike_ID=bike_id).first()
    bike.bike_status = 'rented'
    bike.save()
    mechanic = Mechanic.objects.filter(user__id=user.id).first()
    mechanic.active_service_num= int(mechanic.active_service_num) - 1
    mechanic.total_service_num = int(mechanic.total_service_num) + 1
    service = Service.objects.filter(is_active=True).filter(bike=bike).first()
    reservation = Reservation.objects.filter(reservationStatus = 'confirmed').filter(reserved_bike = bike).first()
    reservation.reservationStatus = 'finished'
    reservation.save()
    service.is_active = False
    service.save()
    mechanic.save()
    messages.success(request, "Bike sended")
    return redirect('/bike/service/all')


@login_required(login_url='/login')
def repair(request, bike_id):
    user = request.user
    if not confirm_mechanic(user.id):
        return HttpResponseForbidden()
    bike = Bike.objects.filter(bike_ID=bike_id).first()
    mechanic = Mechanic.objects.filter(user__id=user.id).first()
    mechanic.active_service_num = int(mechanic.active_service_num) - 1
    mechanic.total_service_num = int(mechanic.total_service_num) + 1
    bike.bike_status = 'free'
    bike.save()
    mechanic.save()
    messages.success(request, 'Bike repaired')
    service = Service.objects.filter(is_active=True).filter(bike=bike).first()
    service.is_active = False
    service.save()
    messages.success(request, "Bike repaired request submitted")
    return redirect('/bike/service/all')


@login_required(login_url='/login')
def return_bike(request, bike_id):
    user = request.user
    if confirm_consumer(user.id):
        bike = Bike.objects.filter(bike_ID=bike_id).first()
        services = Service.objects.filter(is_active = True).filter(bike = bike).all()
        if len(services) > 0:
            messages.error(request, "Bike request already submitted")
            return redirect('/reservation/all')
        mechanic = Mechanic.objects.all().order_by('active_service_num').first()
        service_cur = Service.objects.create(mechanic=mechanic, bike=bike, service_type='receive')
        mechanic.active_service_num = int(mechanic.active_service_num) + 1
        mechanic.save()
        service_cur.save()
        messages.success(request, "Bike return request submitted")
        return redirect('/reservation/all')
    if confirm_mechanic(user.id):
        bike = Bike.objects.filter(bike_ID=bike_id).first()
        bike.bike_status = 'free'
        bike.save()
        mechanic = Mechanic.objects.filter(user__id=user.id).first()
        mechanic.active_service_num = int(mechanic.active_service_num) - 1
        mechanic.total_service_num = int(mechanic.total_service_num) + 1
        service = Service.objects.filter(is_active=True).filter(bike=bike).first()
        service.is_active = False
        service.save()
        mechanic.save()
        messages.success(request, "Bike submitted")
        return redirect('/bike/service/all')
    return HttpResponseForbidden()


@login_required(login_url='/login')
def request(request, bike_id):
    if confirm_consumer:
        bike = Bike.objects.filter(bike_ID=bike_id).first()
        service = Service.objects.filter(is_active=True).filter(bike=bike).all()
        if len(service) > 0:
            messages.error(request, "Bike get request already submitted")
            return redirect('/reservation/all')
        mechanic = Mechanic.objects.all().order_by('active_service_num').first()
        service_cur = Service.objects.create(mechanic=mechanic, bike=bike, service_type='send')
        mechanic.active_service_num = int(mechanic.active_service_num) + 1
        mechanic.save()
        service_cur.save()
        messages.success(request, "Bike return request submitted")
        return redirect('/reservation/all')
    return HttpResponseForbidden()