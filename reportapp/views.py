from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django import forms, template
from .models import Reportapp
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.models import User, Group
from django.views.decorators.http import require_POST

