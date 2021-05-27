from django.db import models
import os
import uuid
from django.utils.translation import gettext_lazy as _


# Create your models here.

def upload_Partner_Logo(instance, filename):
    filename, ext = os.path.splitext(filename)
    return os.path.join(
        'Partner_Logo',
        'Partner_{uuid}_{filename}{ext}'.format(
            uuid=uuid.uuid4(), filename=filename, ext=ext)
    )

class Partner(models.Model):
    name = models.CharField(max_length=15)
    logo = models.ImageField(
        verbose_name=_('Partner Logo'),
        upload_to=upload_Partner_Logo,
        blank=True,
    )
    link = models.URLField()
    def __str__(self):
        return "Partner "+ self.name