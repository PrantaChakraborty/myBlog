from django import forms
from .models import Post, Comment


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'cover', 'body', 'category']


class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'cover', 'body']


class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']


class CommentUpdateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
