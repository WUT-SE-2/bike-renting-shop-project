from django.urls import path
from . import views


urlpatterns = [
    path('getbikes/', views.BikeDataREST.getBikeData),
    path('getcomments/', views.CommentDataREST.getCommentData),
    path('getcomplaints/', views.ComplaintDataREST.getComplaintData),
    path('getreservations/', views.ReservationDataREST.getReservationData),
    path('getpayments/', views.PaymentDataREST.getPaymentData),
    path('getperson/', views.PersonDataREST.getPersonData),
    path('getworkers/', views.WorkerDataREST.getWorkerData),

    path('postbikes/', views.BikeDataREST.postBikeData),
    path('postcomments/', views.CommentDataREST.postCommentData),
    path('postcomplaints/', views.ComplaintDataREST.postComplaintData),
    path('postreservations/', views.ReservationDataREST.postReservationData),
    path('postpayments/', views.PaymentDataREST.postReservationData),
    path('postperson/', views.PersonDataREST.postPersonData),
    path('postworkers/', views.WorkerDataREST.postWorkerData),
    # path('mechanics/', views.getMechanicData),
]