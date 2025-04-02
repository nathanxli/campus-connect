from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_profile, name='create_profile'),
    path('created/', lambda request: render(request, 'network/profile_created.html'), name='profile_created'),
]
