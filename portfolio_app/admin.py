from django.contrib import admin
from .models import (
    UserProfile,
    Education,
    Experience,
    Skill,
    Project,
    ProfileLink
)

admin.site.register(UserProfile)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(ProfileLink)

