from datetime import timezone
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail, EmailMessage
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from .models import Consumer
from bikeshop import settings
from .tokens import generate_token
from django.utils.encoding import force_bytes, force_text
from email.message import EmailMessage
from django.core.mail import EmailMessage, send_mail
from django.contrib.auth.decorators import login_required
from .authentication_helpers import confirm_consumer, confirm_mechanic, confirm_worker
from django.http import HttpResponseForbidden

# Create your views here.


def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        phone_num = request.POST['phone_num']
        if User.objects.filter(username=username):
            messages.error(request, "Username already exist! Please try some other username.")
            return redirect('home')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered!!")
            return redirect('home')

        if len(username) > 20:
            messages.error(request, "Username must be under 20 characters!!")
            return redirect('home')

        if pass1 != pass2:
            messages.error(request, "Passwords didn't match!!")
            return redirect('home')

        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric!!")
            return redirect('home')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.is_active = False
        myuser.save()
        myconsumer = Consumer.objects.create(user=myuser, phoneNumber=phone_num)
        myconsumer.save()
        messages.success(request,
                         "Your Account has been created succesfully!! Please check your email to confirm your email address in order to activate your account.")

        # Welcome Email
        subject = "Welcome to bike renting shop- Django Login!!"
        message = "Hello " + myuser.first_name + "!! \n" + "Welcome to wypozyczalnia rowerkow!! \nThank you for visiting our website\n. We have also sent you a confirmation email, please confirm your email address. \n\nThank You\n"
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject, message, from_email, to_list, fail_silently=True)

        # Email Address Confirmation Email
        current_site = get_current_site(request)
        email_subject = "Confirm your Email @ wypozyczalnia rowerkow - Django Login!!"
        message2 = render_to_string('html/email_conf.html', {

            'name': myuser.first_name,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
            'token': generate_token.make_token(myuser)
        })
        email = EmailMessage(
            email_subject,
            message2,
            settings.EMAIL_HOST_USER,
            [myuser.email],
        )
        email.fail_silently = True
        email.send()

        return redirect('login')

    return render(request, "html/registration.html")


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        myuser = None

    if myuser is not None and generate_token.check_token(myuser, token):
        myuser.is_active = True
        myuser.save()
        login(request, myuser)
        messages.success(request, "Your Account has been activated!!")
        if not confirm_consumer(request.user.id):
            return HttpResponseForbidden()
        return redirect('login')
    else:
        return render(request, 'html/email_fail.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['password']
        user = authenticate(username=username, password=pass1)
        if user is not None:
            login(request, user)
            fname = user.first_name
            messages.success(request, "Logged In Sucessfully!!")
            if confirm_worker(user.id):
                return redirect('/worker/home')
            if confirm_consumer(user.id):
                return redirect('/bike/all')
            if confirm_mechanic(user.id):
                return redirect('/mechanic/home')
        else:
            messages.error(request, "Bad Credentials!!")

    return render(request, "html/login.html")


def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('login')


def home(request):
    return render(request, 'html/home.html')


@login_required(login_url='/login')
def profile_print(request):
    u = request.user
    user = User.objects.filter(id=u.id).first()
    consumer = Consumer.objects.filter(user_id=user.id).first()
    if not confirm_consumer(u.id):
        return HttpResponseForbidden()

    return render(request, 'html/profile-print.html', {'consumer': consumer, 'user': user})


@login_required(login_url='/login')
def profile_edit(request):
    user = request.user
    if not confirm_consumer(request.user.id):
        return HttpResponseForbidden()
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        print(password)
        print(password2)
        phoneNumber = request.POST['phoneNumber']
        print(phoneNumber)
        consumer = Consumer.objects.filter(user__id=user.id).first()
        if password is not None and password2 is not None:
            if password2 == password and password != "":
                user.set_password(password)
        if email is not None:
            if len(User.objects.filter(email=email).all()) == 0:
                user.email = email
        if first_name is not None:
            user.first_name = first_name
        if last_name is not None:
            user.last_name = last_name
        if phoneNumber is not None:
            consumer.phoneNumber = phoneNumber
        user.save()
        consumer.save()
        return redirect('/profileEdit/')
    consumer = Consumer.objects.filter(user__id=user.id).first()
    return render(request, 'html/profile-edit.html', {'consumer': consumer, 'user': user})


@login_required(login_url='/login')
def worker_home(request):
    return render(request, 'html/home-worker.html')


@login_required(login_url='/login')
def mechanic_home(request):
    return render(request, 'html/home-mechanic.html')
