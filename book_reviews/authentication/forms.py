from django import forms
from django.contrib.auth import get_user_model

from django.contrib.auth.forms import UserCreationForm

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email"]

    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    email = forms.EmailField(max_length=255)
