from django.db import models
from django.utils import timezone

# Create your models here.


class Core(models.Model):
    rules = models.TextField(null=True)
    about = models.TextField(null=True)
    needsetup = models.BooleanField(default=True)
    name = models.CharField(max_length=255, null=True)

    def save(self, *args, **kwargs):
        # Check if an instance of this model already exists
        if Core.objects.exists() and not self.pk:
            # If an instance exists and we're not updating an existing one,
            # prevent saving a new instance.
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

