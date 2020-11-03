from django.db import models
from django.conf import settings
from django.shortcuts import reverse

CGPA_OUT_OF = (
    ('Four', '4.0'),
    ('Five', '5.0')
)

PROJECT_TYPE = (
    ('P1', 'Professional Project'),
    ('P2', 'Personal Project')
)


def upload_project_image_to(instance, file_name):
    return f"{instance.project_type}/{instance.title}/{file_name}"


class Education(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='persons_education')
    degree = models.CharField(max_length=100, null=True)
    institute = models.CharField(max_length=100)
    pass_year = models.PositiveIntegerField()
    cgpa = models.DecimalField(max_digits=3, decimal_places=2)
    out_of = models.CharField(max_length=4, choices=CGPA_OUT_OF)

    def __str__(self):
        return str(self.degree)

    def get_absolute_url(self):
        return reverse('portfolio_app:profile')


class Experience(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='persons_experience')
    company_name = models.CharField(max_length=60)
    role = models.CharField(max_length=60)
    started_work_from = models.DateTimeField()
    worked_till = models.DateTimeField()

    def __str__(self):
        return  self.role

    def get_absolute_url(self):
        return reverse("portfolio_app:profile")


class Skill(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='persons_skill')
    skill = models.CharField(max_length=60)

    def __str__(self):
        return self.skill
    
    def get_absolute_url(self):
        return reverse('portfolio_app:profile')


class Project(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='persons_project')
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to=upload_project_image_to, null=True)
    project_type = models.CharField(max_length=30, choices=PROJECT_TYPE)
    used_technologies = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    project_link = models.URLField(blank=True, null=True)
    code_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('portfolio_app:profile')


class ProfileLink(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='persons_profilelink')
    link = models.URLField()
    link_site = models.CharField(max_length=60, blank=True, null=True)

    def __str__(self):
        return self.link

    def get_absolute_url(self):
        return reverse('portfolio_app:profile')

