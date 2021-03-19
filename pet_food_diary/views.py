from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from .forms import PetForm
from .models import PetModel, PetFoodModel, PetFoodAmountModel, MealModel

User = get_user_model()
# A URL to redirect to in case of a not logged in access to a view
loginURL = 'login'


# Create your views here.
class MainPageView(View):
    pass


class PetListView(LoginRequiredMixin, View):
    """Lists all user's pets"""
    login_url = loginURL
    template = "pet_food_diary/petmodel_list.html"

    def get(self, request, *args, **kwargs):
        pet_list = PetModel.objects.filter(owner=kwargs['user_id'])
        context = {
            'pets': pet_list,
        }
        return render(request, self.template, context)


class PetCreateView(LoginRequiredMixin, CreateView):
    '''Creates a pet entry'''
    login_url = loginURL
    model = PetModel
    fields = ('name', 'vet', 'date_of_birth', 'comments')

    #Sets owner to current user. Hidden field
    def form_valid(self, form):
        user = self.request.user
        form.instance.owner = user
        return super(PetCreateView, self).form_valid(form)

    #Redirects to the pet list for the current user
    def get_success_url(self):
        return f"/pet/list/{self.request.user.id}"


class PetUpdateView(LoginRequiredMixin, UpdateView):
    '''Updates a pet entry'''
    login_url = loginURL
    model = PetModel
    fields = ('name', 'vet', 'date_of_birth', 'comments')

    # Sets owner to current user. Hidden field
    def form_valid(self, form):
        user = self.request.user
        form.instance.owner = user
        return super(PetCreateView, self).form_valid(form)

    # Redirects to the pet list for the current user
    def get_success_url(self):
        return f"/pet/list/{self.request.user.id}"


class PetDeleteView(LoginRequiredMixin, DeleteView):
    '''Deletes a pet entry'''
    login_url = loginURL
    model = PetModel

    def get_success_url(self, *args, **kwargs):
        return f"/pet/list/{self.kwargs['user_id']}"


@login_required(login_url=loginURL)
def petFoodDetail(request, pk):
    '''A detailed view of a pet food entry'''
    petFood = PetFoodModel.objects.get(pk=pk)
    context = {
        'petFood': petFood
    }
    return render(request, 'petfood_detail.html', context)


class PetFoodListView(LoginRequiredMixin, View):
    '''Returns a list of all pet food'''
    login_url = loginURL

    def get(self, request, *args, **kwargs):
        petFood = PetFoodModel.objects.all()
        context = {
            'petFood': petFood
        }
        return render(request, 'petfoodmodel_list.html', context)


class PetFoodCreateView(LoginRequiredMixin, CreateView):
    '''Creates a pet food entry. Redirects using get_absolute_url method'''
    login_url = loginURL
    model = PetFoodModel
    fields = '__all__'


class PetFoodUpdateView(LoginRequiredMixin, UpdateView):
    '''Updates a pet food entry'''
    login_url = loginURL
    model = PetFoodModel
    fields = '__all__'


class PetFoodDeleteView(LoginRequiredMixin, DeleteView):
    '''Deletes a pet food entry. Redirects to the list of all pet food'''
    login_url = loginURL
    model = PetFoodModel
    success_url = '/pet_food'


@login_required(login_url=loginURL)
def mealDetail(request, pk):
    '''Detailed view of a meal'''
    meal = MealModel.objects.get(pk=pk)
    context = {
        'meal': meal
    }
    return render(request, 'mealmodel_detail.html', context)


class MealList(LoginRequiredMixin, View):
    '''Returns a list of all meals specific for the chosen pet. If there are no pets found returns a 404'''
    login_url = loginURL

    def get(self, request, *args, **kwargs):
        owner = request.user
        pet = get_object_or_404(PetModel, owner=owner.id)
        meals = MealModel.objects.filter(pet=pet)
        context = {
            'pet': pet,
            'meals': meals
        }
        return render(request, 'mealmodel_list.html', context)


