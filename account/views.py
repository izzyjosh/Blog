#django import 
from django.shortcuts import render,redirect
from django.http import HttpRequest
from django.contrib import messages

#my import 
from .forms import MyUserCreationForm

def signup(request:HttpRequest):
    if request.method == "POST":
        form = MyUserCreationForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect("account:login")

    else:
        form = MyUserCreationForm()

    return render(request,"signup.html",{"form":form})

