from django.urls import path
from .views import (
    search_students, 
    search_teachers, 
    search_results_students, 
    search_results_teachers,
    search_classes,
    search_results_classes,
    search_routine
)
urlpatterns = [
    path('students/', search_students, name="search_students"),
    path('teachers/', search_teachers, name="search_teachers"),
    path('classes/', search_classes, name="search_classes"),
    path('search_results_students/', search_results_students, name="search_results_students"),
    path('search_results_teachers/', search_results_teachers, name="search_results_teachers"),
    path('search_results_classes/', search_results_classes, name="search_results_classes"),
    path('search_routine/', search_routine, name="search_routine"),
]


