from django.urls import path

from petsgram.common.views import index

urlpatterns = [
    path("", index, name='index')
]