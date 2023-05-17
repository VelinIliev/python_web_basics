from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    context = {
        "title": "Home",
        "content": ['xxx'],
        "other": {
            "property1": "property1",
            "property2": "property2",
        },
        "request": request,
    }
    return render(request, 'base.html', context)


def about(request):
    context = {
        "title": "About",
        "content": ["Lorem ipsum dolor sit amet consectetur adipisicing elit. Veritatis sint dicta quas eaque laborum est ducimus, blanditiis similique? Libero animi nam earum voluptatibus porro, dolor tempora dolorum ullam consectetur impedit!"],
        "other": {
            "property1": "property1",
            "property2": "property2",
            "property3": "property3",
            "property4": "property4",
        },
        "request": request,
    }
    return render(request, 'about.html', context)


def contacts(request):
    context = {
        "title": "Contacts",
        "content": ['Lorem ipsum dolor sit amet consectetur adipisicing elit. Veritatis sint dicta quas eaque laborum est ducimus, blanditiis similique? Libero animi nam earum voluptatibus porro, dolor tempora dolorum ullam consectetur impedit!',
                    'Lorem ipsum dolor sit amet consectetur adipisicing elit. Veritatis sint dicta quas eaque laborum est ducimus, blanditiis similique? Libero animi nam earum voluptatibus porro, dolor tempora dolorum ullam consectetur impedit!',
                    'Lorem ipsum dolor sit amet consectetur adipisicing elit. Veritatis sint dicta quas eaque laborum est ducimus, blanditiis similique? Libero animi nam earum voluptatibus porro, dolor tempora dolorum ullam consectetur impedit!',
                    'Lorem ipsum dolor sit amet consectetur adipisicing elit. Veritatis sint dicta quas eaque laborum est ducimus, blanditiis similique? Libero animi nam earum voluptatibus porro, dolor tempora dolorum ullam consectetur impedit!',
                    'Lorem ipsum dolor sit amet consectetur adipisicing elit. Veritatis sint dicta quas eaque laborum est ducimus, blanditiis similique? Libero animi nam earum voluptatibus porro, dolor tempora dolorum ullam consectetur impedit!',
                    'Lorem ipsum dolor sit amet consectetur adipisicing elit. Veritatis sint dicta quas eaque laborum est ducimus, blanditiis similique? Libero animi nam earum voluptatibus porro, dolor tempora dolorum ullam consectetur impedit!',
                    'Lorem ipsum dolor sit amet consectetur adipisicing elit. Veritatis sint dicta quas eaque laborum est ducimus, blanditiis similique? Libero animi nam earum voluptatibus porro, dolor tempora dolorum ullam consectetur impedit!',
                    'Lorem ipsum dolor sit amet consectetur adipisicing elit. Veritatis sint dicta quas eaque laborum est ducimus, blanditiis similique? Libero animi nam earum voluptatibus porro, dolor tempora dolorum ullam consectetur impedit!',
                    'Lorem ipsum dolor sit amet consectetur adipisicing elit. Veritatis sint dicta quas eaque laborum est ducimus, blanditiis similique? Libero animi nam earum voluptatibus porro, dolor tempora dolorum ullam consectetur impedit!',
                    'Lorem ipsum dolor sit amet consectetur adipisicing elit. Veritatis sint dicta quas eaque laborum est ducimus, blanditiis similique? Libero animi nam earum voluptatibus porro, dolor tempora dolorum ullam consectetur impedit!',
                    'Lorem ipsum dolor sit amet consectetur adipisicing elit. Veritatis sint dicta quas eaque laborum est ducimus, blanditiis similique? Libero animi nam earum voluptatibus porro, dolor tempora dolorum ullam consectetur impedit!'],
        "request": request,
    }
    return render(request, 'contacts.html', context)
