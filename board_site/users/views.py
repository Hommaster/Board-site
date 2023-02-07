from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from users.forms import RegisterUserForm
from board.models import *
from board.service import *


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = "board/register_user.html"
    success_url = reverse_lazy("main")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class LoginUser(LoginView):
    authentication_form = AuthenticationForm
    template_name = "board/login_user.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def logout_user(request):
    logout(request)
    return redirect("main")
