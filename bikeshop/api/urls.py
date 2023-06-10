from django.urls import path
from . import views


urlpatterns = [
    path('bikes/', views.Bikes.as_view()),
    path('comments/', views.Comments.as_view()),
    path('complaints/', views.Complaints.as_view()),
    path('reservations/', views.Reservations.as_view()),
    path('payments/', views.Payments.as_view()),
    path('consumers/', views.Consumers.as_view()),
    path('workers/', views.Workers.as_view()),

    path('bike/<int:pk>/', views.Bike.as_view()),
    path('comment/<int:pk>/', views.Comment.as_view()),
    path('complaint/<int:pk>/', views.Complaint.as_view()),
    path('reservation/<int:pk>/', views.Reservation.as_view()),
    path('payment/<int:pk>/', views.Payment.as_view()),
    path('consumer/<int:pk>/', views.Consumer.as_view()),
    path('worker/<int:pk>/', views.Worker.as_view()),
    
]