from django.urls import path
from . import views
from django.shortcuts import render
from django.http import HttpResponse

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_profile, name='create_profile'),
    path('created/', lambda request: render(request, 'network/profile_created.html'), name='profile_created'),
    path('network/', views.network_page, name='network_page'),
    path('profile/', views.profile_view_page, name='profile_view_page'),
]
