from django import forms
from .models import Student
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

class StudentRegisterForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('first_name', 'last_name', 'student_roll')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('first_name', css_class='form-group col-md-6 mb-0'),
                Column('password', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'student_1',
            Submit('submit', 'Register')
        )