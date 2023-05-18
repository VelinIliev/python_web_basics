from django.urls import path

from temp_project.models_demo.views import test

urlpatterns = [
    path("", test),
]