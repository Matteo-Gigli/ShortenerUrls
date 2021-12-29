"""cutter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import make, home

# All of us know how to set the urls.py, but we need of something more.
# If we try this urlpatterns without 'path('<str:token>', home, name='home'),' our site will work,
# but not till the end.
# In fact we will have a short url, but is not connect to any page.
# This happens because is not connected to the Ascii string.
# The second urlpatterns allowed us to use a 'string' in our url, connected with home function.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('<str:token>', home, name='home'),
    path('', make, name='make'),
]
