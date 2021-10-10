from django.db import models
import os
import uuid
from django.utils.translation import gettext_lazy as _
from Administration.models import *
# Create your models here.



def upload_Course_Logo(instance, filename):
    filename, ext = os.path.splitext(filename)
    return os.path.join(
        'Course_Logo',
        'Course_{uuid}_{filename}{ext}'.format(
            uuid=uuid.uuid4(), filename=filename, ext=ext)
    )



class Course(models.Model):
    title = models.CharField(max_length=35)
    logo = models.ImageField(
        verbose_name=_('Course Logo'),
        upload_to=upload_Course_Logo,
        blank=True,
    )
    members = models.ManyToManyField(Member, blank=True)
    def __str__(self):
        return "Course "+ self.title

class Video(models.Model):
    title = models.CharField(max_length=35)

    order = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ['order']

    course = models.ForeignKey(Course, on_delete=models.CASCADE, default=1, related_name='videos')

    video_code = models.CharField(max_length=35)
    def __str__(self):
        return self.course.title + " - "+ self.title