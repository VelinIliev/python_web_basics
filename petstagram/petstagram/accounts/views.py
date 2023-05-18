from django.http import HttpResponse
from django.shortcuts import render


def login_user(request):
    return render(request, template_name='accounts/login-page.html')


def register_user(request):
    return render(request, template_name='accounts/register-page.html')


def show_user_details(request, pk):
    return render(request, template_name='accounts/profile-details-page.html')


def edit_user(request, pk):
    return render(request, template_name='accounts/profile-edit-page.html')


def delete_user(request, pk):
    return render(request, template_name='accounts/profile-delete-page.html')
