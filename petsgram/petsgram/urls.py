from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('petsgram.common.urls')),
    path('accounts/', include('petsgram.accounts.urls')),
    path('pets/', include('petsgram.pets.urls')),
    path('photos/', include('petsgram.photos.urls')),
]
