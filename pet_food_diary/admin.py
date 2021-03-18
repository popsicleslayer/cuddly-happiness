from django.contrib import admin
from .models import PetModel, PetFoodModel, PetFoodAmountModel, MealModel
admin.site.register(PetModel)
admin.site.register(PetFoodModel)
admin.site.register(PetFoodAmountModel)
admin.site.register(MealModel)
# Register your models here.
