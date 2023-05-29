from django.http import HttpResponse
from django.shortcuts import render
from django import forms

from temp_project.forms.forms import PersonForm, PersonCreateForm, TodoForm, TodoCreateForm, Person2CreateForm
from temp_project.forms.models import Person, Person2


def index(request):
    name = None
    if request.method == 'get':
        form = PersonForm()
    else:
        form = PersonForm(request.POST)
        # print(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            Person.objects.create(name=name)

    context = {
        'form': form,
        'name': name,
    }

    return render(request, 'forms.html', context)


def models_forms(request):
    if request.method == 'get':
        form = PersonCreateForm()
    else:
        form = PersonCreateForm(request.POST)
        if form.is_valid():
            form.save()
            # print(form.cleaned_data)
            # pets = form.cleaned_data.pop('pets')
            # person = Person.objects.create(**form.cleaned_data)
            # print(form.cleaned_data)
            # print(pets)
            # person.pets.set(pets)
            # person.save()
    context = {
        'form': form,
    }
    return render(request, 'moldelsforms.html', context)


def index2(request):
    form_class = TodoForm

    if request.method == 'GET':
        form = form_class()
    else:
        form = form_class(request.POST)
        if form.is_valid():
            # form.save()
            return HttpResponse("All is valid")
    context = {
        'form': form
    }
    return render(request, 'forms2.html', context)


def create_person(request):
    form_class = Person2CreateForm

    if request.method == 'GET':
        form = form_class()
    else:
        form = form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("All is valid")
    context = {
        'form': form
    }
    return render(request, 'person.html', context)


def list_persons(request):
    context = {
        'persons': Person2.objects.all()
    }
    return render(request, 'persons.html', context)
