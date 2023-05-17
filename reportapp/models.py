from django.db import models

# Create your models here.
class Reportapp(models.Model):
    username = models.CharField(max_length=255)
    reportedUser = models.CharField(max_length=255)
    reportType = models.CharField(max_length=255)
    reportLink = models.CharField(max_length=255)
    reportDesc = models.TextField()