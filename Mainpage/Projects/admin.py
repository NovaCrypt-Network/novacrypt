from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Team)
admin.site.register(Tag)
admin.site.register(Project)
admin.site.register(TeamRole)
admin.site.register(ProjectRole)
admin.site.register(TeamSlideshowPicture)
admin.site.register(ProjectSlideshowPicture)