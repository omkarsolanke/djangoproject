from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),
    path('home/', views.home, name='home'),
    path('student_register/', views.student_register.as_view(), name='student_register'),
    path('teacher_register/', views.teacher_register.as_view(), name='teacher_register')
]