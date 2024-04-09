#django import 
from django.urls import path

#my import
from . import views

app_name = "main"

urlpatterns = [
        path("",views.index,name="index"),
        path("profile/",views.profile,name="profile"),
        path("post/",views.post,name="post"),
        ]

