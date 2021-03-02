from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class PetModel(models.Model):
    name = models.CharField(max_length=64)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    vet = models.ForeignKey(User, default='Null', on_delete=models.SET_DEFAULT)
    date_of_birth = models.DateField
    comments = models.TextField


class PetFoodModel(models.Model):
    brand = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    proteins = models.IntegerField
    fats = models.IntegerField
    fiber = models.IntegerField
    ash = models.IntegerField
    other = models.TextField


class MealModel(models.Model):
    pet_food = models.ForeignKey(PetFoodModel)
    pet = models.ForeignKey(PetModel, on_delete=models.CASCADE)
    amount = models.IntegerField
    date = models.DateTimeField


class MealPlanModel(models.Model):
    # TYPE_OF_MEAL_CHOICES=(
    #     (0, 'breakfast'),
    #     (1, 'lunch'),
    #     (2, 'dinner')
    # )
    pet_food = models.ForeignKey
    pet = models.OneToOneField(on_delete=models.CASCADE)
    amount = models.IntegerField
    # type_of_meal = models.IntegerField(choices=TYPE_OF_MEAL_CHOICES)
