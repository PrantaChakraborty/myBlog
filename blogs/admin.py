from django.contrib import admin
from .models import Post, Category

# Register your models here.
blog = [Post, Category]
admin.site.register(blog)
