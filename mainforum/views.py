from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect
from .models import Mainforum, Maincomment
from django import forms, template
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)
register = template.Library()

class MainCommentForm(forms.Form):
    commentusername = forms.CharField(max_length=255)
    commentmessage = forms.CharField(widget=forms.Textarea)

class MainPostForm(forms.Form):
    postusername = forms.CharField(max_length=255)
    posttitle = forms.CharField(max_length=255)
    postmessage = forms.CharField(widget=forms.Textarea)

@register.filter(name='has_group') 
def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists() 

# Create your views here.
def homepage(request):
    allpost = Mainforum.objects.all().order_by('-postdate').values()
    context = {'allpost': allpost}
    return render(request, 'main.html', context)

def viewlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            error_message = 'Invalid login credentials. Please try again.'
    else:
        error_message = None

    context = {'error_message': error_message}
    return render(request, 'login.html', context)

def viewlogout(request):
    logout(request)
    return redirect('homepage')

def viewpost(request, id):
    post = Mainforum.objects.get(id=id)
    comments = Maincomment.objects.filter(commentforpost=post)
    form = MainCommentForm(request.POST or None)
    if form.is_valid():
        comment = Maincomment()
        comment.commentusername = form.cleaned_data['commentusername']
        comment.commentmessage = form.cleaned_data['commentmessage']
        comment.commentforpost = post
        comment.save()
        return redirect('viewpost', id=post.id) # type: ignore
    context = {'post': post,
               'comments': comments,
               }
    return render(request, 'viewpost.html', context)

def modonly(request):
    user_groups = request.user.groups.all()
    is_mod = False
    for group in user_groups:
        if group.name == 'Moderator' or group.name == 'Admin':
            is_mod = True
            break
    if is_mod:
        members = User.objects.filter(groups__name='Member')
        context = {'members': members}
        return render(request, 'modpanel.html', context)
    else:
        return HttpResponse(status=404)

def banuser(request, id):
    user_groups = request.user.groups.all()
    is_mod = False
    for group in user_groups:
        if group.name == 'Moderator' or group.name == 'Admin':
            is_mod = True
            break
    if is_mod:
        target = User.objects.get(id=id)
        member = Group.objects.get(name='Member')
        target.groups.remove(member)
        return redirect('modonly')
    else:
        return HttpResponse(status=404)

def createpost(request):
    if request.user.is_authenticated:
        form = MainPostForm(request.POST or None)
        if form.is_valid():
            postcontent = Mainforum()
            postcontent.postusername = form.cleaned_data['postusername']
            postcontent.posttitle = form.cleaned_data['posttitle']
            postcontent.postmessage = form.cleaned_data['postmessage']
            postcontent.save()
            return redirect('viewpost', id=postcontent.id) # type: ignore
        return render(request, 'createpost.html')
    else:
        return redirect('viewlogin')