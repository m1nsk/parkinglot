# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-13 14:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='carmodel',
            old_name='name',
            new_name='model',
        ),
    ]
