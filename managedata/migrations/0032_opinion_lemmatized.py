# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-07 17:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managedata', '0031_remove_itemtopic_category_suggestion'),
    ]

    operations = [
        migrations.AddField(
            model_name='opinion',
            name='lemmatized',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
    ]
