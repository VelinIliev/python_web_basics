from django.db import models


class Profile(models.Model):
    first_name = models.CharField(
        null=False,
        blank=False,
        max_length=30,
    )
    last_name = models.CharField(
        null=False,
        blank=False,
        max_length=30,
    )
    image_url = models.URLField(
        null=False,
        blank=False,
    )
