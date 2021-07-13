from django.urls import path
from . import views




urlpatterns = [
    path("cars/", views.vehicle_cars, name="vehicle_cars"),
    path("bikes/", views.vehicle_bikes, name="vehicle_bikes")
    ]