from django.db import models
import datetime

from wagtail.search import index
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core import blocks
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock
import os
import uuid
from django.utils.translation import ugettext_lazy as _
from django.dispatch import receiver
# Create your models here.

def upload_Thumbnail(instance, filename):
    filename, ext = os.path.splitext(filename)
    return os.path.join(
        'Thumbnail',
        'Thumbnail_{uuid}_{filename}{ext}'.format(
            uuid=uuid.uuid4(), filename=filename, ext=ext)
    )

class BlogPage(Page):
    short_description = models.CharField(max_length = 300)
    thumbnail = models.ImageField(
        verbose_name=_('Thumbnail'),
        upload_to=upload_Thumbnail,
        blank=False,
    )
    thumbnail_desc = models.CharField(max_length = 300)
    category = models.CharField(max_length = 20, choices=[
        ('Science','Science'),
        ('Technology','Technology'),
        ('Mathematics','Mathematics'),
        ('Events','Events'),
        ('Partners','Partners'),
    ],blank=False)
    OrginizationName = models.CharField(max_length=100,default="NovaCrypt")
    OrginizationLink = models.URLField(default="https://novacrypt.org/")
    views = models.IntegerField(default=0,blank=False)
    
    content = StreamField([
        ('paragraph', blocks.RichTextBlock(features=['h1','h2','h3','h4','h5','h6','bold','italic','ol','ul','hr','code','superscript','subscript','strikethrough'])),
        ('image',ImageChooserBlock()),
        ('embed',EmbedBlock()),
    ], blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('short_description'),
        FieldPanel('thumbnail'),
        FieldPanel('thumbnail_desc'),
        StreamFieldPanel('content')
    ]

    promote_panels = Page.promote_panels + [
        FieldPanel('category'),
        FieldPanel('OrginizationName'),
        FieldPanel('OrginizationLink')
    ]
    