from django.urls import path

from temp_project.urls_and_views.views import index, redirect_to_first_department, show_not_found

urlpatterns = [
    path("", index, name='show departments'),
    path("<int:department_id>/", index, name='show department details'),
    path("<int:department_id>/<str:slug_info>", index, name='show department slug'),
    path("redirect", redirect_to_first_department, name='redirect demo'),
    path("not-found/", show_not_found, name='not found'),
]