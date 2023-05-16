from django.urls import path

from temp_project.templates_demo.views import index, about, info

urlpatterns = [
    path("", index, name='index'),
    path("about/", about, name='about'),
    path("info/", info, name='info'),
]