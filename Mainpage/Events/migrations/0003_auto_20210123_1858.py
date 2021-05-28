# Generated by Django 3.1.5 on 2021-01-23 23:58

import Events.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0002_auto_20210123_1734'),
    ]

    operations = [
        migrations.AddField(
            model_name='competition',
            name='img',
            field=models.ImageField(default=django.utils.timezone.now, upload_to=Events.models.upload_Event_Logo, verbose_name='Event'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='webinar',
            name='img',
            field=models.ImageField(default=django.utils.timezone.now, upload_to=Events.models.upload_Event_Logo, verbose_name='Event'),
            preserve_default=False,
        ),
    ]