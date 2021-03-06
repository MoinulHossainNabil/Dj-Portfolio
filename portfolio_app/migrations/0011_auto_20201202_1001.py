# Generated by Django 3.0.7 on 2020-12-02 04:01

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0010_auto_20201129_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='degree',
            field=models.CharField(choices=[('1', 'Master of Science'), ('2', 'Bachelor of Science'), ('3', 'Higher Secondary Certificate'), ('4', 'Secondary School Certificate'), ('5', 'Others')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='education',
            name='major',
            field=models.CharField(choices=[('CSE', 'Computer Science & Engineering'), ('EEE', 'Electronic & Electronics Engineering'), ('CE', 'Civil Enginerring'), ('BBA', 'Bachelor In Business Administratioin'), ('SCI', 'Science'), ('COM', 'Commerce'), ('ARTS', 'ARTS'), ('O', 'Others')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
