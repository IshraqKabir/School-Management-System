from django.db import models
from courses.models import Course
from teachers.models import Teacher
from departments.models import Department

class Batch(models.Model):
    name = models.CharField(max_length=100)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name




