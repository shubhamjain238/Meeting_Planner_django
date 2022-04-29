from django.db import models
from rooms.models import Room

class Meeting(models.Model):
    title = models.CharField(max_length = 100)
    date = models.DateField()
    time = models.TimeField()
    duration = models.IntegerField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)


    def __str__(self):
        return f'{self.title} on {self.date} at {self.time}'