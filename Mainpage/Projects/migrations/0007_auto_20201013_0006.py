# Generated by Django 3.0.7 on 2020-10-13 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Projects', '0006_auto_20201012_2256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='icon',
            field=models.FileField(upload_to='ProjectIcons'),
        ),
    ]
