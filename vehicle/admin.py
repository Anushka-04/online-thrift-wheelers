from django.contrib import admin

from .models import Car, Bike, Wishlist
# Register your models here.

admin.site.register(Car)
admin.site.register(Bike)
admin.site.register(Wishlist)
