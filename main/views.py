# django import
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest,HttpResponse

# my import
from .models import Article, Category
from .forms import PostForm


# index page view
def index(request: HttpRequest) -> HttpResponse:
    categories: QuerySet = Category.objects.all()
    posts: QuerySet = Article.objects.all()

    context = {
        "categories": categories,
        "posts": posts,
    }
    return render(request, "index.html", context)


#when a category is specified
def category(request:HttpRequest, cat_id:int) -> HttpResponse:
    cat_post: Article = Article.objects.filter(category_id=cat_id)

    context = {
            "cat_posts":cat_post,
            }
    return render(request,"index.html",context)


#viewing each post
def post_detail(request:HttpRequest,post_id:int) -> HttpResponse:
    post: Article = get_object_or_404(Article,pk=post_id)

    return render(request,"post.html",{"post":post})


def profile(request: HttpRequest):
    if request.method == "POST":
        first_name: str = request.POST.get("first_name")
        last_name: str = request.POST.get("last_name")
        contact: str = request.POST.get("contact")
        img = request.POST.get("img")

        user = request.user

        user.first_name = first_name
        user.last_name = last_name
        user.contact = contact
        user.profile_pic = img
        user.save()
        return redirect("main:post")

    return render(request, "profile.html")


def post(request: HttpRequest):
    if request.user.first_name == None and request.user.last_name == None:
        return redirect("main:profile")

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            title: str = request.POST.get("title")
            body: str = request.POST.get("body")
            category = request.POST.get("category")
            img = request.POST.get("img")

            cat = Category.objects.get(id=category)

            Article.objects.create(
                title=title,
                body=body,
                category=cat,
                images=img,
                author=request.user,
            )

            return redirect("main:index")

    else:
        form = PostForm()
    return render(request, "post.html", {"form": form})
