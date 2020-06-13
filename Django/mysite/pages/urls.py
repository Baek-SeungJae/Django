# pages/urls.py
from django.contrib import admin
from django.urls import path
from . import views
app_name="pages"
urlpatterns = [

    path('index/',views.index, name = 'index'),
    path('hello/',views.hello, name = 'hello' ),
    path('name/',views.name, name = 'name'),
    path('introduce/', views.introduce, name = 'introduce'),
    path('yourname/<str:name>',views.yourname, name = 'yourname'),
    path('nameAndAge/<str:name>&<str:age>',views.nameAndAge, name = 'nameAndAge'),
    path('multiply/<str:num1>&<str:num2>',views.multiply, name = 'multiply'),
    path('googoodan/<str:num1>&<str:num2>',views.googoodan, name = 'googoodan'),
    path('dtl/',views.dtl, name = 'dtl'),
    path('forif/',views.forif, name = 'forif'),
    path('throw/',views.throw, name = 'throw'),
    path('catch/',views.catch, name = 'catch'),
    path('urlexam/<str:name>',views.urlexam, name = 'urlexam'),
    path('wordtest/',views.wordtest, name = 'wordtest'),
    path('lotto/',views.lotto, name = 'lotto'),
]
