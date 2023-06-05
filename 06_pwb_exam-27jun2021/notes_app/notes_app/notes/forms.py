from django import forms

from notes_app.notes.models import Profile, Note


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class CreateNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = '__all__'


class EditNoteForm(CreateNoteForm):
    ...


class DeleteNoteForm(CreateNoteForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__disable_fields()

    def __disable_fields(self):
        for (name, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
