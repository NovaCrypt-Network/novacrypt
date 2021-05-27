import os
import uuid
from django.utils.translation import gettext_lazy as _

from django.db import models
from django.contrib.auth.models import User


def upload_avatar_to(instance, filename):
    filename, ext = os.path.splitext(filename)
    return os.path.join(
        'member_images',
        'avatar_{uuid}_{filename}{ext}'.format(
            uuid=uuid.uuid4(), filename=filename, ext=ext)
    )
# Create your models here.
class Member(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    avatar = models.ImageField(
        verbose_name=_('profile picture'),
        upload_to=upload_avatar_to,
        blank=False,
        default="avatar_images/DefaultImage.png"
    )
    linkedin = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    github = models.URLField(blank=True)
    discordid = models.CharField(blank=True, max_length=25)
    bio = models.TextField(blank=True,max_length=500)
    xp = models.IntegerField(default=0)
    def __str__(self):
        return self.user.username
