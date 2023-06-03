from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('online_library_app.common_app.urls')),
    path('profile/', include('online_library_app.profile_app.urls')),
    path('book/', include('online_library_app.book_app.urls')),
]
