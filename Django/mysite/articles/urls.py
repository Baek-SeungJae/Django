# pages/urls.py
from django.contrib import admin
from django.urls import path
from . import views
app_name="articles"
urlpatterns = [

    path('index/',views.index, name = 'index'),
    path('new/',views.new, name = 'new'),
    path('create/',views.create, name = 'create'),
    path('detail/<str:no>',views.detail, name='detail'),
    path('delete/<str:no>',views.delete, name='delete'),
    path('update/<str:no>',views.update, name='update'),
    path('updated',views.updated, name='updated'),
]
