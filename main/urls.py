#django import 
from django.urls import path

#my import
from . import views

app_name = "main"

urlpatterns = [
        path("",views.index,name="index"),
        path("post/<int:post_id>/",views.post_detail, name="post"),
        path("profile/",views.profile,name="profile"),
        ]

