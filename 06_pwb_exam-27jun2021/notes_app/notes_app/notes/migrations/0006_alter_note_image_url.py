# Generated by Django 4.2.1 on 2023-06-05 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0005_rename_cont_note_content_alter_note_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='image_url',
            field=models.URLField(default='asd', verbose_name='Image URL'),
            preserve_default=False,
        ),
    ]