from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='/login')
def payment(request):
    return render(request, 'html/payment.html')