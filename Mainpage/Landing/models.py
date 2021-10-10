from django.db import models
import os
import uuid
from django.utils.translation import gettext_lazy as _
# Create your models here.


Tags = (
    (0, 'Standard'),
    (1, 'Beta'),
    (2, 'Down'),
)
class Service(models.Model):
    name = models.CharField(max_length=35)
    tag = models.IntegerField(choices=Tags, default=0)
    link = models.URLField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return "Service "+ self.name




def upload_News_Logo(instance, filename):
    filename, ext = os.path.splitext(filename)
    return os.path.join(
        'News_Logo',
        'News_{uuid}_{filename}{ext}'.format(
            uuid=uuid.uuid4(), filename=filename, ext=ext)
    )


class News(models.Model):
    name = models.CharField(max_length=35)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    logo = models.ImageField(
        verbose_name=_('News Logo'),
        upload_to=upload_News_Logo,
        blank=True,
    )
    desc = models.TextField()
    def __str__(self):
        return "News "+ self.name