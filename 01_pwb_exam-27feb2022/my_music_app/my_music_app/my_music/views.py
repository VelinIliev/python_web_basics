from django.http import HttpResponse
from django.shortcuts import render, redirect

from my_music_app.my_music.forms import CreateAlbumForm, EditAlbumForm, DeleteAlbumForm, CreateAccountForm, \
    DeleteAccountForm
from my_music_app.my_music.models import Album, Profile


def get_profile():
    try:
        profile = Profile.objects.get()
        return profile
    except Profile.DoesNotExist:
        return None


def index(request):
    profile = get_profile()

    if profile is None:
        return profile_add(request)

    context = {
        'albums': Album.objects.all(),
    }

    return render(request, 'common/home-with-profile.html', context=context)


def profile_add(request):
    if request.method == 'GET':
        form = CreateAccountForm()
    else:
        form = CreateAccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'not_logged': True,
    }
    return render(request, 'common/home-no-profile.html', context)


def album_add(request):
    if request.method == 'GET':
        form = CreateAlbumForm()
    else:
        form = CreateAlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")

    context = {
        'form': form,
    }
    return render(request, 'album/add-album.html', context)


def album_details(request, pk):
    album = Album.objects.filter(id=pk).get()
    context = {
        'album': album
    }
    return render(request, 'album/album-details.html', context=context)


def album_edit(request, pk):
    album = Album.objects.filter(pk=pk).get()

    if request.method == "GET":
        form = EditAlbumForm(instance=album)
    else:
        form = EditAlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'form': form,
        'album': album,
    }
    return render(request, 'album/edit-album.html', context=context)


def album_delete(request, pk):
    album = Album.objects.filter(pk=pk).get()

    if request.method == "GET":
        form = DeleteAlbumForm(instance=album)
    else:
        form = DeleteAlbumForm(request.POST, instance=album)
        if form.is_valid:
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'album': album,
    }

    return render(request, 'album/delete-album.html', context=context)


def profile_details(request):
    user = Profile.objects.get()
    number_of_albums = Album.objects.count()
    context = {
        'user': user,
        'number_of_albums': number_of_albums
    }
    return render(request, 'account/profile-details.html', context)


def profile_delete(request):
    profile = get_profile()

    if request.method == "GET":
        form = DeleteAccountForm(instance=profile)
    else:
        form = DeleteAccountForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'form': form,
    }

    return render(request, 'account/profile-delete.html', context)
