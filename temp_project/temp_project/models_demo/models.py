from django.db import models
from datetime import date


class Project(models.Model):
    name = models.CharField(max_length=30)
    code_name = models.CharField(max_length=10, unique=True)
    deadline = models.DateField()

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name}'


class Employee(models.Model):
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(unique=True)
    works_full_time = models.BooleanField()
    job_level = models.CharField(
        max_length=20,
        choices=(
            ("jr.", "Junior"),
            ("reg.", "Regular"),
            ("sr.", "Senior"),
        ),
        verbose_name="Seniority Level"
    )
    photo = models.URLField()
    birthdate = models.DateField()
    review = models.TextField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    # One to many
    department = models.ForeignKey(Department, on_delete=models.RESTRICT, default=1)
    # Many to many
    projects = models.ManyToManyField(Project)

    @property
    def fullname(self):
        return f'{self.first_name} {self.last_name}'

    @property
    def age(self):
        today = date.today()
        age = today - self.birthdate
        age = int(age.days / 365)
        return age

    def __str__(self):
        return f'id: {self.pk}, Name: {self.fullname}, Level: {self.job_level}, Age: {self.age}'

# Employee.objects.raw('SQL code here')
# Employee.objects.all() # select
# Employee.objects.create() # insert
# Employee.objects.filter() # update + where
# Employee.objects.update() # update
