from django.db import models

from temp_project.forms.validators import validate_text, ValueInRangeValidator


class Pet(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Person(models.Model):
    MAX_NAME_LENGTH = 30
    name = models.CharField(max_length=MAX_NAME_LENGTH)
    age = models.PositiveIntegerField()
    pets = models.ManyToManyField(
        Pet,
    )


class Person2(models.Model):
    class Meta:
        ordering = ['id']
    name = models.CharField(max_length=30)
    profile_image = models.ImageField(
        upload_to='images',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name


class Todo(models.Model):
    MAX_TODOS = 3
    MAX_TEXT_LEN = 25
    text = models.CharField(max_length=MAX_TEXT_LEN, validators=(validate_text,))
    priority = models.IntegerField(validators=(ValueInRangeValidator(1, 10),))
    is_done = models.BooleanField(null=False, blank=False, default=False)
    assignee = models.ForeignKey(Person2, on_delete=models.RESTRICT, )
