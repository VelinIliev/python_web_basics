from django.http import HttpResponse
from django.shortcuts import render, redirect

from my_plant_app.my_plant.forms import CreateProfileForm, CreatePlantForm, EditPlantForm, DeletePlantForm, \
    EditProfileForm, DeleteProfileForm
from my_plant_app.my_plant.models import Profile, Plant


def get_user():
    try:
        user = Profile.objects.get()
        return True
    except Profile.DoesNotExist:
        return False


def index(request):
    context = {
        'logged': get_user(),
    }

    return render(request, 'home-page.html', context)


def profile_create(request):
    if request.method == "GET":
        form = CreateProfileForm()
    else:
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue view')

    context = {
        'form': form,
        'logged': get_user(),
    }
    return render(request, 'create-profile.html', context)


def profile_details(request):
    count_stars = Plant.objects.count()
    if count_stars == 0:
        count_stars = 0
    else:
        count_stars = range(count_stars if count_stars <= 3 else 3)

    user = Profile.objects.get()
    context = {
        'user': user,
        'logged': get_user(),
        'count_stars': count_stars
    }
    return render(request, 'profile-details.html', context)


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
        'user': user,
        'logged': get_user(),
        'form': form
    }
    return render(request, 'edit-profile.html', context)


def profile_delete(request):
    user = Profile.objects.get()
    if request.method == "GET":
        form = DeleteProfileForm(instance=user)
    else:
        form = DeleteProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'logged': get_user(),
        'form': form,
    }
    return render(request, 'delete-profile.html', context)


def catalogue_view(request):
    context = {
        'plants': Plant.objects.all(),
        'logged': get_user(),
    }
    return render(request, 'catalogue.html', context)


def plant_create(request):
    if request.method == "GET":
        form = CreatePlantForm()
    else:
        form = CreatePlantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue view')

    context = {
        'logged': get_user(),
        'form': form,
    }
    return render(request, 'create-plant.html', context)


def plant_details(request, pk):
    plant = Plant.objects.filter(pk=pk).get()
    context = {
        'logged': get_user(),
        'plant': plant,
    }
    return render(request, 'plant-details.html', context)


def plant_edit(request, pk):
    plant = Plant.objects.filter(pk=pk).get()

    if request.method == "GET":
        form = EditPlantForm(instance=plant)
    else:
        form = EditPlantForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('catalogue view')

    context = {
        'logged': get_user(),
        'plant': plant,
        'form': form,
    }
    return render(request, 'edit-plant.html', context)


def plant_delete(request, pk):
    plant = Plant.objects.filter(pk=pk).get()

    if request.method == "GET":
        form = DeletePlantForm(instance=plant)
    else:
        form = DeletePlantForm(request.POST, instance=plant)
        form.save()
        return redirect('catalogue view')

    context = {
        'logged': get_user(),
        'plant': plant,
        'form': form,
    }
    return render(request, 'delete-plant.html', context)
