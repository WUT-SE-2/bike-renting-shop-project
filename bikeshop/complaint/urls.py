from django.urls import path
from . import views

urlpatterns = [
    path('all/', views.all),
    path('close/<int:complaint_id>', views.close),
    path('create/<int:reservation_id>', views.create),
    path('reopen/<int:complaint_id>', views.reopen),
    path('detail/<int:complaint_id>', views.detail),
]