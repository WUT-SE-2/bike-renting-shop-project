from django.shortcuts import render, redirect
from .models import Complaint
from datetime import datetime, timedelta, timezone
from reservation.models import Reservation
from authentication.authentication_helpers import confirm_consumer, confirm_mechanic, confirm_worker
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from comment.models import Comment
from authentication.models import Mechanic, Worker
from django.contrib import messages


# Create your views here.

@login_required(login_url='/login')
def detail(request, complaint_id):
    user = request.user
    if confirm_consumer(user.id):
        complaint = Complaint.objects.filter(comp_ID=complaint_id).first()
        comments = Comment.objects.filter(complaint__comp_ID=complaint_id).all().order_by('date')
        return render(request, 'html/complaint-detail.html', {'complaint': complaint, 'comments': comments})
    if confirm_mechanic(user.id):
        complaint = Complaint.objects.filter(comp_ID=complaint_id).first()
        comments = Comment.objects.filter(complaint__comp_ID=complaint_id).all().order_by('date')
        return render(request, 'html/complaint-detail-mechanic.html', {'complaint': complaint, 'comments': comments})
    if confirm_worker(user.id):
        complaint = Complaint.objects.filter(comp_ID=complaint_id).first()
        comments = Comment.objects.filter(complaint__comp_ID=complaint_id).all().order_by('date')
        return render(request, 'html/complaint-detail-worker.html', {'complaint': complaint, 'comments': comments})
    return HttpResponseForbidden()


@login_required(login_url='/login')
def all(request):
    user = request.user
    if confirm_consumer(user.id):
        complaints = Complaint.objects.filter(issue_person__id=user.id).all().order_by('-comp_ID')
        return render(request, 'html/complaint-list.html', {'complaints': complaints})
    if confirm_worker(user.id):
        complaints = Complaint.objects.filter(worker__user__id=user.id).all()
        return render(request, 'html/complaint-list-worker.html', {'complaints': complaints})
    if confirm_mechanic(user.id):
        complaints = Complaint.objects.filter(mechanic__user__id=user.id).all()
        return render(request, 'html/complaint-list-mechanic.html', {'complaints': complaints})
    return HttpResponseForbidden()


@login_required(login_url='/login')
def close(request, complaint_id):
    if not confirm_consumer(request.user.id) and not confirm_worker(request.user.id):
        return HttpResponseForbidden()
    if Complaint.objects.filter(comp_ID=complaint_id).exists():
        complaint = Complaint.objects.filter(comp_ID=complaint_id).first()
        complaint.status = 'closed'
        complaint.last_updated = datetime.now(timezone.utc)
        complaint.save()
        mechanic = complaint.mechanic
        worker = complaint.worker
        mechanic.active_ticket_num = mechanic.active_ticket_num - 1
        mechanic.total_tickets_num = mechanic.total_tickets_num + 1
        worker.active_ticket_num = worker.active_ticket_num - 1
        worker.total_tickets_num = worker.total_tickets_num + 1
        mechanic.save()
        worker.save()
        messages.success(request, "Complaint has been closed")
    return redirect('/complaint/all')


@login_required(login_url='/login')
def reopen(request, complaint_id):
    if not confirm_consumer(request.user.id) and not confirm_worker(request.user.id):
        return HttpResponseForbidden()
    if Complaint.objects.filter(comp_ID=complaint_id).exists():
        complaint = Complaint.objects.filter(comp_ID=complaint_id).first()
        timediff = datetime.now(timezone.utc) - complaint.last_updated
        if timediff.days < 31:
            complaint.status = 'opened'
            complaint.last_updated = datetime.now(timezone.utc)
            complaint.save()
            mechanic = complaint.mechanic
            worker = complaint.worker
            mechanic.active_ticket_num = mechanic.active_ticket_num + 1
            mechanic.total_tickets_num = mechanic.total_tickets_num - 1
            worker.active_ticket_num = worker.active_ticket_num + 1
            worker.total_tickets_num = worker.total_tickets_num - 1
            mechanic.save()
            worker.save()
            messages.success(request, "Complaint has been reopened")
        else:
            messages.error(request, "Complaint is too old to be reopened please create a new complaint")
    return redirect('/complaint/all')


# this is only a post
@login_required(login_url='/login')
def create(request, reservation_id):
    user = request.user
    if not confirm_consumer(user.id):
        return HttpResponseForbidden()
    reservation = Reservation.objects.filter(reservation_ID=reservation_id).first()
    if request.method == "POST":
        details = request.POST['details']
        complaint = Complaint.objects.create(description=details, issue_person=user, reservation=reservation,
                                             status='opened')
        mechanic = Mechanic.objects.all().order_by('active_ticket_num').first()
        worker = Worker.objects.all().order_by('active_ticket_num').first()
        mechanic.active_ticket_num = mechanic.active_ticket_num + 1
        worker.active_ticket_num = worker.active_ticket_num + 1
        mechanic.save()
        worker.save()
        complaint.worker = worker
        complaint.mechanic = mechanic
        complaint.save()
        messages.success(request, "Complaint has been created")
        return redirect('/complaint/all/')

    return render(request, 'html/complaint.html', {'reservation': reservation})
