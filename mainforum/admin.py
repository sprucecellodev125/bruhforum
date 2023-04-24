from django.contrib import admin
from .models import Mainforum, Maincomment

# Register your models here.
admin.site.register(Mainforum)
admin.site.register(Maincomment)