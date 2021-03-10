from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View

from .forms import PetForm
from .models import PetModel

User = get_user_model()

# Create your views here.
class MainPageView(View):
    def get(self, request, *args, **kwargs):
        pass

class AddPetView(LoginRequiredMixin, View):
    """Allows adding a new pet to the user"""
    form = PetForm
    template = "pet_food_diary/add_pet.html"
    def get(self, request, *args, **kwargs):
        context = {
            'form': self.form,
        }
        return render(request, self.template, context)
    def post(self, request, *args, **kwargs):
        current_user= request.user
        form = self.form(request.POST)
        if form.is_valid():
            pet = PetModel()
            pet.owner = current_user
            pet.name = form.cleaned_data.get('name')
            pet.vet = form.cleaned_data.get('vet')
            pet.date_of_birth = form.cleaned_data.get('date_of_birth')
            pet.comments = form.cleaned_data.get('Comments')
            pet.save()
            messages.success(request, 'Your pet has been successfully saved')
        return redirect('pet_list', user=current_user)


class PetListView(LoginRequiredMixin, View):
    """Lists all user's pets"""
    template = "pet_food_diary/pet_list.html"
    def get(self, request, *args, **kwargs):
        pet_list = PetModel.objects.filter(owner='user_id')
        username = User.objects.filter(pk='user_id').username
        context = {
            'pets': pet_list,
            'username': username,
        }
        return render(request, self.template, context)