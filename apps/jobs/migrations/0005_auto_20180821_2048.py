# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-08-21 20:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0001_initial'),
        ('jobs', '0004_auto_20180821_2044'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='worker',
        ),
        migrations.AddField(
            model_name='job',
            name='workers',
            field=models.ManyToManyField(related_name='planned_jobs', to='login_app.User'),
        ),
    ]
