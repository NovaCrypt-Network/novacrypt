from django.db import models
import os
import uuid
from django.utils.translation import gettext_lazy as _
from django.forms import ModelForm
from django.forms.widgets import TextInput, DateTimeInput, FileInput
from datetime import timezone, datetime, timedelta
import pytz
from django.utils import timezone as tz1

def upload_Slideshow(instance, filename):
    filename, ext = os.path.splitext(filename)
    return os.path.join(
        'Event_Slideshow',
        'Slide_{uuid}_{filename}{ext}'.format(
            uuid=uuid.uuid4(), filename=filename, ext=ext)
    )
def upload_Judge(instance, filename):
    filename, ext = os.path.splitext(filename)
    return os.path.join(
        'Event_Judges',
        'Judge_{uuid}_{filename}{ext}'.format(
            uuid=uuid.uuid4(), filename=filename, ext=ext)
    )
def upload_Speaker(instance, filename):
    filename, ext = os.path.splitext(filename)
    return os.path.join(
        'Event_Speakers',
        'Speaker_{uuid}_{filename}{ext}'.format(
            uuid=uuid.uuid4(), filename=filename, ext=ext)
    )
def upload_Event_Logo(instance, filename):
    filename, ext = os.path.splitext(filename)
    return os.path.join(
        'Event_Logo',
        'Event_{uuid}_{filename}{ext}'.format(
            uuid=uuid.uuid4(), filename=filename, ext=ext)
    )
# Create your models here.
class Judge(models.Model):
    picture = models.ImageField(
        verbose_name=_('Event Judges'),
        upload_to=upload_Judge,
        blank=True,
        default="avatar_images/DefaultImage.png"
    )
    name = models.CharField(max_length=100)
    field = models.CharField(max_length=100)
    def __str__(self):
            return self.name

class Competition(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField()
    competition_type = models.CharField(max_length=100)
    description = models.TextField()
    judges = models.ManyToManyField(Judge,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    img = models.ImageField(
        verbose_name=_('Event'),
        upload_to=upload_Event_Logo,
        blank=False,
    )
    description_field_number_1 = models.CharField(max_length=100)
    description_field_text_1 = models.CharField(max_length=100)
    description_field_number_2 = models.CharField(max_length=100)
    description_field_text_2 = models.CharField(max_length=100)
    description_field_number_3 = models.CharField(max_length=100)
    description_field_text_3 = models.CharField(max_length=100)
    description_field_number_4 = models.CharField(max_length=100)
    description_field_text_4 = models.CharField(max_length=100)

    URL = models.URLField(blank=True)

    def __str__(self):
        return "Competition: "+ self.title
    def type(self):
        return "Competition"

class CompetitionSlideshowPicture(models.Model):
    event = models.ForeignKey(Competition,on_delete=models.CASCADE)
    picture = models.ImageField(
        verbose_name=_('Slide'),
        upload_to=upload_Slideshow,
        blank=True,
    )
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=300)
    def __str__(self):
            return self.event.__str__() + " " + self.title

class FAQ(models.Model):
    event = models.ForeignKey(Competition,on_delete=models.CASCADE)
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=500)

    def __str__(self):
            return self.event.__str__() + " question"

class Prize(models.Model):
    event = models.ForeignKey(Competition,on_delete=models.CASCADE)
    prize = models.CharField(max_length=100)
    descr = models.CharField(max_length=100)
    def __str__(self):
            return self.event.__str__() + " prize"

class Schedule(models.Model):
    event = models.ForeignKey(Competition,on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    title = models.CharField(max_length=100)
    descr = models.CharField(max_length=500)

    def __str__(self):
            return self.event.__str__() + " schedule " + self.title

    def getstart(self):
        return self.start_time.astimezone(pytz.timezone('America/New_York')).strftime('%b %d, %I:%M %p')

    def getend(self):
        return self.end_time.astimezone(pytz.timezone('America/New_York')).strftime('%b %d, %I:%M %p')

#Begin AMA/Webinar/Ideathon stuff

class Webinar(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    img = models.ImageField(
        verbose_name=_('Event'),
        upload_to=upload_Event_Logo,
        blank=False,
    )
    URL = models.URLField(blank=True)
    def __str__(self):
        return "Webinar: "+ self.title
    def type(self):
        return "Webinar"
    def is_past_due(self):
        return tz1.now() > self.date

class Speaker(models.Model):
    event = models.ForeignKey(Webinar,on_delete=models.CASCADE)
    picture = models.ImageField(
        verbose_name=_('Event Speakers'),
        upload_to=upload_Speaker,
        blank=True,
        default="avatar_images/DefaultImage.png"
    )
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    description = models.TextField()

class WebinarSlideshowPicture(models.Model):
    event = models.ForeignKey(Webinar,on_delete=models.CASCADE)
    picture = models.ImageField(
        verbose_name=_('Slide'),
        upload_to=upload_Slideshow,
        blank=True,
    )
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=300)


