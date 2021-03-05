from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View

from .forms import PetForm

User = get_user_model()

# Create your views here.
class MainPageView(View):
    def get(self, request, *args, **kwargs):
        pass

class AddPetView(LoginRequiredMixin, View):
    form = PetForm
    template_name = "pet_food_diary/add_pet.html"
    def get(self, request, *args, **kwargs):
        pass