# class MealCreateView(LoginRequiredMixin, View):
#     """Allows adding a new meal. Redirects to adding amount and type of food used"""
#     login_url = loginURL
#     template = "pet_food_diary/add_meal.html"
#
#     def get(self, request, *args, **kwargs):
#         form = MealForm(user=self.request.user)
#         context = {
#             'form': form,
#         }
#         return render(request, self.template, context)
#
#     def post(self, request, *args, **kwargs):
#         form = MealForm(request.POST)
#         if form.is_valid():
#             meal = MealModel()
#             meal.pet = PetModel.objects.filter(owner=self.request.user.id)
#             meal.date = form.cleaned_data.get('date')
#             meal.save()
#         return redirect('add_amount')


# class PetFoodAmountCreateView(LoginRequiredMixin, View):
#     """Adds type and amount of pet food used"""
#     login_url = loginURL
#     form = PetFoodAmountForm
#     template = "pet_food_diary/add_amount.html"
#
#     def get(self, request, *args, **kwargs):
#         context = {
#             'form': self.form,
#         }
#         return render(request, self.template, context)
#
#     def post(self, request, *args, **kwargs):
#         form = self.form(request.POST)
#         if form.is_valid():
#             amount = PetFoodAmountModel()
#             amount.meal = form.cleaned_data.get('meal')
#             amount.pet_food = form.cleaned_data.get('pet_food')
#             amount.grams = form.cleaned_data.get('grams')
#             amount.save()
#         return redirect('meal_list')


class MealCreateView(LoginRequiredMixin, CreateView):
    """Allows adding a new meal. Redirects to adding amount and type of food used"""
    login_url = loginURL
    model = MealModel
    fields = ('pet', 'date')
    success_url = 'details'

    # Limits pet choices to the ones owned by the currently logged in user
    def get_form(self, *args, **kwargs):
        form = super(MealCreateView, self).get_form(*args, **kwargs)
        form.fields['pet'].queryset = PetModel.objects.filter(owner=self.request.user)
        return form


class PetFoodAmountCreateView(LoginRequiredMixin, CreateView):
    """Adds type and amount of pet food used to a chosen meal"""
    login_url = loginURL
    model = PetFoodAmountModel
    fields = '__all__'
    success_url = '/meal'

    #Limits meal choices to the ones created by currently logged in user
    def get_form(self, *args, **kwargs):
        form = super(PetFoodAmountCreateView, self).get_form(*args, **kwargs)
        form.fields['meal'].queryset = MealModel.objects.filter(pet__owner=self.request.user)
        return form

class MealUpdateView(LoginRequiredMixin, UpdateView):
    '''Updates meal db entries'''
    login_url = loginURL
    model = MealModel
    fields = ('pet', 'date')

    # Limits pet choices to the ones owned by the currently logged in user
    def get_form(self, *args, **kwargs):
        form = super(MealCreateView, self).get_form(*args, **kwargs)
        form.fields['pet'].queryset = PetModel.objects.filter(owner=self.request.user)
        return form


class PetFoodAmountUpdateView(LoginRequiredMixin, UpdateView):
    '''Updates amount and pet food used entries in a chosen meal'''
    login_url = loginURL
    model = PetFoodAmountModel
    fields = '__all__'

    # Limits meal choices to the ones created by currently logged in user
    def get_form(self, *args, **kwargs):
        form = super(PetFoodAmountCreateView, self).get_form(*args, **kwargs)
        form.fields['meal'].queryset = MealModel.objects.filter(pet__owner=self.request.user)
        return form


class MealDeleteView(LoginRequiredMixin, DeleteView):
    '''Deletes a meal. Redirects to the list of all meals'''
    login_url = loginURL
    model = PetFoodAmountModel
    success_url = '/meal'


class PetFoodAmountDeleteView(LoginRequiredMixin, DeleteView):
    '''Deletes a amount and pet food used entry for a meal. Redirects to the list of all meals'''
    login_url = loginURL
    model = PetFoodAmountModel
    success_url = '/meal'
