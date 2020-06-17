# pages/urls.py
from django.contrib import admin
from django.urls import path
from . import views
app_name="movies"
urlpatterns = [
    path('',views.movies, name = 'movies'),
    path('new/',views.new, name = 'new'),
    path('<int:id>',views.detail, name = 'detail'),
    path('<int:id>/edit/',views.edit, name = 'edit'),
    path('<int:id>/delete/',views.delete, name = 'delete'),
]

