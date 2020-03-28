from django.urls import path
from .views import add_courses, course_list, add_teacher_course

urlpatterns = [
    path('add_courses/', add_courses, name="add_courses"),
    path('course_list/', course_list, name="course_list"),
    path('add_teacher_course/<int:teacher_roll>', add_teacher_course, name="add_teacher_course"),
    
]
