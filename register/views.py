
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.shortcuts import render
from django.views import View

from .forms import UserRegisterForm, UserLoginForm

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
            clean_dt = form.cleaned_data
            User.objects.create_user(
                username=clean_dt['username'],
                email=clean_dt['email'],
                password=clean_dt['password1'],
                is_vet=clean_dt['is_vet']
            )
            message='User created!'
        context = {
            'message': message,
            'form': form,
        }
        return render(request, 'register.html', context)


class LoginView(View):
    template_name = 'pet_food_diary/login.html'
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
        return render(request, 'pet_food_diary/logout.html', context)