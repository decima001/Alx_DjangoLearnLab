from relationship_app.models import Author, Library

# 1. Query all books by a specific author
def query_books_by_author():
    author = Author.objects.get(name="Chinua Achebe")
    books = author.books.all()
    for book in books:
        print(book.title)

# 2. List all books in a library
def list_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    for book in books:
        print(book.title)

# 3. Retrieve the librarian for a library
def get_librarian(library_name):
    library = Library.objects.get(name=library_name)
    print(f"Librarian: {library.librarian.name}")
