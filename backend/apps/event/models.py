from django.db import models
from apps.musical_group.models import UserMusicalInstrumentStyle


class Event(models.Model):
    title = models.CharField(max_length=255)
    start = models.DateTimeField()
    end = models.DateTimeField()
    users = models.ManyToManyField(UserMusicalInstrumentStyle)

    def __str__(self):
        return self.title
