from django.urls import path

from notes_app.notes.views import index, note_add, note_edit, note_delete, note_details, profile, profile_delete

urlpatterns = [
    path('', index, name='index'),
    path('profile/', profile, name='profile'),
    path('add/', note_add, name='note add'),
    path('edit/<int:pk>/', note_edit, name='note edit'),
    path('delete/<int:pk>/', note_delete, name='note delete'),
    path('details/<int:pk>/', note_details, name='note details'),
    path('profile/delete/<int:pk>/', profile_delete, name='profile delete'),
]
