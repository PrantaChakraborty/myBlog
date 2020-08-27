import uuid

from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=100)


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cover = models.ImageField(upload_to='blog_cover/', blank=True)
    title = models.CharField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    body = models.TextField(null=False)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
