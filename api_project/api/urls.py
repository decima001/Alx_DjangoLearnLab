from django.urls import path
from .views import BookList
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import BookList, BookViewSet

# Create and register the router
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Existing ListAPIView route
    path('books/', BookList.as_view(), name='book-list'),
    # token auth endpoint
    path('auth/token/', obtain_auth_token, name='api-token'),  
    # Register ViewSet routes (CRUD)
    path('', include(router.urls)),
]