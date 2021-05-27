from django.db import models
import os
import uuid
from django.utils.translation import gettext_lazy as _


# Create your models here.

def upload_Subsidiary_Logo(instance, filename):
    filename, ext = os.path.splitext(filename)
    return os.path.join(
        'Subsidiary_Logo',
        'Subsidiary_{uuid}_{filename}{ext}'.format(
            uuid=uuid.uuid4(), filename=filename, ext=ext)
    )

class Subsidiary(models.Model):
    name = models.CharField(max_length=35)
    logo = models.ImageField(
        verbose_name=_('Subsidiary Logo'),
        upload_to=upload_Subsidiary_Logo,
        blank=True,
    )
    link = models.URLField()
    def __str__(self):
        return "Subsidiary "+ self.name