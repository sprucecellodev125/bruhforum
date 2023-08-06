from django.db import models
from django.utils import timezone


class Core(models.Model):
    rules = models.TextField(null=True)
    about = models.TextField(null=True)
    needsetup = models.BooleanField(default=True)
    name = models.CharField(max_length=255, null=True)

    def save(self, *args, **kwargs):
        if Core.objects.exists() and not self.pk:
            raise Exception("You can't put more than 1 object in Core. Did you mean to edit it?")
        super().save(*args, **kwargs)


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
