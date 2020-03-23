from django import forms
from .models import Course

class AddCourseForm(ModelForm):
    class Meta:
        model : Course
        fields = [
            'course_code'
        ]
