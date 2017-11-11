# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-11 16:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('color', models.CharField(max_length=10)),
                ('description', models.TextField()),
            ],
        ),
    ]
