from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm
from django.contrib.auth.mixins import AccessMixin
from django.contrib.auth.models import User
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from users.forms import *
from board.service import *
from board.models import *


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = "users/register_user.html"
    success_url = reverse_lazy("main")

    def form_valid(self, form):
        form.save()
        cart_create()
        return super().form_valid(form)
    

class LoginUser(AccessMixin, LoginView):
    authentication_form = AuthenticationForm
    template_name = "users/login_user.html"
    redirect_authenticated_user = reverse_lazy("main")

    def form_valid(self, form):
        return super().form_valid(form)


def logout_user(request):
    logout(request)
    return redirect("main")


class UserProfile(UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = "users/profile.html"
    success_url = reverse_lazy("main")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class UserPasswordChange(PasswordChangeView):
    template_name = "users/pas_ch.html"
    form_class = PasswordChangeForm
    success_url = reverse_lazy("login")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class AUserPasswordChange(UserPasswordChange):
    template_name = "users/pas_ch.html"
    success_url = reverse_lazy("password_done")
    form_class = PasswordChangeForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


def password_change_done(request):
    return render(request, "password_change_done.html")
