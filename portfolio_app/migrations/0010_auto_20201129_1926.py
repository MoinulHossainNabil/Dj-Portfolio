# Generated by Django 3.0.7 on 2020-11-29 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0009_userprofile_profession'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='degree',
            field=models.CharField(choices=[('MSC', 'Master of Science'), ('BSC', 'Bachelor of Science'), ('HSC', 'Higher Scondary Certificate'), ('SSC', 'Secondary School Certificate'), ('O', 'Others')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='education',
            name='major',
            field=models.CharField(choices=[('CSE', 'Computer Science & Engineering'), ('EEE', 'Electronic & Electronics Engineering'), ('CE', 'Civil Enginerring'), ('BBA', 'Bachelor In Business Administratioin'), ('O', 'Others')], max_length=100, null=True),
        ),
    ]
