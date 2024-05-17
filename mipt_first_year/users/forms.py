from django import forms
from django.apps import apps
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.TextInput()
    last_name = forms.TextInput()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']


class UserUpdateForm(forms.ModelForm):
    first_name = forms.TextInput()
    last_name = forms.TextInput()

    class Meta:
        model = User
        fields = ['first_name', 'last_name']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = apps.get_model('users', 'Profile')
        fields = ['image']
