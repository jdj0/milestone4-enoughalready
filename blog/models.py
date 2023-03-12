from django.db import models
from accounts.models import UserAccount


class Blog(models.Model):
    title = models.CharField(max_length=99)
    content = models.TextField()
    image = models.ImageField(null=True, blank=True, upload_to="images/")
    published = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
