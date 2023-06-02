from django.db import models
from django.utils import timezone

# Create your models here.


class Core(models.Model):
    rules = models.TextField()
    about = models.TextField()


class Post(models.Model):
    postusername = models.CharField(max_length=255)
    postuserid = models.IntegerField(null=True)
    postmessage = models.TextField()
    posttitle = models.CharField(max_length=255)
    postdate = models.DateTimeField(default=timezone.now)


class Comment(models.Model):
    commentusername = models.CharField(max_length=255)
    commentuserid = models.IntegerField(null=True)
    commentmessage = models.TextField()
    commentforpost = models.ForeignKey(Post, on_delete=models.CASCADE)
    commentdate = models.DateTimeField(default=timezone.now)
