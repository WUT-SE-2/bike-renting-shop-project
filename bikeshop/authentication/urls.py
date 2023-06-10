from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.signout, name='signout'),
    path('activate/<slug:uidb64>/<slug:token>', views.activate, name="activate"),
    path('profile/', views.profile_print),
    path('profileEdit/', views.profile_edit),
    path('mechanic/home', views.home_mechanic),
    path('worker/home', views.home_worker),

]