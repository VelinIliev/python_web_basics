from enum import Enum

from django.core.validators import MinLengthValidator
from django.db import models

from my_plant_app.my_plant.validators import validate_capital_first_letter, validate_only_letters


class Profile(models.Model):
    username = models.CharField(
        null=False,
        blank=False,
        max_length=10,
        validators=(MinLengthValidator(2),)
    )
    first_name = models.CharField(
        null=False,
        blank=False,
        max_length=20,
        validators=(validate_capital_first_letter,)
    )
    last_name = models.CharField(
        null=False,
        blank=False,
        max_length=20,
        validators=(validate_capital_first_letter,)
    )
    profile_picture = models.URLField(
        null=True,
        blank=True,
    )


class PlantTypesEnum(Enum):
    OUTDOOR = 'Outdoor Plants'
    INDOOR = 'Indoor Plants'

    @classmethod
    def choices(cls):
        return [(x.name, x.value) for x in cls]


class Plant(models.Model):
    plant_type = models.CharField(
        null=False,
        blank=False,
        max_length=14,
        choices=(PlantTypesEnum.choices()),
        verbose_name="Type"
    )
    name = models.CharField(
        null=False,
        blank=False,
        max_length=20,
        validators=(MinLengthValidator(2), validate_only_letters, )
    )
    image_url = models.URLField(
        null=False,
        blank=False,
        verbose_name="Image URL"
    )
    description = models.CharField(
        null=False,
        blank=False
    )
    price = models.FloatField(
        null=False,
        blank=False,
    )