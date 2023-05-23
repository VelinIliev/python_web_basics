from django.http import HttpResponse
from django.shortcuts import render
from django import forms

from temp_project.forms.forms import PersonForm, PersonCreateForm
from temp_project.forms.models import Person


def index(request):
    name = None
    if request.method == 'get':
        form = PersonForm()
    else:
        form = PersonForm(request.POST)
        print(request.POST)
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
