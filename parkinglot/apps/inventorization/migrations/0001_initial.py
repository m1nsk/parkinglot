# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-13 16:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('parking', '0005_auto_20170613_1824'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventorization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('inventoriztion', models.ManyToManyField(to='parking.AutoCard')),
            ],
        ),
    ]
