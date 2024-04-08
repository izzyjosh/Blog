#python import 
import uuid 
from uuid import UUID

#django import
from django.db import models
from django.contrib.auth.models import AbstractUser


class UserModel(AbstractUser):
    id:UUID = models.UUIDField(
            primary_key=True,
            editable=False,
            default=uuid.uuid4)
    username:str = models.CharField(max_length=50,unique=True)
    first_name:str = models.CharField(max_length=50,blank=True,null=True)
    last_name:str = models.CharField(max_length=50,blank=True,null=True)
    email:str = models.EmailField(max_length=50)
    contact:int = models.IntegerField(blank=True,null=True)
    profile_pic = models.ImageField(upload_to="user_dp",blank=True,null=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
