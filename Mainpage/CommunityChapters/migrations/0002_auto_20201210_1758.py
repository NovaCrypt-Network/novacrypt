# Generated by Django 3.0.7 on 2020-12-10 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CommunityChapters', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chapter',
            name='instagram',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='chapter',
            name='website',
            field=models.URLField(blank=True),
        ),
    ]