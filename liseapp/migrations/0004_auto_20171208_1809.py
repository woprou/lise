# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-08 18:09
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('liseapp', '0003_auto_20171208_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 8, 18, 9, 57, 829080)),
        ),
    ]
