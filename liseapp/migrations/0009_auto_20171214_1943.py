# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-14 19:43
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('liseapp', '0008_auto_20171214_1744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 14, 19, 43, 10, 492587)),
        ),
    ]
