from django.urls import path

from online_library_app.common_app.views import index

urlpatterns = [
    path('', index, name='index'),
]