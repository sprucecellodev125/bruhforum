import json
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Core, Post, Comment
from django import forms, template
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_POST
import logging

logger = logging.getLogger(__name__)
register = template.Library()


class CommentForm(forms.Form):
    commentusername = forms.CharField(max_length=255)
    commentuserid = forms.IntegerField()
    commentmessage = forms.CharField(widget=forms.Textarea)


class PostForm(forms.Form):
    postusername = forms.CharField(max_length=255)
    postuserid = forms.IntegerField()
    posttitle = forms.CharField(max_length=255)
    postmessage = forms.CharField(widget=forms.Textarea)


class OverviewSettings(forms.Form):
    rules = forms.CharField(widget=forms.Textarea)
    about = forms.CharField(widget=forms.Textarea)
    name = forms.CharField(max_length=255)


def homepage(request):
    allpost = Post.objects.all().order_by('-postdate').values()
    try:
        core = Core.objects.get()
    except Core.DoesNotExist:
        core = None
    
    need_setup = Core.objects.values_list('needsetup', flat=True).first()
    is_mod = False
    if request.user.is_staff:
            is_mod = True

    context = {
        'allpost': allpost,
        'is_mod': is_mod,
        'core': core,
        'need_setup': need_setup,
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


@login_required
def createpost(request):
    core = Core.objects.get()
    form = PostForm(request.POST or None)
    if form.is_valid():
        postcontent = Post()
        postcontent.postusername = form.cleaned_data['postusername']
        postcontent.postuserid = form.cleaned_data['postuserid']
        postcontent.posttitle = form.cleaned_data['posttitle']
        postcontent.postmessage = form.cleaned_data['postmessage']
        postcontent.save()
        return redirect('viewpost', id=postcontent.id)
    return render(request, 'createpost.html', {'core': core})


def viewpost(request, id):
    post = Post.objects.get(id=id)
    comments = Comment.objects.filter(commentforpost=post)
    form = CommentForm(request.POST or None)
    need_setup = Core.objects.values_list('needsetup', flat=True).first()
    core = Core.objects.get()
    is_mod = False
    is_banned = True
    if request.user.is_staff:
            is_mod = True

    if form.is_valid():
        comment = Comment()
        comment.commentusername = form.cleaned_data['commentusername']
        comment.commentuserid = form.cleaned_data['commentuserid']
        comment.commentmessage = form.cleaned_data['commentmessage']
        comment.commentforpost = post
        comment.save()
        return redirect('viewpost', id=post.id)
    context = {'post': post,
               'comments': comments,
               'is_mod': is_mod,
               'is_banned': is_banned,
               'need_setup': need_setup,
               'core': core
               }

    return render(request, 'viewpost.html', context)


def viewmember(request, id):
    member = User.objects.get(pk=id)
    groups = member.groups.all()
    context = {
        'member': member,
        'groups': groups,
        'joined_date': member.date_joined
    }
    return render(request, "user.html", context)


def overview(request):
    is_mod = False
    core = Core.objects.first()
    if request.method == 'POST':
        form = OverviewSettings(request.POST)
        if form.is_valid():
            name_value = form.cleaned_data['name']
            about_value = form.cleaned_data['about']
            rules_value = form.cleaned_data['rules']

            core.name = name_value
            core.about = about_value
            core.rules = rules_value
            core.needsetup = False
            core.save()

            return redirect('overview')
    else:
        form = OverviewSettings(initial={
            'name': core.name,
            'about': core.about,
            'rules': core.rules
        })

    if request.user.is_staff:
        is_mod = True

    if is_mod:
        context = {
            'core': core,
            'form': form
        }
        return render(request, 'overview.html', context)
    else:
        return HttpResponse(status=404)


def roles(request):
    is_mod = False
    core = Core.objects.first()
    roles = Group.objects.all()
    if request.user.is_staff:
        is_mod = True
    if is_mod:
        context = {
            'core': core,
            'roles': roles
        }
        return render(request, 'overview.html', context)
    else:
        return HttpResponse(status=404)
    

@require_POST
def banuser(request):
    is_mod = False
    if request.user.is_staff:
        is_mod = True
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
    is_mod = False
    if request.user.is_staff:
            is_mod = True
    if is_mod:
        data = json.loads(request.body)
        postid = data.get('postId')
        try:
            post = Post.objects.get(id=postid)
            post.delete()
            return JsonResponse({'status': 'success'})
        except Post.DoesNotExist:
            return JsonResponse({'status': 'Post not found'}, status=400)
        except Exception as e:
            return JsonResponse({'status': str(e)}, status=500)
    else:
        return JsonResponse({'status': 'Unauthorized'}, status=401)


@require_POST
def removecomment(request):
    is_mod = False
    if request.user.is_staff:
            is_mod = True
    if is_mod:
        data = json.loads(request.body)
        commentid = data.get('commentId')
        try:
            comment = Comment.objects.get(id=commentid)
            comment.delete()
            return JsonResponse({'status': 'success'})
        except Comment.DoesNotExist:
            return JsonResponse({'status': 'Comment not found'}, status=400)
        except Exception as e:
            return JsonResponse({'status': str(e)}, status=500)
    else:
        return JsonResponse({'status': 'Unauthorized'}, status=401)
