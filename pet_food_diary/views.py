from django.contrib.auth import authenticate, get_user_model, login, logout
from django.shortcuts import render
from django.views import View

from .forms import UserLoginForm

User = get_user_model()

# Create your views here.
class MainPageView(View):
    def get(self, request, *args, **kwargs):
        pass


class LoginView(View):
    template_name = '/pet_food_diary/login.html'
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
        return render(request, '/pet_food_diary/logout.html', context)


class CreateUserView(View):
    def get(self, request, *args, **kwargs):
        pass


class AddPetView(View):
    def get(self, request, *args, **kwargs):
        pass