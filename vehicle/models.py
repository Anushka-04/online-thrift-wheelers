from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse


class Car(models.Model):
	name = models.CharField(max_length=50)
	km_driven = models.IntegerField(null=True, blank=True)
	fuel_type = models.CharField(max_length=50)
	transmission_type = models.CharField(max_length=50)
	seller_type = models.CharField(max_length=50)
	year_bought = models.IntegerField(null=True, blank=True)
	price = models.FloatField(null=True, blank=True)
	image = models.ImageField(upload_to ='uploads/Cars/')
	owner = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('vehicle:car-detail',kwargs={"pk":self.pk})


class Bike(models.Model):
	name = models.CharField(max_length=50)
	km_driven = models.IntegerField(null=True, blank=True)
	seller_type = models.CharField(max_length=50)
	year_bought = models.IntegerField(null=True, blank=True)
	price = models.FloatField(null=True, blank=True)
	image = models.ImageField(upload_to ='uploads/Bikes/')
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	
	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('vehicle:bike-detail',kwargs={"pk":self.pk})

		