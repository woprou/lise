# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-21 00:09
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managedata', '0010_auto_20171117_0007'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestcategory',
            name='date_request',
            field=models.DateField(default=datetime.date(2017, 11, 21)),
        ),
    ]
