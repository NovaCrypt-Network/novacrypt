# Generated by Django 3.0.7 on 2020-10-13 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Projects', '0003_auto_20201012_2235'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='description',
            field=models.TextField(default=0, max_length=20),
            preserve_default=False,
        ),
    ]
