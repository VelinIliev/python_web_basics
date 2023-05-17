from django.urls import path

from testProject.main.views import index, about, contacts

urlpatterns = [
    path("", index, name='home'),
    path("about/", about, name='about'),
    path("contacts/", contacts, name='contacts'),
]