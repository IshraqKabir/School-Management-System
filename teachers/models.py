from django.db import models
from django.contrib.auth.models import User
from courses.models import Course

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    teacher_roll = models.IntegerField()
    courses = models.ManyToManyField(Course)
    user_type = "teacher"
    
    def __str__(self):
        return self.user.username

class Teacher_Course(models.Model):
    title = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher = models.ManyToManyField(Teacher)
    sunday = models.BooleanField(default=False)
    sunday_timing = models.CharField(max_length=100)
    monday = models.BooleanField(default=False)
    monday_timing = models.CharField(max_length=100)

    def __str__(self):
        return self.teacher + '-' + self.title