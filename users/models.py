from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default="default.jpg",upload_to="static/images")
	address = models.CharField(max_length=30)
	contact = models.IntegerField(unique=True)


	def __str__(self):
		return f"{self.user.username} Profile"
