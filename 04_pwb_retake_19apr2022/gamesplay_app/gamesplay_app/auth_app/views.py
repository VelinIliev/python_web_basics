from django.http import HttpResponse
from django.shortcuts import render, redirect

from gamesplay_app.auth_app.forms import CreateProfileForm, EditProfileForm
from gamesplay_app.auth_app.models import Profile
from gamesplay_app.gameplay_app.models import Game
from gamesplay_app.utils import get_user


def profile_create(request):
    if request.method == "GET":
        form = CreateProfileForm()
    else:
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'logged': get_user(),
        'form': form,
    }
    return render(request, 'profile/create-profile.html', context)


def profile_details(request):
    user = Profile.objects.get()

    count_games = Game.objects.count()

    full_name = None
    if user.first_name and user.last_name:
        full_name = f'{user.first_name} {user.last_name}'
    elif user.first_name:
        full_name = f'{user.first_name}'
    elif user.last_name:
        full_name = f'{user.last_name}'

    if count_games > 0:
        games = Game.objects.all()
        count_rating = sum([x.rating for x in games]) / count_games
    else:
        count_rating = 0

    context = {
        'logged': get_user(),
        'user': user,
        'full_name': full_name,
        'count_games': count_games,
        'count_rating': count_rating,
    }
    return render(request, 'profile/details-profile.html', context)


def profile_edit(request):
    user = Profile.objects.get()
    if request.method == "GET":
        form = EditProfileForm(instance=user)
    else:
        form = EditProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile details')

    context = {
        'logged': get_user(),
        'form': form,
    }
    return render(request, 'profile/edit-profile.html', context)


def profile_delete(request):
    if request.method == "POST":
        Profile.objects.all().delete()
        Game.objects.all().delete()
        return redirect('index')

    context = {
        'logged': get_user(),
    }
    return render(request, 'profile/delete-profile.html', context)
