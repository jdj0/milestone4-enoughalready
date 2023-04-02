from django import forms
from .models import Blog, Comment


class BlogUpdateForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'subtitle', 'content', 'image')


class BlogCreateForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'subtitle', 'content', 'image')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
