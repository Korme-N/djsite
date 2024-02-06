from rest_framework.authtoken.admin import User
from django.db import models
from rest_framework.reverse import reverse


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    views_count = models.IntegerField(default=0)
