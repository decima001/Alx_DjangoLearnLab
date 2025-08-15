from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import register_view, profile_view

from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    PostDetailView,
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView,
)

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='blog/logout.html'), name='logout'),
    path('register/', register_view, name='register'),
    path('profile/', profile_view, name='profile'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('comment/<int:pk>/edit/', views.comment_edit, name='comment_edit'),
    path('comment/<int:pk>/delete/', views.comment_delete, name='comment_delete'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment_create'),
    path('comment/<int:pk>/edit/', CommentUpdateView.as_view(), name='comment_edit'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment_update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
]

