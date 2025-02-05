
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('all', views.all_users, name='users'),
    path('task/<int:task_id>/upload/', views.upload_document, name='upload_document'),
]