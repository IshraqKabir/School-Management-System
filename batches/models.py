from django.db import models
from courses.models import Course
from teachers.models import Teacher

class Batch(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name




