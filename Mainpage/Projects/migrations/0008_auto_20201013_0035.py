# Generated by Django 3.0.7 on 2020-10-13 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Projects', '0007_auto_20201013_0006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='icon',
            field=models.ImageField(upload_to='TeamIcons'),
        ),
    ]