from django.db import models
from accounts.models import UserAccount
from django.contrib.auth.models import User


class Blog(models.Model):
    title = models.CharField(max_length=99)
    subtitle = models.CharField(null=True, max_length=99)
    content = models.TextField()
    image = models.ImageField(upload_to="images/")
    published = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    published = models.DateTimeField(auto_now_add=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
