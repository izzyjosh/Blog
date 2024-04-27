from django.contrib import admin
from django import forms
from .models import Category, Article ,Comment, Subscriber, EmailNewsletter
from ckeditor.fields import RichTextFormField
from typing import List
from django.core.mail import send_mail
from django.conf import settings


admin.site.register(Category)
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Subscriber)

# Newsletter form

class NewsLetterAdminForm(forms.ModelForm):
    model = EmailNewsletter
    fields = "__all__"
    widgets = {
            "messages": RichTextFormField,
            }

@admin.register(EmailNewsletter)
class NewsletterAdmin(admin.ModelAdmin):
    form: NewsLetterAdminForm  = NewsLetterAdminForm

    def save_model(self, request,obj,form,change) -> None:
        super().save_model(request,obj,form,change)

        subject:str = obj.subject
        message:str = obj.message
        recipient:List = [subscriber.email for subscriber in obj.recepient.all()]
        from_email: str = settings.EMAIL_HOST_USER

        send_mail(subject,"",from_email,recipient,fail_silently=False,html_message=message)
