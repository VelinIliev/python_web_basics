from django.contrib import admin

from temp_project.models_demo.models import Employee, Department, Project


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'fullname', 'email', 'job_level', 'age')
    list_filter = ('job_level',)
    search_fields = ('first_name', 'last_name')


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
