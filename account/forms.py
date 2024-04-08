#django import 
from django import forms 
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm,PasswordResetForm,SetPasswordForm

User = get_user_model()


class MyUserCreationForm(UserCreationForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)


    username = forms.CharField(
            label="",
            required=True,
            help_text="",
            widget=forms.TextInput(attrs={
                "name":"username",
                "type":"text",
                "placeholder":"Username",
                "class":"form-control",
                }))


    email = forms.EmailField(
            label="",
            required=True,
            widget=forms.EmailInput(attrs={
                "name":"email",
                "type":"email",
                "placeholder":"Email",
                "class":"form-control",
                }))


    password1 = forms.CharField(
            label="",
            required=True,
            help_text="",
            widget=forms.PasswordInput(attrs={
                "name":"password1",
                "type":"password",
                "placeholder":"Password",
                "class":"form-control",
                }))

    password2 = forms.CharField(
            label="",
            required=True,
            help_text="",
            widget=forms.PasswordInput(attrs={
                "name":"password2",
                "type":"password",
                "placeholder":"Confirm Password",
                "class":"form-control",
                }))


    class Meta:
        model = User
        fields = ("username","email","password1","password2")



class CustomPasswordResetForm(PasswordResetForm):

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

    email = forms.EmailField(
            label="",
            required=True,
            widget=forms.EmailInput(attrs={
                "name":"email",
                "type":"email",
                "placeholder":"Valid Email",
                "class":"form-control"
                })
            )
    class Meta:
        model = User
        fields = ("email")




class CustomSetPasswordForm(SetPasswordForm):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

    newpassword1 = forms.CharField(
            label="",
            required=True,
            help_text="",
            widget = forms.PasswordInput(attrs={
                "placeholder":"password",
                "type":"password",
                "name":"password1",
                "class":"form-control m-2",
                })
            )
    newpassword2 = forms.CharField(
            label="",
            required=True,
            help_text="",
            widget = forms.PasswordInput(attrs={
                "placeholder":"confirm password",
                "type":"password",
                "name":"password1",
                "class":"form-control m-2",
                })
            )
    class Meta:
        model = User
        fields = ("newpassword1","newpassword2")

