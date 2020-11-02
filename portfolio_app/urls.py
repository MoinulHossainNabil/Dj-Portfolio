from django.contrib import admin
from django.urls import path
from .views import (
    HomeView,
    AddEducationView,
    AddExperienceView,
    AddSkillView,
    AddProjectView,
    AddProfileLinkView
)

app_name = 'portfolio_app'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('add-education/', AddEducationView.as_view(), name='education'),
    path('add-experience/', AddExperienceView.as_view(), name='experience'),
    path('add-skill/', AddSkillView.as_view(), name='skill'),
    path('add-project/', AddProjectView.as_view(), name='project'),
    path('add-profilelink/', AddProfileLinkView.as_view(), name='profilelink'),
]
