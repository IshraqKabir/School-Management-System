from django import forms
from django.forms import Select

from .models import Class

class Create_Class_Form(forms.ModelForm):
    class Meta:
        model = Class
        fields = [
            'course',
            'teacher',
            'day',
            'timing',
            'batch',
            'section',
            'room'
        ]
        widgets = {
            'choice_field': Select(attrs={'multiple': 'True'}),
        }
