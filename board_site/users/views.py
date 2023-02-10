from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import AccessMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from users.forms import *


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = "users/register_user.html"
    success_url = reverse_lazy("main")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class LoginUser(AccessMixin, LoginView):
    authentication_form = AuthenticationForm
    template_name = "users/login_user.html"
    redirect_authenticated_user = reverse_lazy("main")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def logout_user(request):
    logout(request)
    return redirect("main")


class UserProfile(UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = "users/profile.html"
    success_url = reverse_lazy("main")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class UserPasswordChange(PasswordChangeView):
    template_name = "users/pas_ch.html"
    form_class = PasswordChangeForm
    success_url = reverse_lazy("login")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


# st 303-309, write a password resset classes ^_^
class SendMassageAndPasswordResetView(PasswordResetView):
    pass


