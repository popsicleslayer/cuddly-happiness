from django.contrib import admin
from .models import PetModel, PetFoodModel, PetFoodAmountModel
admin.site.register(PetModel)
admin.site.register(PetFoodModel)
admin.site.register(PetFoodAmountModel)

# Register your models here.
