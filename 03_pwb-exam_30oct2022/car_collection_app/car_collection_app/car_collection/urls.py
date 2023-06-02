from django.urls import path

from car_collection_app.car_collection.views import index, profile_create, profile_details, profile_edit, \
    profile_delete, car_create, car_details, car_edit, car_delete, catalogue

urlpatterns = [
    path('', index, name='index'),
    path('profile/create/', profile_create, name='profile create'),
    path('profile/details/', profile_details, name='profile details'),
    path('profile/edit/', profile_edit, name='profile edit'),
    path('profile/delete/', profile_delete, name='profile delete'),
    path('car/create/', car_create, name='car create'),
    path('car/<int:pk>/details/', car_details, name='car details'),
    path('car/<int:pk>/edit/', car_edit, name='car edit'),
    path('car/<int:pk>/delete/', car_delete, name='car delete'),
    path('catalogue/', catalogue, name='catalogue'),
]