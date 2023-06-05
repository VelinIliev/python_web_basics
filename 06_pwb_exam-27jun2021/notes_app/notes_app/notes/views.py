from django.http import HttpResponse
from django.shortcuts import render, redirect

from notes_app.notes.forms import CreateProfileForm, CreateNoteForm, EditNoteForm, DeleteNoteForm
from notes_app.notes.models import Profile, Note


def get_user():
    try:
        user = Profile.objects.get()
        return True
    except Profile.DoesNotExist:
        return False


def index(request):
    user = get_user()

    if not user:
        if request.method == "GET":
            form = CreateProfileForm()
        else:
            form = CreateProfileForm(request.POST)

            if form.is_valid():
                form.save()
                return redirect('index')

        context = {
            'form': form,
        }
        return render(request, 'home-no-profile.html', context)

    notes = Note.objects.all()
    context = {
        'notes': notes,
    }
    return render(request, 'home-with-profile.html', context)


def note_add(request):
    if request.method == "GET":
        form = CreateNoteForm()
    else:
        form = CreateNoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'form': form,
    }
    return render(request, 'note-create.html', context)


def note_edit(request, pk):
    note = Note.objects.filter(pk=pk).get()
    if request.method == "GET":
        form = EditNoteForm(instance=note)
    else:
        form = EditNoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        'form': form,
        'note': note,
    }
    return render(request, 'note-edit.html', context)


def note_delete(request, pk):
    note = Note.objects.filter(pk=pk).get()

    if request.method == "GET":
        form = DeleteNoteForm(instance=note)
    else:
        note.delete()
        return redirect('index')
    context = {
        'form': form,
        'note': note,
    }
    return render(request, 'note-delete.html', context)


def note_details(request, pk):
    note = Note.objects.filter(pk=pk).get()
    context = {
        'note': note,
    }
    return render(request, 'note-details.html', context)


def profile(request):
    count_notes = Note.objects.count()
    user = Profile.objects.get()
    context = {
        'count_notes': count_notes,
        'user': user,
    }
    return render(request, 'profile.html', context)


def profile_delete(request, pk):
    user = Profile.objects.filter(pk=pk).get()
    Note.objects.all().delete()
    user.delete()
    return redirect('index')