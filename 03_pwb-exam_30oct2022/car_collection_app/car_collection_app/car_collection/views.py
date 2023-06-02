from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import render, redirect

from car_collection_app.car_collection.forms import CreateProfileForm, CreateCarForm, EditCarForm, DeleteCarForm, \
    EditProfileForm, DeleteProfileForm
from car_collection_app.car_collection.models import Profile, Car


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
    return render(request, 'common/index.html', context)


def profile_create(request):
    if request.method == "GET":
        form = CreateProfileForm()
    else:
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'logged': get_user(),
        'form': form,
    }
    return render(request, 'profile/profile-create.html', context)


def profile_details(request):
    total_price = Car.objects.all().aggregate(Sum('price'))
    user = Profile.objects.get()
    full_name = None
    if user.first_name and user.last_name:
        full_name = f'{user.first_name} {user.last_name}'
    elif user.first_name:
        full_name = f'{user.first_name}'
    elif user.last_name:
        full_name = f'{user.last_name}'

    context = {
        'logged': get_user(),
        'user': user,
        'full_name': full_name,
        'total_price': total_price['price__sum'],
    }
    return render(request, 'profile/profile-details.html', context)


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
        'user': user,
        'form': form,
    }
    return render(request, 'profile/profile-edit.html', context)


def profile_delete(request):
    user = Profile.objects.get()

    if request.method == "GET":
        form = DeleteProfileForm(instance=user)
    else:
        form = DeleteProfileForm(request.POST, instance=user)
        form.save()
        return redirect('index')

    context = {
        'logged': get_user(),
        'form': form,
    }

    return render(request, 'profile/profile-delete.html', context)


def catalogue(request):
    cars = Car.objects.all()
    cars_count = Car.objects.count()
    context = {
        'logged': get_user(),
        'cars': cars,
        'cars_count': cars_count,
    }
    return render(request, 'common/catalogue.html', context)


def car_create(request):
    if request.method == "GET":
        form = CreateCarForm()
    else:
        form = CreateCarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'logged': get_user(),
        'form': form
    }
    return render(request, 'car/car-create.html', context)


def car_details(request, pk):
    car = Car.objects.filter(pk=pk).get()
    context = {
        'logged': get_user(),
        'car': car
    }
    return render(request, 'car/car-details.html', context)


def car_edit(request, pk):
    car = Car.objects.filter(pk=pk).get()

    if request.method == "GET":
        form = EditCarForm(instance=car)
    else:
        form = EditCarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'logged': get_user(),
        'car': car,
        'form': form,
    }
    return render(request, 'car/car-edit.html', context)


def car_delete(request, pk):
    car = Car.objects.filter(pk=pk).get()

    if request.method == "GET":
        form = DeleteCarForm(instance=car)
    else:
        form = DeleteCarForm(request.POST, instance=car)
        form.save()
        return redirect('catalogue')

    context = {
        'logged': get_user(),
        'car': car,
        'form': form,
    }
    return render(request, 'car/car-delete.html', context)
