from django import forms
from .models import Education, Experience, Skill, Project, ProfileLink


class EducationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['degree'].widget.attrs.update({"placeholder": "Enter degree with major"})
        self.fields['institute'].widget.attrs.update({"placeholder": "Enter institution name"})
        self.fields['pass_year'].widget.attrs.update({"placeholder": "Enter passing year"})
        self.fields['cgpa'].widget.attrs.update({"placeholder": "Enter cgpa"})

    class Meta:
        model = Education
        fields = ('degree', 'institute', 'pass_year', 'cgpa', 'out_of',)


class ExperienceForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['company_name'].widget.attrs.update({"placeholder": "Enter company name"})
        self.fields['role'].widget.attrs.update({"placeholder": "Enter role"})

    class Meta:
        model = Experience
        fields = ('company_name', 'role', 'started_work_from', 'worked_till')


class SkillForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['skill'].widget.attrs.update({"placeholder": "Enter skill"})

    class Meta:
        model = Skill
        fields = ('skill', )


class ProjectForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({"placeholder": "Enter project title"})
        self.fields['used_technologies'].widget.attrs.update({"placeholder": "Enter the key technologies", "rows": "5"})
        self.fields['description'].widget.attrs.update({"placeholder": "Enter project description", "rows": "5"})
        self.fields['project_link'].widget.attrs.update({"placeholder": "Enter project link if any"})
        self.fields['code_link'].widget.attrs.update({"placeholder": "Enter source code link if any"})
    
    class Meta:
        model = Project
        fields = (
            'title',
            'project_type',
            'used_technologies',
            'description',
            'project_link',
            'code_link'
        )


class ProfileLinkForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['link'].widget.attrs.update({"placeholder": "Enter profile link"})
        self.fields['link_site'].widget.attrs.update({"placeholder": "Link site i.e (hackerrank, leetcode)"})
    
    class Meta:
        model = ProfileLink
        fields = (
            'link',
            'link_site',
        )
