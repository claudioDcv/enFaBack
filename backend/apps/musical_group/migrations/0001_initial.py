# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-07 19:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MusicalGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('color', models.CharField(max_length=10)),
                ('directors', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('guest_musician', models.ManyToManyField(blank=True, related_name='guest_musicians', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Grupo Musical',
                'verbose_name_plural': 'Grupos Musicales',
            },
        ),
        migrations.CreateModel(
            name='MusicalStyle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Estilo Musical',
                'verbose_name_plural': 'Estilos Musicales',
            },
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('color', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name': 'Playlist',
                'verbose_name_plural': 'Playlists',
            },
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('color', models.CharField(max_length=10)),
                ('guest_musician', models.ManyToManyField(blank=True, related_name='song_guest_musicians', to=settings.AUTH_USER_MODEL)),
                ('musical_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='songs', to='musical_group.MusicalGroup')),
                ('musical_styles', models.ManyToManyField(to='musical_group.MusicalStyle')),
                ('permanent_musician', models.ManyToManyField(blank=True, related_name='song_permanent_musicians', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Tema',
                'verbose_name_plural': 'Temas',
            },
        ),
        migrations.AddField(
            model_name='playlist',
            name='songs',
            field=models.ManyToManyField(to='musical_group.Song'),
        ),
        migrations.AddField(
            model_name='musicalgroup',
            name='musical_styles',
            field=models.ManyToManyField(to='musical_group.MusicalStyle'),
        ),
        migrations.AddField(
            model_name='musicalgroup',
            name='permanent_musician',
            field=models.ManyToManyField(blank=True, related_name='permanent_musicians', to=settings.AUTH_USER_MODEL),
        ),
    ]
