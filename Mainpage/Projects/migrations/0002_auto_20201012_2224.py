# Generated by Django 3.0.7 on 2020-10-13 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Administration', '0002_member_user'),
        ('Projects', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='team',
            name='members',
            field=models.ManyToManyField(blank=True, to='Administration.Member'),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('completion', models.IntegerField(choices=[(0, 'Planned'), (1, 'Prototype'), (2, 'Testing'), (3, 'Improving'), (4, 'Finalizing'), (5, 'Funding')])),
                ('description', models.TextField(max_length=40)),
                ('icon', models.ImageField(upload_to='icons')),
                ('thumbnail', models.ImageField(upload_to='thumbnails')),
                ('tags', models.ManyToManyField(blank=True, to='Projects.Tag')),
                ('teams', models.ManyToManyField(blank=True, to='Projects.Team')),
            ],
        ),
    ]