from django.contrib import admin
from .models import Core, Post, Comment

# Register your models here.
admin.site.register(Core)
admin.site.register(Post)
admin.site.register(Comment)
