from django.urls import path
from . import views


urlpatterns = [
    path('add/<int:complaint_id>', views.add),
]