# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-14 19:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managedata', '0038_business_sublocation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='rating',
            field=models.FloatField(default=0.0),
        ),
    ]
