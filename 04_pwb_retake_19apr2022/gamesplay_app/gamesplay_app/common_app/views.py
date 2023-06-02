from django.http import HttpResponse
from django.shortcuts import render

from gamesplay_app.gameplay_app.models import Game
from gamesplay_app.utils import get_user


def index(request):
    context = {
        'logged': get_user()
    }
    return render(request, 'common/home-page.html', context)


def dashboard(request):
    games = Game.objects.all()
    context = {
        'logged': get_user(),
        'games': games,
    }
    return render(request, 'common/dashboard.html', context)
