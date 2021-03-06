from django.db import models
from django.conf import settings
from django.shortcuts import reverse
from django.db.models import signals
from ckeditor.fields import RichTextField

PROJECT_TYPE = (
    ('P1', 'Professional Project'),
    ('P2', 'Personal Project')
)

DEGREE = (
    ('2.1', 'Masters Degree'),
    ('2.2', 'Master of Science'),
    ('3.1', 'Bachelor Degree'),
    ('3.2', 'Bachelor of Science'),
    ('3.3', 'Bachelor in Business Administration'),
    ('3.4', 'Bachelor in Arts'),
    ('4.1', 'Diploma Degree'),
    ('5.1', 'Higher Secondary Certificate'),
    ('5.2', 'A Level'),
    ('6.1', 'Secondary School Certificate'),
    ('6.2', 'O Level'),
    ('7.1', 'Others')
)


def upload_project_image_to(instance, file_name):
    return f"{instance.project_type}/{instance.title}/{file_name}"


def upload_user_image_to(instance,file_name):
    return f"profile_photos/{instance.user.username}/{file_name}"


def upload_user_resume_to(instance, file_name):
    return f"resumes/{instance.user.username}/{file_name}"


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    phone_number = models.BigIntegerField(null=True, blank=True)
    profession = models.CharField(max_length=100, null=True, blank=True)
    photo = models.ImageField(null=True, blank=True, upload_to=upload_user_image_to)
    resume = models.FileField(null=True, blank=True, upload_to=upload_user_resume_to)
    date_of_birth = models.DateTimeField(null=True, blank=True)
    about = RichTextField(null=True, blank=True)
    joined = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse("portfolio_app:profile")


class Education(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='persons_education')
    degree = models.CharField(max_length=100, choices=DEGREE, null=True)
    major = models.CharField(max_length=100, null=True)
    institute = models.CharField(max_length=100)
    pass_year = models.PositiveIntegerField()
    cgpa = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    out_of = models.CharField(max_length=5, null=True, blank=True)

    def __str__(self):
        return self.get_degree_display()

    def get_absolute_url(self):
        return reverse('portfolio_app:profile')


class Experience(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='persons_experience')
    company_name = models.CharField(max_length=60)
    role = models.CharField(max_length=60)
    started_work_from = models.DateTimeField()
    worked_till = models.DateTimeField()
    work_description = models.TextField(null=True, blank=True)

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
    description = RichTextField(blank=True, null=True)
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


class Certification(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    title = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('portfolio_app:profile')


def create_user_profile_by_signals(sender, instance, created, *args, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


signals.post_save.connect(create_user_profile_by_signals, sender=settings.AUTH_USER_MODEL)