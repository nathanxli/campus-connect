from django.urls import path
from . import views
from django.shortcuts import render
from django.http import HttpResponse

urlpatterns = [
    path('', lambda request: HttpResponse("Welcome to the home page!")),
    path('create/', views.create_profile, name='create_profile'),
    path('created/', lambda request: render(request, 'network/profile_created.html'), name='profile_created'),
]
