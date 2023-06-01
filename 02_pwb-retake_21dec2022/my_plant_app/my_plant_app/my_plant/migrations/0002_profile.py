# Generated by Django 4.2.1 on 2023-06-01 09:59

import django.core.validators
from django.db import migrations, models
import my_plant_app.my_plant.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('my_plant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(2)])),
                ('first_name', models.CharField(max_length=20, validators=[my_plant_app.my_plant.validators.validate_capital_first_letter])),
                ('last_name', models.CharField(max_length=20, validators=[my_plant_app.my_plant.validators.validate_capital_first_letter])),
                ('profile_picture', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
