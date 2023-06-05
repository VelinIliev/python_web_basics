from django.db import models


class Recipe(models.Model):
    title = models.CharField(
        max_length=30,
        null=False,
        blank=False,
    )
    image_url = models.URLField(
        name=False,
        blank=False,
        verbose_name="Image URL"
    )
    description = models.TextField(
        null=False,
        blank=False,
    )
    ingredients = models.CharField(
        max_length=250,
        null=False,
        blank=False,
    )
    time = models.IntegerField(
        null=False,
        blank=False,
    )