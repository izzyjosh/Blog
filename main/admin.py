#django import
from django.contrib import admin
from django.db import models as m

#my import 
from . import models

#third party import
from ckeditor.widgets import CKEditorWidget

admin.site.register(models.Categorie)

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','created_on')
    search_fields = ['title', 'content','author']


admin.site.register(models.Article,ArticleAdmin)
admin.site.register(models.Comment)

