from django.contrib import admin
from .models import Book

# Register the Book model with custom admin configurations
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Show these fields in the list view
    list_filter = ('publication_year', 'author')  # Add filters for easy navigation
    search_fields = ('title', 'author')  # Enable search by title and author
