# Generated by Django 3.0.7 on 2020-12-07 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0011_auto_20201202_1001'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='education',
            name='degree',
            field=models.CharField(choices=[('Debt', ((11, 'Credit Card'), (12, 'Student Loans'), (13, 'Taxes'))), ('Entertainment', ((21, 'Books'), (22, 'Games'))), ('Everyday', ((31, 'Groceries'), (32, 'Restaurants')))], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='education',
            name='major',
            field=models.CharField(choices=[('CSE', 'Computer Science & Engineering'), ('EEE', 'Electronic & Electronics Engineering'), ('CE', 'Civil Enginerring'), ('BBA', 'Bachelor In Business Administration'), ('SCI', 'Science'), ('COM', 'Commerce'), ('ARTS', 'Arts'), ('O', 'Others')], max_length=100, null=True),
        ),
    ]
