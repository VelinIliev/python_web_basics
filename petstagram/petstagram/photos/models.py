from django.core.validators import MinLengthValidator
from django.db import models

from petstagram.pets.models import Pet
from petstagram.photos.validators import validate_file_size
from petstagram.common.utils.mixins import StrFromFieldsMixin


class Photo(StrFromFieldsMixin, models.Model):
    str_fields = ("photo", "location")

    MIN_DESCRIPTION_LEN = 10
    MAX_DESCRIPTION_LEN = 300

    MAX_LOCATION_LEN = 30

    photo = models.ImageField(
        upload_to='photos/',
        null=False,
        blank=True,
        validators=(validate_file_size,)
    )
    description = models.CharField(
        max_length=MAX_DESCRIPTION_LEN,
        validators=(
            MinLengthValidator(MIN_DESCRIPTION_LEN),
        ),
        null=True,
        blank=True
    )
    location = models.CharField(
        max_length=MAX_LOCATION_LEN,
        null=True,
        blank=True
    )

    publication_date = models.DateField(
        null=False,
        blank=True,
        auto_now=True
    )

    tagged_pets = models.ManyToManyField(
        Pet,
        blank=True,
        null=True
    )
