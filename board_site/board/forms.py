from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import *


class BbForm(ModelForm):
    class Meta:
        model = Bb
        fields = ("title", "content", "price", "rubric", "photo")


class RegisterUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
