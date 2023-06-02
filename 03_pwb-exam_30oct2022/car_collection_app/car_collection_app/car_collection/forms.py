from django import forms

from car_collection_app.car_collection.models import Profile, Car


class BaseProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'email', 'age', 'password']
        widgets = {
            "username": forms.TextInput(),
            "email": forms.EmailInput(),
            "age": forms.NumberInput(),
            "password": forms.PasswordInput(),
        }


class CreateProfileForm(BaseProfileForm):
    ...


class DeleteProfileForm(BaseProfileForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.hidden_fields()

    def __hidden_fields(self):
        for (name, field) in self.fields.items():
            field.widget = forms.HiddenInput()

    def save(self, commit=True):
        if commit:
            self.instance.delete()
            Car.objects.all().delete()
        return self.instance


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        widgets = {
            "username": forms.TextInput(),
            "email": forms.EmailInput(),
            "age": forms.NumberInput(),
            "password": forms.TextInput(),
            "first_name": forms.TextInput(),
            "last_name": forms.TextInput(),
            "picture": forms.URLInput(),
        }


class BaseCarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'


class CreateCarForm(BaseCarForm):
    ...


class EditCarForm(BaseCarForm):
    ...


class DeleteCarForm(BaseCarForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__disable_fields()

    def __disable_fields(self):
        for (name, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'

    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance
