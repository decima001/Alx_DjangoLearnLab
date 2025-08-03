from django.urls import path
from .views import BookList
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet

# Create and register the router
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Existing ListAPIView route
    path('books/', BookList.as_view(), name='book-list'),

    # Register ViewSet routes (CRUD)
    path('', include(router.urls)),
]