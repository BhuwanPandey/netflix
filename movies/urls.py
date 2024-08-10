from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("watch/<int:id>/",views.watch,name="watch"),
    path("info/<int:id>/",views.info,name="info"),
    path("<str:name>/",views.name,name="name"),
]
