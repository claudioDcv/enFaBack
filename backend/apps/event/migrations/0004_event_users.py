# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-10 18:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musical_group', '0007_auto_20171109_1425'),
        ('event', '0003_auto_20171110_1750'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='users',
            field=models.ManyToManyField(to='musical_group.UserMusicalInstrumentStyle'),
        ),
    ]