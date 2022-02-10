from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class UserRegisterForm(forms.Form):
    username = forms.CharField(label='Username', required=True)
    email = forms.EmailField()
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(label="Repeat password", widget=forms.PasswordInput, required=True)
    is_vet = forms.BooleanField(label='I am a veterinarian', required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'is_vet']


    def clean_password2(self):
        """ Checks if provided passwords match"""
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            raise ValidationError("Passwords don't match")
        else:
            return password2

    def clean_username(self):
        """Checks if username is already in use"""
        username =self.cleaned_data.get('username')
        if User.objects.filter(username=username):
            raise ValidationError('This username is already in use')
        else:
            return username


class UserLoginForm(forms.Form):
    username = forms.CharField(label='Login', required=True)
    password = forms.CharField(widget=forms.PasswordInput())


