from django.db import models
from django.template.defaultfilters import slugify

from petstagram.common.utils.mixins import StrFromFieldsMixin


class Pet(StrFromFieldsMixin, models.Model):
    str_fields = ('id', 'name')

    MAX_NAME = 30

    name = models.CharField(
        max_length=MAX_NAME,
        null=False,
        blank=False
    )
    personal_photo = models.URLField()
    date_of_birth = models.DateField(
        null=True,
        blank=True
    )
    slug = models.SlugField(
        null=False,
        blank=True,
        unique=True,
        editable=False
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(f'{self.name}-{self.id}')
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name