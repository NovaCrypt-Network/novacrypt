from django.db import models
from django.db import models
from Administration.models import Member
import os
import uuid
from django.utils.translation import gettext_lazy as _

# Create your models here.
def upload_Competition_img(instance, filename):
    filename, ext = os.path.splitext(filename)
    return os.path.join(
        'Competition_img',
        'Competition_{uuid}_{filename}{ext}'.format(
            uuid=uuid.uuid4(), filename=filename, ext=ext)
    )

def upload_Opportunity_img(instance, filename):
    filename, ext = os.path.splitext(filename)
    return os.path.join(
        'Opportunities_img',
        'Opportunities_{uuid}_{filename}{ext}'.format(
            uuid=uuid.uuid4(), filename=filename, ext=ext)
    )

def upload_Internship_img(instance, filename):
    filename, ext = os.path.splitext(filename)
    return os.path.join(
        'Internships_img',
        'Internships_{uuid}_{filename}{ext}'.format(
            uuid=uuid.uuid4(), filename=filename, ext=ext)
    )



TYPE_CHOICES = (
    (0, 'Individual'),
    (1, 'Team')
)


class Competition_Tag(models.Model):
    tag = models.CharField(max_length=30)
    def __str__(self):
        return "Competition - "+self.tag

class Funding_Tag(models.Model):
    tag = models.CharField(max_length=30)
    def __str__(self):
        return "Funding - "+self.tag

class Opportunity_Tag(models.Model):
    tag = models.CharField(max_length=30)
    def __str__(self):
        return "Opportunities - "+self.tag

class Internship_Tag(models.Model):
    tag = models.CharField(max_length=30)
    def __str__(self):
        return "Internships - "+self.tag



class Competition(models.Model):
    name = models.CharField(max_length=75)
    logo = models.ImageField(
        verbose_name=_('Competition Logo'),
        upload_to=upload_Competition_img,
        blank=True,
    )
    description = models.TextField()
    link= models.URLField()
    tags = models.ManyToManyField(Competition_Tag)
    def __str__(self):
        return self.name

        
class Funding(models.Model):
    name = models.CharField(max_length=75)
    amount = models.BigIntegerField()
    description = models.TextField()
    duedate = models.DateField()
    type = models.IntegerField(choices=TYPE_CHOICES)
    link= models.URLField()
    tags = models.ManyToManyField(Funding_Tag)
    def __str__(self):
        return self.name

        
class Opportunity(models.Model):
    name = models.CharField(max_length=75)
    logo = models.ImageField(
        verbose_name=_('Opportunity Logo'),
        upload_to=upload_Opportunity_img,
        blank=True,
    )
    description = models.TextField()
    link= models.URLField()
    tags = models.ManyToManyField(Opportunity_Tag)
    def __str__(self):
        return self.name

        
class Internship(models.Model):
    name = models.CharField(max_length=75)
    logo = models.ImageField(
        verbose_name=_('Internship Logo'),
        upload_to=upload_Internship_img,
        blank=True,
    )
    description = models.TextField()
    link= models.URLField()
    tags = models.ManyToManyField(Internship_Tag)
    def __str__(self):
        return self.name
