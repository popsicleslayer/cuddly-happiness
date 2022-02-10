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
    path('pet/list/', pet.PetListView.as_view(), name='pet_list'),
    path('pet/add/', pet.PetCreateView.as_view(), name='add_pet'),
    path('pet/details/<int:pk>/', pet.PetDetailView.as_view(), name='pet_detail'),
    path('pet/edit/<int:pk>/', pet.PetUpdateView.as_view(), name='edit_pet'),
    path('pet/delete/<int:pk>/', pet.PetDeleteView.as_view(), name='delete_pet'),
    path('pet_food/', pet.PetFoodListView.as_view(), name='pet_food_list'),
    path('pet_food/details/<int:pk>/', pet.pet_food_detail, name='pet_food'),
    path('pet_food/add/', pet.PetFoodCreateView.as_view(), name='add_pet_food'),
    path('pet_food/update/<int:pk>/', pet.PetFoodUpdateView.as_view(), name='update_pet_food'),
    path('pet_food/delete/<int:pk>/', pet.PetFoodDeleteView.as_view(), name='delete_pet_food'),
    path('meal/', pet.MealList.as_view(), name='meal_list'),
    path('meal/detail/<int:pk>/', pet.meal_detail, name='meal_detail'),
    path('meal/add/', pet.MealCreateView.as_view(), name='add_meal'),
    path('meal/add/details/', pet.PetFoodAmountCreateView.as_view(), name='add_amount'),
    path('meal/update/<int:pk>/', pet.MealUpdateView.as_view(), name='update_meal'),
    path('meal/detail/update/<int:pk>/', pet.PetFoodAmountUpdateView.as_view(), name='update_amount'),
    path('meal/delete/<int:pk>/', pet.MealDeleteView.as_view(), name='delete_meal'),
    path('meal/detail/delete/<int:pk>/', pet.PetFoodAmountDeleteView.as_view(), name='delete_amount'),


]
