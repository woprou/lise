# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-26 01:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('managedata', '0017_auto_20171126_0146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemtopic',
            name='status',
            field=models.CharField(choices=[('novo', 'Novo'), ('ativo', 'Ativo'), ('recusado', 'Recusado')], default='novo', max_length=20),
        ),
        migrations.AlterField(
            model_name='itemtopic',
            name='topic',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='itemtopics', to='managedata.Topic'),
        ),
    ]
