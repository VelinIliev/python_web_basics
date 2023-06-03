from django.db import models


class Book(models.Model):
    title = models.CharField(
        null=False,
        blank=False,
        max_length=30,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    image = models.URLField(
        null=False,
        blank=False,
    )
    type = models.CharField(
        null=False,
        blank=False,
        max_length=30
    )