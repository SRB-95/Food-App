from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
    # additional field
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'last_name', 'email','password1','password2']         #lastname addeds