from enum import Enum

from django.db import models

from my_music_app.my_music.validators import price_validator, username_min_length, username_content


class AlbumGenres(Enum):
    POP = "Pop Music"
    JAZZ = "Jazz Music"
    RNB = "R&B Music"
    ROCK = "Rock Music"
    COUNTRY = "Country Music"
    DANCE = "Dance Music"
    HIPHOP = "Hip Hop Music"
    OTHER = "Other"

    @classmethod
    def choices(cls):
        return [(x.name, x.value) for x in cls]


class Album(models.Model):
    # GENRE_CHOICES = [
    #     ("Pop Music", "Pop Music"),
    #     ("Jazz Music", "Jazz Music"),
    #     ("R&B Music", "R&B Music"),
    #     ("Rock Music", "Rock Music"),
    #     ("Country Music", "Country Music"),
    #     ("Dance Music", "Dance Music"),
    #     ("Hip Hop Music", "Hip Hop Music"),
    #     ("Other", "Other"),
    # ]

    class Meta:
        ordering = ('genre', 'artist', 'name')

    name = models.CharField(
        unique=True,
        null=False,
        blank=False,
        max_length=30,
    )
    artist = models.CharField(
        null=False,
        blank=False,
        max_length=30
    )
    genre = models.CharField(
        null=False,
        blank=False,
        max_length=30,
        choices=AlbumGenres.choices(),
    )
    description = models.CharField(
        null=True,
        blank=True
    )
    image_url = models.URLField(
        null=False,
        blank=False,
    )
    price = models.FloatField(
        null=False,
        blank=False,
        validators=(price_validator,)
    )


class Profile(models.Model):
    username = models.CharField(
        null=False,
        blank=False,
        max_length=15,
        validators=(username_min_length, username_content)
    )
    email = models.EmailField(
        null=False,
        blank=False,
    )
    age = models.PositiveIntegerField(
        null=True,
        blank=True,
    )
