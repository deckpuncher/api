# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-18 09:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobseeker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobseeker',
            name='dob',
            field=models.DateField(verbose_name='DOB'),
        ),
    ]
