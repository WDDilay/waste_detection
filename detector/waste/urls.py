from django.urls import path
from django.shortcuts import render
from . import views

urlpatterns = [
    path('', views.sample, name='main'),
    path('upload/', views.upload_image, name='upload_image'),
]