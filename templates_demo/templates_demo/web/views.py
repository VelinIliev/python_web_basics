import random
from datetime import datetime

from django.shortcuts import render, redirect


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f'Name: {self.name}, age: {self.age}'


def index(request):
    context = {
        'title': 'softUni home page',
        'value': random.random(),
        'info': {
            'address': 'Sofia'
        },
        'student': Student("Velko", 24),
        'student_info': Student("Velko", 24).get_info(),
        'some_list': ['Ivan', 'Petkan', 'Dragan'],
        'some_date': datetime.now(),
        'students': ['Ivan', 'Petkan', 'Maria', 'Pesho', 'Pesho'],
        'values': list(range(1, 20))
    }
    return render(request, 'index.html', context)


def redirect_to_home(request):
    return redirect('index')

def about(request):
    return render(request, 'about.html')

def info(request):
    return render(request, 'info.html')