from django import forms
from .models import Teacher
class TeacherRegisterForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ('first_name', 'last_name', 'teacher_roll')