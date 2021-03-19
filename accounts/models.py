from django.db import models


class Detail(models.Model):
    displayphoto = models.ImageField(default="default1.png", blank=True)
    fullname = models.CharField(max_length=30, default=None)
    displayname = models.CharField(max_length=30)
    mobile = models.CharField(max_length=10, unique=True)
    dob = models.DateField()
    email = models.EmailField(max_length=30)
    bio = models.TextField(max_length=130)

    def __str__(self):
        return self.fullname
