from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'collocation'

urlpatterns = [
    path('', views.home_view, name='collocation')
]