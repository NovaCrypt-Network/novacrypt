# Generated by Django 3.1.5 on 2021-01-26 04:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0005_auto_20210125_2319'),
    ]

    operations = [
        migrations.RenameField(
            model_name='competition',
            old_name='CompetitionURL',
            new_name='URL',
        ),
        migrations.RenameField(
            model_name='webinar',
            old_name='WebinarURL',
            new_name='URL',
        ),
    ]
