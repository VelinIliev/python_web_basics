from django.urls import path
from django101.tasks.views import index, show_all_tasks

urlpatterns = [
    path('', index),
    path('all', show_all_tasks),
]