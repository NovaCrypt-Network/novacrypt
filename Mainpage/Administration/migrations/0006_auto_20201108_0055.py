# Generated by Django 3.0.7 on 2020-11-08 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Administration', '0005_member_bio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='bio',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]