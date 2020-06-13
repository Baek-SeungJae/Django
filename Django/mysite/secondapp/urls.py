# second/urls.py
from django.contrib import admin
from django.urls import path
from . import views
app_name="secondapp"
urlpatterns = [
    path('login/',views.login, name = 'login'),
    path('static_example/',views.static_example),
]