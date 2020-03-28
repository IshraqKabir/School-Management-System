from django.db import models

class Room(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=100)

    def __str__(self):
        room = self.name + ' - ' + str(self.number)
        return room

