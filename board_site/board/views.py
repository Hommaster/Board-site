from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView
from board.forms import BbForm
from board.models import *
from board.service import *
from board.utils import *


class MainListView(ListView):
    paginate_by = 6
    model = Bb
    context_object_name = "bbs"
    template_name = "board/main.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = get_all_objects(Rubric)
        return context


class Search(ListView):
    template_name= "board/main.html"
    paginate_by = 6
    context_object_name = "bbs"
    
    # title__icontains -> нечувствительность к регистру
    # serching -> имя поля из html страницы, точнее значение, которое ввел пользователь в форму )
    def get_queryset(self):
        return Bb.objects.filter(title__icontains=self.request.GET.get("serching"))
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["serching"] = self.request.GET.get("serching")
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

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

        
        
class BbCreateView(CreateView):
    template_name = "board/create.html"
    form_class = BbForm
    success_url = reverse_lazy("main")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = get_all_objects(Rubric)
        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    # def post(self, request, *args, **kwargs):
    #     object_post = request.POST
    #     print(object_post)
    
#   ПОЛНОСТЬЮ ПЕРЕПИСАТЬ СОЗДАНИЕ, ВЫНЕСТИ ВСЕ НА СТРАНИЦУ И ПЕРЕПИСАТЬ СОЗДАНИЕ СТРАНИЦЫ



class ContentDetailView(DetailView):
    model = Bb
    template_name = 'board/bb_deteil.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = get_all_objects(Rubric)
        return context


class ByRubricListView(ListView):
    model = Bb
    paginate_by = 6
    context_object_name = 'bbs'
    template_name = "board/main.html"

    def get_queryset(self):
        return Bb.objects.filter(rubric=self.kwargs['rubric_id'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = get_all_objects(Rubric)

        try:
            current_rubric = Rubric.objects.get(pk=self.kwargs['rubric_id'])
        except Bb.DoesNotExist:
            raise Http404("Рубрики не чуществует")

        context['current_rubric'] = current_rubric
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

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)








































