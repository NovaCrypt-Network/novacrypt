# Generated by Django 3.1.3 on 2021-01-29 23:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Partners', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='partner',
            name='link',
            field=models.URLField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
