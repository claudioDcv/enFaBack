from django.db import models
from django.contrib.auth.models import User


class MusicalInstrument(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Instrumento Musical'
        verbose_name_plural = 'Instrumentos Musicales'

    def __str__(self):
        return self.name


class MusicalStyle(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Estilo Musical'
        verbose_name_plural = 'Estilos Musicales'

    def __str__(self):
        return self.name

    def as_dict(self):
        return {
            "id": self.id,
            "text": self.name,
        }


class UserMusicalInstrumentStyle(models.Model):
    user = models.ForeignKey(User)
    musical_styles = models.ManyToManyField(MusicalStyle)
    musical_instruments = models.ManyToManyField(
        MusicalInstrument,
        related_name='musical_instrument',
    )

    class Meta:
        verbose_name = 'Musico Intrumento y Estilo'
        verbose_name_plural = 'Musicos Instrumento y Estilos'

    def __str__(self):
        return self.user.username


class MusicalGroup(models.Model):
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=10)
    musical_styles = models.ManyToManyField(MusicalStyle)
    directors = models.ManyToManyField(UserMusicalInstrumentStyle)
    guest_musician = models.ManyToManyField(
        UserMusicalInstrumentStyle,
        related_name='guest_musicians',
        blank=True,
    )
    permanent_musician = models.ManyToManyField(
        UserMusicalInstrumentStyle,
        related_name='permanent_musicians',
        blank=True,
    )

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
    guest_musician = models.ManyToManyField(
        UserMusicalInstrumentStyle,
        related_name='song_guest_musicians',
        blank=True,
    )
    permanent_musician = models.ManyToManyField(
        UserMusicalInstrumentStyle,
        related_name='song_permanent_musicians',
        blank=True,
    )

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
