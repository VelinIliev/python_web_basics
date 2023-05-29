import uuid

from django import forms
from django.core.exceptions import ValidationError

from temp_project.forms.model_validators import validate_max_todos_per_person
from temp_project.forms.models import Person, Todo, Person2
from temp_project.forms.validators import validate_text, validate_priority, ValueInRangeValidator


class PersonForm(forms.Form):
    your_name = forms.CharField(
        max_length=30,
        help_text="Enter your name",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter your name',
                'class': 'test-class'
            }
        )
    )
    age = forms.IntegerField(
        required=False,
        label='Your age',
        initial=0,
        help_text="Enter your age",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter your age'
            }
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(),
        required=False
    )
    url = forms.CharField(
        required=False,
        widget=forms.URLInput()
    )
    password = forms.CharField(
        widget=forms.PasswordInput(),
        required=False
    )

    story = forms.CharField(
        widget=forms.Textarea(),
        required=False
    )
    CHOICES = ((0, "Child"), (1, "High School"), (2, "Student"), (3, "Adult"))

    occupancy = forms.ChoiceField(
        choices=CHOICES,
        required=False,
    )
    occupancy2 = forms.ChoiceField(
        choices=CHOICES,
        widget=forms.RadioSelect(),
        required=False,
    )
    occupancy3 = forms.MultipleChoiceField(
        choices=CHOICES,
        widget=forms.SelectMultiple(),
        required=False,
    )
    checkbox = forms.BooleanField(
        required=False
    )
    checkbox2 = forms.BooleanField(
        required=False
    )


class PersonCreateForm(forms.ModelForm):
    # story = forms.CharField(
    #     widget=forms.Textarea(),
    #     required=False
    # )
    class Meta:
        model = Person
        fields = '__all__'  # or ('name', 'age')
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Test',
                    'class': 'test-class'
                }
            )
        }
        help_texts = {
            'name': "Yor name"
        }
        labels = {
            'age': "The age"
        }


class TodoForm(forms.Form):
    text = forms.CharField(
        max_length=30,
        validators=(validate_text,),
        error_messages={
            'required': "Това поле е задължително"
        }
    )
    is_done = forms.BooleanField(required=False)
    # priority = forms.IntegerField(validators=(validate_priority,))
    priority = forms.IntegerField(validators=(ValueInRangeValidator(1, 10),))


class TodoCreateForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'

    def clean(self):
        return super().clean()

    def clean_text(self):
        return self.cleaned_data['text'].lower()

    def clean_assignee(self):
        assignee = self.cleaned_data['assignee']
        validate_max_todos_per_person(assignee)
        return assignee


class Person2CreateForm(forms.ModelForm):
    class Meta:
        model = Person2
        fields = '__all__'

    def clean_profile_image(self):
        profile_image = self.cleaned_data['profile_image']
        profile_image.name = str(uuid.uuid4())
        return profile_image
