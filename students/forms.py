from django import forms
from .models import Student
class StudentRegisterForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('first_name', 'last_name', 'student_roll')