import json
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View, CreateView, UpdateView, DeleteView
from django.http import JsonResponse
from django.contrib.auth.models import User
from .models import (
    Education,
    Experience,
    Skill,
    Project,
    ProfileLink
)
from .forms import (
    EducationForm,
    ExperienceForm,
    SkillForm,
    ProjectForm,
    ProfileLinkForm
)


class HomeView(View):
    @staticmethod
    def has_section(qs):
        return qs.exists()

    def get(self, *args, **kwargs):
        user = str(self.request.user)
        context = {}
        if user == "AnonymousUser":
            user = 1
        else:
            user = self.request.user
        education_qs = Education.objects.filter(user=user)
        experience_qs = Experience.objects.filter(user=user)
        personal_project_qs = Project.objects.filter(user=user, project_type="P2")
        skill_qs = Skill.objects.filter(user=user)
        profile_link_qs = ProfileLink.objects.filter(user=user)
        context['has_education'] = self.has_section(education_qs)
        context['has_experience'] = self.has_section(experience_qs)
        context['has_personal_project'] = self.has_section(personal_project_qs)
        context['has_profile_link'] = self.has_section(profile_link_qs)
        context['has_skill'] = self.has_section(skill_qs)
        context['education'] = education_qs
        context['experience'] = experience_qs
        context['personal_project'] = personal_project_qs
        context['skill'] = skill_qs
        context['profile_link'] = profile_link_qs
        return render(self.request, 'index.html', context)


class UserHomeView(View):
    def get(self, *args, **kwargs):
        context = {}
        user_object = User.objects.filter(username=kwargs.get('user_name'))
        if user_object.exists():
            user = user_object[0]
            education_qs = Education.objects.filter(user__username=user)
            experience_qs = Experience.objects.filter(user__username=user)
            personal_project_qs = Project.objects.filter(user__username=user, project_type="P2")
            skill_qs = Skill.objects.filter(user__username=user)
            profile_link_qs = ProfileLink.objects.filter(user__username=user)
            context['has_education'] = HomeView.has_section(education_qs)
            context['has_experience'] = HomeView.has_section(experience_qs)
            context['has_personal_project'] = HomeView.has_section(personal_project_qs)
            context['has_skill'] = HomeView.has_section(skill_qs)
            context['has_profile_link'] = HomeView.has_section(profile_link_qs)
            context['education'] = education_qs
            context['experience'] = experience_qs
            context['personal_project'] = personal_project_qs
            context['skill'] = skill_qs
            context['profile_link'] = profile_link_qs

        else:
            messages.warning(self.request, "User does not exist")
            return redirect('portfolio_app:home')
        return render(self.request, 'index.html', context)


class UserProfileView(View):
    def get(self, *args, **kwargs):
        context = {}
        education_qs = Education.objects.filter(user=self.request.user)
        experience_qs = Experience.objects.filter(user=self.request.user)
        personal_project_qs = Project.objects.filter(user=self.request.user)
        skill_qs = Skill.objects.filter(user=self.request.user)
        profile_link_qs = ProfileLink.objects.filter(user=self.request.user)
        context['user_education'] = education_qs
        context['user_experience'] = experience_qs
        context['user_project'] = personal_project_qs
        context['user_skill'] = skill_qs
        context['user_profile_link'] = profile_link_qs
        temp_list = [
            'Python', 'C programming', 'java',
            'C++', 'Django', 'Flask', 'Django Rest Framework',
            'Flask Rest Api', 'HTML', 'CSS', 'Bootstrap', 'React js',
            'Windows', 'Linux', 'Beautifulsoup', 'Machine Learning', 'Amazon Web Services',
            'Mysql', 'Postgre', 'SQLite', 'S3 Bucket', 'Ec2', 'Python Boto3 Sdk'
            ]
        context['temp_list'] = temp_list
        return render(self.request, 'profile/user_profile.html', context)


class AddEducationView(LoginRequiredMixin, CreateView):
    model = Education
    template_name = 'education_form.html'
    form_class = EducationForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddEducationView, self).form_valid(form)


class AddExperienceView(LoginRequiredMixin, CreateView):
    model = Experience
    template_name = 'experience_form.html'
    form_class = ExperienceForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddExperienceView, self).form_valid(form)


@method_decorator(csrf_exempt, name='dispatch')
class AddSkillView(LoginRequiredMixin, View):
    def post(self, *args, **kwargs):
        data = json.loads(self.request.body)
        for d in data:
            Skill.objects.get_or_create(user=self.request.user, skill=str(d).capitalize())
        response = {
            "response": "ok"
        }
        messages.success(self.request, "Skills Updated Successfully")
        return JsonResponse(response, safe=False)

    def get(self, *args, **kwargs):
        data = Skill.objects.filter(user=self.request.user).order_by('-id')
        return render(self.request, 'skill_form.html', {"data": data})


class AddProjectView(LoginRequiredMixin, CreateView):
    model = Project
    template_name = 'project_form.html'
    form_class = ProjectForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddProjectView, self).form_valid(form)


class AddProfileLinkView(LoginRequiredMixin, CreateView):
    model = ProfileLink
    template_name = 'profilelink_form.html'
    form_class = ProfileLinkForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddProfileLinkView, self).form_valid(form)


class UpdateEducationView(UpdateView):
    model = Education
    template_name = 'education_form.html'
    form_class = EducationForm

    def form_valid(self, form):
        return super(UpdateEducationView, self).form_valid(form)


class UpdateExperienceView(UpdateView):
    model = Experience
    template_name = 'experience_form.html'
    form_class = ExperienceForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(UpdateExperienceView, self).form_valid(form)


class UpdateSkillView(UpdateView):
    pass


class UpdateProjectView(UpdateView):
    model = Project
    template_name = 'project_form.html'
    form_class = ProjectForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(UpdateProjectView, self).form_valid(form)


class UpdateProfileLinkView(UpdateView):
    model = ProfileLink
    template_name = 'profilelink_form.html'
    form_class = ProfileLinkForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(UpdateProfileLinkView, self).form_valid(form)


class DeleteSkillView(DeleteView):
    model = Skill
    success_url = reverse_lazy('/portfolio/user_profile/')
    template_name = 'profile/delete_skill.html'


def delete_skill(request, pk):
    try:
        skill_to_delete = Skill.objects.get(pk=pk)
        skill_to_delete.delete()
        messages.success(request, "Successfully Deleted")
        return redirect('portfolio_app:profile')
    except ObjectDoesNotExist:
        messages.warning(request, "Opps!! The object does not exist")
        return redirect('portfolio_app:profile')
