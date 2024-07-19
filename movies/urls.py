from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    # path("watch/",views.watch,name="watch"),
    path("watch/<int:id>/",views.watch,name="watch"),
    path("info/<int:id>/",views.info,name="info"),
    path("<str:name>/",views.name,name="name"),
    path("<str:name>/<int:id>",views.moviedetail,name="detail"),
]
