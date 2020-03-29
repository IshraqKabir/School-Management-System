from django.db import models
from departments.models import Department

class Course(models.Model):
    title = models.CharField(max_length=100)
    course_department = models.ForeignKey(Department, on_delete=models.CASCADE)
    course_code = models.IntegerField()

    def __str__(self):
        return self.title




