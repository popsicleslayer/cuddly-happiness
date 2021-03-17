from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Veterinarian(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_vet = models.BooleanField(default=False)

class PetModel(models.Model):
    name = models.CharField(max_length=64)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner_name')
    # vet = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE, related_name='vet_name')
    date_of_birth = models.DateField()
    comments = models.TextField(null=True)


class PetFoodModel(models.Model):
    brand = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    proteins = models.FloatField()
    fats = models.FloatField()
    fiber = models.FloatField()
    ash = models.FloatField()
    other = models.TextField()

    def get_absolute_url(self):
        return f'/pet_food/{self.id}/'


class MealModel(models.Model):
    pet_food_used = models.ManyToManyField(PetFoodModel, through='PetFoodAmountModel')
    pet = models.ForeignKey(PetModel, on_delete=models.CASCADE)
    date = models.DateTimeField()


class PetFoodAmountModel(models.Model):
    meal = models.ForeignKey(MealModel, on_delete=models.CASCADE)
    pet_food = models.ForeignKey(PetFoodModel, on_delete=models.CASCADE)
    grams = models.IntegerField()
