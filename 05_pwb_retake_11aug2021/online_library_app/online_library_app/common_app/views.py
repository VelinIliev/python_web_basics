from django.http import HttpResponse
from django.shortcuts import render, redirect

from online_library_app.book_app.models import Book
from online_library_app.common_app.forms import CreateProfileForm
from online_library_app.profile_app.models import Profile


def get_user():
    try:
        user = Profile.objects.get()
        return user
    except Profile.DoesNotExist:
        return None


def index(request):
    user = get_user()
    books = Book.objects.all()

    if user:
        page = 'common/home-with-profile.html'
    else:
        page = 'common/home-no-profile.html'

    if request.method == 'GET':
        form = CreateProfileForm()
    else:
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'user': user,
        'form': form,
        'books': books,
    }
    return render(request, page, context)
