from django.db import models
from django.contrib.auth.models import User
from courses.models import Course

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    student_roll = models.IntegerField()
    courses = models.ManyToManyField(Course)
    
    def __str__self():
        return self.student_roll
