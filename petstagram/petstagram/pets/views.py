from django.http import HttpResponse
from django.shortcuts import render, redirect

from petstagram.pets.forms import PetDeleteForm, PetCreateForm, PetEditForm
from petstagram.pets.utils import get_by_petname_and_username


def add_pet(request):
    form = PetCreateForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('details user', pk=1)

    context = {'form': form}
    return render(request, template_name='pets/pet-add-page.html', context=context)


def details_pet(request, username, pet_slug):
    pet = get_by_petname_and_username(pet_slug, username)
    context = {
        'pet': pet,
        'total_photos_count': pet.photo_set.count(),
        'pet_photos': pet.photo_set.all(),
    }
    return render(request, 'pets/pet-details-page.html', context)


def edit_pet(request, username, pet_slug):
    pet = get_by_petname_and_username(pet_slug, username)

    if request.method == 'GET':
        form = PetEditForm(instance=pet)
    else:
        form = PetEditForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('details pet', username=username, pet_slug=pet_slug)

    context = {
        'form': form,
        'pet_slug': pet_slug,
        'username': username
        }

    return render(request, template_name='pets/pet-edit-page.html', context=context)


def delete_pet(request, username, pet_slug):

    pet = get_by_petname_and_username(pet_slug, username)

    if request.method == 'POST':
        pet.delete()
        return redirect('details user', pk=1)

    form = PetDeleteForm(instance=pet)

    context = {
        'form': form,
        'pet_slug': pet_slug,
        'username': username
    }
    return render(request, template_name='pets/pet-delete-page.html', context=context)
