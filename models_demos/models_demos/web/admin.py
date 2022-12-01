from django.contrib import admin

from models_demos.web.models import Employee, Department, Project, AccessCard


# Register your models here.

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'level', 'department')
    list_filter = ('level',)
    search_fields = ('first_name', 'last_name',)

    fieldsets = (
        ("Personal info",
             {
                'fields': ('first_name', 'last_name'),
             }
         ),
        ('Professional info',
            {
                'fields': ('level', 'years_of_experience'),
            }
         ),
        ('Company info',
            {
                'fields': ('email', 'department')
            }

        )
    )


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass


@admin.register(AccessCard)
class AccessCardAdmin(admin.ModelAdmin):
    pass
