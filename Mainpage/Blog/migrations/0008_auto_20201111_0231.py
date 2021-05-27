# Generated by Django 3.0.7 on 2020-11-11 08:31

import Blog.models
from django.db import migrations, models
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0007_auto_20201108_0003'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpage',
            name='date',
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='content',
            field=wagtail.core.fields.StreamField([('paragraph', wagtail.core.blocks.RichTextBlock(features=['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'bold', 'italic', 'ol', 'ul', 'hr', 'code', 'superscript', 'subscript', 'strikethrough'])), ('image', wagtail.images.blocks.ImageChooserBlock()), ('embed', wagtail.embeds.blocks.EmbedBlock())], blank=True),
        ),
        migrations.AlterField(
            model_name='blogpage',
            name='thumbnail',
            field=models.ImageField(upload_to=Blog.models.upload_Thumbnail, verbose_name='Thumbnail'),
        ),
    ]
