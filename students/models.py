from django.db import models
from django.contrib.auth.models import User
from courses.models import Course
from batches.models import Batch

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    student_roll = models.IntegerField()
    courses = models.ManyToManyField(Course)
    batch = models.ManyToManyField(Batch)
    user_type = "student"
    
    def __str__(self):
        return self.user.username
