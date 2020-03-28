from django.urls import path
from .views import home, profile_of_others

urlpatterns = [
    path('', home, name="home"),
    path('pages/profiles/<int:id>/', profile_of_others, name="profile_of_others"),
    
]
