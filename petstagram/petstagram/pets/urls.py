from django.urls import path

from petstagram.pets.views import add_pet, details_pet, edit_pet, delete_pet

urlpatterns = [
    path("add/", add_pet, name='add pet'),
    path("<str:username>/pet/<slug:pet_slug>/", details_pet, name='details pet'),
    path("<str:username>/pet/<slug:pet_slug>/edit/", edit_pet, name='edit pet'),
    path("<str:username>/pet/<slug:pet_slug>/delete/", delete_pet, name='delete pet'),
]