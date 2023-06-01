from django import forms

from my_plant_app.my_plant.models import Profile, Plant


class BaseProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('username', 'first_name', 'last_name')
        widgets = {
            "username": forms.TextInput(),
            "first_name": forms.TextInput(),
            "last_name": forms.TextInput(),
        }


class CreateProfileForm(BaseProfileForm):
    ...


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
        widgets = {
            "username": forms.TextInput(),
            "first_name": forms.TextInput(),
            "last_name": forms.TextInput(),
            "profile_picture": forms.URLInput(),
        }


class DeleteProfileForm(BaseProfileForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__hidden_fields()

    def __hidden_fields(self):
        for (name, field) in self.fields.items():
            field.widget = forms.HiddenInput()

    def save(self, commit=True):
        if commit:
            Plant.objects.all().delete()
            self.instance.delete()
        return self.instance


class BasePlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = '__all__'
        widgets = {
            'image_url': forms.URLInput(),
            'description': forms.Textarea(),
            'price': forms.NumberInput()
        }


class CreatePlantForm(BasePlantForm):
    ...


class EditPlantForm(BasePlantForm):
    ...


class DeletePlantForm(BasePlantForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__disable_fields()

    def __disable_fields(self):
        for (name, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            # field.widget.attrs['readonly'] = 'readonly'

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance
