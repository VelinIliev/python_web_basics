# Generated by Django 4.2.1 on 2023-06-02 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameplay_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='title',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]