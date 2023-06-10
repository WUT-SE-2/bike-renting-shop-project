from django.shortcuts import render, redirect
from .models import Comment
from complaint.models import Complaint
from datetime import datetime, timezone
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
@login_required(login_url='/login')
def add(request, complaint_id):
    user = request.user
    if request.method == 'POST':
        description = request.POST['description']
        complaint = Complaint.objects.filter(comp_ID=complaint_id).first()
        if complaint is not None and description is not None and description != "":
            comment = Comment.objects.create(user=user, comment=description, complaint=complaint)
            complaint.last_updated = datetime.now(timezone.utc)
            complaint.save()
            comment.save()
            messages.success(request, "Comment has been added")
        else:
            messages.error("Comment can't be empty")
    href_redirect = "/complaint/detail/" + str(complaint_id)
    return redirect(href_redirect)
