from django.shortcuts import render
from board.models import *
from board.service import *


def index(request):
    bbs = get_all_objects(Bb)
    context = {
        'bbs': bbs,
    }
    return render(request, 'board/main.html', context=context)


