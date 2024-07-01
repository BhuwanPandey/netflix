from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("register/",views.register,name="register"),
    path("login/",views.loginn,name="login"),
    path("logout/",views.logout,name="logout"),
]
