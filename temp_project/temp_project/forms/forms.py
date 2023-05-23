from django import forms

from temp_project.forms.models import Person


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
