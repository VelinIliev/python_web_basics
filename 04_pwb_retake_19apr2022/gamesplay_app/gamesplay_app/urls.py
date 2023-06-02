from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('gamesplay_app.common_app.urls')),
    path('game/', include('gamesplay_app.gameplay_app.urls')),
    path('profile/', include('gamesplay_app.auth_app.urls')),
]
