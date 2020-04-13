from django.db import models
from courses.models import Course
from batches.models import Batch
from teachers.models import Teacher
from days.models import Day
from timings.models import Timing
from rooms.models import Room

class Class(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, default="", on_delete=models.CASCADE)
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    timing = models.ForeignKey(Timing, on_delete=models.CASCADE)
    # day = models.CharField(max_length=20, default="")
    # timing = models.CharField(max_length=20, default="")
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.DO_NOTHING)
    section_choices = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
    )
    section = models.CharField(max_length=20, choices=section_choices, null=True)

    def __str__(self):
        return self.batch.name + '=>' + self.course.title

    class Meta:
        verbose_name = 'Class'
        verbose_name_plural = 'Classes'
