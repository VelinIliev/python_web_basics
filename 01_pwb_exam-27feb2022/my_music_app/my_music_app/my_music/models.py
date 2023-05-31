from django.db import models

from my_music_app.my_music.validators import price_validator, username_min_length, username_content


class Album(models.Model):
    GENRE_CHOICES = [
        ("Pop Music", "Pop Music"),
        ("Jazz Music", "Jazz Music"),
        ("R&B Music", "R&B Music"),
        ("Rock Music", "Rock Music"),
        ("Country Music", "Country Music"),
        ("Dance Music", "Dance Music"),
        ("Hip Hop Music", "Hip Hop Music"),
        ("Other", "Other"),
    ]

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
        choices=GENRE_CHOICES,
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
