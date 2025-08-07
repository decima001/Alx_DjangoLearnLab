from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer
from rest_framework import filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import generics, permissions, filters
from django_filters import rest_framework
from django_filters.rest_framework import DjangoFilterBackend

# ListView - Get all books
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Public access

# DetailView - Get single book by ID
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

# CreateView - Add new book
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # You could associate created_by here if needed
        serializer.save()

# UpdateView - Modify existing book
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

# DeleteView - Delete a book
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
# Create your views here.

class BookCreateView(generics.CreateAPIView):
    ...
    def perform_create(self, serializer):
        # Example of adding extra logic: logging, user tracking, etc.
        serializer.save()

class BookUpdateView(generics.UpdateAPIView):
    ...
    def perform_update(self, serializer):
        # You can track updates or validate something before save
        serializer.save()

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    search_fields = ['title']
    ordering_fields = ['publication_year']
    permission_classes = [IsAuthenticatedOrReadOnly]

# List all books with filtering, searching, and ordering
    # Add filters, search, and ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Fields to allow filtering
    filterset_fields = ['title', 'publication_year', 'author']

    # Fields to allow searching
    search_fields = ['title', 'author__name']

    # Fields to allow ordering
    ordering_fields = ['title', 'publication_year']



# BookListView supports filtering, searching, and ordering:
# - Filtering by: title, publication_year, author
# - Searching on: title, author name (case-insensitive)
# - Ordering by: title, publication_year (asc or desc using - prefix)
#
# Examples:
# /api/books/?title=1984
# /api/books/?search=Achebe
# /api/books/?ordering=-publication_year