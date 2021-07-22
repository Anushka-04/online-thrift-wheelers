from django.db import models

# Create your models here.
class Car(models.Model):
	name = models.CharField(max_length=50)
	km_driven = models.IntegerField(null=True, blank=True)
	fuel_type = models.CharField(max_length=50)
	transmission_type = models.CharField(max_length=50)
	seller_type = models.CharField(max_length=50)
	year_bought = models.IntegerField(null=True, blank=True)
	price = models.FloatField(null=True, blank=True)
	image = models.ImageField(upload_to ='uploads/Cars/')

	owner = models.CharField(max_length=50)


	def __str__(self):
		return self.name


class Bike(models.Model):
	name = models.CharField(max_length=50)
	km_driven = models.IntegerField(null=True, blank=True)
	seller_type = models.CharField(max_length=50)
	year_bought = models.IntegerField(null=True, blank=True)
	price = models.FloatField(null=True, blank=True)
	image = models.ImageField(upload_to ='uploads/Bikes/')

	owner = models.CharField(max_length=50)


	def __str__(self):
		return self.name

		