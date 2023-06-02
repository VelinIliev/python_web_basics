from django.urls import path, include

from gamesplay_app.gameplay_app.views import game_create, game_details, game_edit, game_delete

urlpatterns = [
    path('create/', game_create, name='game create'),
    path('details/<int:pk>/', game_details, name='game details'),
    path('edit/<int:pk>/', game_edit, name='game edit'),
    path('delete/<int:pk>/', game_delete, name='game delete'),

]