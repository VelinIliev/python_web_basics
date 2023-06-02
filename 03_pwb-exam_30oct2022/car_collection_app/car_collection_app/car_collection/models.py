from enum import Enum

from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator
from django.db import models

from car_collection_app.car_collection.validators import min_length_validator, year_validator


class Profile(models.Model):
    username = models.CharField(
        null=False,
        blank=False,
        max_length=10,
        validators=(min_length_validator,)
    )
    email = models.EmailField(
        null=False,
        blank=False,
    )
    age = models.IntegerField(
        null=False,
        blank=False,
        validators=(MinValueValidator(18),)
    )
    password = models.CharField(
        null=False,
        blank=False,
        max_length=30,
    )
    first_name = models.CharField(
        null=True,
        blank=True,
        max_length=30,
    )
    last_name = models.CharField(
        null=True,
        blank=True,
        max_length=30,
    )
    picture = models.URLField(
        null=True,
        blank=True,
        verbose_name="Profile Picture"
    )


class CarChoices(Enum):
    SPORT = 'Sports Car'
    PICKUP = 'Pickup'
    CROSSOVER = 'Crossover'
    MINIBUS = 'Minibus'
    OTHER = 'Other'

    @classmethod
    def choices(cls):
        return [(x.name, x.value) for x in cls]


class Car(models.Model):
    type = models.CharField(
        null=True,
        blank=True,
        max_length=10,
        choices=CarChoices.choices()
    )
    model = models.CharField(
        null=False,
        blank=False,
        max_length=20,
        validators=(min_length_validator,)
    )
    year = models.IntegerField(
        null=False,
        blank=False,
        validators=(year_validator,)
    )
    price = models.FloatField(
        null=False,
        blank=False,
        validators=(MinValueValidator(1),)
    )
    image_url = models.URLField(
        null=False,
        blank=False,
    )
