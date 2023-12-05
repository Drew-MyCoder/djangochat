from django.db import models
from datetime import datetime

# Create your models here.
class Room(models.Model):
    def __str__(self) -> str:
        return self.name
    name = models.CharField(max_length=5000)

class Message(models.Model):
    def __str__(self) -> str:
        return self.room
    value = models.CharField(max_length=10000000)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=5000)
    room = models.CharField(max_length=5000)