from django.urls import path

from temp_project.forms.views import index, models_forms

urlpatterns = [
    path("", index, name='index forms'),
    path("models/", models_forms, name='models forms'),
]