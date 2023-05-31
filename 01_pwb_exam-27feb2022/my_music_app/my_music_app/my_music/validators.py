import re

from django.core.exceptions import ValidationError


def price_validator(value):
    if value < 0:
        raise ValidationError("Price can't be negative number ")


def username_min_length(value):
    if len(value) < 2:
        raise ValidationError("Username must be at least 2 characters long")


def username_content(value):
    if not re.match("^[A-Za-z0-9_]*$", value):
        raise ValidationError("Ensure this value contains only letters, numbers, and underscore.")
