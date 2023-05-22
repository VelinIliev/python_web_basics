from django.http import HttpResponse
from django.shortcuts import render

from petstagram.pets.utils import get_by_petname_and_username


def add_pet(request):
    return render(request, template_name='pets/pet-add-page.html')


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
    return render(request, template_name='pets/pet-edit-page.html')


def delete_pet(request, username, pet_slug):
    pet = get_by_petname_and_username(pet_slug, username)
    return render(request, template_name='pets/pet-delete-page.html')
