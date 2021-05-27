from django.db import models
import os
import uuid
from django.utils.translation import gettext_lazy as _


# Create your models here.


class Announcement(models.Model):
    announcement= models.CharField(max_length=1500)
    def __str__(self):
        return "Announcement "+ self.name