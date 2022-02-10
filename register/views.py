
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.shortcuts import render, redirect
from django.views import View

from .forms import UserRegisterForm, UserLoginForm

from pet_food_diary.models import Veterinarian

# Create your views here.
User = get_user_model()

class RegisterUserView(View):
    form_class = UserRegisterForm
    def get(self, request, *args, **kwargs):
        context = {
            'form' : self.form_class()
        }
        return render(request, 'register.html', context)

    def post(self, request, *args, **kwargs):
        form = UserRegisterForm(request.POST)
        message = None
        if form.is_valid():
            # form.save()
            clean_dt = form.cleaned_data
            user = User.objects.create_user(
                username=clean_dt['username'],
                email=clean_dt['email'],
                password=clean_dt['password1'],
            )
            Veterinarian.objects.create(user=user, is_vet=clean_dt['is_vet'])
            message = 'User created!'
        context = {
            'message': message,
            'form': form,
        }
        return render(request, 'register.html', context)


class LoginView(View):
    template_name = 'register/login.html'

    def get(self, request, *args, **kwargs):
        context = {
            'form': UserLoginForm(),
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = UserLoginForm(request.POST)
        message = None
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                # return redirect('pet_list', pk=user.id)
            else:
                message = 'Login credentials incorrect'
        else:
            message='Login credentials incorrect'
        context = {
            'form': form,
            'message': message,
        }
        return render(request, self.template_name, context)


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        message = "You're not logged in"
        if request.user.is_authenticated:
            logout(request)
            message = 'You just logged out!'
        context = {
            'message': message,
        }
        return render(request, 'register/logout.html', context)