from django.db import models

from petstagram.photos.models import Photo


class Comment(models.Model):
    MAX_COMMENT_SIZE = 300

    comment_text = models.CharField(
        null=False,
        blank=False,
        max_length=MAX_COMMENT_SIZE,
    )

    published_on = models.DateTimeField(
        auto_now=True,
        null=False,
        blank=True
    )

    to_photo = models.ForeignKey(
        Photo,
        on_delete=models.RESTRICT,
        null=False,
        blank=True
    )


class Like(models.Model):
    to_photo = models.ForeignKey(
        Photo,
        on_delete=models.RESTRICT
    )
