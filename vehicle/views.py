from django.shortcuts import render, get_object_or_404
from .models import Car, Bike
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

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
		return Car.objects.filter(owner=user)

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