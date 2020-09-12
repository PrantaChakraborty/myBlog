import uuid
from django.conf import settings
from django.db import models
from django.urls import reverse

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_category_view', kwargs={'pk': self.pk})


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cover = models.ImageField(upload_to='blog_cover/', blank=True)
    title = models.CharField(max_length=250)
    category = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField(null=False)
    date = models.DateField(auto_now_add=True)

    class Meta:
        permissions = [
            ('special_permission', 'Can read all posts'),
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail_view', args=[str(self.id)])


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    comment = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, )
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.comment


