# Generated by Django 4.1.3 on 2022-12-01 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_employee_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='level',
            field=models.CharField(choices=[('jr.', 'Junior'), ('reg', 'Regular'), ('sr', 'Senior')], default='jr.', max_length=25),
            preserve_default=False,
        ),
    ]
