# Generated by Django 3.1.3 on 2021-02-05 21:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Projects', '0018_projectslideshowpicture_teamslideshowpicture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teamslideshowpicture',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Projects.team'),
        ),
    ]
