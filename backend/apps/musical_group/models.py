from django.db import models
from django.contrib.auth.models import User

class MusicalStyle(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Estilo Musical'
        verbose_name_plural = 'Estilos Musicales'

    def __str__(self):
        return self.name


class MusicalGroup(models.Model):
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=10)
    musical_styles = models.ManyToManyField(MusicalStyle)
    directors = models.ManyToManyField(User)
    guest_musician = models.ManyToManyField(User, related_name='guest_musicians', blank=True)
    permanent_musician = models.ManyToManyField(User, related_name='permanent_musicians', blank=True)

    class Meta:
        verbose_name = 'Grupo Musical'
        verbose_name_plural = 'Grupos Musicales'

    def __str__(self):
        return self.name


class Song(models.Model):
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=10)
    musical_styles = models.ManyToManyField(MusicalStyle)
    musical_group = models.ForeignKey(MusicalGroup, related_name='songs')
    guest_musician = models.ManyToManyField(User, related_name='song_guest_musicians', blank=True)
    permanent_musician = models.ManyToManyField(User, related_name='song_permanent_musicians', blank=True)

    class Meta:
        verbose_name = 'Tema'
        verbose_name_plural = 'Temas'

    def __str__(self):
        return self.name


class Playlist(models.Model):
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=10)
    songs = models.ManyToManyField(Song)

    class Meta:
        verbose_name = 'Playlist'
        verbose_name_plural = 'Playlists'

    def __str__(self):
        return self.name
