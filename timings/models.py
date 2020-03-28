from django.db import models

class Timing(models.Model):
    time = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.time
