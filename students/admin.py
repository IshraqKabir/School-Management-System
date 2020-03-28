from django.contrib import admin
from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name', 'student_roll')

admin.site.register(Student, StudentAdmin)