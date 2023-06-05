from django.db import models


class Profile(models.Model):
    first_name = models.CharField(
        null=False,
        blank=False,
        max_length=20,
    )
    last_name = models.CharField(
        null=False,
        blank=False,
        max_length=20,
    )
    age = models.IntegerField(
        null=False,
        blank=False,
    )
    image_url = models.URLField(
        null=True,
        blank=True,
        verbose_name='Image URL'
    )


class Note(models.Model):
    title = models.CharField(
        null=False,
        blank=False,
        max_length=30,
    )
    image_url = models.URLField(
        null=False,
        blank=False,
        verbose_name='Image URL'
    )
    content = models.TextField(
        null=False,
        blank=False,
    )
