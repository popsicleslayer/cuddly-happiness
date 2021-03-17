from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from .forms import PetForm, MealForm
from .models import PetModel, PetFoodModel, PetFoodAmountModel, MealModel

User = get_user_model()
loginURL = 'login'


# Create your views here.
class MainPageView(View):
    def get(self, request, *args, **kwargs):
        pass


class AddPetView(LoginRequiredMixin, View):
    """Allows adding a new pet to the user"""
    login_url = loginURL
    form = PetForm
    template = "pet_food_diary/add_pet.html"

    def get(self, request, *args, **kwargs):
        context = {
            'form': self.form,
        }
        return render(request, self.template, context)

    def post(self, request, *args, **kwargs):
        current_user = request.user
        form = self.form(request.POST)
        if form.is_valid():
            pet = PetModel()
            pet.owner = current_user
            pet.name = form.cleaned_data.get('name')
            pet.date_of_birth = form.cleaned_data.get('date_of_birth')
            pet.comments = form.cleaned_data.get('Comments')
            pet.save()
            messages.success(request, 'Your pet has been successfully saved')
        return redirect('pet_list', user_id=current_user)


class PetListView(LoginRequiredMixin, View):
    """Lists all user's pets"""
    login_url = loginURL
    template = "pet_food_diary/pet_list.html"

    def get(self, request, *args, **kwargs):
        pet_list = PetModel.objects.filter(owner=kwargs['user_id'])
        # username = User.objects.filter(pk=kwargs['user_id'])
        context = {
            'pets': pet_list,
            # 'username': username,
        }
        return render(request, self.template, context)


class EditPetView(LoginRequiredMixin, View):
    """Allows user to edit an already existing pet entry. Prefills form with db data about pet."""
    login_url = loginURL
    form = PetForm
    template = "pet_food_diary/edit_pet.html"
    # pet = get_object_or_404(PetModel, pk='pet_id')

    def get(self, request, *args, **kwargs):
        form = self.form(request.POST, instance=self.pet)
        context = {
            'form': form
        }
        return render(request, self.template, context)

    def post(self, request, *args, **kwargs):
        current_user = request.user
        if self.form.is_valid():
            self.form.save()
            messages.success(request, 'Changes saved')
        return redirect('pet_list', user_id=current_user)


class PetDeleteView(LoginRequiredMixin, DeleteView):
    login_url = loginURL
    model = PetModel
    success_url = 'pet_list'

@login_required(login_url= loginURL)
def petFoodDetail(request, pk):
    petFood = PetFoodModel.objects.get(pk=pk)
    context = {
        'petFood': petFood
    }
    return render(request, 'petfood_detail.html', context)

class PetFoodListView(LoginRequiredMixin, View):
    login_url = loginURL

    def get(self, request, *args, **kwargs):
        petFood = PetFoodModel.objects.all()
        context = {
            'petFood': petFood
        }
        return render(request, 'petfoodmodel_list.html', context)


class PetFoodCreateView(LoginRequiredMixin, CreateView):
    login_url = loginURL
    model = PetFoodModel
    fields = '__all__'


class PetFoodUpdateView(LoginRequiredMixin, UpdateView):
    login_url = loginURL
    model = PetFoodModel
    fields = '__all__'


class PetFoodDeleteView(LoginRequiredMixin, DeleteView):
    login_url = loginURL
    model = PetFoodModel
    success_url = 'pet_food_list'


@login_required(login_url= loginURL)
def mealDetail(request, pk):
    meal = MealModel.objects.get(pk=pk)
    context = {
        'meal': meal
    }
    return render(request, 'mealmodel_detail.html', context)


class MealList(LoginRequiredMixin, View):
    login_url = loginURL
    def get(self, request, *args, **kwargs):
        owner = request.user
        pet = PetModel.objects.get(owner=owner.id)
        meals = MealModel.objects.filter(pet=pet)
        context = {
            'meals': meals
        }
        return render(request, 'mealmodel_list.html', context)


class MealCreateView(LoginRequiredMixin, View):
    """Allows adding a new pet to the user"""
    login_url = loginURL
    # form = MealForm(user=self.request.user)
    template = "pet_food_diary/add_meal.html"

    def get(self, request, *args, **kwargs):
        form = MealForm(user=self.request.user)
        context = {
            'form': form,
        }
        return render(request, self.template, context)

    def post(self, request, *args, **kwargs):
        current_user = request.user
        form = self.form(request.POST)
        if form.is_valid():
            pet = PetModel()
            pet.owner = current_user
            pet.name = form.cleaned_data.get('name')
            pet.date_of_birth = form.cleaned_data.get('date_of_birth')
            pet.comments = form.cleaned_data.get('Comments')
            pet.save()
            messages.success(request, 'Your pet has been successfully saved')
        return redirect('pet_list', user_id=current_user)