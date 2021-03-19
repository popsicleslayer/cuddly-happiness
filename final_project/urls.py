"""final_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

import pet_food_diary.views as pet
import register.views as register_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', pet.MainPageView.as_view(), name='main'),
    path('create_user/', register_views.RegisterUserView.as_view(), name='register_user'),
    path('login/', register_views.LoginView.as_view(), name='login'),
    path('logout/', register_views.LogoutView.as_view(), name='logout'),
    path('pet/list/<int:user_id>/', pet.PetListView.as_view(), name='pet_list'),
    path('pet/add/', pet.PetCreateView.as_view(), name='add_pet'),
    path('pet/edit/<int:pk>/', pet.PetUpdateView.as_view(), name='edit_pet'),
    path('pet/delete/<int:pk>/', pet.PetDeleteView.as_view(), name='delete_pet'),
    path('pet_food/', pet.PetFoodListView.as_view(), name='pet_food_list'),
    path('pet_food/<int:pk>/', pet.petFoodDetail, name='pet_food'),
    path('pet_food/add/', pet.PetFoodCreateView.as_view(), name='add_pet_food'),
    path('pet_food/update/<int:pk>/', pet.PetFoodUpdateView.as_view(), name='update_pet_food'),
    path('pet_food/delete/<int:pk>/', pet.PetFoodDeleteView.as_view(), name='delete_pet_food'),
    path('meal/', pet.MealList.as_view(), name='meal_list'),
    path('meal/detail/<int:pk>/', pet.mealDetail, name='meal_detail'),
    path('meal/add/', pet.MealCreateView.as_view(), name='add_meal'),
    path('meal/add/details/', pet.PetFoodAmountCreateView.as_view(), name='add_amount'),
    path('meal/update/<int:pk>/', pet.MealUpdateView.as_view(), name='update_meal'),
    path('meal/detail/update/<int:pk>/', pet.PetFoodAmountUpdateView.as_view(), name='update_amount'),
    path('meal/delete/<int:pk>/', pet.MealDeleteView.as_view(), name='delete_meal'),
    path('meal/detail/delete/<int:pk>/', pet.PetFoodAmountDeleteView.as_view(), name='delete_amount'),


]
