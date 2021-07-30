from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse

SELLER_TYPE = (("Dealer", "Dealer"), ("Individual", "Individual"))
TRANSMISSION_TYPE = (("Automatic", "Automatic"), ("Manual", "Manual"))

class Car(models.Model):
	name = models.CharField(max_length=50)
	km_driven = models.IntegerField(null=True, blank=True)
	fuel_type = models.CharField(max_length=50)
	transmission_type = models.CharField(max_length=50, choices=TRANSMISSION_TYPE, default="Automatic")
	seller_type = models.CharField(max_length=50, choices=SELLER_TYPE, default="Individual")
	year_bought = models.IntegerField(null=True, blank=True)
	price = models.FloatField(null=True, blank=True)
	image = models.ImageField(upload_to ='uploads/Cars/')
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	users_wishlist = models.ManyToManyField(User,related_name="users_wishlist",blank=True)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('vehicle:car-detail',kwargs={"pk":self.pk})


	def get_add_to_cart(self):
		return reverse("vehicle:add-to-wishlist", kwargs={"pk": self.pk})


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

class Wishlist(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	wished_car = models.ForeignKey(Car,on_delete=models.CASCADE)
	added_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
	    return self.wished_car.name

		