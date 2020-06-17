# pages/urls.py
from django.contrib import admin
from django.urls import path
from . import views
app_name = "articles_2"
urlpatterns = [
    path('index/', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('update/<int:article_pk>', views.update, name='update'),
    path('detail/<int:article_pk>', views.detail, name='detail'),
]
