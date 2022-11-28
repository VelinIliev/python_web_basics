from django.urls import path

from departments.departments_app.views import show_departments, show_departments_by_id, redirect_to_first_department, \
    show_not_found

urlpatterns = [
    path('', show_departments),
    path('<int:department_id>/', show_departments_by_id, name='show departments'),
    path('int/<int:department_id>/', show_departments),
    path('redirect/', redirect_to_first_department),
]