# Generated by Django 3.2.6 on 2021-10-10 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Subsidiaries', '0004_auto_20210622_1735'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subsidiary',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='subsidiary',
            name='order',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
