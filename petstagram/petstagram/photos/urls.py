from django.urls import path

from petstagram.photos.views import add_photo, details_photo, edit_photo

urlpatterns = [
    path("add/", add_photo, name='add photo'),
    path("<int:pk>/", details_photo, name='details photo'),
    path("<int:pk>/edit/", edit_photo, name='edit photo'),
]