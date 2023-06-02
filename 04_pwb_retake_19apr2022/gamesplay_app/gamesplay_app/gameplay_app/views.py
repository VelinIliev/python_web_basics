from django.http import HttpResponse
from django.shortcuts import render, redirect

from gamesplay_app.gameplay_app.forms import CreateGameForm, DeleteGameForm
from gamesplay_app.gameplay_app.models import Game
from gamesplay_app.utils import get_user


def game_create(request):
    if request.method == "GET":
        form = CreateGameForm()
    else:
        form = CreateGameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'logged': get_user(),
        'form': form,
    }
    return render(request, 'game/create-game.html', context)


def game_details(request, pk):
    game = Game.objects.filter(pk=pk).get()

    context = {
        'logged': get_user(),
        'game': game,
    }

    return render(request, 'game/details-game.html', context)


def game_edit(request, pk):
    game = Game.objects.filter(pk=pk).get()
    if request.method == "GET":
        form = CreateGameForm(instance=game)
    else:
        form = CreateGameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {
        'logged': get_user(),
        'form': form,
        'game': game
    }
    return render(request, 'game/edit-game.html', context)


def game_delete(request, pk):
    game = Game.objects.filter(pk=pk).get()

    if request.method == "GET":
        form = DeleteGameForm(instance=game)
    else:
        form = DeleteGameForm(request.POST, instance=game)
        game.delete()
        return redirect('dashboard')

    context = {
        'logged': get_user(),
        'form': form,
        'game': game
    }
    return render(request, 'game/delete-game.html', context)
