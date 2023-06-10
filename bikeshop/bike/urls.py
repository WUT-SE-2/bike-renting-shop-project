from django.urls import path
from . import views

urlpatterns = [
    path('item/<int:bike_id>', views.item),
    path('all/', views.all),
    path('service/<int:bike_id>', views.service),
    path('add', views.add),
    path('service/all', views.service_all),
    path('repair/<int:bike_id>', views.repair),
    path('return/<int:bike_id>', views.return_bike),
    path('send/<int:bike_id>', views.send_bike),
    path('request/<int:bike_id>', views.request)
]