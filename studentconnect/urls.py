# studentconnect/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('network.urls')),  # 👈 this line includes your app's URLs
]
