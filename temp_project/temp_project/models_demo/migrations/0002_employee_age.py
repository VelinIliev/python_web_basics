# Generated by Django 4.2.1 on 2023-05-18 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models_demo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='age',
            field=models.IntegerField(null=True),
        ),
    ]
