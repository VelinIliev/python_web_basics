from django.urls import path

from temp_project.forms.views import index, models_forms, index2, create_person, list_persons

urlpatterns = [
    path("", index, name='index forms'),
    path("index2/", index2, name='index2 forms'),
    path("models/", models_forms, name='models forms'),
    path("person/", create_person, name='create person'),
    path("persons/", list_persons, name='list persons'),
]