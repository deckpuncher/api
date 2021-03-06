# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-18 12:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jobseeker',
            fields=[
                ('JobseekerId', models.CharField(default=32534015, max_length=8, primary_key=True, serialize=False)),
                ('FirstName', models.CharField(max_length=100)),
                ('LastName', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=200)),
                ('dob', models.DateField(verbose_name='DOB')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AboutMe', models.TextField(max_length=1000)),
                ('PreferredWorkLocation', models.CharField(max_length=50)),
                ('PreferredIndustry', models.CharField(max_length=200)),
                ('Skills', models.CharField(max_length=50)),
                ('jobseeker', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='jobseekers.Jobseeker')),
            ],
        ),
    ]
