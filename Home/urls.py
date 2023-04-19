"""Car_Rental URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django import views
from django.contrib import admin
from django.urls import path
from Home import views

urlpatterns = [
    path("", views.index, name= 'Home'),
    path("Home/", views.index, name= 'Home'),
    path("login/", views.login, name= 'login'),
    path("signup/", views.signup, name= 'signup'),
    path("earnwithyourcar/", views.earnwithyourcar, name= 'earnwithyourcar'),
    path("carlist/", views.carlist, name= 'carlist'),
    path("loginEWC/", views.loginEWC, name= 'loginEWC'),
    path("signupEWC/", views.signupEWC, name= 'signupEWC'),
    path("about/", views.about, name= 'about'),
    path("contact", views.contact, name= 'contact'),
    path("index2/", views.index2, name= 'index2'),
    path("booked/", views.booked, name= 'booked'),
    path("carlistl/", views.carlistl, name= 'carlistl')



]
