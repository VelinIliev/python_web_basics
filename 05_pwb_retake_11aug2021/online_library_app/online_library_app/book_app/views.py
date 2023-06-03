from django.http import HttpResponse
from django.shortcuts import render, redirect

from online_library_app.book_app.forms import CreateBookForm
from online_library_app.book_app.models import Book
from online_library_app.profile_app.models import Profile


def book_add(request):
    user = Profile.objects.get()
    if request.method == "GET":
        form = CreateBookForm()
    else:
        form = CreateBookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'user': user,
    }

    return render(request, 'book/add-book.html', context)


def book_edit(request, pk):
    book = Book.objects.filter(pk=pk).get()
    user = Profile.objects.get()
    if request.method == "GET":
        form = CreateBookForm(instance=book)
    else:
        form = CreateBookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('index')
    context={
        'form': form,
        'book': book,
        'user': user,
    }
    return render(request, 'book/edit-book.html', context)


def book_details(request, pk):
    book = Book.objects.filter(pk=pk).get()
    user = Profile.objects.get()

    context = {
        'book': book,
        'user': user,
    }
    return render(request, 'book/book-details.html', context)


def book_delete(request, pk):
    book = Book.objects.filter(pk=pk).get()
    book.delete()
    return redirect('index')
