# Generated by Django 3.0.7 on 2020-10-13 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Projects', '0004_team_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='icon',
            field=models.FileField(blank=True, upload_to='TeamIcons'),
        ),
    ]