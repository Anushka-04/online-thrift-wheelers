from django.shortcuts import render

from vehicle.models import Car

def index(request):
	cars = Car.objects.all()
	context = {'cars': cars}

	return render(request, "index.html", context)





