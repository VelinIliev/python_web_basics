# Generated by Django 4.2.1 on 2023-05-18 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('models_demo', '0008_department_alter_employee_job_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='department',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='models_demo.department'),
        ),
    ]
