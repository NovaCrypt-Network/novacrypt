# Generated by Django 3.1.5 on 2021-01-26 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Administration', '0008_member_xp'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='discordid',
            field=models.CharField(blank=True, max_length=25),
        ),
    ]
