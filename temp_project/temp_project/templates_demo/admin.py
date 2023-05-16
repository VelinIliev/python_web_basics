from django.contrib import admin

from temp_project.templates_demo.models import Template


@admin.register(Template)
class Template(admin.ModelAdmin):
    list_display = ('id', 'name', 'priority')