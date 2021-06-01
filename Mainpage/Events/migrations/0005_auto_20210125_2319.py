# Generated by Django 3.1.5 on 2021-01-26 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0004_auto_20210124_2252'),
    ]

    operations = [
        migrations.AddField(
            model_name='competition',
            name='CompetitionURL',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='webinar',
            name='WebinarURL',
            field=models.URLField(blank=True),
        ),
    ]