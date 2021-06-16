from django.db import models
from Administration.models import Member
import os
import uuid
from django.utils.translation import gettext_lazy as _


# Create your models here.
def upload_Team_Logo(instance, filename):
    filename, ext = os.path.splitext(filename)
    return os.path.join(
        'Team_Logo',
        'Team_{uuid}_{filename}{ext}'.format(
            uuid=uuid.uuid4(), filename=filename, ext=ext)
    )
def upload_Team_Logo_inner(instance, filename):
    filename, ext = os.path.splitext(filename)
    return os.path.join(
        'Team_Logo_inner',
        'Team_{uuid}_{filename}{ext}'.format(
            uuid=uuid.uuid4(), filename=filename, ext=ext)
    )
def upload_Project_Logo(instance, filename):
    filename, ext = os.path.splitext(filename)
    return os.path.join(
        'Project_Logo',
        'Project_{uuid}_{filename}{ext}'.format(
            uuid=uuid.uuid4(), filename=filename, ext=ext)
    )
def upload_Project_Thumbnail(instance, filename):
    filename, ext = os.path.splitext(filename)
    return os.path.join(
        'Project_Thumnnail',
        'Project_{uuid}_{filename}{ext}'.format(
            uuid=uuid.uuid4(), filename=filename, ext=ext)
    )
def upload_Project_Images(instance, filename):
    filename, ext = os.path.splitext(filename)
    return os.path.join(
        'Project_Images',
        'Project_{uuid}_{filename}{ext}'.format(
            uuid=uuid.uuid4(), filename=filename, ext=ext)
    )

def upload_ProjectSlideshow(instance, filename):
    filename, ext = os.path.splitext(filename)
    return os.path.join(
        'Project_Slideshow',
        'Slide_{uuid}_{filename}{ext}'.format(
            uuid=uuid.uuid4(), filename=filename, ext=ext)
    )

def upload_TeamSlideshow(instance, filename):
    filename, ext = os.path.splitext(filename)
    return os.path.join(
        'Team_Slideshow',
        'Slide_{uuid}_{filename}{ext}'.format(
            uuid=uuid.uuid4(), filename=filename, ext=ext)
    )
STATUS_CHOICES = (
    (0, 'Planned'),
    (1, 'Prototype'),
    (2, 'Testing'),
    (3, 'Improving'),
    (4, 'Finalizing'),
    (5, 'Funding')
)

class Tag(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name
class Team(models.Model):
    name = models.CharField(max_length=15)
    icon = models.ImageField(
        verbose_name=_('Team Logo'),
        upload_to=upload_Team_Logo,
        blank=True,
    )
    IconCardBGColor = models.CharField(max_length=6, default="FFFFFF")
    inner_icon = models.ImageField(
        verbose_name=_('Team Logo Inner'),
        upload_to=upload_Team_Logo_inner,
        blank=True,
    )
    description = models.TextField(max_length=40)
    members = models.ManyToManyField(Member)
    def __str__(self):
        return "Team "+self.name

class Project(models.Model):
    name = models.CharField(max_length=15)
    completion = models.IntegerField(choices=STATUS_CHOICES)
    description = models.TextField(max_length=100)
    teams = models.ManyToManyField(Team,blank=True)
    tags = models.ManyToManyField(Tag,blank=True)
    icon = models.ImageField(
        verbose_name=_('Project Logo'),
        upload_to=upload_Project_Logo,
        blank=True,
    )
    thumbnail = models.ImageField(
        verbose_name=_('Project Thumbnail'),
        upload_to=upload_Project_Thumbnail,
        blank=True,
    )
    Desc1Image = models.ImageField(
        verbose_name=_('Project Images'),
        upload_to=upload_Project_Images,
        blank=True,
    )
    Desc1Title = models.CharField(max_length=25)
    LongDesc1 = models.TextField()
    Desc2Image = models.ImageField(
        verbose_name=_('Project Images'),
        upload_to=upload_Project_Images,
        blank=True,
    )
    Desc2Title = models.CharField(max_length=25)
    LongDesc2 = models.TextField()
    Desc3Image = models.ImageField(
        verbose_name=_('Project Images'),
        upload_to=upload_Project_Images,
        blank=True,
    )
    Desc3Title = models.CharField(max_length=25)
    LongDesc3 = models.TextField()
    PaperURL = models.URLField(blank=True)
    def __str__(self):
        return "Project "+self.name

class TeamRole(models.Model):
    Title = models.CharField(max_length=50,default="Member")
    Team = models.ForeignKey(Team,on_delete=models.CASCADE)
    User = models.OneToOneField(Member,on_delete=models.CASCADE)
    def __str__(self):
        return self.User.user.first_name + " " + self.User.user.last_name + " | " + self.Title + " for Team " + self.Team.name

class ProjectRole(models.Model):
    Title = models.CharField(max_length=50,default="Member")
    Project = models.ForeignKey(Project,on_delete=models.CASCADE)
    User = models.OneToOneField(Member,on_delete=models.CASCADE)
    def __str__(self):
        return self.User.user.first_name + " " + self.User.user.last_name + " | " + self.Title + " for Project " + self.Project.name



class ProjectSlideshowPicture(models.Model):
    event = models.ForeignKey(Project,on_delete=models.CASCADE)
    picture = models.ImageField(
        verbose_name=_('Slide'),
        upload_to=upload_ProjectSlideshow,
        blank=True,
    )
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=300)
    def __str__(self):
            return self.event.__str__() + " " + self.title

class TeamSlideshowPicture(models.Model):
    event = models.ForeignKey(Team,on_delete=models.CASCADE)
    picture = models.ImageField(
        verbose_name=_('Slide'),
        upload_to=upload_TeamSlideshow,
        blank=True,
    )
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=300)
    def __str__(self):
            return self.event.__str__() + " " + self.title