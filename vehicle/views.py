from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Car, Bike, Wishlist
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView, View
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
from django.http import HttpResponse, HttpResponseRedirect

with open('C:\\Users\\Acer\\Desktop\\Projects\\thrift-wheelers\\thriftwheelers\\vehicle\\random_forest_regression_model_car.pkl', 'rb') as car:
	model_car = pickle.load(car)

class CarCreateView(LoginRequiredMixin, CreateView):
	model = Car
	template_name = "car-form.html"
	fields = ["name","km_driven","fuel_type","transmission_type","seller_type","year_bought","price","image"]

	def form_valid(self, form):
		form.instance.owner = self.request.user
		return super().form_valid(form)



class CarListView(ListView):
	model = Car
	template_name = "cars.html"
	context_object_name = "cars"
	paginate_by = 3

class CarDetailView(DetailView):
	model = Car
	template_name = "car-detail.html"

class BikeDetailView(DetailView):
	model = Bike
	template_name = "bike-detail.html"

class UserCarListView(ListView):
	model = Car
	template_name = "my-ads-cars.html"
	context_object_name = "cars"
	paginate_by = 4

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Car.objects.filter(owner=user.id)

class CarAdUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
	model = Car
	template_name = "car-form.html"
	fields = ["name","km_driven","fuel_type","transmission_type","seller_type","year_bought","price","image"]

	def form_valid(self, form):
		form.instance.owner = self.request.user
		return super().form_valid(form)

	def test_func(self):
		car = self.get_object()
		if self.request.user == car.owner:
			return True
		else:
			return False

class CarAdDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
	model = Car
	template_name="ad_confirm_delete.html"
	success_url = "/"

	def test_func(self):
		car = self.get_object()
		if self.request.user == car.owner:
			return True
		else:
			return False

class BaseView(View):
    template_context = {
        "cars": Car.objects.all(),
        "bikes": Bike.objects.all(),
    }


@login_required
def add_to_wishlist(request,pk):

   car = get_object_or_404(Car,id=pk)
   user =request.user
   user.car_set.add(car)
   user.save()
   url = reverse('vehicle:user_wishlist',kwargs={'pk':user.id})
   return HttpResponseRedirect(url)

   '''wished_car,created = Wishlist.objects.get_or_create(wished_car=car,
   pk = car.pk,
   user = request.user,
   )
   print(car)
   if created:
   	messages.info(request,'The Car was already added to your wishlist')
   else:
   	messages.info(request,'The Car was added to your wishlist')
   return redirect('vehicle:wishlist',pk=pk)'''

def wishlist(request,pk):
	user_id = request.user.id
	user = User.objects.filter(pk=user_id).first()
	cars = Car.objects.filter(pk=pk).first()
	wishlist = cars.users_wishlist.all()
	#cars = Car.objects.filter(users_wishlist=user)
	print(user)
	print(cars)
	print(wishlist)
	return render(request,"my-wishlist.html",{'wishlist':wishlist})

def car_calculator(request):
	Fuel_Type_Diesel = 0
	if request.method == 'POST':
		year = int(request.POST.get('Year'))
		Present_Price = float(request.POST.get('Present_Price'))
		Kms_Driven = int(request.POST.get('Kms_Driven'))
		Kms_Driven2 = np.log(Kms_Driven)
		Owner = int(request.POST.get('Owner'))
		Fuel_Type_Petrol = request.POST.get('Fuel_Type_Petrol')
		if Fuel_Type_Petrol == 'Petrol':
			Fuel_Type_Petrol = 1
			Fuel_Type_Diesel = 0

		else:
			Fuel_Type_Petrol = 0
			Fuel_Type_Diesel = 1
		
		Year = 2021-year

		Seller_Type_Individual = request.POST.get('Seller_Type_Individual')
		if Seller_Type_Individual == 'Individual':
			Seller_Type_Individual = 1
		else:
			Seller_Type_Individual = 0

		Transmission_Manual = request.POST.get('Transmission_Manual')
		if Transmission_Manual == 'Manual':
			Transmission_Manual = 1
		else:
			Transmission_Manual = 0

		prediction = model_car.predict([[Present_Price, Kms_Driven2, Owner, Year, Fuel_Type_Diesel, 
										Fuel_Type_Petrol, Seller_Type_Individual, Transmission_Manual]])
		
		output = round(prediction[0],2)

		if output <= 0:
			context = {'prediction_text': "Sorry you cannot sell this car"}
			return render(request, "car_calculator.html", context)

		else:
			context = {'prediction_text': "You can sell the car at {} lakhs".format(output)}
			return render(request, "car_calculator.html", context)

	else:
		return render(request, "car_calculator.html")


class Search(BaseView):
    def get(self,request):
        query=request.GET.get("query",None)
        if not query:
            return redirect("vehicle:cars")
        self.template_context["search_result"] = Car.objects.filter(
        name__icontains = query
        )
        self.template_context["search_query"] = query
        return render(request,"search-result.html",self.template_context)



def user_wishlist(request,pk):
	user = User.objects.filter(pk=pk).first()
	cars = user.car_set.all()
	return render(request,"my-wishlist.html",{'cars':cars})



