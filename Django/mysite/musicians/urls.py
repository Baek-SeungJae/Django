# pages/urls.py
from django.contrib import admin
from django.urls import path
from . import views
app_name="musicians"
urlpatterns = [
    path('',views.index, name = 'index'),
    path('create/',views.create, name = 'create'),
    path('<int:musician_pk>/',views.detail, name = 'detail'),
    path('<int:musician_pk>/update',views.update, name = 'update'),
    path('<int:musician_pk>/delete',views.delete, name = 'delete'),
    path('<int:musician_pk>/create', views.album_create, name='album_create'),
]

