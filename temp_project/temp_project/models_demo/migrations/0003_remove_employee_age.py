# Generated by Django 4.2.1 on 2023-05-18 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('models_demo', '0002_employee_age'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='age',
        ),
    ]
