from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Competition)
admin.site.register(Funding)
admin.site.register(Opportunity)
admin.site.register(Internship)
admin.site.register(Competition_Tag)
admin.site.register(Funding_Tag)
admin.site.register(Opportunity_Tag)
admin.site.register(Internship_Tag)
