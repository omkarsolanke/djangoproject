from django.urls import path
from ..CustomLogin import views


urlpatterns = [
    path("register", views.register, name="register"),
    path("login_user", views.login_user, name="login_user"),
    path("logout_user", views.logout_user, name="logout_user"),
    path("home", views.home, name="home")
]