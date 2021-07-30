from django.urls import path
from . import views
from .views import (CarCreateView,CarListView,CarDetailView, BikeDetailView,UserCarListView,CarAdUpdateView,
  CarAdDeleteView,wishlist,add_to_wishlist,car_calculator, Search,user_wishlist)

app_name = "vehicle"
urlpatterns = [
    path("cars/",CarListView.as_view(), name="cars"),
     path('cars/new/',CarCreateView.as_view(),name="cars-ad"),
    path('cars/<int:pk>/',CarDetailView.as_view(),name="car-detail"),
    path('bike/<int:pk>/',BikeDetailView.as_view(),name="bike-detail"),
   	path('user/<str:username>',UserCarListView.as_view(),name="user-ads"),
   	path('cars/<int:pk>/update/',CarAdUpdateView.as_view(),name="car-update"),
   	path('cars/<int:pk>/delete/',CarAdDeleteView.as_view(),name="car-delete"),
   	 path("wishlist/<int:pk>/",views.wishlist, name="wishlist"),
    path("add-to-wishlist/<int:pk>/", add_to_wishlist, name="add-to-wishlist"),
    path("carpricepredict/",car_calculator,name="carpricepredict"),
    path("search/", Search.as_view(), name="search"),
    path("user_wishlist/<int:pk>",user_wishlist,name="user_wishlist")
    ]