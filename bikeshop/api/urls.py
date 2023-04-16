from django.urls import path
from . import views


urlpatterns = [
    path('bikes/', views.getBikeData),
    path('comments/', views.getCommentData),
    path('complaints/', views.getComplaintData),
    path('reservations/', views.getReservationData),
    path('payments/', views.getPaymentData),
    path('consumers/', views.getConsumerData),
    path('workers/', views.getWorkerData),
    # path('mechanics/', views.getMechanicData),
]