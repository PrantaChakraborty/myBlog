from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from .models import Post, Category, Comment

# Register your models here.


class CommentInline(admin.TabularInline):
    model = Comment


class PostAdmin(admin.ModelAdmin):
    inlines = [CommentInline]


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Comment)
