# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-12 18:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_newspage_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newspage',
            name='author',
        ),
    ]
