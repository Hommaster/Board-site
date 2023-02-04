from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from board.forms import BbForm
from board.models import *
from board.service import *


def index(request):
    bbs = get_all_objects(Bb)
    rubrics = get_all_objects(Rubric)
    context = {
        'bbs': bbs,
        'rubrics': rubrics,
    }
    return render(request, 'board/main.html', context=context)


def by_rubric(request, rubric_id):
    bbs = Bb.objects.filter(rubric=rubric_id)
    rubrics = get_all_objects(Rubric)
    current_rubric = Rubric.objects.filter(pk=rubric_id)
    context = {
        'bbs': bbs,
        "rubrics": rubrics,
        "current_rubric": current_rubric,
    }
    return render(request, 'board/by_rubric.html', context=context)


class BbCreateView(CreateView):
    template_name = "board/create.html"
    form_class = BbForm
    success_url = reverse_lazy("main")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = get_all_objects(Rubric)
        return context
