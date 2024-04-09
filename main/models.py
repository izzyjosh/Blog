#django import
from django.db import models
from django.contrib.auth import get_user_model

#other import 
import uuid
from datetime import time
from ckeditor.fields import RichTextField

User = get_user_model()


class Category(models.Model):
    name:str = models.CharField(max_length=50)
    date:time = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name_plural = "Categories"


    def __str__(self):
        return self.name

class Article(models.Model):
    author:User = models.ForeignKey(User,on_delete=models.CASCADE)
    title:str = models.CharField(max_length=400)
    body:str = RichTextField()
    category:Category = models.ForeignKey(Category,on_delete=models.CASCADE)
    created:time = models.DateTimeField(auto_now_add=True)
    updated:time = models.DateTimeField(auto_now=True)
    images = models.ImageField(upload_to="article_images")
    likecount:int = models.IntegerField(blank=True,null=True)

    class Meta:
        ordering = ("-created",)

    def __str__(self):
        return f"{self.author.username} : {self.title}"



class Comment(models.Model):
    comment:str = models.CharField(max_length=500)
    username:str = models.CharField(max_length=100)
    email:str = models.EmailField()
    article:Article = models.ForeignKey(Article,on_delete=models.CASCADE)
    date:time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return f"{self.username}: {self.comment}"



