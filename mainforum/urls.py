from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('create/', views.createpost, name='createpost'),
    path('post/<int:id>', views.viewpost, name='viewpost'),
    path('accounts/login/', views.viewlogin, name='viewlogin'),
    path('accounts/logout/', views.viewlogout, name='viewlogout'),
    path('settings/', views.forumsettings, name='forumsettings'),
    path('users/<int:id>', views.viewmember, name="viewuser"),
    path('api/banuser/', views.banuser, name='banuser'),
    path('api/removecomment/', views.removecomment, name='removecomment'),
    path('api/removepost/', views.removepost, name='removepost'),
    path('setup/', views.setup, name='setup')
]
