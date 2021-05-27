import os
import uuid
from django.utils.translation import gettext_lazy as _

from django.db import models
from Administration.models import Member

BRANCH_CHOICES = [
    ('Management', 'Management'),
    ('Web Development', 'Web Development'),
    ('Finance', 'Finance'),
    ('Graphic Design', 'Graphic Design'),
    ('Marketing', 'Marketing'),
    ('Human Resources', 'Human Resources'),
    ('Writing', 'Writing'),
]

def upload_avatar_to(instance, filename):
    filename, ext = os.path.splitext(filename)
    return os.path.join(
        'team_member_images',
        'avatar_{uuid}_{filename}{ext}'.format(
            uuid=uuid.uuid4(), filename=filename, ext=ext)
    )
# Create your models here.
class TeamMember(models.Model):
    user = models.OneToOneField(Member,on_delete=models.CASCADE)
    branch = models.CharField(max_length=50,choices=BRANCH_CHOICES)
    subposition = models.CharField(max_length=100)
    def __str__(self):
        return self.user.user.username
