import json

from django.shortcuts import render
from django import http

from temp_project.projects.models import Task


# def index(request):
#     return http.HttpResponse('request')


def show_all_tasks(request):
    all_tasks = Task.objects.order_by('name').all()
    result = ', '.join(f'{t.name}({t.id})' for t in all_tasks)
    print(list(all_tasks))
    return http.HttpResponse(result)


def index(request):
    context = {
        'title': "The task app!",
        'tasks': Task.objects.all()
    }
    return render(request, 'index.html', context)
