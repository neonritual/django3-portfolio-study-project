from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from . import views


app_name = 'blog'

urlpatterns = [
    path('', views.all_blogs, name="blogs"),
    path('<int:blog_id>/', views.detail, name="detail")
]
