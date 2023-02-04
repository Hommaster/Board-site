from django.shortcuts import render
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
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.filter(pk=rubric_id)
    context = {
        'bbs': bbs,
        "rubrics": rubrics,
        "current_rubric": current_rubric,
    }
    return render(request, 'board/by_rubric.html', context=context)


