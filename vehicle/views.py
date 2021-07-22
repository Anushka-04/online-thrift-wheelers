from django.shortcuts import render

from .models import Car, Bike
# Create your views here.


def vehicle_cars(request):
	cars = Car.objects.all()
	context = {'cars': cars}

	return render(request,"cars.html", context)


def vehicle_bikes(request):
	bikes = Bike.objects.all()
	context = {'bikes': bikes}

	return render(request, "bikes.html", context)
