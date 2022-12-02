from datetime import date

from django.db import models
from django.urls import reverse

from models_demos.web.validators import validate_before_today


class AuditInfoMixin(models.Model):

    class Meta:
        abstract = True

    created_on = models.DateTimeField(
        auto_now_add=True,
    )
    updated_on = models.DateTimeField(
        auto_now=True,
    )


class Department(AuditInfoMixin, models.Model):
    name = models.CharField(max_length=25)
    slug = models.SlugField(
        unique=True
    )

    def get_absolute_url(self):
        url = reverse('department details', kwargs={'slug': self.slug, })
        return url

    def __str__(self):
        return f'{self.name}'


class Project(AuditInfoMixin, models.Model):
    name = models.CharField(max_length=30)
    code_name = models.CharField(
        max_length=10,
        unique=True,
    )
    deadline = models.DateField()

    def __str__(self):
        return f'{self.name} - {self.code_name}'


class Employee(AuditInfoMixin, models.Model):

    class Meta:
        ordering = ['age', '-years_of_experience']

    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)

    review = models.TextField()

    # years_of_experience = models.IntegerField()
    years_of_experience= models.PositiveIntegerField()
    # set on creation
    created_on = models.DateTimeField(
        auto_now_add=True,
    )
    # set on each update
    updated_on = models.DateTimeField(
        auto_now=True,
    )
    start_date = models.DateField(validators=(validate_before_today,))
    # time_filed = models.TimeField()
    # date_time_filed = models.DateTimeField()

    # char field + validations
    email = models.EmailField()

    age = models.IntegerField()

    url_field = models.URLField()

    full_time = models.BooleanField()

    level = models.CharField(
        max_length=25,
        choices=(
            ('Junior', 'Junior'),
            ('Regular', 'Regular'),
            ('Senior', "Senior" ),
        )
    )

    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
    )

    projects = models.ManyToManyField(
        Project,
    )

    @property
    def fullname(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def years_of_employment(self):
        return date.today() - self.start_date

    def __str__(self):
        return f'ID: {self.pk}; Name: {self.fullname}'


class AccessCard(models.Model):
    employee = models.OneToOneField(
        Employee,
        on_delete=models.CASCADE,
        primary_key=True
    )
