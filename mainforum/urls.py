from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('create/', views.createpost, name='createpost'),
    path('post/<int:id>', views.viewpost, name='viewpost'),
    path('login/', views.viewlogin, name='viewlogin'),
    path('logout/', views.viewlogout, name='viewlogout'),
    path('mods/', views.modonly, name='modonly'),
    path('api/banuser/', views.banuser, name='banuser'),
]
