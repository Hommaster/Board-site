from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError


class RegisterUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(max_length=50, help_text="Введите новое имя", label="Имя")
    email = forms.EmailField(help_text="Введите новый адрес электронной почты", label="Почта")

    class Meta:
        model = User
        fields = ("username", "email")

    def clean(self):
        super().clean()
        errors = {}

        if not self.cleaned_data["username"]:
            errors["username"] = ValidationError("Вы забыли ввести свое имя")

        if not self.cleaned_data["email"]:
            errors["email"] = ValidationError("Вы забыли ввесьти свой email")

        need = ["@", "gmail", ".com", "mail", ".ru"]

        for item in need:
            if item not in self.cleaned_data["email"]:
                ValidationError("Проверьте формат почты")


class UserPasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ("password1", "password2")

