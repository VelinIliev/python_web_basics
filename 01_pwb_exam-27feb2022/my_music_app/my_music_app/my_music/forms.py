from django import forms

from my_music_app.my_music.models import Profile, Album


class CreateAccountForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

        widgets = {
            'username': forms.TextInput(
                attrs={
                    'placeholder': 'Username',
                }),
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Email',
                }),
            'age': forms.NumberInput(
                attrs={
                    'type': 'number',
                    'min_value': 0,
                    'placeholder': 'Age',
                }
            ),
        }


class CreateAlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Album Name',
                }),
            'artist': forms.TextInput(
                attrs={
                    'placeholder': 'Artist Name',
                }),
            'description': forms.TextInput(
                attrs={
                    'placeholder': 'Description',
                }),
            'image_url': forms.URLInput(
                attrs={
                    'placeholder': 'Image URL',
                }),
            'price': forms.NumberInput(
                attrs={
                    'placeholder': 'Price',
                }),
        }


class EditAlbumForm(CreateAlbumForm):
    ...


class DeleteAlbumForm(CreateAlbumForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__disable_fields()

    def __disable_fields(self):
        for (name, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'
