"""WebProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see: https://docs.djangoproject.com/en/4.0/topics/http/urls/
    1. Add a URL to urlpatterns:  path('', views.home, name='home')
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
"""
from django.contrib import admin
from django.urls import path
from .views import *

#    /

urlpatterns = [
    path('', homePageTempalate, name="homePage"),
    path('about/', AboutPageView.as_view(), name="about page"),
    path('actors/', ActorsPageView.as_view(), name="actors page"),
    path('rawContent/', homePageView, name="rawContent"),
]
