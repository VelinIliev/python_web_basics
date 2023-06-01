from django.core.exceptions import ValidationError


def validate_capital_first_letter(value):
    if not value[0].isupper():
        raise ValidationError("Your name must start with a capital letter!")


def validate_only_letters(value):
    if not value.isalpha():
        raise ValidationError("Plant name should contain only letters!")
