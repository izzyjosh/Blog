# django import
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest, HttpResponse
from django.db.models import Q,F
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from typing import List
from django.contrib.auth import get_user_model

# my import
from .models import Article, Category,Comment
from .forms import PostForm,SubscriberForm

User = get_user_model()

# index page view
def index(request: HttpRequest) -> HttpResponse:
    search: str = request.GET.get("search", "")
    query_param: str = request.GET.get("cat","")
    categories: QuerySet = Category.objects.all()

    posts: QuerySet = Article.objects.filter(
        Q(title__icontains=search) | 
        Q(author__username__icontains=search),
        category__name__icontains=query_param,
    )

    if request.method == "POST":
        form: SubscriberForm = SubscriberForm(request.POST)

        if form.is_valid():
            subscriber = form.save()
            
            recipient:List = [subscriber.email]
            from_email:str = settings.EMAIL_HOST_USER
            subject:str = "Subscription For Newsletter"
            html_message:str = render_to_string("email_content.html",{"email":subscriber.email})

            messages.success(request,"Thanks for subscribing to our NewsLetter")

            send_mail(subject,"",from_email,recipient,fail_silently=True,html_message=html_message)

            return redirect("main:index")

        else:
            messages.error(request,"Invalid email")
    else:
        form: SubscriberForm = SubscriberForm()

    context = {
            "categories": categories,
            "posts": posts,
            "form":form,
        }

    return render(request, "index.html", context)


# viewing each post
def post_detail(request: HttpRequest, post_id: int) -> HttpResponse:
    post: Article = get_object_or_404(Article, pk=post_id)
    post.likecount = F("likecount") + 1
    post.save()
    post.refresh_from_db()

    comments: QuerySet = Comment.objects.filter(article=post)

    related_posts: QuerySet = Article.objects.filter(category=post.category)

    context = {
            "post":post,
            "comments":comments,
            "related_posts":related_posts,
            }

    if request.method == "POST":
        username:str = request.POST.get("name")
        email:str = request.POST.get("email")
        comment:str = request.POST.get("comment")


        user: User = User.objects.get(email=email)

        context["user"] = user
        
        Comment.objects.create(
                username=username,
                email=email,
                comment=comment,
                article=post,)

        
        return render(request, "post.html", context)

    return render(request, "post.html", context)
