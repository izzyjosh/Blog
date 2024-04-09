#django import 
from django import forms
from django.contrib.auth import get_user_model

#my import 
from .models import Comment, Article

#third party import 
from ckeditor.widgets import CKEditorWidget
from ckeditor.fields import RichTextField

User = get_user_model()


class CommentForm(forms.ModelForm):
    username = forms.CharField(
            required=True,
            label="",
            widget = forms.TextInput(attrs={
                "name":"username",
                "type":"text",
                "placeholder":"Username",
                "class":"form-control",
                }))



    email = forms.EmailField(
        required=True,
        label="",
        widget = forms.TextInput(attrs={
            "name":"email",
            "type":"email",
            "placeholder":"Valid Email",
            "class":"form-control",
            }))


    comment = forms.CharField(
        required=True,
        label="",
        widget = forms.TextInput(attrs={
            "name":"comment",
            "type":"text",
            "placeholder":"Comment here ...",
            "class":"form-control",
            }))

    class Meta:
        model = User
        fields = ("username","email","comment")





class PostForm(forms.ModelForm):

    title:str = forms.CharField(
            label = "Title Of Article",
            required = True,
            help_text = "",
            widget = forms.Textarea(attrs={
                "name":"title",
                "type":"text",
                "class":"form-control",
                "cols":"4"}))


    body:str = forms.CharField(
            label = "CONCLUSION",
            required = True,
            help_text = "",
            widget = forms.Textarea(attrs={
                "name":"conclusion",
                "type":"text",
                "class":"form-control",
                "cols":"4"}))



    class Meta:
        model = Article
        fields = ("title","body","category")
        widgets = {
                "category": forms.Select(attrs={
                    "class":"form-control",
                    "name":"category",
                    }),
                }

