# Generated by Django 4.1.3 on 2022-12-01 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0011_project_employee_projects'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessCard',
            fields=[
                ('employee', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='web.employee')),
            ],
        ),
    ]
