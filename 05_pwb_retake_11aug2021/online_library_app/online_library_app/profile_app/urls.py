from django.urls import path

from online_library_app.profile_app.views import profile, profile_edit, profile_delete

urlpatterns = [
    path('', profile, name='profile view'),
    path('edit/', profile_edit, name='profile edit'),
    path('delete/', profile_delete, name='profile delete'),
]