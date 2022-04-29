from django.db import models

class Room(models.Model):
    name = models.CharField(max_length = 200)
    floor = models.IntegerField()
    room_no = models.IntegerField()

    def __str__(self):
        return f'{self.name}, Room No. {self.room_no} on {self.floor} floor'