from django.urls import path, include
from django.urls import path
from django.contrib import admin
from .views import PostList
from .views import PostDetailView, PostList


urlpatterns = [
    path('posts/', PostList.as_view(), name='post-list'),
    path('post-details/<int:id>/', PostDetailView.as_view(), name='post-details'),
]

