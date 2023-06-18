from django.urls import path, include
from . import views
from django.shortcuts import render
from django.http import HttpResponse

urlpatterns = [
    path('', views.taiwan, name = 'taiwan'), 
    path('ajax_refresh_county', views.ajax_refresh_county, name = 'ajax_refresh_county'),
]