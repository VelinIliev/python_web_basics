# Generated by Django 4.1.3 on 2022-12-02 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0016_fill_slug_2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='slug',
            field=models.SlugField(default='none', unique=True),
            preserve_default=False,
        ),
    ]
