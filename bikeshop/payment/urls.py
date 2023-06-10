from django.urls import path
from . import views


urlpatterns = [
    path('payment-confirm/<int:reservation_id>', views.payment),
    path('pay/<int:reservation_id>', views.pay),
    path('all/', views.all),
    path('add/', views.add)
]