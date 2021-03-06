# Generated by Django 3.0.7 on 2020-12-07 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0012_auto_20201207_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='degree',
            field=models.CharField(choices=[('1', (('PHD', 'Doctor of Phillosopy'),)), ('2', (('MSC', 'Master of Science'), ('MD', 'Masters Degree'))), ('3', (('BSC', 'Bachelor of Science'), ('BBA', 'Bachelor in Business Administration'), ('BA', 'Bachelor in Arts'), ('BL', 'Bachelor of Law'), ('BD', 'Bachelor Degree'), ('O', 'Others'))), ('4', (('HSC', 'Higher Secondary Certificate'), ('AL', 'A Level'), ('D', 'Dhakil/Madrasa'), ('O', 'Others'))), ('5', (('SSC', 'Secondary School Certificate'), ('OL', 'O Level'), ('D', 'Dhakil/Madrasa'), ('O', 'Others')))], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='education',
            name='major',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
