from django import forms
from .models import Blog


class BlogUpdateForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'subtitle', 'content', 'image')


class BlogCreateForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'subtitle', 'content', 'image')
