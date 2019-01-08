"""fv URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from . import views
from django.urls import path



urlpatterns = [
    path('', views.index, name='index'),
    path('register/' ,views.register, name='register'),
    path('login/', views.login, name= 'login'),
    path('about/', views.about, name= 'about'),
    path('contactus/', views.contact, name= 'contactus'),
    path('create/', views.createuser,name= 'post'),
    path('verfy/', views.loginverify, name='veryfy'),
    path('u/', views.testu, name='u'),
    path('show/', views.show,name='show'),



]
