from django.urls import path
from .views import add_courses

urlpatterns = [
    path('add_courses/', add_courses, name="add_courses")
]
