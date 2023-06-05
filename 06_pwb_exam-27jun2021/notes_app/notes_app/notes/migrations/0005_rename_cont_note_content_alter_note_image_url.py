# Generated by Django 4.2.1 on 2023-06-05 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0004_note'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='cont',
            new_name='content',
        ),
        migrations.AlterField(
            model_name='note',
            name='image_url',
            field=models.URLField(blank=True, null=True, verbose_name='Image URL'),
        ),
    ]
