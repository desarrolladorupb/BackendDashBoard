# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-18 12:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lcperformance', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comite',
            name='codigo_expa',
        ),
    ]
