from django.urls import path
from . import views


urlpatterns = [
path('bikes/', views.getBikeData),
path('comments/', views.getCommentData),
path('complaints/', views.getComplaintData),
path('reservations/', views.getReservationData),
path('payments/', views.getPaymentdata),
path('consumers/', views.getConsumerdata),
path('workers/', views.getWorkerdata),
path('mechanics/', views.getMechanicdata),
]