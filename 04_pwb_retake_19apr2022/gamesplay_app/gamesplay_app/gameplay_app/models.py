from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Game(models.Model):
    CATEGORY_CHOICES = (
        ('Action', 'Action'),
        ('Adventure', 'Adventure'),
        ('Puzzle', 'Puzzle'),
        ('Strategy', 'Strategy'),
        ('Sports', 'Sports'),
        ('Board/Card Game', 'Board/Card Game'),
        ('Other', 'Other')
    )
    title = models.CharField(
        null=False,
        blank=False,
        max_length=30,
        unique=True,
    )
    category = models.CharField(
        null=False,
        blank=False,
        max_length=15,
        choices=CATEGORY_CHOICES,
    )
    rating = models.FloatField(
        null=True,
        blank=True,
        validators=(MinValueValidator(0.1), MaxValueValidator(5), )
    )
    max_level = models.IntegerField(
        null=True,
        blank=True,
        validators=(MinValueValidator(1),)
    )
    image_url = models.URLField(
        null=False,
        blank=False,
        verbose_name="Image URL"
    )
    summary = models.TextField(
        null=True,
        blank=True,
    )
