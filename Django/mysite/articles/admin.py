from django.contrib import admin
from .models import Article, Comment
# Register your models here.



class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id','title','content','created_at','updated_at')

admin.site.register(Article,ArticleAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('article','content','created_at')

admin.site.register(Comment,CommentAdmin)
