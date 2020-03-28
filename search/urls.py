from django.urls import path
from .views import search_students, search_teachers, search_results_students, search_results_teachers

urlpatterns = [
    path('students/', search_students, name="search_students"),
    path('teachers/', search_teachers, name="search_teachers"),
    path('search_results_students/', search_results_students, name="search_results_students"),
    path('search_results_teachers/', search_results_teachers, name="search_results_teachers"),
]


