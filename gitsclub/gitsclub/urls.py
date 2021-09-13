from re import template
from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views


from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.newmember, name='newmember'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('groups/', views.groups, name='groups'),
    path('creategroup/', views.creategroup, name='creategroup'),
    path('about/', views.about, name='about'),
]


# Unused Url
# path('group/<int:id>', views.group, name='group'),
