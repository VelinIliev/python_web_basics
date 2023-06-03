from django.http import HttpResponse
from django.shortcuts import render, redirect

from online_library_app.book_app.models import Book
from online_library_app.profile_app.forms import EditProfileForm, DeleteProfileForm
from online_library_app.profile_app.models import Profile


def profile(request):
    user = Profile.objects.get()
    context = {
        'user': user
    }
    return render(request, 'profile/profile.html', context)


def profile_edit(request):
    user = Profile.objects.get()
    if request.method == "GET":
        form = EditProfileForm(instance=user)
    else:
        form = EditProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile view')

    context = {
        'form': form,
        'user': user,
    }
    return render(request, 'profile/edit-profile.html', context)


def profile_delete(request):
    user = Profile.objects.get()
    if request.method == "GET":
        form = DeleteProfileForm(instance=user)
    else:
        user.delete()
        Book.objects.all().delete()
        return redirect('index')
    context = {
        'form': form,
        'user': user,
    }
    return render(request, 'profile/delete-profile.html', context)
