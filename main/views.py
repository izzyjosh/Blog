#django import 
from django.shortcuts import render,redirect
from django.http import HttpRequest

#my import 
from .models import Article,Category
from .forms import PostForm


def index(request:HttpRequest):
    categories:QuerySet = Category.objects.all()
    posts:QuerySet = Article.objects.all()
    editors_pic = Article.objects.all()[:3]
    trending = Article.objects.order_by("?")[:3]

    context = {
            "categories":categories,
            "posts":posts,
            "editors_pic":editors_pic,
            "trending":trending
            }
    return render(request,"index.html",context)



def profile(request:HttpRequest):
    if request.method == "POST":
        first_name:str = request.POST.get("first_name")
        last_name:str = request.POST.get("last_name")
        contact:str = request.POST.get("contact")
        img = request.POST.get("img")

        user = request.user

        user.first_name = first_name
        user.last_name = last_name
        user.contact = contact
        user.profile_pic = img
        user.save()
        return redirect("main:post")


    return render(request,"profile.html")



def post(request:HttpRequest):
    if request.user.first_name == None and request.user.last_name== None:
        return redirect("main:profile")

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            title:str = request.POST.get("title")
            body:str = request.POST.get("body")
            category = request.POST.get("category")
            img = request.POST.get("img")

            cat = Category.objects.get(id=category)

            Article.objects.create(
                    title=title,
                    body=body,
                    category=cat,
                    images=img,
                    author=request.user,)

            return redirect("main:index")

    else:
        form = PostForm()
    return render(request,"post.html",{"form":form})


