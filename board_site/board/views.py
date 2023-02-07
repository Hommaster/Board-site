from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView

from board.forms import BbForm, RegisterUserForm
from board.models import *
from board.service import *


class MainListView(ListView):
    model = Bb
    context_object_name = "bbs"
    template_name = "board/main.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = get_all_objects(Rubric)
        return context


class BbCreateView(CreateView):
    template_name = "board/create.html"
    form_class = BbForm
    success_url = reverse_lazy("main")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = get_all_objects(Rubric)
        return context


def content(request):
    return render(request, "board/bb_deteil.html")


class ContentDetailView(DetailView):
    model = Bb
    template_name = 'board/bb_deteil.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = get_all_objects(Rubric)
        return context


class ByRubricListView(ListView):
    model = Bb
    context_object_name = 'bbs'
    template_name = "board/main.html"

    def get_queryset(self):
        return Bb.objects.filter(rubric=self.kwargs['rubric_id'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = get_all_objects(Rubric)
        context['current_rubric'] = Rubric.objects.get(pk=self.kwargs['rubric_id'])
        return context


class BbEditView(UpdateView):
    model = Bb
    form_class = BbForm
    template_name = 'board/edit_form.html'
    success_url = reverse_lazy("main")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = get_all_objects(Rubric)
        return context


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

