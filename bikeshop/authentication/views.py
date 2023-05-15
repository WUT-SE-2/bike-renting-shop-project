from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'html/homepage.html')


def login(request):
    return render(request, 'html/login.html')


def edit_profile(request):
    return render(request, 'html/editprofile.html')


def register(request):
    return render(request, 'html/registration.html')