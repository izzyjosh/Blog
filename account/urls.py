#django import 
from django.urls import path
from django.contrib.auth import views as auth_views

#my import 
from . import views

app_name = "account"

urlpatterns =[
        path("",auth_views.LoginView.as_view(template_name="signin.html"),name="login"),
        path("signup/",views.signup,name="signup"),
        path("logout/",auth_views.LogoutView.as_view(),name="logout"),
        ]

