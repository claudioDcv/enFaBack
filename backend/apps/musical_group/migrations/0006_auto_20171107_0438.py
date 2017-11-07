# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-07 04:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('musical_group', '0005_musicalgroup_directors'),
    ]

    operations = [
        migrations.AddField(
            model_name='musicalgroup',
            name='guest_musician',
            field=models.ManyToManyField(related_name='guest_musicians', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='musicalgroup',
            name='permanent_musician',
            field=models.ManyToManyField(related_name='permanent_musicians', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='song',
            name='musical_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='songs', to='musical_group.MusicalGroup'),
        ),
    ]