"""
URL configuration for AurexBackend project.

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
from AurexApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include("AurexApp.urls")),
    path("", contact_list, name="contact_list"),
    path("startup_list", startup_list, name="startup_list"),
    path("startups/<int:pk>/", startup_detail, name="startup_detail"),
    path("investor_list", investor_list, name="investor_list"),
    path("investors/<int:pk>/", investor_detail, name="investor_detail"),
]
