# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2020-04-23 15:51
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0005_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='first_visit',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 23, 15, 51, 2, 991259), null=True),
        ),
        migrations.AddField(
            model_name='page',
            name='last_visit',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 23, 15, 51, 2, 991296), null=True),
        ),
    ]