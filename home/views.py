from django.shortcuts import render
from vehicle.models import Car
from django.views.generic import DetailView

def index(request):
    cars = Car.objects.all()
    context = {'cars': cars}
    return render(request, "index.html", context)
	

def carform(request):
	return render(request,"form.html")





