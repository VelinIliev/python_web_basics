from django.urls import path

from templates_demo.web.views import index, redirect_to_home, about, info

urlpatterns = (
    path('', index, name="index"),
    path("go-to-home/", redirect_to_home, name='redirect to home'),
    path("about/", about, name='about'),
    path("info/", info, name='info'),
)