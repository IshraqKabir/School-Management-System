from django.urls import path
from django.contrib.auth import views as auth_views
from .views import profile, logout, update, register_student, register_teacher

urlpatterns = [
    path('register/student', register_student, name="register_student"),
    path('register/teacher', register_teacher, name="register_teacher"),
    path('login/', auth_views.LoginView.as_view(
        template_name="accounts/login.html"
    ), name="login"),
    path('logout/', auth_views.LogoutView.as_view(
        template_name="accounts/logout.html"
    ), name="logout"),
    path('profile/', profile, name="profile"),
    path('update/', update, name="update")
]
