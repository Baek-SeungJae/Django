# pages/urls.py
from django.contrib import admin
from django.urls import path
from . import views
app_name="articles"
urlpatterns = [

    path('index/',views.index, name = 'index'),
    path('new/',views.index, name = 'new'),
    path('create/',views.index, name = 'create'),
    
]
