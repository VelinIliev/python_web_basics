import random
from datetime import datetime

from django.shortcuts import render


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f'Name: {self.name}, age: {self.age}'


def index(request):
    context = {
        'title': "some title",
        'value': random.random(),
        'info': {
            'address': "some address"
        },
        'student': Student("Doncho", 19).get_info(),
        'student2': Student("Doncho", 19),
        'number': 2,
        'join': ["Ivan", 'Petkan', 'Maria'],
        'date': datetime.now(),
        'float_number': 0.12345678901234567890,
        'students': ['Pesho', 'Pesho', 'Gosho', 'Ivan', 'Petkan'],
        # 'students': [],
        'values': list(range(20))

    }
    return render(request, 'templates_demo.html', context)


def about(request):
    return render(request, 'about.html')


def info(request):
    return render(request, 'info.html')
