from django.urls import path
from . import views

urlpatterns = [
    path("register/",views.register,name="register"),
    path("profile/",views.profile,name="profile"),
    path("login/",views.loginn,name="login"),
    path("logout/",views.logout,name="logout"),
    
]
