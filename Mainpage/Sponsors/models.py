from django.db import models
import os
import uuid
from django.utils.translation import ugettext_lazy as _

# Create your models here.
TIERS = [
    (0,"Diamond"),
    (1,"Gold"),
    (2,"Silver"),
    (3,"Bronze"),
]
def upload_Sponsor_Logo(instance, filename):
    filename, ext = os.path.splitext(filename)
    return os.path.join(
        'Sponsor_Logo',
        'Sponsor_{uuid}_{filename}{ext}'.format(
            uuid=uuid.uuid4(), filename=filename, ext=ext)
    )
class Sponsor(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(
        verbose_name=_('Sponsor'),
        upload_to=upload_Sponsor_Logo,
        blank=False,
    )
    link = models.URLField()
    tier = models.IntegerField(choices=TIERS)
    def __str__(self):
        return "Sponsor " + self.name