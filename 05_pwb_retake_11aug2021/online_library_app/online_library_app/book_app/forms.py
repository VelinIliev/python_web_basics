from django import forms

from online_library_app.book_app.models import Book


class CreateBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

        widgets = {
            'title': forms.TextInput(
                attrs={
                    'placeholder': 'Title',
                }),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Description',
                    'id': 'description'
                }),
            'image': forms.URLInput(
                attrs={
                    'placeholder': 'Image',
                }),
            'type': forms.TextInput(
                attrs={
                    'placeholder': 'Fiction, Novel, Crime...',
                }),
        }