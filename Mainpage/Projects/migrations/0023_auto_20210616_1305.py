# Generated by Django 3.1.3 on 2021-06-16 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Projects', '0022_auto_20210616_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='IconCardBGColor',
            field=models.CharField(default='FFFFFF', max_length=6),
        ),
    ]
