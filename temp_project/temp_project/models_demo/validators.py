from datetime import date

from django.core.exceptions import ValidationError


def validate_birthdate(value):
    if date.today() == value:
        raise ValidationError(f'Impossible!')