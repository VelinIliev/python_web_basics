from django.urls import path

from temp_project.projects.views import index, show_all_tasks

urlpatterns = [
    path("", index),
    path('all/', show_all_tasks),
]