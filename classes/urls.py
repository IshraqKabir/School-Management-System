from django.urls import path
from .views import add_class

urlpatterns = [
    path('add_class/', add_class, name="add_class"),
    
]
