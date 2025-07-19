from relationship_app.models import Author, Library

# Query all books by a specific author
author = Author.objects.get(name="Chinua Achebe")
books_by_author = author.books.all()

# List all books in a library
library = Library.objects.get(name="National Library")
books_in_library = library.books.all()

# Retrieve the librarian for a library
librarian = library.librarian
