from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', include('temp_project.projects.urls')),
    path('templates/', include('temp_project.templates_demo.urls')),
    path('urls/', include('temp_project.urls_and_views.urls')),
]
