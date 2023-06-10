from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.all),
    path('cancel/<int:reservation_id>', views.cancel),
    path('reserve/<int:bike_id>', views.reserve),
    path('detail/<int:reservation_id>', views.detail),
    path('confirm/<int:reservation_id>', views.confirm),
    path('decline/<int:reservation_id>', views.decline),
]