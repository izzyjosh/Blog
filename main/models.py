#django import
from django.db import models
from django.contrib.auth import get_user_model

#other import 
import uuid
from datetime import time
from ckeditor.fields import RichTextField

User = get_user_model()


class Categorie(models.Model):
    name:str  = models.CharField(max_length=50)
    date_created:time  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    title:str = models.TextField()
    body:str = RichTextField()
    author:User = models.ForeignKey(User,on_delete=models.CASCADE)
    category:Categorie = models.ForeignKey(Categorie,on_delete=models.CASCADE)
    created_on  = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="article_image")
    likecount:int= models.IntegerField()

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.author.username


class Comment(models.Model):
    comment:str = models.CharField(max_length=500)
    username:str = models.CharField(max_length=100)
    email:str = models.EmailField()
    owner:Article = models.ForeignKey(Article,on_delete=models.CASCADE)
    date:time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return self.username

