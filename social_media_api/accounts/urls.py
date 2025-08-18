# accounts/urls.py
from django.urls import path, include
from .views import RegisterView, LoginView, ProfileView
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet
from .views import PostViewSet

router = DefaultRouter()
router.register("users", UserViewSet)
router.register("posts", PostViewSet)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path("", include(router.urls)),
]
