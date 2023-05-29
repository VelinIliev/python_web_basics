from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', include('temp_project.projects.urls')),
    path('templates/', include('temp_project.templates_demo.urls')),
    path('urls/', include('temp_project.urls_and_views.urls')),
    path('models/', include('temp_project.models_demo.urls')),
    path('forms/', include('temp_project.forms.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
