from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    title = models.CharField(max_length=100)
    subject = models.CharField(max_length=20)
    body = models.TextField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(default="def.png", blank=True)
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50]+"..."
