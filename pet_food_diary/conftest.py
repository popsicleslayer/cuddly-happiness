import pytest
from django.contrib.auth.models import User
from django.test import Client
from django.urls import reverse

from pet_food_diary.models import PetModel, PetFoodModel, PetFoodAmountModel, MealModel, Veterinarian

@pytest.fixture()
def client():
    return Client()

@pytest.fixture()
def user():
    return User.objects.create_user(
        username='test_user',
        password='password',
        email='mail@test.test',
    )

@pytest.fixture()
def vet():
    vet_user = User.objects.create_user(
        username='user',
        password='password',
        email='mail2@test.test',
    )
    Veterinarian.objects.create(user=vet_user, is_vet=True)
    return vet_user

@pytest.fixture()
def pet(user, vet):
    return PetModel.objects.create(
        name='PetName',
        owner= user,
        vet=vet,
        date_of_birth='2020-03-03',
        comments='Pet breed',
    )

@pytest.fixture()
def petfood():
    return PetFoodModel.objects.create(
        brand='Brand',
        name='Name',
        proteins='12',
        fiber='1,2',
        ash='0,1',
        other='Other'
    )

@pytest.fixture()
def meal(petfood, pet):
    return MealModel.objects.create(
        pet_food_used=petfood,
        pet=pet,
        date='2013-03-16T17:41:28'
    )

@pytest.fixture()
def amount(meal, petfood):
    return PetFoodAmountModel.objects.create(
        meal=meal,
        pet_food=petfood,
        grams='123'
    )