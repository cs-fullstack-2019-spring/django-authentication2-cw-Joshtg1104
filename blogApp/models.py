from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# model for the blog project
class Blog(models.Model):
    username = models.CharField(max_length=40, default="")
    blog_title = models.CharField(max_length=60, default="")
    blog_entry = models.TextField(max_length=300, default="")
    blog_key = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.username
