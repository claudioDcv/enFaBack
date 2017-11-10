from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=255)
    start_dt = models.DateTimeField()
    end_dt = models.DateTimeField()

    def __str__(self):
        return self.name
