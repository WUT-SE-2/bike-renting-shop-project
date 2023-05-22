from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
<<<<<<< HEAD
    path('login/', views.login, name='login'),
=======
    path('login/', views.login),
>>>>>>> b5f63c77815bb65aed112e968d38bd7df1d54c0b
    path('register/', views.register)
]