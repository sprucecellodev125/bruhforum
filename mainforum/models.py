from django.db import models
from django.utils import timezone

# Create your models here.

class Mainforum(models.Model):
    postusername = models.CharField(max_length=255)
    postmessage = models.TextField()
    posttitle = models.CharField(max_length=255)
    postdate = models.DateTimeField(default=timezone.now)

class Maincomment(models.Model):
    commentusername = models.CharField(max_length=255)
    commentmessage = models.TextField()
    commentforpost = models.ForeignKey(Mainforum, on_delete=models.CASCADE)
    commentdate = models.DateTimeField(default=timezone.now)