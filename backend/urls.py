"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path,include
from django.http import HttpResponse

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('monitor.urls')),
    path('', lambda request: HttpResponse("Welcome to Process Monitor API")),  # Optional: homepage
]
   
""" include('monitor.urls') tells Django:

“Take all the URLs defined in monitor/urls.py and attach them after api/.”

api is not a folder or app—it’s just part of the URL.

It’s used to namespace your URLs, so all your API endpoints start with /api/.

Example: you can have /admin/ for the admin panel and /api/... for API endpoints.
In short:
api exists in the URL, not as a physical folder. It’s a common convention to separate your API from your frontend URLs.

"""