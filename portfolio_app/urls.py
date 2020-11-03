from django.contrib import admin
from django.urls import path
from .views import (
    HomeView,
    UserProfileView,
    AddEducationView,
    AddExperienceView,
    AddSkillView,
    AddProjectView,
    AddProfileLinkView,
    UpdateEducationView,
    UpdateExperienceView,
    UpdateProjectView,
    UpdateProfileLinkView,
    DeleteSkillView,
    delete_skill
)

app_name = 'portfolio_app'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('user_profile/', UserProfileView.as_view(), name='profile'),
    path('add-education/', AddEducationView.as_view(), name='education'),
    path('add-experience/', AddExperienceView.as_view(), name='experience'),
    path('add-skill/', AddSkillView.as_view(), name='skill'),
    path('add-project/', AddProjectView.as_view(), name='project'),
    path('add-profilelink/', AddProfileLinkView.as_view(), name='profilelink'),
    path('update-education/<int:pk>/', UpdateEducationView.as_view(), name='update-education'),
    path('update-experience/<int:pk>/', UpdateExperienceView.as_view(), name='update-experience'),
    path('update-project/<int:pk>/', UpdateProjectView.as_view(), name='update-project'),
    path('update-profilelink/<int:pk>/', UpdateProfileLinkView.as_view(), name='update-profilelink'),
    # path('delete-skill/<int:pk>/', DeleteSkillView.as_view(), name='delete-skill'),
    path('delete-skill/<int:pk>/', delete_skill, name='delete-skill'),
]
