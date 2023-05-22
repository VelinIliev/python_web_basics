from django.core.exceptions import ValidationError


def validate_file_size(value):
    MB_LIMIT = 5.0

    if value.size > MB_LIMIT * 1024 * 1024:
        raise ValidationError(f"The maximum file size can be uploaded is {MB_LIMIT} MB")
