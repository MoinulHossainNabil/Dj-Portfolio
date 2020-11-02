import json
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View, CreateView
from django.http import JsonResponse
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
    def get(self, *args, **kwargs):
        return render(self.request, 'index.html', {})


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
        return JsonResponse(response, safe=False)

    def get(self, *args, **kwargs):
        data = Skill.objects.order_by('-id')
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



