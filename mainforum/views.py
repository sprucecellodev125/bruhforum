import json
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect
from .models import Mainforum, Maincomment
from django import forms, template
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_POST
import logging

logger = logging.getLogger(__name__)
register = template.Library()

class MainCommentForm(forms.Form):
    commentusername = forms.CharField(max_length=255)
    commentuserid = forms.IntegerField()
    commentmessage = forms.CharField(widget=forms.Textarea)

class MainPostForm(forms.Form):
    postusername = forms.CharField(max_length=255)
    postuserid = forms.IntegerField()
    posttitle = forms.CharField(max_length=255)
    postmessage = forms.CharField(widget=forms.Textarea)

# Public content
# This is where my bad coding practice goes on

def homepage(request):
    allpost = Mainforum.objects.all().order_by('-postdate').values()
    rulestxt = open("rules.txt", "r")
    rules = rulestxt.read()
    user_groups = request.user.groups.all()
    is_mod = False
    for group in user_groups:
        if group.name == 'Moderator' or group.name == 'Admin':
            is_mod = True

        if is_mod:
            break

    context = {
        'allpost': allpost,
        'is_mod': is_mod,
        'rules': rules,
               }
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

    context = {'error': error_message}
    return render(request, 'login.html', context)

def viewlogout(request):
    logout(request)
    return redirect('homepage')

def createpost(request):
    if request.user.is_authenticated:
        form = MainPostForm(request.POST or None)
        if form.is_valid():
            postcontent = Mainforum()
            postcontent.postusername = form.cleaned_data['postusername']
            postcontent.postuserid = form.cleaned_data['postuserid']
            postcontent.posttitle = form.cleaned_data['posttitle']
            postcontent.postmessage = form.cleaned_data['postmessage']
            postcontent.save()
            return redirect('viewpost', id=postcontent.id)
        return render(request, 'createpost.html')
    else:
        return redirect('viewlogin')

def viewpost(request, id):
    post = Mainforum.objects.get(id=id)
    comments = Maincomment.objects.filter(commentforpost=post)
    form = MainCommentForm(request.POST or None)
    user_groups = request.user.groups.all()
    is_mod = False
    is_banned = True
    for group in user_groups:
        if group.name == 'Moderator' or group.name == 'Admin':
            is_mod = True

        if group.name == 'Member' or group.name == 'Moderator' or group.name == 'Admin':
            is_banned = False
        
        if is_mod and not is_banned:
            break
    if form.is_valid():
        comment = Maincomment()
        comment.commentusername = form.cleaned_data['commentusername']
        comment.commentuserid = form.cleaned_data['commentuserid']
        comment.commentmessage = form.cleaned_data['commentmessage']
        comment.commentforpost = post
        comment.save()
        return redirect('viewpost', id=post.id) # type: ignore
    context = {'post': post,
               'comments': comments,
               'is_mod': is_mod,
               'is_banned': is_banned,
               }
    return render(request, 'viewpost.html', context)

# Mod-only category

def viewmember(request, id):
    member = User.objects.get(pk=id)
    groups = member.groups.all()
    context = {
        'member': member,
        'groups': groups,
        'joined_date': member.date_joined
    }
    return render(request, "user.html", context)

def modonly(request):
    user_groups = request.user.groups.all()
    is_mod = False
    for group in user_groups:
        if group.name == 'Moderator' or group.name == 'Admin':
            is_mod = True

    if is_mod:
        members = User.objects.filter(groups__name='Member')
        context = {'members': members}
        return render(request, 'modpanel.html', context)
    else:
        return HttpResponse(status=404)

@require_POST
def banuser(request):
    user_groups = request.user.groups.all()
    is_mod = False
    for group in user_groups:
        if group.name == 'Moderator' or group.name == 'Admin':
            is_mod = True
            break
    if is_mod:
        data = json.loads(request.body)
        userid = data.get('userId')
        try:
            target = User.objects.get(id=userid)
            member = Group.objects.get(name='Member')
            target.groups.remove(member)
            return JsonResponse({'status': 'success'})
        except User.DoesNotExist:
            return JsonResponse({'status': 'User not found'}, status=400)
        except Exception as e:
            return JsonResponse({'status': str(e)}, status=500)
    else:
        return JsonResponse({'status': 'Unauthorized'}, status=401)

@require_POST
def removepost(request):
    user_groups = request.user.groups.all()
    is_mod = False
    for group in user_groups:
        if group.name == 'Moderator' or group.name == 'Admin':
            is_mod = True
            break
    if is_mod:
        data = json.loads(request.body)
        postid = data.get('postId')
        try:
            post = Mainforum.objects.get(id=postid)
            post.delete()
            return JsonResponse({'status': 'success'})
        except Mainforum.DoesNotExist:
            return JsonResponse({'status': 'Post not found'}, status=400)
        except Exception as e:
            return JsonResponse({'status': str(e)}, status=500)
    else:
        return JsonResponse({'status': 'Unauthorized'}, status=401)

@require_POST
def removecomment(request):
    user_groups = request.user.groups.all()
    is_mod = False
    for group in user_groups:
        if group.name == 'Moderator' or group.name == 'Admin':
            is_mod = True
            break
    if is_mod:
        data = json.loads(request.body)
        commentid = data.get('commentId')
        try:
            comment = Maincomment.objects.get(id=commentid)
            comment.delete()
            return JsonResponse({'status': 'success'})
        except Mainforum.DoesNotExist:
            return JsonResponse({'status': 'Comment not found'}, status=400)
        except Exception as e:
            return JsonResponse({'status': str(e)}, status=500)
    else:
        return JsonResponse({'status': 'Unauthorized'}, status=401)